"""Async and sync clients. Both drive the same transport-free plans."""

from __future__ import annotations

import time
from collections.abc import Awaitable, Callable, Mapping
from typing import Any

from uex._http import AsyncTransport, SyncTransport
from uex.cache.lru import LruFront
from uex.cache.sqlite import SqliteStore
from uex.cache.store import CacheStore
from uex.client_base import BASE_URL, ClientConfig, Plan, Result
from uex.core.endpoints import ENDPOINTS, Endpoint
from uex.core.namespaces import NAMESPACES
from uex.core.ratelimit import TokenBucket
from uex.core.requests import check_auth, check_requirements, normalize_params
from uex.core.retry import should_retry
from uex.errors import UexError
from uex.models import MODELS
from uex.models.base import Model, ResultMeta

REQUEST_RATE = 120
REQUEST_PER = 60.0


class _Default:
    pass


DEFAULT_CACHE = _Default()


def _default_cache() -> CacheStore:
    return LruFront(SqliteStore())


def _wrap(endpoint: Endpoint, data: Any, meta: ResultMeta) -> Model | list[Model]:
    model_cls = MODELS[endpoint.model]
    if endpoint.single:
        return model_cls.from_payload(data or {}, meta)
    rows = data if isinstance(data, list) else []
    return [model_cls.from_payload(row, meta) for row in rows]


class _ClientCore:
    """Everything both clients share except the transport call itself."""

    def __init__(
        self,
        *,
        cache: CacheStore | _Default | None,
        base_url: str,
        token: str | None,
        secret_key: str | None,
        timeout: float,
        clock: Callable[[], float],
    ) -> None:
        self.config = ClientConfig(
            base_url=base_url, token=token, secret_key=secret_key, timeout=timeout
        )
        self.cache: CacheStore | None = _default_cache() if isinstance(cache, _Default) else cache
        self._clock = clock
        self._bucket = TokenBucket(REQUEST_RATE, REQUEST_PER)

    def plan(self, endpoint: Endpoint, params: Mapping[str, str], *, fresh: bool) -> Plan:
        return Plan(self.config, self.cache, endpoint, params, fresh=fresh, clock=self._clock)

    def purge_cache(self, *, endpoint: str | None = None) -> int:
        """Drop cached entries, optionally only for one endpoint."""
        if self.cache is None:
            return 0
        prefix = None if endpoint is None else f"{endpoint}|"
        return self.cache.purge(prefix=prefix)


class AsyncClient(_ClientCore):
    def __init__(
        self,
        transport: AsyncTransport | None = None,
        *,
        cache: CacheStore | _Default | None = DEFAULT_CACHE,
        base_url: str = BASE_URL,
        token: str | None = None,
        secret_key: str | None = None,
        timeout: float = 20.0,
        clock: Callable[[], float] = time.time,
        sleep: Callable[[float], Awaitable[None]] | None = None,
    ) -> None:
        super().__init__(
            cache=cache,
            base_url=base_url,
            token=token,
            secret_key=secret_key,
            timeout=timeout,
            clock=clock,
        )
        self._transport = transport
        if sleep is None:
            import asyncio

            sleep = asyncio.sleep
        self._sleep = sleep
        for namespace_name, methods in NAMESPACES.items():
            setattr(self, namespace_name, _AsyncNamespace(self, methods))

    def resource(self, endpoint: str) -> _AsyncEndpointCall:
        return _AsyncEndpointCall(self, ENDPOINTS[endpoint])

    async def __aenter__(self) -> AsyncClient:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        if self._transport is not None:
            await self._transport.aclose()
        if self.cache is not None:
            self.cache.close()

    def _get_transport(self) -> AsyncTransport:
        if self._transport is None:
            from uex.transports import resolve_async

            self._transport = resolve_async(self.config.timeout)
        return self._transport

    async def run(self, plan: Plan) -> Result:
        hit = plan.cached()
        if hit is not None:
            return hit
        delay = self._bucket.acquire_delay()
        if delay > 0:
            await self._sleep(delay)
        attempt = 0
        while True:
            try:
                response = await self._get_transport().send(plan.request())
                return plan.accept(response)
            except UexError as exc:
                retry_delay = should_retry(exc, attempt)
                if retry_delay is None:
                    fallback = plan.fallback(exc)
                    if fallback is not None:
                        return fallback
                    raise
                await self._sleep(retry_delay)
                attempt += 1

    async def fetch(self, endpoint: Endpoint, values: Mapping[str, Any], *, fresh: bool) -> Result:
        check_auth(endpoint, token=self.config.token, secret_key=self.config.secret_key)
        params = normalize_params(endpoint, values)
        check_requirements(endpoint, params)
        return await self.run(self.plan(endpoint, params, fresh=fresh))


