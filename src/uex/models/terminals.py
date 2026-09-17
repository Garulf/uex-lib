"""Generated from the UEX API 2.0 documentation. Scalar fields only;
arrays and nested objects stay reachable through ``raw``.
"""

from __future__ import annotations

from dataclasses import dataclass

from uex.models.base import Model


@dataclass(frozen=True)
class Terminal(Model):
    id: int | None = None
    id_star_system: int | None = None
    id_planet: int | None = None
    id_orbit: int | None = None
    id_moon: int | None = None
    id_space_station: int | None = None
    id_outpost: int | None = None
    id_poi: int | None = None
    id_city: int | None = None
    id_faction: int | None = None
    id_company: int | None = None
    name: str | None = None
    fullname: str | None = None
    nickname: str | None = None
    displayname: str | None = None
    code: str | None = None
    type: str | None = None
    contact_url: str | None = None
    screenshot: str | None = None
    screenshot_full: str | None = None
    screenshot_author: str | None = None
    mcs: int | None = None
    is_available: bool | None = None
    is_available_live: bool | None = None
    is_visible: bool | None = None
    is_default_system: bool | None = None
    is_affinity_influenceable: bool | None = None
    is_habitation: bool | None = None
    is_refinery: bool | None = None
    is_cargo_center: bool | None = None
    is_medical: bool | None = None
    is_food: bool | None = None
    is_shop_fps: bool | None = None
    is_shop_vehicle: bool | None = None
    is_refuel: bool | None = None
    is_repair: bool | None = None
    is_nqa: bool | None = None
    is_jump_point: bool | None = None
    is_player_owned: bool | None = None
    is_auto_load: bool | None = None
    has_loading_dock: bool | None = None
    has_docking_port: bool | None = None
    has_freight_elevator: bool | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    star_system_name: str | None = None
    planet_name: str | None = None
    orbit_name: str | None = None
    moon_name: str | None = None
    space_station_name: str | None = None
    outpost_name: str | None = None
    city_name: str | None = None
    faction_name: str | None = None
    company_name: str | None = None
    max_container_size: int | None = None


@dataclass(frozen=True)
class TerminalDistance(Model):
    orbit_name_origin: str | None = None
    terminal_name_origin: str | None = None
    terminal_nickname_origin: str | None = None
    terminal_code_origin: str | None = None
    orbit_name_destination: str | None = None
    terminal_name_destination: str | None = None
    terminal_nickname_destination: str | None = None
    terminal_code_destination: str | None = None
    distance: float | None = None
