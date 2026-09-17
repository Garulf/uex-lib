from uex.core.endpoints import ENDPOINTS, PUBLIC, SECRET, TOKEN


def test_registers_all_get_endpoints() -> None:
    assert len(ENDPOINTS) == 76


def test_names_match_paths_for_simple_cases() -> None:
    assert ENDPOINTS["commodities"].path == "commodities"
    assert ENDPOINTS["commodities_prices"].path == "commodities_prices"


def test_secret_endpoints_are_all_marked() -> None:
    secret_names = {
        "user_notifications",
        "user_trades",
        "user_refineries_jobs",
        "fleet",
        "wallet_balance",
        "marketplace_favorites",
        "marketplace_negotiations",
        "marketplace_negotiations_messages",
    }
    for name in secret_names:
        assert ENDPOINTS[name].auth == SECRET


def test_token_only_endpoints() -> None:
    for name in ("commodities_averages", "organizations", "data_monitor", "data_info"):
        assert ENDPOINTS[name].auth == TOKEN


def test_most_endpoints_are_public() -> None:
    assert sum(1 for e in ENDPOINTS.values() if e.auth == PUBLIC) == 64


def test_single_object_endpoints() -> None:
    for name in ("game_versions", "data_parameters", "user", "wallet_balance", "organizations"):
        assert ENDPOINTS[name].single is True