class _AsyncEndpointCall:
    def __init__(self, client: AsyncClient, endpoint: Endpoint) -> None:
        self.client = client
        self.endpoint = endpoint

    async def __call__(self, *, fresh: bool = False, **kwargs: Any) -> Model | list[Model]:
        data, meta = await self.client.fetch(self.endpoint, kwargs, fresh=fresh)
        return _wrap(self.endpoint, data, meta)


class _AsyncNamespace:
    def __init__(self, client: AsyncClient, methods: Mapping[str, str]) -> None:
        for method_name, endpoint_name in methods.items():
            setattr(self, method_name, _AsyncEndpointCall(client, ENDPOINTS[endpoint_name]))


class Client(_ClientCore):
    def __init__(
        self,
        transport: SyncTransport | None = None,
        *,
        cache: CacheStore | _Default | None = DEFAULT_CACHE,
        base_url: str = BASE_URL,
        token: str | None = None,
        secret_key: str | None = None,
        timeout: float = 20.0,
        clock: Callable[[], float] = time.time,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        super().__init__(
            cache=cache,
            base_url=base_url,
            token=token,
            secret_key=secret_key,
            timeout=timeout,
            clock=clock,
        )
        self._transport = transport
        self._sleep = sleep
        for namespace_name, methods in NAMESPACES.items():
            setattr(self, namespace_name, _SyncNamespace(self, methods))

    def resource(self, endpoint: str) -> _SyncEndpointCall:
        return _SyncEndpointCall(self, ENDPOINTS[endpoint])

    def __enter__(self) -> Client:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def close(self) -> None:
        if self._transport is not None:
            self._transport.close()
        if self.cache is not None:
            self.cache.close()

    def _get_transport(self) -> SyncTransport:
        if self._transport is None:
            from uex.transports import resolve_sync

            self._transport = resolve_sync(self.config.timeout)
        return self._transport

    def run(self, plan: Plan) -> Result:
        hit = plan.cached()
        if hit is not None:
            return hit
        delay = self._bucket.acquire_delay()
        if delay > 0:
            self._sleep(delay)
        attempt = 0
        while True:
            try:
                response = self._get_transport().send(plan.request())
                return plan.accept(response)
            except UexError as exc:
                retry_delay = should_retry(exc, attempt)
                if retry_delay is None:
                    fallback = plan.fallback(exc)
                    if fallback is not None:
                        return fallback
                    raise
                self._sleep(retry_delay)
                attempt += 1

    def fetch(self, endpoint: Endpoint, values: Mapping[str, Any], *, fresh: bool) -> Result:
        check_auth(endpoint, token=self.config.token, secret_key=self.config.secret_key)
        params = normalize_params(endpoint, values)
        check_requirements(endpoint, params)
        return self.run(self.plan(endpoint, params, fresh=fresh))


class _SyncEndpointCall:
    def __init__(self, client: Client, endpoint: Endpoint) -> None:
        self.client = client
        self.endpoint = endpoint

    def __call__(self, *, fresh: bool = False, **kwargs: Any) -> Model | list[Model]:
        data, meta = self.client.fetch(self.endpoint, kwargs, fresh=fresh)
        return _wrap(self.endpoint, data, meta)


class _SyncNamespace:
    def __init__(self, client: Client, methods: Mapping[str, str]) -> None:
        for method_name, endpoint_name in methods.items():
            setattr(self, method_name, _SyncEndpointCall(client, ENDPOINTS[endpoint_name]))
