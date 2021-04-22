import asyncio
import base64
import hashlib
import logging
import re
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import urlparse

import aiofiles
import aiohttp

from openapi_client.exceptions import ApiException

CONTENT_RANGE_REGEXP = re.compile(r"^bytes (\d+)-(\d+)/(\d+|\*)$")


logger = logging.getLogger(__name__)


async def download_file(
    url: str,
    target: Path,
    chunk_size: int = 16777216,
    timeout: float = 5.0,
    client: Optional[aiohttp.ClientSession] = None,
    executor: Optional[ThreadPoolExecutor] = None,
) -> Tuple[Path, int]:
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
        executor: The ThreadPoolExecutor to execute local
            file I/O in. If not supplied, default executor is used.

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
    async with aiofiles.open(target, "wb", executor=executor) as fileobj:
        size = await download_fileobj(
            url, fileobj, chunk_size=chunk_size, timeout=timeout, client=client
        )

    return target, size


async def download_fileobj(
    url: str,
    fileobj,
    chunk_size: int = 16777216,
    timeout: float = 5.0,
    client: Optional[aiohttp.ClientSession] = None,
) -> int:
    """Download a url to a file object using multiple requests.

    It is assumed that the file server supports multipart downloads (range
    requests).

    Args:
        url: The url to retrieve.
        fileobj: The (binary) file object to write into, supporting async I/O.
        chunk_size: The number of bytes per request. Default: 16MB.
        timeout: The total timeout in seconds.
        client: If not supplied, a default ClientSession will be created.

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


async def upload_file(
    url: str,
    file_path: Path,
    chunk_size: int = 16777216,
    timeout: float = 5.0,
    client: Optional[aiohttp.ClientSession] = None,
    md5: Optional[bytes] = None,
    executor: Optional[ThreadPoolExecutor] = None,
) -> int:
    """Upload a file at specified file path to a url.

    The upload is accompanied by an MD5 hash so that the file server checks
    the integrity of the file.

    Args:
        url: The url to upload to.
        file_path: The file path to read data from.
        chunk_size: The size of the chunk in the streaming upload. Note that this
            function does not do multipart upload. Default: 16MB.
        timeout: The total timeout in seconds.
        client: If not supplied, a default ClientSession will be created.
        md5: The MD5 digest (binary) of the file. Supply the MD5 if you already
            have access to it. Otherwise this function will compute it for you.
        executor: The ThreadPoolExecutor to execute local file I/O and MD5 hashing
            in. If not supplied, default executor is used.

    Returns:
        The total number of uploaded bytes.

    Raises:
        IOError: Raised if the provided file is incompatible or empty.
        openapi_client.exceptions.ApiException: raised on unexpected server
            responses (HTTP status codes other than 206, 413, 429, 503)
        urllib3.exceptions.HTTPError: various low-level HTTP errors that persist
            after retrying: connection errors, timeouts, decode errors,
            invalid HTTP headers, payload too large (HTTP 413), too many
            requests (HTTP 429), service unavailable (HTTP 503)
    """
    # cast string to Path if necessary
    if isinstance(file_path, str):
        file_path = Path(file_path)

    # open the file
    async with aiofiles.open(file_path, "rb", executor=executor) as fileobj:
        size = await upload_fileobj(
            url,
            fileobj,
            chunk_size=chunk_size,
            timeout=timeout,
            client=client,
            md5=md5,
            executor=executor,
        )

    return size


async def _iter_chunks(fileobj, chunk_size: int):
    """Yield chunks from a file stream"""
    assert chunk_size > 0
    while True:
        data = await fileobj.read(chunk_size)
        if len(data) == 0:
            break
        yield data


async def _compute_md5(
    fileobj,
    chunk_size: int,
    executor: Optional[ThreadPoolExecutor] = None,
):
    """Return the md5 digest for given fileobj."""
    loop = asyncio.get_running_loop()

    await fileobj.seek(0)
    hasher = hashlib.md5()
    async for chunk in _iter_chunks(fileobj, chunk_size=chunk_size):
        # From python docs: the Python GIL is released for data larger than
        # 2047 bytes at object creation or on update.
        # So it makes sense to do the hasher updates in a threadpool.
        await loop.run_in_executor(executor, partial(hasher.update, chunk))
    return await loop.run_in_executor(executor, hasher.digest)


async def upload_fileobj(
    url: str,
    fileobj,
    chunk_size: int = 16777216,
    timeout: float = 5.0,
    client: Optional[aiohttp.ClientSession] = None,
    md5: Optional[bytes] = None,
    executor: Optional[ThreadPoolExecutor] = None,
) -> int:
    """Upload a file object to a url.

    The upload is accompanied by an MD5 hash so that the file server checks
    the integrity of the file.

    Args:
        url: The url to upload to.
        fileobj: The (binary) file object to read from.
        chunk_size: The size of the chunk in the streaming upload. Note that this
            function does not do multipart upload. Default: 16MB.
        timeout: The total timeout in seconds.
        client: If not supplied, a default ClientSession will be created.
        md5: The MD5 digest (binary) of the file. Supply the MD5 if you already
            have access to it. Otherwise this function will compute it for you.
        executor: The ThreadPoolExecutor to execute local MD5 hashing
            in. If not supplied, default executor is used.

    Returns:
        The total number of uploaded bytes.

    Raises:
        IOError: Raised if the provided file is incompatible or empty.
        openapi_client.exceptions.ApiException: raised on unexpected server
            responses (HTTP status codes other than 206, 413, 429, 503)
        urllib3.exceptions.HTTPError: various low-level HTTP errors that persist
            after retrying: connection errors, timeouts, decode errors,
            invalid HTTP headers, payload too large (HTTP 413), too many
            requests (HTTP 429), service unavailable (HTTP 503)
    """
    # There are two ways to upload in S3 (Minio):
    # - PutObject: put the whole object in one time
    # - multipart upload: requires presigned urls for every part
    # We can only do the first option as we have no other presigned urls.
    # So we take the first option, but we do stream the request body in chunks.

    # We will get hard to understand tracebacks if the fileobj is not
    # in binary mode. So use a trick to see if fileobj is in binary mode:
    if not isinstance(await fileobj.read(0), bytes):
        raise IOError(
            "The file object is not in binary mode. Please open with mode='rb'."
        )

    file_size = await fileobj.seek(0, 2)  # go to EOF
    if file_size == 0:
        raise IOError("The file object is empty.")

    # For computing the MD5 we need to do an extra pass on the file.
    if md5 is None:
        md5 = await _compute_md5(fileobj, chunk_size, executor=executor)

    if client is None:
        client_needs_closing = True
        client = aiohttp.ClientSession()
    else:
        client_needs_closing = False

    try:
        await fileobj.seek(0)
        async_iterable = _iter_chunks(fileobj, chunk_size=chunk_size)
        # Tested: both Content-Length and Content-MD5 are checked by Minio
        headers = {
            "Content-Length": str(file_size),
            "Content-MD5": base64.b64encode(md5).decode(),
        }
        response = await client.request(
            "PUT",
            url,
            data=async_iterable,
            headers=headers,
            timeout=timeout,
        )
        if response.status != 200:
            raise ApiException(status=response.status, reason=response.reason)

        return file_size
    finally:
        if client_needs_closing:
            await client.close()
