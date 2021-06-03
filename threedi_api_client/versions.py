import re

from .openapi import V3AlphaApi, V3Api

API_VERSIONS = {
    "v3": V3Api,
    "v3-alpha": V3AlphaApi,
}

VERSION_REGEX = re.compile(r"(.*)\/v[0-9./]$")


def host_has_version(host: str):
    return bool(VERSION_REGEX.findall(host))


def host_remove_version(host: str):
    matches = VERSION_REGEX.findall(host)
    if matches:
        return matches[0]
    else:
        return host
