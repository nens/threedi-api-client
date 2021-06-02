import jwt
import re
import warnings
from datetime import datetime, timedelta
from threedi_api_client.openapi import ApiClient
from threedi_api_client.openapi import Configuration
from threedi_api_client.openapi import V3Api
from threedi_api_client.openapi import Authenticate

from threedi_api_client.config import Config, EnvironConfig

# Get new token REFRESH_TIME_DELTA before it really expires.
REFRESH_TIME_DELTA = timedelta(hours=4).total_seconds()


def host_has_version(host: str):
    return bool(re.findall(r"(.*)\/v3.*", host))


def host_remove_version(host: str):
    matches = re.findall(r"(.*)\/v3.*", host)
    if matches:
        return matches[0]
    else:
        return host


def get_auth_token(username: str, password: str, api_host: str):
    api_client = ApiClient(
        Configuration(
            username=username,
            password=password,
            host=host_remove_version(api_host)
        )
    )
    api = V3Api(api_client)
    return api.auth_token_create(Authenticate(username, password))


def is_token_usable(token: str) -> bool:
    if token is None:
        return False

    try:
        # Get payload without verifying signature,
        # does NOT validate claims (including exp)
        payload = jwt.decode(
            token,
            options={"verify_signature": False},
        )
    except (jwt.exceptions.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return False

    expiry_dt = datetime.utcfromtimestamp(payload["exp"])
    sec_left = (expiry_dt - datetime.utcnow()).total_seconds()
    return sec_left >= REFRESH_TIME_DELTA


def refresh_api_key(config: Configuration):
    """Refreshes the access key if its expired"""
    api_key = config.api_key.get("Authorization")
    if is_token_usable(api_key):
        return

    refresh_key = config.api_key['refresh']
    if is_token_usable(refresh_key):
        api_client = ApiClient(Configuration(host_remove_version(config.host)))
        api = V3Api(api_client)
        token = api.auth_refresh_token_create(
            {"refresh": config.api_key['refresh']}
        )
    else:
        token = get_auth_token(config.username, config.password, config.host)
    config.api_key = {
        'Authorization': token.access,
        'refresh': token.refresh
    }


class ThreediApiClient:
    def __new__(cls, env_file=None, config=None):
        if env_file is not None:
            user_config = Config(env_file)
        elif config is not None:
            user_config = config
        else:
            user_config = EnvironConfig()

        # Determine whether there is a version in the host. If so, warn and
        # use the legacy API client.
        if host_has_version(user_config.get("API_HOST")):
            warnings.warn(
                "API_HOST provided with an API version. This implies usage of "
                "the legacy openapi_client. Please remove "
                "the version to use the new client and silence warnings.",
                UserWarning,
            )
            from openapi_client import ApiClient as LegacyApiClient
            client_cls = LegacyApiClient
        else:
            client_cls = ApiClient

        configuration = Configuration(
            host=user_config.get("API_HOST"),
            username=user_config.get("API_USERNAME"),
            password=user_config.get("API_PASSWORD"),
            api_key={"Authorization": '', "refresh": ''},
            api_key_prefix={"Authorization": "Bearer"}
        )
        configuration.refresh_api_key_hook = refresh_api_key

        return client_cls(configuration)
