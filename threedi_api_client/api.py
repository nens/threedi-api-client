from .openapi import ApiClient, Configuration

try:
    from threedi_api_client.aio.openapi.api_client import ApiClient as AsyncApiClient
    from threedi_api_client.aio.aiohttp_retry import RetryClient, ExponentialRetry
except ImportError:
    AsyncApiClient = None

from .auth import refresh_api_key
from .config import Config, EnvironConfig
from .versions import API_VERSIONS, host_has_version

import urllib3


RETRY_AFTER_STATUS_CODES = frozenset({413, 429, 503, 504})


class ThreediApi:
    """Client for the 3Di API.

    The API object exposes numerous methods that interface with the API,
    all named according to the pattern ``{resource}_{action}``, for example ``simulations_list``.
    Consult the docstrings of these methods for further information

    ThreediApi requires a THREEDI_API_HOST and user credentials (THREEDI_API_USERNAME, THREEDI_API_PASSWORD). These can either be stored in
    a ``.env`` file, supplied via environment variables, or passed as a config dictionary.

    Alternatively, supply an THREEDI_API_ACCESS_TOKEN. If the THREEDI_API_ACCESS_TOKEN has expired, there are 3 methods
    implemented for automatic token renewal:

    - refresh token without client secret: supply a THREEDI_API_REFRESH_TOKEN
    - refresh token with client secret: supply a THREEDI_API_REFRESH_TOKEN and THREEDI_API_CLIENT_SECRET
    - client credentials flow: supply a THREEDI_API_CLIENT_SECRET

    For personal api token authentication supply a THREEDI_API_PERSONAL_API_TOKEN.

    For the client_credentials flow, direct usage of ``threedi_api_client.auth.refresh_oauth2_token``
    is recommended to fetch the initial access token.

    1) A sample ``.env`` file could look like this::

        THREEDI_API_HOST=https://api.3di.live
        THREEDI_API_USERNAME=your.username
        THREEDI_API_PASSWORD=your.password

    This is used in your script as follows:

    .. code:: python

        from threedi_api_client import ThreediApi

        env_file = "<path>/.env"
        with ThreediApi(env_file=env_file) as api:
            ...

    2) The same variables can be set as environment variables from the terminal
    that you use to run the python interpreter with. On Windows::

        set THREEDI_API_HOST "https://api.3di.live"
        set THREEDI_API_USERNAME "your.username"
        set THREEDI_API_PASSWORD "your.password"

    On Linux or OSX::

        export THREEDI_API_HOST=https://api.3di.live
        export THREEDI_API_USERNAME=your.username
        export THREEDI_API_PASSWORD=your.password

    3) The ``config`` keyword argument can be used like:

    .. code:: python

        from threedi_api_client import ThreediApi
        from getpass import getpass

        config = {
            "THREEDI_API_HOST": "https://api.3di.live",
            "THREEDI_API_USERNAME": "your.username",
            "THREEDI_API_PASSWORD": getpass(),
        }

        with ThreediApi(config=config) as api:
            ...

    Args:
        env_file (str or pathlib.Path): path to a configuration file
        config (dict): configuration dictionary for this client
        version (str): the API version to use (default: 'v3')
        asynchronous (bool): whether to return an asynchronous API client for
          usage with asyncio. Note: this requires installation of ``threedi_api_client[aio]``.
        retries (int or object): the number of retries; see notes section for more
          granular control over the retry policy

    Returns:
        This class constructs an Api object that was autogenerated by the OpenAPI
        generator. The autogenerated code lives under ``threedi_api_client.openapi``.

    Notes:
        **Timeouts**

        A request without a timeout may block your python script indefinitely. It is always
        a good idea to prevent this by setting a timeout. Do this using the ``_request_timeout``
        parameter on every api request. It is currently not possible to configure a default timeout.

        **Retry policy**

        It is common to configure a retry policy to prevent exceptions due to the service being
        temporarily unavailable. The ``ThreediApi`` supports this through the ``retries``
        parameter. Due to different backends, the configuration details differ between synchronous
        and asynchronous usage.

        For basic usage, supply an integer (which is the maximum number of retries):

        >>> api = ThreediApi(..., retries=3)

        For synchronous usage, you may also supply a ``urllib3.util.Retry`` object
        (see `urllib3 docs <https://urllib3.readthedocs.io/en/stable/user-guide.html#retrying-requests>`_):

        >>> import urllib3
        >>> policy = urllib3.util.Retry(total=3, backoff_factor=1.0)
        >>> api = ThreediApi(..., retries=policy)

        For asynchronous usage, you may also supply a ``aiohttp_retry.ExponentialRetry`` object. See
        the `aiohttp_retry docs <https://github.com/inyutin/aiohttp_retry>`_). The ``aiohttp_retry``
        package is shipped with ``threedi_api_client``.

        >>> from threedi_api_client.aio import aiohttp_retry
        >>> policy = aiohttp_retry.ExponentialRetry(attempts=3, factor=1.0)
        >>> api = ThreediApi(..., retries=policy)

        Other configuration options are::

        - the exceptions on which to retry (default: None)
        - the statuses on which to retry (default: 413, 429, 503, 504)
        - the HTTP methods on which to retry (default: 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PUT', 'TRACE')

    """

    def __init__(
        self, env_file=None, config=None, version="v3", asynchronous=False, retries=3
    ):
        if env_file is not None:
            user_config = Config(env_file)
        elif config is not None:
            user_config = config
        else:
            user_config = EnvironConfig()

        host = user_config.get("THREEDI_API_HOST")
        if not host:
            raise ValueError(
                "ThreediApi requires the THREEDI_API_HOST configuration value."
            )

        # Get the config variables
        username = user_config.get("THREEDI_API_USERNAME")
        password = user_config.get("THREEDI_API_PASSWORD")
        access_token = user_config.get("THREEDI_API_ACCESS_TOKEN")
        refresh_token = user_config.get("THREEDI_API_REFRESH_TOKEN")
        client_secret = user_config.get("THREEDI_API_CLIENT_SECRET")

        personal_api_token = user_config.get("THREEDI_API_PERSONAL_API_TOKEN")

        basic = all(x for x in (username, password))
        tokens = bool(access_token)
        is_personal_api_token = bool(personal_api_token)

        if sum([basic, tokens, is_personal_api_token]) != 1:
            raise ValueError(
                "ThreediAPI requires either "
                "THREEDI_API_USERNAME and THREEDI_API_PASSWORD or "
                "THREEDI_API_ACCESS_TOKEN and THREEDI_API_REFRESH_TOKEN or "
                "THREEDI_API_PERSONAL_API_TOKEN as "
                "configuration values."
            )

        # Determine whether there is a version in the host
        if host_has_version(host):
            raise ValueError(
                f"Invalid THREEDI_API_HOST '{host}'. The ThreediApi expects that the "
                f"version is not included."
            )

        if is_personal_api_token:
            configuration = Configuration(
                host=host,
                username="__key__",
                password=personal_api_token
            )
        else:
            configuration = Configuration(
                host=host,
                username=username,
                password=password,
                api_key={
                    "Authorization": access_token,
                    "refresh": refresh_token,
                    "client_secret": client_secret,
                },
                api_key_prefix={"Authorization": "Bearer"},
            )
            configuration.refresh_api_key_hook = refresh_api_key

        configuration.retries = retries

        if asynchronous:
            if AsyncApiClient is None:
                raise ImportError(
                    "Please install threedi_api_client with [aio] support to use "
                    "asynchronous mode."
                )
            self._client = AsyncApiClient(configuration)
            if configuration.retries is not None:
                # convert an integer to an ExpontentialRetry instance
                if isinstance(configuration.retries, int):
                    configuration.retries = ExponentialRetry(
                        attempts=configuration.retries
                    )
                # The autogenerated aiohttp client does not handle retries.
                # Inject this function by replacing the pool_manager.
                self._client.rest_client.pool_manager = RetryClient(
                    client_session=self._client.rest_client.pool_manager,
                    retry_options=configuration.retries,
                )
        else:
            if isinstance(configuration.retries, int):
                configuration.retries = urllib3.util.Retry.from_int(
                    configuration.retries
                )
            # This adds 504 to the default status codes:
            if not configuration.retries.status_forcelist:
                configuration.retries.status_forcelist = RETRY_AFTER_STATUS_CODES
            self._client = ApiClient(configuration)

        # Determine what API version to use
        try:
            api_cls = API_VERSIONS[version]
        except KeyError:
            raise ValueError(
                f"Invalid API version '{version}'. Available options are: {set(API_VERSIONS.keys())}."
            )

        self._api = api_cls(self._client)

        self.version = version
        self.asynchronous = asynchronous

    def __getattr__(self, item):
        """Dispatch methods to self._api"""
        return getattr(self._api, item)

    def __dir__(self):
        """Fix autocompletion"""
        return sorted(set(self.__dict__.keys()) | set(dir(self._api)))

    def close(self):
        """Closes the client"""
        return self._client.close()

    def __enter__(self):
        if self.asynchronous:
            raise RuntimeError(
                "'with' used on asynchronous client. Please use 'async with' instead."
            )
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    async def __aenter__(self):
        if not self.asynchronous:
            raise RuntimeError(
                "'async with' used on synchronous client. Please use 'with' instead."
            )
        return self

    async def __aexit__(self, *args, **kwargs):
        await self.close()
