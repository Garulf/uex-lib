"""Transport adapters. The core never imports these; the clients resolve one lazily."""

from __future__ import annotations

from uex._http import AsyncTransport, SyncTransport
from uex.transports.urllib import UrllibTransport


def resolve_sync(timeout: float) -> SyncTransport:
    return UrllibTransport(timeout=timeout)


def resolve_async(timeout: float) -> AsyncTransport:
    try:
        from uex.transports.httpx import AsyncHttpxTransport
    except ImportError:
        pass
    else:
        return AsyncHttpxTransport(timeout=timeout)
    try:
        from uex.transports.aiohttp import AiohttpTransport
    except ImportError:
        pass
    else:
        return AiohttpTransport(timeout=timeout)
    raise ImportError(
        "no async HTTP library found: install uex[httpx] or uex[aiohttp],"
        " or pass transport= to AsyncClient"
    )


__all__ = ["UrllibTransport", "resolve_async", "resolve_sync"]
