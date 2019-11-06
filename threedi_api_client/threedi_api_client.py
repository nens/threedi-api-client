from os import environ

import jwt

from openapi_client import ApiClient
from openapi_client import Configuration
from openapi_client import AuthApi
from openapi_client.models import Authenticate

from threedi_api_client.config import Config

# Token expires at:
# jwt_token.exp + EXPIRE_LEEWAY seconds
# (thus EXPIRE_LEEWAY seconds before it really expires)
EXPIRE_LEEWAY = -300


class ApiAccess:
    def __init__(self, env_file=None):
        self._user_config = Config(env_file)
        self._client = None
        self._access_token = None

    def _get_api_tokens(self, username, password):
        configuration = Configuration()
        configuration.host = self._user_config.get("API_HOST")
        api_client = ApiClient(configuration)
        auth = AuthApi(api_client)
        return auth.auth_token_create(Authenticate(username, password))

    def _is_token_usable(self):
        if self._access_token is None:
            return False

        # Check if not expired...
        try:
            jwt.decode(
                self._access_token,
                options={"verify_signature": False},
                leeway=EXPIRE_LEEWAY,
            )
        except Exception:
            return False

        return True

    @property
    def access_token(self):
        if self._is_token_usable():
            return self._access_token
        # Access token is not usable (None/expired)
        # get a new one
        tokens = self._get_api_tokens(
            self._user_config.get("API_USERNAME"),
            self._user_config.get("API_PASSWORD"),
        )
        self._access_token = tokens.access
        return self._access_token

    def get_auth_headers(self):
        """
        Get auth headers usable for requests.
        """
        api_client = self._api_client
        return {
            "Authorization": api_client.configuration.api_key_prefix[
                "Authorization"
            ]
            + " "
            + api_client.configuration.api_key["Authorization"]
        }

    @property
    def _api_client(self):
        """
        Create api client if self._access_token
        is not usable or return the cached self._client
        """
        configuration = Configuration()
        configuration.host = self._user_config.get("API_HOST")
        configuration.api_key["Authorization"] = self.access_token
        configuration.api_key_prefix["Authorization"] = "Bearer"
        self._client = ApiClient(configuration)
        return self._client


class ThreediApiClient:
    def __new__(cls, env_file=None):
        cls._ac = ApiAccess(env_file)
        return cls._ac._api_client

    @classmethod
    def api_access(cls, env_file=None):
        if not hasattr(cls, "_ac"):
            cls.__new__(cls, env_file)
        return cls._ac
        # raise AttributeError("class has to be instantiated first")
