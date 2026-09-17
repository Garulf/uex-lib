"""Live checks against the real API. Enable with UEX_NETWORK=1."""

from __future__ import annotations

import json
import os

import pytest

from uex._http import Request
from uex.client_base import USER_AGENT
from uex.transports.aiohttp import AiohttpTransport
from uex.transports.httpx import AsyncHttpxTransport, HttpxTransport
from uex.transports.urllib import UrllibTransport

pytestmark = [
    pytest.mark.network,
    pytest.mark.skipif(os.environ.get("UEX_NETWORK") != "1", reason="set UEX_NETWORK=1"),
]

REQ = Request(
    "GET",
    "https://api.uexcorp.space/2.0/game_versions",
    {"Accept": "application/json", "User-Agent": USER_AGENT},
)


def _check(body: bytes, status: int) -> None:
    assert status == 200
    payload = json.loads(body)
    assert payload["status"] == "ok"
    assert payload["data"]["live"]


def test_urllib_live() -> None:
    res = UrllibTransport().send(REQ)
    _check(res.body, res.status)


def test_httpx_live() -> None:
    t = HttpxTransport()
    res = t.send(REQ)
    t.close()
    _check(res.body, res.status)


async def test_httpx_async_live() -> None:
    t = AsyncHttpxTransport()
    res = await t.send(REQ)
    await t.aclose()
    _check(res.body, res.status)


async def test_aiohttp_live() -> None:
    t = AiohttpTransport()
    res = await t.send(REQ)
    await t.aclose()
    _check(res.body, res.status)
