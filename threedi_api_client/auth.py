import base64
import json
from datetime import datetime, timedelta
from typing import Tuple
from functools import lru_cache

import urllib3

from .files import get_pool
from .openapi import Configuration
from .versions import host_remove_version

# Get new token REFRESH_TIME_DELTA before it really expires.
REFRESH_TIME_DELTA = timedelta(minutes=5).total_seconds()


class AuthenticationError(Exception):
    pass


def send_json_request(method, url, **kwargs):
    """Helper function for sending a request and decoding the JSON response.

    The request body, if supplied, will be automatically JSON-encoded.

    The request has a default policy of 3 retries.

    Raises an AuthenticationError if the response is not successful. Optionally
    supply an 'error_msg' to change the message.
    """
    headers = kwargs.pop("headers", {})
    error_msg = kwargs.pop("error_msg", "Error sending request")
    headers["Accept"] = "application/json"
    if "body" in kwargs:
        assert not isinstance(kwargs["body"], (bytes, str))
        kwargs["body"] = json.dumps(kwargs["body"])
        headers["Content-Type"] = "application/json"
    resp = get_pool().request(method, url, headers=headers, **kwargs)
    if resp.status not in (200, 201):
        try:
            detail = json.loads(resp.data)
            if "detail" in detail:
                detail = detail["detail"]
            elif "error" in detail:
                detail = detail["error"]
        except Exception:
            detail = f"server responded with error code {resp.status}"
        raise AuthenticationError(f"{error_msg}: {detail}")
    return json.loads(resp.data.decode("ISO-8859-1"))


@lru_cache(1)
def decode_jwt(token):
    """Decode a JWT without checking its signature"""
    # JWT consists of {header}.{payload}.{signature}
    _, payload, _ = token.split(".")
    # JWT should be padded with = (base64.b64decode expects this)
    payload += "=" * (-len(payload) % 4)
    return json.loads(base64.b64decode(payload))


def is_token_usable(token: str) -> bool:
    if token is None:
        return False

    try:
        payload = decode_jwt(token)
    except Exception:
        return False

    expiry_dt = datetime.utcfromtimestamp(payload["exp"])
    sec_left = (expiry_dt - datetime.utcnow()).total_seconds()
    return sec_left >= REFRESH_TIME_DELTA


def get_issuer(token: str) -> bool:
    if token is None:
        return

    try:
        payload = decode_jwt(token)
    except Exception:
        return

    return payload.get("iss")


def get_client_id(token: str) -> str:
    if token is None:
        return

    try:
        payload = decode_jwt(token)
    except Exception:
        return

    return payload.get("client_id")


def refresh_api_key(config: Configuration):
    """Refreshes the access key if it is expired"""
    api_key = config.api_key.get("Authorization")
    if is_token_usable(api_key):
        return
    issuer = get_issuer(api_key)
    if issuer is None:
        access_token, refresh_token = refresh_simplejwt_token(config)
    else:
        access_token, refresh_token = refresh_oauth2_token(issuer, config)
    config.api_key = {"Authorization": access_token, "refresh": refresh_token}


def refresh_simplejwt_token(config: Configuration) -> Tuple[str, str]:
    refresh_key = config.api_key.get("refresh")
    if is_token_usable(refresh_key):
        tokens = send_json_request(
            method="POST",
            url=f"{host_remove_version(config.host)}/v3/auth/refresh-token/",
            body={"refresh": refresh_key},
            error_msg="Cannot refresh the access token",
        )
    else:
        if not config.username or not config.password:
            raise AuthenticationError(
                "Cannot fetch a new access token because username/password were not supplied."
            )
        tokens = send_json_request(
            method="POST",
            url=f"{host_remove_version(config.host)}/v3/auth/token/",
            body={"username": config.username, "password": config.password},
            error_msg="Cannot fetch an access token",
        )
    return tokens["access"], tokens["refresh"]


def oauth2_autodiscovery(issuer: str):
    # use autodiscovery to fetch server details
    return send_json_request(
        method="GET",
        url=f"{issuer}/.well-known/openid-configuration",
        error_msg=f"Cannot discover the authorization server '{issuer}'",
    )


def refresh_oauth2_token(issuer: str, config: Configuration):
    refresh_token = config.api_key.get("refresh")
    if not refresh_token:
        raise AuthenticationError(
            "Cannot fetch a new access token because THREEDI_API_REFRESH_TOKEN was not supplied."
        )
    client_id = get_client_id(config.api_key.get("Authorization"))
    if not client_id:
        raise AuthenticationError(
            "Cannot fetch a new access token because the access token does not contain a client_id."
        )

    # send the refresh token request
    token_url = oauth2_autodiscovery(issuer)["token_endpoint"]
    fields = {"grant_type": "refresh_token", "refresh_token": refresh_token}

    # include client id and optionally secret in headers/body
    client_id = get_client_id(config.api_key.get("Authorization"))
    client_secret = config.api_key.get("client_secret")
    if client_secret:
        # Include id + secret in headers using basic auth
        headers = urllib3.make_headers(basic_auth=f"{client_id}:{client_secret}")
    else:
        # Include only id (in body)
        headers = {}
        fields["client_id"] = client_id

    tokens = send_json_request(
        method="POST",
        url=token_url,
        fields=fields,
        headers=headers,
        encode_multipart=False,
        error_msg="Failed to refresh the access token",
    )
    access_token = tokens["access_token"]
    return access_token, refresh_token
