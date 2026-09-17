"""Build links to the UEX Corp website, not the API.

These are plain URL builders with no network calls of their own; they exist
because the site's query strings (comma-formatted numbers, specific filter
names) aren't obvious from the API alone.
"""

from __future__ import annotations

from urllib.parse import urlencode

TRADE_ROUTES_URL = "https://uexcorp.space/trade/routes/"
TRADE_ROUTE_DETAIL_URL = "https://uexcorp.space/trade/route"


def _format_value(value: object) -> str:
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, int | float):
        return f"{value:,.0f}" if float(value).is_integer() else f"{value:,}"
    return str(value)


def trade_routes_url(
    *,
    id_vehicle: int | None = None,
    investment: int | float | None = None,
    id_faction: int | None = None,
    id_star_system_origin: int | None = None,
    id_star_system_destination: int | None = None,
    terminal_origin: str | None = None,
    terminal_destination: str | None = None,
    orbit_origin: str | None = None,
    orbit_destination: str | None = None,
    commodity: str | None = None,
    scu: int | None = None,
    distance: int | float | None = None,
    weight: int | float | None = None,
    stops: int | None = None,
    mcs: int | None = None,
    sort_by: str | None = None,
    is_loop: bool | None = None,
    is_average: bool | None = None,
    is_favorite: bool | None = None,
    is_monitored: bool | None = None,
    is_on_ground: bool | None = None,
    is_player_owned: bool | None = None,
    is_predictable: bool | None = None,
    is_space_station: bool | None = None,
    is_auto_load: bool | None = None,
    is_nqa: bool | None = None,
    has_loading_dock: bool | None = None,
    has_refuel: bool | None = None,
    safe_commodities: bool | None = None,
) -> str:
    """Build a link to the UEX trade route finder, pre-filled with filters.

    Numeric filters are formatted with thousands separators the way the site's
    own form renders them, e.g. ``investment=20000`` becomes ``investment=20,000``
    (percent-encoded to ``20%2C000`` in the final URL).
    """
    filters = {
        "id_vehicle": id_vehicle,
        "investment": investment,
        "id_faction": id_faction,
        "id_star_system_origin": id_star_system_origin,
        "id_star_system_destination": id_star_system_destination,
        "terminal_origin": terminal_origin,
        "terminal_destination": terminal_destination,
        "orbit_origin": orbit_origin,
        "orbit_destination": orbit_destination,
        "commodity": commodity,
        "scu": scu,
        "distance": distance,
        "weight": weight,
        "stops": stops,
        "mcs": mcs,
        "sort_by": sort_by,
        "is_loop": is_loop,
        "is_average": is_average,
        "is_favorite": is_favorite,
        "is_monitored": is_monitored,
        "is_on_ground": is_on_ground,
        "is_player_owned": is_player_owned,
        "is_predictable": is_predictable,
        "is_space_station": is_space_station,
        "is_auto_load": is_auto_load,
        "is_nqa": is_nqa,
        "has_loading_dock": has_loading_dock,
        "has_refuel": has_refuel,
        "safe_commodities": safe_commodities,
    }
    params = {k: _format_value(v) for k, v in filters.items() if v is not None}
    if not params:
        return TRADE_ROUTES_URL
    return f"{TRADE_ROUTES_URL}?{urlencode(params)}"


def trade_route_detail_url(code: str) -> str:
    """Build a link to one specific route, by the ``code`` a routes lookup returns."""
    return f"{TRADE_ROUTE_DETAIL_URL}?{urlencode({'code': code})}"
