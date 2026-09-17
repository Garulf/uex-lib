from uex.core.retry import should_retry
from uex.errors import ApiError, InvalidRequest, RateLimited, ServerError, TransportError


def test_rate_limited_retries_once_with_retry_after() -> None:
    exc = RateLimited(retry_after=7.0)
    assert should_retry(exc, 0) == 7.0
    assert should_retry(exc, 1) is None


def test_rate_limited_without_retry_after_uses_default() -> None:
    assert should_retry(RateLimited(), 0) == 0.5


def test_server_error_retries_twice_then_gives_up() -> None:
    exc = ServerError(503)
    assert should_retry(exc, 0) == 0.5
    assert should_retry(exc, 1) == 1.5
    assert should_retry(exc, 2) is None


def test_transport_error_retries() -> None:
    assert should_retry(TransportError("boom"), 0) == 0.5


def test_invalid_request_never_retried() -> None:
    assert should_retry(InvalidRequest(400, "missing_required_input"), 0) is None


def test_generic_api_error_never_retried() -> None:
    assert should_retry(ApiError(418), 0) is None
