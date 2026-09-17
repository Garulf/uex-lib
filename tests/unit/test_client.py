from __future__ import annotations

from typing import Any

import pytest

from tests.conftest import (
    AsyncFakeTransport,
    FakeClock,
    FakeTransport,
    ok_response,
)
from uex import AsyncClient, Client, MemoryStore
from uex._http import Response
from uex.errors import AuthRequired, MissingParameter, ServerError
from uex.models import Commodity, GameVersions, Vehicle


class Sleeper:
    def __init__(self) -> None:
        self.calls: list[float] = []

    async def __call__(self, delay: float) -> None:
        self.calls.append(delay)

    def sync(self, delay: float) -> None:
        self.calls.append(delay)


def make_async(
    clock: FakeClock, responses: list[Response], **kw: Any
) -> tuple[AsyncClient, AsyncFakeTransport, Sleeper]:
    transport = AsyncFakeTransport(responses)
    sleeper = Sleeper()
    kw.setdefault("cache", MemoryStore())
    client = AsyncClient(transport, clock=clock, sleep=sleeper, **kw)
    return client, transport, sleeper


def make_sync(
    clock: FakeClock, responses: list[Response], **kw: Any
) -> tuple[Client, FakeTransport, Sleeper]:
    transport = FakeTransport(responses)
    sleeper = Sleeper()
    kw.setdefault("cache", MemoryStore())
    client = Client(transport, clock=clock, sleep=sleeper.sync, **kw)
    return client, transport, sleeper


async def test_get_caches_using_endpoint_ttl(clock: FakeClock) -> None:
    client, transport, _ = make_async(clock, [ok_response([{"slug": "orig-100i"}])])
    ships = await client.vehicles.list(id_company=195)
    assert isinstance(ships, list) and isinstance(ships[0], Vehicle)
    assert ships[0].slug == "orig-100i"
    assert ships[0].meta.cached is False
    assert transport.requests[0].url.endswith("vehicles?id_company=195")
    again = await client.vehicles.list(id_company=195)
    assert again[0].meta.cached is True
    assert len(transport.requests) == 1


async def test_response_max_age_overrides_endpoint_ttl(clock: FakeClock) -> None:
    client, transport, _ = make_async(
        clock,
        [
            ok_response([{"id": 1}], {"Cache-Control": "public, max-age=10"}),
            ok_response([{"id": 1}], {"Cache-Control": "public, max-age=10"}),
        ],
    )
    await client.commodities.list()
    clock.advance(11)
    await client.commodities.list()
    assert len(transport.requests) == 2


async def test_single_object_endpoint_wraps_one_model(clock: FakeClock) -> None:
    client, _, _ = make_async(clock, [ok_response({"live": "4.10.1", "ptu": None})])
    versions = await client.game_versions.current()
    assert isinstance(versions, GameVersions)
    assert versions.live == "4.10.1"


async def test_fresh_bypasses_cache(clock: FakeClock) -> None:
    client, transport, _ = make_async(clock, [ok_response([{"id": 1}]), ok_response([{"id": 1}])])
    await client.commodities.list()
    await client.commodities.list(fresh=True)
    assert len(transport.requests) == 2


async def test_missing_required_param_raises_before_any_request(clock: FakeClock) -> None:
    client, transport, _ = make_async(clock, [])
    with pytest.raises(MissingParameter):
        await client.commodities.prices()
    assert transport.requests == []


async def test_token_endpoint_without_token_raises(clock: FakeClock) -> None:
    client, transport, _ = make_async(clock, [])
    with pytest.raises(AuthRequired):
        await client.organizations.get(id_organization=1)
    assert transport.requests == []


async def test_secret_endpoint_needs_token_and_secret_key(clock: FakeClock) -> None:
    client, transport, _ = make_async(clock, [], token="app-token")
    with pytest.raises(AuthRequired):
        await client.user.wallet_balance()
    assert transport.requests == []


async def test_secret_endpoint_succeeds_with_both_credentials(clock: FakeClock) -> None:
    client, transport, _ = make_async(
        clock, [ok_response({"balance": 500.0})], token="app-token", secret_key="user-secret"
    )
    balance = await client.user.wallet_balance()
    assert balance.balance == 500.0
    req = transport.requests[0]
    assert req.headers["Authorization"] == "Bearer app-token"
    assert req.headers["secret-key"] == "user-secret"


async def test_secret_endpoint_responses_are_never_cached(clock: FakeClock) -> None:
    client, transport, _ = make_async(
        clock,
        [ok_response({"balance": 1.0}), ok_response({"balance": 2.0})],
        token="t",
        secret_key="s",
    )
    await client.user.wallet_balance()
    await client.user.wallet_balance()
    assert len(transport.requests) == 2


async def test_retries_then_stale_fallback(clock: FakeClock) -> None:
    client, transport, sleeper = make_async(clock, [ok_response([{"id": 1}])])
    first = await client.commodities.list()
    assert first[0].id == 1
    clock.advance(10**7)
    for _ in range(3):
        transport.push(Response(500, {}, b""))
    stale = await client.commodities.list()
    assert stale[0].meta.stale is True
    assert sleeper.calls[-2:] == [0.5, 1.5]


async def test_server_error_without_cache_raises_after_retries(clock: FakeClock) -> None:
    client, _, sleeper = make_async(clock, [Response(500, {}, b"")] * 3, cache=None)
    with pytest.raises(ServerError):
        await client.commodities.list()
    assert sleeper.calls == [0.5, 1.5]


async def test_purge_cache_by_endpoint(clock: FakeClock) -> None:
    client, transport, _ = make_async(clock, [ok_response([{"id": 1}]), ok_response([{"id": 1}])])
    await client.commodities.list()
    assert client.purge_cache(endpoint="commodities") == 1
    await client.commodities.list()
    assert len(transport.requests) == 2


async def test_context_manager_closes_transport(clock: FakeClock) -> None:
    client, transport, _ = make_async(clock, [])
    async with client:
        pass
    assert transport.closed


def test_sync_client_mirrors_async(clock: FakeClock) -> None:
    client, transport, _sleeper = make_sync(
        clock, [ok_response([{"code": "AGRI"}]), ok_response([{"code": "AGRI"}])]
    )
    with client:
        first = client.commodities.list()
        assert isinstance(first, list) and isinstance(first[0], Commodity)
        cached = client.commodities.list()
        assert cached[0].meta.cached is True
    assert transport.closed


def test_sync_retry_and_fallback(clock: FakeClock) -> None:
    client, transport, sleeper = make_sync(clock, [ok_response([{"id": 1}])])
    assert client.commodities.list()[0].id == 1
    clock.advance(10**6)
    for _ in range(3):
        transport.push(Response(503, {}, b""))
    assert client.commodities.list()[0].meta.stale is True
    assert sleeper.calls[-2:] == [0.5, 1.5]


def test_cache_none_disables_storage(clock: FakeClock) -> None:
    transport = FakeTransport([ok_response([{"id": 1}]), ok_response([{"id": 1}])])
    client = Client(transport, cache=None, clock=clock)
    client.commodities.list()
    client.commodities.list()
    assert len(transport.requests) == 2
    assert client.purge_cache() == 0
