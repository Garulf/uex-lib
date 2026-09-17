"""Generated from the UEX API 2.0 documentation. Scalar fields only;
arrays and nested objects stay reachable through ``raw``.
"""

from __future__ import annotations

from dataclasses import dataclass

from uex.models.base import Model


@dataclass(frozen=True)
class RefineryMethod(Model):
    id: int | None = None
    name: str | None = None
    code: str | None = None
    rating_yield: int | None = None
    rating_cost: int | None = None
    rating_speed: int | None = None
    date_added: int | None = None
    date_modified: int | None = None


@dataclass(frozen=True)
class RefineryYield(Model):
    id: int | None = None
    id_commodity: int | None = None
    id_star_system: int | None = None
    id_planet: int | None = None
    id_orbit: int | None = None
    id_moon: int | None = None
    id_space_station: int | None = None
    id_city: int | None = None
    id_outpost: int | None = None
    id_poi: int | None = None
    id_faction: int | None = None
    id_terminal: int | None = None
    id_report: int | None = None
    value: int | None = None
    value_week: int | None = None
    value_month: int | None = None
    date_added: int | None = None
    date_modified: int | None = None
    commodity_name: str | None = None
    star_system_name: str | None = None
    planet_name: str | None = None
    orbit_name: str | None = None
    moon_name: str | None = None
    space_station_name: str | None = None
    city_name: str | None = None
    outpost_name: str | None = None
    terminal_name: str | None = None


@dataclass(frozen=True)
class RefineryCapacity(Model):
    id: int | None = None
    id_commodity: int | None = None
    id_star_system: int | None = None
    id_planet: int | None = None
    id_orbit: int | None = None
    id_moon: int | None = None
    id_space_station: int | None = None
    id_city: int | None = None
    id_outpost: int | None = None
    id_poi: int | None = None
    id_faction: int | None = None
    id_terminal: int | None = None
    id_report: int | None = None
    value: int | None = None
    value_week: int | None = None
    value_month: int | None = None
    date_added: int | None = None
    date_modified: int | None = None
    star_system_name: str | None = None
    planet_name: str | None = None
    orbit_name: str | None = None
    moon_name: str | None = None
    space_station_name: str | None = None
    city_name: str | None = None
    outpost_name: str | None = None
    terminal_name: str | None = None


@dataclass(frozen=True)
class RefineryAudit(Model):
    id: int | None = None
    id_commodity: int | None = None
    id_star_system: int | None = None
    id_planet: int | None = None
    id_orbit: int | None = None
    id_moon: int | None = None
    id_space_station: int | None = None
    id_city: int | None = None
    id_outpost: int | None = None
    id_poi: int | None = None
    id_faction: int | None = None
    id_terminal: int | None = None
    yield_: int | None = None
    capacity: int | None = None
    method: int | None = None
    quantity: int | None = None
    quantity_yield: int | None = None
    quantity_inert: int | None = None
    total_cost: int | None = None
    total_time: int | None = None
    date_added: int | None = None
    date_reported: int | None = None
    game_version: str | None = None
    datarunner: str | None = None
    commodity_name: str | None = None
    star_system_name: str | None = None
    planet_name: str | None = None
    orbit_name: str | None = None
    moon_name: str | None = None
    space_station_name: str | None = None
    city_name: str | None = None
    outpost_name: str | None = None
    terminal_name: str | None = None
