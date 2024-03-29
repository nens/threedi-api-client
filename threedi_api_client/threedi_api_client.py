import warnings

from threedi_api_client.openapi.configuration import Configuration

from .auth import refresh_api_key
from .config import Config, EnvironConfig
from .versions import host_has_version


class ThreediApiClient:
    """Legacy client for the 3Di API

    This client is legacy: please use the ThreediApi instead. A warning will
    be emitted if this client used.

    Args:
        env_file: path to a configuration file
        config: configuration dictionary for this client

    Returns:
        This class constructs an openapi_client.ApiClient object, which is
        autogenerated by the OpenAPI generator.
    """

    def __new__(cls, env_file=None, config=None):
        warnings.warn(
            "ThreediApiClient is pending deprecation. Please use the new "
            "threedi_api_client.ThreediApi instead.",
            UserWarning,
        )

        if env_file is not None:
            user_config = Config(env_file)
        elif config is not None:
            user_config = config
        else:
            user_config = EnvironConfig()

        # Determine whether there is a version in the host. The legacy API client
        # requires this.
        api_host = user_config.get("API_HOST")
        if api_host is not None and not host_has_version(api_host):
            raise ValueError(
                f"Invalid API_HOST '{api_host}'. The (legacy) ThreediApiClient expects a "
                f"version to be present."
            )

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            from openapi_client import ApiClient as LegacyApiClient

        configuration = Configuration(
            host=api_host,
            username=user_config.get("API_USERNAME"),
            password=user_config.get("API_PASSWORD"),
            api_key={"Authorization": "", "refresh": ""},
            api_key_prefix={"Authorization": "Bearer"},
        )
        configuration.refresh_api_key_hook = refresh_api_key

        return LegacyApiClient(configuration)
