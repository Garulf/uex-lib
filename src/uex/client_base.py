"""Transport-free fetch plan shared by the async and sync clients.

Driver loop (implemented once per client in ``client.py``):

1. Unless ``fresh``, return ``plan.cached()`` when it yields a fresh entry.
2. Send ``plan.request()`` with retries per ``should_retry``; on success
   return ``plan.accept(response)``.
3. On final failure return ``plan.fallback(exc)`` if it yields a stale entry,
   otherwise raise.
"""

from __future__ import annotations

import time
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any

from uex import __version__
from uex._http import Request, Response
from uex.cache.entry import Entry
from uex.cache.keys import make_key
from uex.cache.store import CacheStore
from uex.core.endpoints import SECRET, Endpoint
from uex.core.parse import parse_response
from uex.core.requests import build_request
from uex.errors import UexError
from uex.models.base import ResultMeta

BASE_URL = "https://api.uexcorp.space/2.0"
USER_AGENT = f"uex-lib/{__version__} (+https://github.com/Garulf/uex-lib)"

Result = tuple[Any, ResultMeta]


@dataclass(frozen=True)
class ClientConfig:
    base_url: str = BASE_URL
    user_agent: str = USER_AGENT
    token: str | None = None
    secret_key: str | None = None
    timeout: float = 20.0


class Plan:
    """One logical fetch: a list, a single object, or a mixed-shape endpoint."""

    def __init__(
        self,
        config: ClientConfig,
        cache: CacheStore | None,
        endpoint: Endpoint,
        params: Mapping[str, str],
        *,
        fresh: bool = False,
        clock: Callable[[], float] = time.time,
    ) -> None:
        self.config = config
        self.cache = cache
        self.endpoint = endpoint
        self.params = params
        self.fresh = fresh
        self.clock = clock
        self.key = make_key(endpoint.name, params)

    def cacheable(self) -> bool:
        return self.endpoint.ttl is not None and self.endpoint.auth != SECRET

    def _meta(self, *, cached: bool, stale: bool, fetched_at: float) -> ResultMeta:
        return ResultMeta(
            endpoint=self.endpoint.name, cached=cached, stale=stale, fetched_at=fetched_at
        )

    def cached(self) -> Result | None:
        if self.cache is None or self.fresh or not self.cacheable():
            return None
        entry = self.cache.get(self.key)
        if entry is None or not entry.is_fresh(self.clock()):
            return None
        return entry.payload, self._meta(cached=True, stale=False, fetched_at=entry.stored_at)

    def request(self) -> Request:
        return build_request(
            self.config.base_url,
            self.endpoint,
            self.params,
            user_agent=self.config.user_agent,
            token=self.config.token,
            secret_key=self.config.secret_key,
        )

    def accept(self, response: Response) -> Result:
        parsed = parse_response(response, endpoint=self.endpoint.name)
        now = self.clock()
        if self.cacheable() and self.cache is not None:
            ttl = self.endpoint.ttl
            seconds = parsed.max_age if parsed.max_age is not None else ttl.total_seconds()  # type: ignore[union-attr]
            self.cache.put(self.key, Entry(parsed.data, stored_at=now, expires_at=now + seconds))
        return parsed.data, self._meta(cached=False, stale=False, fetched_at=now)

    def fallback(self, exc: UexError) -> Result | None:
        if self.cache is None:
            return None
        entry = self.cache.get(self.key)
        if entry is None:
            return None
        return entry.payload, self._meta(cached=True, stale=True, fetched_at=entry.stored_at)
