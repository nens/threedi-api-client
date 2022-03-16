from datetime import datetime, timedelta, timezone
from unittest import mock

import jwt
import pytest

from threedi_api_client.auth import (
    AuthenticationError,
    is_token_usable,
    refresh_api_key,
    refresh_oauth2_token,
    refresh_simplejwt_token,
    REFRESH_TIME_DELTA,
)
from threedi_api_client.openapi import Configuration

SECRET_KEY = "abcd1234"


def get_token(claims):
    return jwt.encode(claims, SECRET_KEY, algorithm="HS256")


def get_token_with_expiry(claims, delta_time=None) -> int:
    if delta_time is None:
        delta_time = timedelta(seconds=(REFRESH_TIME_DELTA + 10))
    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    exp = (utc_now + delta_time).replace(tzinfo=timezone.utc).timestamp()

    return get_token({**claims, **{"exp": exp}})


@pytest.fixture
def configuration_username_password():
    return Configuration(host="host", username="harry", password="topsecret")


@pytest.fixture
def configuration_simplejwt():
    return Configuration(
        host="host",
        api_key={"Authorization": get_token({"exp": 0}), "refresh": "my-refresh"},
    )


@pytest.fixture
def configuration_oauth2():
    return Configuration(
        host="host",
        api_key={
            "Authorization": get_token({"iss": "cognito", "exp": 0}),
            "refresh": "my-refresh",
            "client_id": "cid",
        },
    )


def test_is_token_usable_not_expired():
    assert is_token_usable(get_token_with_expiry({"user": "harry"}))


def test_is_token_usable_expired():
    dt = timedelta(seconds=(REFRESH_TIME_DELTA - 10))
    assert not is_token_usable(get_token_with_expiry({"user": "harry"}, dt))


@mock.patch(
    "threedi_api_client.auth.refresh_simplejwt_token", return_value=(None, None)
)
def test_refresh_api_key_hook_username_password(
    refresh_m, configuration_username_password
):
    refresh_api_key(configuration_username_password)
    refresh_m.assert_called_once_with(configuration_username_password)


@mock.patch(
    "threedi_api_client.auth.refresh_simplejwt_token", return_value=(None, None)
)
def test_refresh_api_key_hook_simplejwt(refresh_m, configuration_simplejwt):
    refresh_api_key(configuration_simplejwt)
    refresh_m.assert_called_once_with(configuration_simplejwt)


@mock.patch("threedi_api_client.auth.refresh_oauth2_token", return_value=(None, None))
def test_refresh_api_key_hook_oauth2(refresh_m, configuration_oauth2):
    refresh_api_key(configuration_oauth2)
    refresh_m.assert_called_once_with("cognito", configuration_oauth2)


@mock.patch("threedi_api_client.auth.send_json_request")
def test_refresh_simplejwt_username_password(
    send_json_request, configuration_username_password
):
    send_json_request.return_value = {"access": "a", "refresh": "b"}

    access, refresh = refresh_simplejwt_token(configuration_username_password)

    _, kwargs = send_json_request.call_args
    assert kwargs == {
        "method": "POST",
        "url": "host/v3/auth/token/",
        "body": {"password": "topsecret", "username": "harry"},
    }
    assert access == "a"
    assert refresh == "b"


@mock.patch("threedi_api_client.auth.send_json_request")
def test_refresh_simplejwt_token(send_json_request, configuration_simplejwt):
    send_json_request.return_value = {"access": "a", "refresh": "b"}

    configuration_simplejwt.api_key["refresh"] = get_token_with_expiry({})
    access, refresh = refresh_simplejwt_token(configuration_simplejwt)

    _, kwargs = send_json_request.call_args
    assert kwargs == {
        "method": "POST",
        "url": "host/v3/auth/refresh-token/",
        "body": {"refresh": configuration_simplejwt.api_key["refresh"]},
    }

    assert access == "a"
    assert refresh == "b"


def test_refresh_simplejwt_token_no_refresh(configuration_simplejwt):
    with pytest.raises(AuthenticationError):
        refresh_simplejwt_token(configuration_simplejwt)
