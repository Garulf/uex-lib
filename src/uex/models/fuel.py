"""Generated from the UEX API 2.0 documentation. Scalar fields only;
arrays and nested objects stay reachable through ``raw``.
"""

from __future__ import annotations

from dataclasses import dataclass

from uex.models.base import Model


@dataclass(frozen=True)
class FuelPrice(Model):
    id: int | None = None
    id_commodity: int | None = None
    id_star_system: int | None = None
    id_planet: int | None = None
    id_orbit: int | None = None
    id_moon: int | None = None
    id_city: int | None = None
    id_outpost: int | None = None
    id_poi: int | None = None
    id_faction: int | None = None
    id_terminal: int | None = None
    price_buy: float | None = None
    price_buy_min: float | None = None
    price_buy_min_week: float | None = None
    price_buy_min_month: float | None = None
    price_buy_max: float | None = None
    price_buy_max_week: float | None = None
    price_buy_max_month: float | None = None
    price_buy_avg: float | None = None
    price_buy_avg_week: float | None = None
    price_buy_avg_month: float | None = None
    faction_affinity: int | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    commodity_name: str | None = None
    commodity_code: str | None = None
    commodity_slug: str | None = None
    star_system_name: str | None = None
    planet_name: str | None = None
    orbit_name: str | None = None
    moon_name: str | None = None
    space_station_name: str | None = None
    outpost_name: str | None = None
    city_name: str | None = None
    terminal_name: str | None = None
    terminal_code: str | None = None
    terminal_slug: str | None = None
    terminal_mcs: int | None = None


@dataclass(frozen=True)
class FuelPriceSummary(Model):
    id: int | None = None
    id_commodity: int | None = None
    id_terminal: int | None = None
    price_buy: float | None = None
    price_buy_avg: float | None = None
    date_added: int | None = None
    date_modified: int | None = None
    commodity_name: str | None = None
    commodity_code: str | None = None
    commodity_slug: str | None = None
    terminal_name: str | None = None
    terminal_code: str | None = None
    terminal_slug: str | None = None
