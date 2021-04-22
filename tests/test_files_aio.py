import io
from unittest import mock

import pytest

from threedi_api_client.aio.files import download_fileobj, download_file
from openapi_client.exceptions import ApiException
from aiofiles.threadpool import AsyncBufferedIOBase
from mock import AsyncMock


class AsyncBytesIO:
    """Just for testing, dumb async version of BytesIO"""

    def __init__(self):
        self._io = io.BytesIO()

    async def tell(self, *args, **kwargs):
        return self._io.tell(*args, **kwargs)

    async def seek(self, *args, **kwargs):
        return self._io.seek(*args, **kwargs)

    async def read(self, *args, **kwargs):
        return self._io.read(*args, **kwargs)

    async def write(self, *args, **kwargs):
        return self._io.write(*args, **kwargs)


@pytest.fixture
async def aio_request():
    with mock.patch("aiohttp.ClientSession.request", new_callable=AsyncMock) as aio_request:
        yield aio_request


@pytest.fixture
async def responses_single():
    # mimics aiohttp.ClientResponse
    response = mock.Mock()
    response.headers = {"Content-Range": "bytes 0-41/42"}
    response.status = 206
    response.read = AsyncMock(return_value=b"X" * 42)
    return [response]


@pytest.fixture
async def responses_double():
    # mimics aiohttp.ClientResponse
    response1 = mock.Mock()
    response1.headers = {"Content-Range": "bytes 0-63/65"}
    response1.status = 206
    response1.read = AsyncMock(return_value=b"X" * 64)
    response2 = mock.Mock()
    response2.headers = {"Content-Range": "bytes 64-64/65"}
    response2.status = 206
    response2.read = AsyncMock(return_value=b"X")
    return [response1, response2]


@pytest.mark.asyncio
async def test_download_fileobj(aio_request, responses_single):
    stream = AsyncBytesIO()
    aio_request.side_effect = responses_single

    await download_fileobj("some-url", stream, chunk_size=64)

    aio_request.assert_called_with(
        "GET",
        "some-url",
        headers={"Range": "bytes=0-63"},
        timeout=5.0,
    )
    assert await stream.tell() == 42


@pytest.mark.asyncio
async def test_download_fileobj_two_chunks(aio_request, responses_double):
    stream = AsyncBytesIO()
    aio_request.side_effect = responses_double

    await download_fileobj("some-url", stream, chunk_size=64)

    (_, kwargs1), (_, kwargs2) = aio_request.call_args_list
    assert kwargs1["headers"] == {"Range": "bytes=0-63"}
    assert kwargs2["headers"] == {"Range": "bytes=64-127"}
    assert await stream.tell() == 65


@pytest.mark.asyncio
async def test_download_fileobj_no_multipart(aio_request, responses_single):
    """The remote server does not support range requests"""
    responses_single[0].status = 200
    aio_request.side_effect = responses_single

    with pytest.raises(ApiException) as e:
        await download_fileobj("some-url", None, chunk_size=64)

    assert e.value.status == 200
    assert e.value.reason == "The file server does not support multipart downloads."


@pytest.mark.asyncio
async def test_download_fileobj_forbidden(aio_request, responses_single):
    """The remote server does not support range requests"""
    responses_single[0].status = 403
    aio_request.side_effect = responses_single

    with pytest.raises(ApiException) as e:
        await download_fileobj("some-url", None, chunk_size=64)

    assert e.value.status == 403


@pytest.mark.asyncio
@mock.patch(
        "threedi_api_client.aio.files.download_fileobj", new_callable=AsyncMock
    )
async def test_download_file(mocked_download_fileobj, tmp_path):
    await download_file(
        "http://domain/a.b", tmp_path / "c.d", chunk_size=64, timeout=3.0, connector="foo"
    )

    args, kwargs = mocked_download_fileobj.call_args
    assert args[0] == "http://domain/a.b"
    assert isinstance(args[1], AsyncBufferedIOBase)
    assert args[1].mode == "wb"
    assert args[1].name == str(tmp_path / "c.d")
    assert kwargs["chunk_size"] == 64
    assert kwargs["timeout"] == 3.0
    assert kwargs["connector"] == "foo"


@pytest.mark.asyncio
@mock.patch(
        "threedi_api_client.aio.files.download_fileobj", new_callable=AsyncMock
    )
async def test_download_file_directory(mocked_download_fileobj, tmp_path):
    # if a target directory is specified, a filename is created from the url
    await download_file(
        "http://domain/a.b", tmp_path, chunk_size=64, timeout=3.0, connector="foo"
    )

    args, kwargs = mocked_download_fileobj.call_args
    assert args[1].name == str(tmp_path / "a.b")
