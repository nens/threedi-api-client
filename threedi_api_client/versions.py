import re

from .openapi import V3AlphaApi, V3Api

API_VERSIONS = {
    "v3": V3Api,
    "v3-alpha": V3AlphaApi,
}


def host_has_version(host: str):
    return bool(re.findall(r"(.*)\/v[0-9]+.*", host))


def host_remove_version(host: str):
    matches = re.findall(r"(.*)\/v[0-9]+.*", host)
    if matches:
        return matches[0]
    else:
        return host
