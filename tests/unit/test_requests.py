from __future__ import annotations

import pytest

from uex.core.endpoints import ENDPOINTS
from uex.core.requests import build_request, check_auth, check_requirements, normalize_params
from uex.errors import AuthRequired, MissingParameter


def test_normalize_drops_none_and_stringifies() -> None:
    ep = ENDPOINTS["commodities_prices"]
    out = normalize_params(ep, {"id_terminal": 1, "id_commodity": None})
    assert out == {"id_terminal": "1"}


def test_normalize_joins_multi_ids() -> None:
    ep = ENDPOINTS["commodities_prices"]
    out = normalize_params(ep, {"id_terminal": [1, 2, 3]})
    assert out == {"id_terminal": "1,2,3"}


def test_normalize_rejects_too_many_multi_ids() -> None:
    ep = ENDPOINTS["commodities_prices"]
    with pytest.raises(ValueError, match="at most 10"):
        normalize_params(ep, {"id_terminal": list(range(11))})


def test_normalize_coerces_bools() -> None:
    ep = ENDPOINTS["companies"]
    out = normalize_params(ep, {"is_item_manufacturer": True})
    assert out == {"is_item_manufacturer": "1"}


def test_check_requirements_any_satisfied() -> None:
    ep = ENDPOINTS["commodities_prices"]
    check_requirements(ep, {"id_terminal": "1"})


def test_check_requirements_any_missing_raises() -> None:
    ep = ENDPOINTS["commodities_prices"]
    with pytest.raises(MissingParameter):
        check_requirements(ep, {})


def test_check_requirements_all_missing_raises() -> None:
    ep = ENDPOINTS["polls_audit"]
    with pytest.raises(MissingParameter):
        check_requirements(ep, {})


def test_check_requirements_none_needed() -> None:
    ep = ENDPOINTS["commodities"]
    check_requirements(ep, {})


def test_check_auth_public_needs_nothing() -> None:
    check_auth(ENDPOINTS["commodities"], token=None, secret_key=None)


def test_check_auth_token_endpoint_requires_token() -> None:
    with pytest.raises(AuthRequired):
        check_auth(ENDPOINTS["organizations"], token=None, secret_key=None)
    check_auth(ENDPOINTS["organizations"], token="t", secret_key=None)


def test_check_auth_secret_endpoint_requires_both() -> None:
    ep = ENDPOINTS["wallet_balance"]
    with pytest.raises(AuthRequired):
        check_auth(ep, token=None, secret_key=None)
    with pytest.raises(AuthRequired):
        check_auth(ep, token="t", secret_key=None)
    check_auth(ep, token="t", secret_key="s")


def test_build_request_adds_auth_headers_and_sorts_params() -> None:
    ep = ENDPOINTS["commodities_prices"]
    req = build_request(
        "https://api.uexcorp.space/2.0",
        ep,
        {"id_terminal": "1", "id_commodity": "2"},
        user_agent="ua",
        token="tok",
        secret_key="sec",
    )
    assert (
        req.url == "https://api.uexcorp.space/2.0/commodities_prices?id_commodity=2&id_terminal=1"
    )
    assert req.headers["Authorization"] == "Bearer tok"
    assert req.headers["secret-key"] == "sec"


def test_build_request_without_auth_omits_headers() -> None:
    ep = ENDPOINTS["commodities"]
    req = build_request(
        "https://api.uexcorp.space/2.0", ep, {}, user_agent="ua", token=None, secret_key=None
    )
    assert "Authorization" not in req.headers
    assert "secret-key" not in req.headers
    assert req.url == "https://api.uexcorp.space/2.0/commodities"
