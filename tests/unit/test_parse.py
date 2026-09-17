from __future__ import annotations

import json

import pytest

from uex._http import Response
from uex.core.parse import parse_response
from uex.errors import ApiError, InvalidRequest, NotFound, RateLimited, ServerError

HTML = b"<html><title>Page Not Found - 404 - UEX</title></html>"


def _ok(data: object, headers: dict[str, str] | None = None) -> Response:
    body = json.dumps({"status": "ok", "http_code": 200, "data": data, "message": ""}).encode()
    return Response(200, headers or {}, body)


def test_ok_payload_returns_data() -> None:
    parsed = parse_response(_ok([{"id": 1}]), endpoint="commodities")
    assert parsed.data == [{"id": 1}]


def test_max_age_parsed_from_cache_control() -> None:
    parsed = parse_response(
        _ok({}, {"Cache-Control": "public, max-age=1800, must-revalidate"}), endpoint="commodities"
    )
    assert parsed.max_age == 1800.0


def test_missing_cache_control_gives_no_max_age() -> None:
    parsed = parse_response(_ok({}), endpoint="commodities")
    assert parsed.max_age is None


def test_404_raises_not_found() -> None:
    with pytest.raises(NotFound) as exc:
        parse_response(Response(404, {}, HTML), endpoint="nope")
    assert exc.value.endpoint == "nope"


def test_429_status_code_raises_rate_limited() -> None:
    body = json.dumps({"status": "requests_limit_reached", "http_code": 429, "data": None}).encode()
    with pytest.raises(RateLimited):
        parse_response(Response(429, {}, body), endpoint="commodities")


def test_envelope_rate_limit_status_without_http_429() -> None:
    body = json.dumps({"status": "requests_limit_reached", "http_code": 200, "data": None}).encode()
    with pytest.raises(RateLimited):
        parse_response(Response(200, {}, body), endpoint="commodities")


def test_5xx_raises_server_error() -> None:
    with pytest.raises(ServerError) as exc:
        parse_response(Response(503, {}, b"down"), endpoint="commodities")
    assert exc.value.status == 503


def test_missing_required_input_raises_invalid_request() -> None:
    body = json.dumps(
        {"status": "missing_required_input", "http_code": 400, "data": None, "message": "Missing"}
    ).encode()
    with pytest.raises(InvalidRequest) as exc:
        parse_response(Response(400, {}, body), endpoint="commodities_prices")
    assert exc.value.code == "missing_required_input"


def test_non_json_200_raises_api_error() -> None:
    with pytest.raises(ApiError):
        parse_response(Response(200, {}, HTML), endpoint="commodities")


def test_retry_after_header_is_read() -> None:
    body = json.dumps({"status": "requests_limit_reached", "http_code": 429, "data": None}).encode()
    with pytest.raises(RateLimited) as exc:
        parse_response(Response(429, {"Retry-After": "3"}, body), endpoint="commodities")
    assert exc.value.retry_after == 3.0
