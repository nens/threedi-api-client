import logging
import re
from pathlib import Path
from typing import BinaryIO, Optional, Tuple
from urllib.parse import urlparse

import aiohttp
import aiofiles

from openapi_client.exceptions import ApiException

CONTENT_RANGE_REGEXP = re.compile(r"^bytes (\d+)-(\d+)/(\d+|\*)$")


logger = logging.getLogger(__name__)


async def download_file(
    url: str,
    target: Path,
    chunk_size: int = 16777216,
    timeout: float = 5.0,
    client: Optional[aiohttp.ClientSession] = None,
) -> Tuple[str, int]:
    """Download a file to a specified path on disk.

    It is assumed that the file server supports multipart downloads (range
    requests).

    Args:
        url: The url to retrieve.
        target: The location to copy to. If this is an existing file, it is
            overwritten. If it is a directory, a filename is generated from
            the filename in the url.
        chunk_size: The number of bytes per request. Default: 16MB.
        timeout: The total timeout in seconds.
        client: If not supplied, a default ClientSession will be created.

    Returns:
        Tuple of file path, total number of uploaded bytes.

    Raises:
        openapi_client.exceptions.ApiException: raised on unexpected server
            responses (HTTP status codes other than 206, 413, 429, 503)
        urllib3.exceptions.HTTPError: various low-level HTTP errors that persist
            after retrying: connection errors, timeouts, decode errors,
            invalid HTTP headers, payload too large (HTTP 413), too many
            requests (HTTP 429), service unavailable (HTTP 503)
    """
    # cast string to Path if necessary
    if isinstance(target, str):
        target = Path(target)

    # if it is a directory, take the filename from the url
    if target.is_dir():
        target = target / urlparse(url)[2].rsplit("/", 1)[-1]

    # open the file
    async with aiofiles.open(target, "wb") as fileobj:
        size = await download_fileobj(
            url, fileobj, chunk_size=chunk_size, timeout=timeout, client=client
        )

    return target, size


async def download_fileobj(
    url: str,
    fileobj: BinaryIO,
    chunk_size: int = 16777216,
    timeout: float = 5.0,
    client: Optional[aiohttp.ClientSession] = None,
) -> int:
    """Download a url to a file object using multiple requests.

    It is assumed that the file server supports multipart downloads (range
    requests).

    Args:
        url: The url to retrieve.
        fileobj: The (binary) file object to write into. It should support
            asynchronous writing.
        chunk_size: The number of bytes per request. Default: 16MB.
        timeout: The total timeout in seconds.
        pool: If not supplied, a default connection pool will be
            created with a retry policy of 3 retries after 1, 2, 4 seconds.

    Returns:
        The total number of downloaded bytes.

    Raises:
        openapi_client.exceptions.ApiException: raised on unexpected server
            responses (HTTP status codes other than 206, 413, 429, 503)
        urllib3.exceptions.HTTPError: various low-level HTTP errors that persist
            after retrying: connection errors, timeouts, decode errors,
            invalid HTTP headers, payload too large (HTTP 413), too many
            requests (HTTP 429), service unavailable (HTTP 503)
    """

    if client is None:
        client_needs_closing = True
        client = aiohttp.ClientSession()
    else:
        client_needs_closing = False

    # Our strategy here is to just start downloading chunks while monitoring
    # the Content-Range header to check if we're done. Although we could get
    # the total Content-Length from a HEAD request, not all servers support
    # that (e.g. Minio).
    try:
        start = 0
        while True:
            # download a chunk
            stop = start + chunk_size - 1
            headers = {"Range": "bytes={}-{}".format(start, stop)}

            response = await client.request(
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
            await fileobj.write(await response.read())

            # parse content-range header (e.g. "bytes 0-3/7") for next iteration
            content_range = response.headers["Content-Range"]
            start, stop, total = [
                int(x) for x in CONTENT_RANGE_REGEXP.findall(content_range)[0]
            ]
            if stop + 1 >= total:
                break
            start += chunk_size

        return total
    finally:
        if client_needs_closing:
            await client.close()
