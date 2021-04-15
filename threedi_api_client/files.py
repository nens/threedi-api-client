import logging
import re
from pathlib import Path
from typing import BinaryIO, Optional, Tuple
from urllib.parse import urlparse

import urllib3

from openapi_client.exceptions import ApiException

CONTENT_RANGE_REGEXP = re.compile(r"^bytes (\d+)-(\d+)/(\d+|\*)$")


logger = logging.getLogger(__name__)


def get_pool(retries: int = 3, backoff_factor: int = 1) -> urllib3.PoolManager:
    """Create a PoolManager with a retry policy.

    The default retry policy has 3 retries with 1, 2, 4 second intervals.

    Args:
        retries: Total number of retries per request
        backoff_factor: Multiplier for retry delay times (1, 2, 4, ...)
    """
    return urllib3.PoolManager(
        retries=urllib3.util.retry.Retry(retries, backoff_factor=backoff_factor)
    )


def download_file(
    url: str,
    target: Path,
    chunk_size: int = 16777216,
    timeout: float = 5.0,
    pool: Optional[urllib3.PoolManager] = None,
) -> Tuple[str, int]:
    """Download a file to a specified path on disk.

    It is assumed that the file server supports multipart downloads (range
    requests).

    Args:
        url: The url to retrieve.
        target: The location to copy to. If this is an existing file, it is
            overwritten. If it is a directory, a filename is generated from
            the filename in the url.
        chunk_size: numer of bytes per request. Default: 16MB.
        timeout: the total timeout in seconds
        pool: an optional PoolManager. if not given, a default one will be
            created with a retry policy of 3 retries after 1, 2, 4 seconds.

    Returns:
        tuple of file path, total file size in bytes

    Raises:
        openapi_client.exceptions.ApiException: raised on unexpected server
            responses (HTTP status codes other than 206, 413, 429, 503)
        urllib3.exceptions.HTTPError: various low-level HTTP errors that persist
            after retrying: connection errors, timeouts, decode errors,
            invalid HTTP headers, payload too large (HTTP 413), too many
            requests (HTTP 429), service unavailable (HTTP 503)
    """
    # cast string to Path if necessary
    target = Path(target)

    # if it is a directory, take the filename from the url
    if target.is_dir():
        target = target / urlparse(url)[2].rsplit("/", 1)[-1]

    # open the file
    with target.open("wb") as fileobj:
        size = download_fileobj(
            url, fileobj, chunk_size=chunk_size, timeout=timeout, pool=pool
        )

    return target, size


def download_fileobj(
    url: str,
    fileobj: BinaryIO,
    chunk_size: int = 16777216,
    timeout: float = 5.0,
    pool: Optional[urllib3.PoolManager] = None,
) -> int:
    """Download a url to a file object using multiple requests.

    It is assumed that the file server supports multipart downloads (range
    requests).

    Args:
        url: the url to retrieve
        filename: the file location to copy to.
        chunk_size: numer of bytes per request. Default: 16MB.
        timeout: the total timeout in seconds
        pool: an optional PoolManager. if not given, a default one will be
            created with a retry policy of 3 retries after 1, 2, 4 seconds.

    Returns:
        total file size in bytes

    Raises:
        openapi_client.exceptions.ApiException: raised on unexpected server
            responses (HTTP status codes other than 206, 413, 429, 503)
        urllib3.exceptions.HTTPError: various low-level HTTP errors that persist
            after retrying: connection errors, timeouts, decode errors,
            invalid HTTP headers, payload too large (HTTP 413), too many
            requests (HTTP 429), service unavailable (HTTP 503)
    """
    if pool is None:
        pool = get_pool()

    # Our strategy here is to just start downloading chunks while monitoring
    # the Content-Range header to check if we're done. Although we could get
    # the total Content-Length from a HEAD request, not all servers support
    # that (e.g. Minio).
    start = 0
    while True:
        # download a chunk
        stop = start + chunk_size - 1
        headers = {"Range": f"bytes={start}-{stop}"}

        # Send the request and get the data with the openapi-generator
        # ApiClient instance. It will raise on non-2XX responses.
        response = pool.request(
            "GET",
            url,
            headers=headers,
            timeout=timeout,
        )
        if response.status == 200:
            raise ApiException(
                status=200,
                reason="The file server does not support multipart downloads.",
            )
        elif response.status != 206:
            raise ApiException(http_resp=response)

        # write to file
        fileobj.write(response.data)

        # parse content-range header (e.g. "bytes 0-3/7") for next iteration
        content_range = response.headers["Content-Range"]
        start, stop, total = [
            int(x) for x in CONTENT_RANGE_REGEXP.findall(content_range)[0]
        ]
        if stop + 1 >= total:
            break
        start += chunk_size

    return total
