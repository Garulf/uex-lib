from uex.errors import (
    ApiError,
    AuthRequired,
    InvalidRequest,
    MissingParameter,
    NotFound,
    RateLimited,
    ServerError,
    UexError,
)


def test_hierarchy() -> None:
    assert issubclass(NotFound, ApiError)
    assert issubclass(InvalidRequest, ApiError)
    assert issubclass(RateLimited, ApiError)
    assert issubclass(ServerError, ApiError)
    assert issubclass(ApiError, UexError)
    assert issubclass(AuthRequired, UexError)
    assert issubclass(MissingParameter, (UexError, ValueError))


def test_auth_required_message() -> None:
    exc = AuthRequired("wallet_balance", "secret_key")
    assert "wallet_balance" in str(exc)
    assert "secret_key" in str(exc)


def test_missing_parameter_message() -> None:
    exc = MissingParameter("commodities_prices", "any", ("id_terminal", "id_commodity"))
    assert "id_terminal" in str(exc)
    assert "id_commodity" in str(exc)


def test_rate_limited_defaults() -> None:
    exc = RateLimited()
    assert exc.status == 429
    assert exc.code == "requests_limit_reached"
    assert exc.retry_after is None
