from uex.links import trade_route_detail_url, trade_routes_url


def test_matches_the_documented_example() -> None:
    url = trade_routes_url(id_vehicle=147, investment=20000)
    assert url == "https://uexcorp.space/trade/routes/?id_vehicle=147&investment=20%2C000"


def test_no_filters_returns_bare_finder_url() -> None:
    assert trade_routes_url() == "https://uexcorp.space/trade/routes/"


def test_string_filters_are_passed_through() -> None:
    url = trade_routes_url(commodity="agricium", terminal_origin="area-18")
    assert "commodity=agricium" in url
    assert "terminal_origin=area-18" in url


def test_bool_filters_become_1_or_0() -> None:
    url = trade_routes_url(is_loop=True, is_on_ground=False)
    assert "is_loop=1" in url
    assert "is_on_ground=0" in url


def test_none_filters_are_omitted() -> None:
    url = trade_routes_url(id_vehicle=None, investment=5000)
    assert "id_vehicle" not in url
    assert "investment=5%2C000" in url


def test_large_numbers_get_thousands_separators() -> None:
    url = trade_routes_url(distance=1234567)
    assert "distance=1%2C234%2C567" in url


def test_route_detail_url_from_code() -> None:
    assert trade_route_detail_url("9db9ca68") == "https://uexcorp.space/trade/route?code=9db9ca68"
