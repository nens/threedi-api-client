import base64
import json
from datetime import datetime, timedelta
from typing import Tuple

import urllib3

from .files import get_pool
from .openapi import Configuration
from .versions import host_remove_version

# Get new token REFRESH_TIME_DELTA before it really expires.
REFRESH_TIME_DELTA = timedelta(minutes=5).total_seconds()


class AuthenticationError(Exception):
    pass


def send_json_request(method, url, **kwargs):
    headers = kwargs.pop("headers", {})
    headers["Accept"] = "application/json"
    if "body" in kwargs:
        kwargs["body"] = json.dumps(kwargs["body"])
        headers["Content-Type"] = "application/json"
    resp = get_pool().request(method, url, headers=headers, **kwargs)
    if resp.status not in (200, 201):
        error_msg = kwargs.get("error_msg", "Error sending request")
        try:
            detail = json.loads(resp.data)["detail"]
        except Exception:
            detail = f"server responded with error code {resp.status}"
        raise AuthenticationError(f"{error_msg}: {detail}")
    return json.loads(resp.data.decode("ISO-8859-1"))


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
    if refresh_token is None:
        return None, None

    # send the refresh token request
    token_url = oauth2_autodiscovery(issuer)["token_endpoint"]
    fields = {"grant_type": "refresh_token", "refresh_token": refresh_token}

    # include client id and optionally secret in headers/body
    client_id = config.api_key.get("client_id")
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
