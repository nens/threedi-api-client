import io
from unittest import mock

import pytest
import asyncio

from threedi_api_client.aio.files import download_fileobj, download_file
from openapi_client.exceptions import ApiException
from aiofiles.threadpool import AsyncBufferedIOBase


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


# https://stackoverflow.com/questions/29881236/how-to-mock-asyncio-coroutines
def get_mock_coro(*return_values):
    values = iter(return_values)

    @asyncio.coroutine
    def mock_coro(*args, **kwargs):
        return next(values)

    return mock.Mock(wraps=mock_coro)


@pytest.fixture
async def client():
    # mimics aiohttp.ClientSession
    client = mock.Mock()
    return client


@pytest.fixture
async def responses_single():
    # mimics aiohttp.ClientResponse
    response = mock.Mock()
    response.headers = {"Content-Range": "bytes 0-41/42"}
    response.status = 206
    response.read = get_mock_coro(b"X" * 42)
    return [response]


@pytest.fixture
async def responses_double():
    # mimics aiohttp.ClientResponse
    response1 = mock.Mock()
    response1.headers = {"Content-Range": "bytes 0-63/65"}
    response1.status = 206
    response1.read = get_mock_coro(b"X" * 64)
    response2 = mock.Mock()
    response2.headers = {"Content-Range": "bytes 64-64/65"}
    response2.status = 206
    response2.read = get_mock_coro(b"X")
    return [response1, response2]


@pytest.mark.asyncio
async def test_download_fileobj(client, responses_single):
    stream = AsyncBytesIO()
    client.request.side_effect = get_mock_coro(*responses_single)
    await download_fileobj("some-url", stream, chunk_size=64, client=client)

    client.request.assert_called_with(
        "GET",
        "some-url",
        headers={"Range": "bytes=0-63"},
        timeout=5.0,
    )
    assert await stream.tell() == 42


@pytest.mark.asyncio
async def test_download_fileobj_two_chunks(client, responses_double):
    stream = AsyncBytesIO()
    client.request.side_effect = get_mock_coro(*responses_double)
    await download_fileobj("some-url", stream, chunk_size=64, client=client)

    (_, kwargs1), (_, kwargs2) = client.request.call_args_list
    assert kwargs1["headers"] == {"Range": "bytes=0-63"}
    assert kwargs2["headers"] == {"Range": "bytes=64-127"}
    assert await stream.tell() == 65


@pytest.mark.asyncio
async def test_download_fileobj_no_multipart(client, responses_single):
    """The remote server does not support range requests"""
    responses_single[0].status = 200
    client.request.side_effect = get_mock_coro(*responses_single)

    with pytest.raises(ApiException) as e:
        await download_fileobj("some-url", None, chunk_size=64, client=client)

    assert e.value.status == 200
    assert e.value.reason == "The file server does not support multipart downloads."


@pytest.mark.asyncio
async def test_download_fileobj_forbidden(client, responses_single):
    """The remote server does not support range requests"""
    responses_single[0].status = 403
    client.request.side_effect = get_mock_coro(*responses_single)

    with pytest.raises(ApiException) as e:
        await download_fileobj("some-url", None, chunk_size=64, client=client)

    assert e.value.status == 403


@pytest.fixture
async def mocked_download_fileobj():
    download_fileobj = get_mock_coro(None)
    with mock.patch(
        "threedi_api_client.aio.files.download_fileobj", new=download_fileobj
    ):
        yield download_fileobj


@pytest.mark.asyncio
async def test_download_file(tmp_path, mocked_download_fileobj):
    await download_file(
        "http://domain/a.b", tmp_path / "c.d", chunk_size=64, timeout=3.0, client="foo"
    )

    args, kwargs = mocked_download_fileobj.call_args
    assert args[0] == "http://domain/a.b"
    assert isinstance(args[1], AsyncBufferedIOBase)
    assert args[1].mode == "wb"
    assert args[1].name == str(tmp_path / "c.d")
    assert kwargs["chunk_size"] == 64
    assert kwargs["timeout"] == 3.0
    assert kwargs["client"] == "foo"


@pytest.mark.asyncio
async def test_download_file_directory(mocked_download_fileobj, tmp_path):
    # if a target directory is specified, a filename is created from the url
    await download_file(
        "http://domain/a.b", tmp_path, chunk_size=64, timeout=3.0, client="foo"
    )

    args, kwargs = mocked_download_fileobj.call_args
    assert args[1].name == str(tmp_path / "a.b")
