import io
from unittest import mock

import pytest
from urllib3.response import HTTPResponse

from threedi_api_client.files import download_file, download_fileobj


@pytest.fixture
def pool():
    pool = mock.Mock()
    return pool


@pytest.fixture
def responses_single():
    return [
        HTTPResponse(
            body=b"X" * 42,
            headers={"Content-Range": "bytes 0-41/42"},
            status=206,
        )
    ]


@pytest.fixture
def responses_double():
    return [
        HTTPResponse(
            body=b"X" * 64,
            headers={"Content-Range": "bytes 0-63/65"},
            status=206,
        ),
        HTTPResponse(
            body=b"X",
            headers={"Content-Range": "bytes 64-64/65"},
            status=206,
        ),
    ]


def test_download_fileobj(pool, responses_single):
    stream = io.BytesIO()
    pool.request.side_effect = responses_single
    download_fileobj("some-url", stream, chunk_size=64, pool=pool)

    pool.request.assert_called_with(
        "GET",
        "some-url",
        headers={"Range": "bytes=0-63"},
        timeout=5.0,
    )
    assert stream.tell() == 42


def test_download_fileobj_two_chunks(pool, responses_double):
    stream = io.BytesIO()
    pool.request.side_effect = responses_double
    download_fileobj("some-url", stream, chunk_size=64, pool=pool)

    (_, kwargs1), (_, kwargs2) = pool.request.call_args_list
    assert kwargs1["headers"] == {"Range": "bytes=0-63"}
    assert kwargs2["headers"] == {"Range": "bytes=64-127"}
    assert stream.tell() == 65
