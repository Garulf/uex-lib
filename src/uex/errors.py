from __future__ import annotations


class UexError(Exception):
    """Base class for every error raised by uex."""


class TransportError(UexError):
    """The HTTP transport could not complete the request."""


class CacheError(UexError):
    """The cache store failed."""


class AuthRequired(UexError):
    """The endpoint needs a credential the client was not given."""

    def __init__(self, endpoint: str, credential: str) -> None:
        self.endpoint = endpoint
        self.credential = credential
        super().__init__(f"{endpoint} requires {credential}; pass {credential}= to the client")


class MissingParameter(UexError, ValueError):
    """The endpoint's required query parameters were not supplied."""

    def __init__(self, endpoint: str, mode: str, names: tuple[str, ...]) -> None:
        self.endpoint = endpoint
        self.names = names
        joined = ", ".join(names)
        wording = "at least one of" if mode == "any" else "all of"
        super().__init__(f"{endpoint} requires {wording}: {joined}")


class ApiError(UexError):
    def __init__(
        self,
        status: int,
        code: str | None = None,
        message: str | None = None,
        body: bytes = b"",
    ) -> None:
        self.status = status
        self.code = code
        self.body = body
        super().__init__(message or f"API returned HTTP {status}" + (f" ({code})" if code else ""))


class NotFound(ApiError):
    def __init__(self, endpoint: str) -> None:
        self.endpoint = endpoint
        super().__init__(404, message=f"{endpoint}: not found")


class InvalidRequest(ApiError):
    """The API rejected the request; ``code`` is its status string."""

    def __init__(self, status: int, code: str, message: str = "", body: bytes = b"") -> None:
        text = f"API rejected the request: {code}" + (f" ({message})" if message else "")
        super().__init__(status, code, text, body)


class RateLimited(ApiError):
    def __init__(self, retry_after: float | None = None, body: bytes = b"") -> None:
        self.retry_after = retry_after
        super().__init__(429, "requests_limit_reached", "rate limited by the API", body)


class ServerError(ApiError):
    def __init__(self, status: int, code: str | None = None, body: bytes = b"") -> None:
        super().__init__(status, code, f"API server error HTTP {status}", body)
