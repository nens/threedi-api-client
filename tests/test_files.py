import io
from unittest import mock

import pytest
from urllib3.response import HTTPResponse

from openapi_client.exceptions import ApiException
from threedi_api_client.files import (download_file, download_fileobj,
                                      upload_file, upload_fileobj)


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


def test_download_fileobj_no_multipart(pool, responses_single):
    """The remote server does not support range requests"""
    responses_single[0].status = 200
    pool.request.side_effect = responses_single

    with pytest.raises(ApiException) as e:
        download_fileobj("some-url", None, chunk_size=64, pool=pool)

    assert e.value.status == 200
    assert e.value.reason == "The file server does not support multipart downloads."


def test_download_fileobj_forbidden(pool, responses_single):
    """The remote server does not support range requests"""
    responses_single[0].status = 403
    pool.request.side_effect = responses_single

    with pytest.raises(ApiException) as e:
        download_fileobj("some-url", None, chunk_size=64, pool=pool)

    assert e.value.status == 403


@mock.patch("threedi_api_client.files.download_fileobj")
def test_download_file(download_fileobj, tmp_path):
    download_file(
        "http://domain/a.b", tmp_path / "c.d", chunk_size=64, timeout=3.0, pool="foo"
    )

    args, kwargs = download_fileobj.call_args
    assert args[0] == "http://domain/a.b"
    assert isinstance(args[1], io.IOBase)
    assert args[1].mode == "wb"
    assert args[1].name == str(tmp_path / "c.d")
    assert kwargs["chunk_size"] == 64
    assert kwargs["timeout"] == 3.0
    assert kwargs["pool"] == "foo"


@mock.patch("threedi_api_client.files.download_fileobj")
def test_download_file_directory(download_fileobj, tmp_path):
    # if a target directory is specified, a filename is created from the url
    download_file("http://domain/a.b", tmp_path, chunk_size=64, timeout=3.0, pool="foo")

    args, kwargs = download_fileobj.call_args
    assert args[1].name == str(tmp_path / "a.b")


@pytest.fixture
def upload_response():
    return HTTPResponse(status=200)


@pytest.fixture
def fileobj():
    stream = io.BytesIO()
    stream.write(b"X" * 39)
    stream.seek(0)
    return stream


def test_upload_fileobj(pool, fileobj, upload_response):
    pool.request.return_value = upload_response
    upload_fileobj("some-url", fileobj, pool=pool)

    # base64.b64encode(hashlib.md5(b"X" * 39).digest()).decode()
    expected_md5 = "Q2zMNJgyazDIkoSqvpOqVg=="
    pool.request.assert_called_with(
        "PUT",
        "some-url",
        body=b"X" * 39,
        headers={"Content-Length": "39", "Content-MD5": expected_md5},
        timeout=5.0,
    )


def test_upload_fileobj_empty_file():
    with pytest.raises(IOError, match="The file object is empty."):
        upload_fileobj("some-url", io.BytesIO())


def test_upload_fileobj_non_binary_file():
    with pytest.raises(IOError, match="The file object is not in binary*"):
        upload_fileobj("some-url", io.StringIO())


def test_upload_fileobj_errors(pool, fileobj, upload_response):
    upload_response.status = 400
    pool.request.return_value = upload_response
    with pytest.raises(ApiException) as e:
        upload_fileobj("some-url", fileobj, pool=pool)

    assert e.value.status == 400


@mock.patch("threedi_api_client.files.upload_fileobj")
def test_upload_file(upload_fileobj, tmp_path):
    path = tmp_path / "myfile"
    with path.open("wb") as f:
        f.write(b"X")

    upload_file("http://domain/a.b", path, timeout=3.0, pool="foo")

    args, kwargs = upload_fileobj.call_args
    assert args[0] == "http://domain/a.b"
    assert isinstance(args[1], io.IOBase)
    assert args[1].mode == "rb"
    assert args[1].name == str(path)
    assert kwargs["timeout"] == 3.0
    assert kwargs["pool"] == "foo"
