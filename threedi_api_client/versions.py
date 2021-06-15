import re

from .openapi import V3Api

API_VERSIONS = {
    "v3": V3Api,
}

try:
    from .openapi import V3AlphaApi
    API_VERSIONS["v3-alpha"] = V3AlphaApi
except ImportError:
    pass


try:
    from .openapi import V3BetaApi
    API_VERSIONS["v3-beta"] = V3BetaApi
except ImportError:
    pass



VERSION_REGEX = re.compile(r"(.*)\/v[0-9./]+$")


def host_has_version(host: str):
    return bool(VERSION_REGEX.findall(host))


def host_remove_version(host: str):
    matches = VERSION_REGEX.findall(host)
    if matches:
        return matches[0]
    else:
        return host
