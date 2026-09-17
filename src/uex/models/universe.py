"""Generated from the UEX API 2.0 documentation. Scalar fields only;
arrays and nested objects stay reachable through ``raw``.
"""

from __future__ import annotations

from dataclasses import dataclass

from uex.models.base import Model


@dataclass(frozen=True)
class StarSystem(Model):
    id: int | None = None
    id_faction: int | None = None
    id_jurisdiction: int | None = None
    name: str | None = None
    code: str | None = None
    is_available: bool | None = None
    is_available_live: bool | None = None
    is_visible: bool | None = None
    is_default: bool | None = None
    wiki: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    faction_name: str | None = None
    jurisdiction_name: str | None = None


@dataclass(frozen=True)
class Planet(Model):
    id: int | None = None
    id_star_system: int | None = None
    id_faction: int | None = None
    id_jurisdiction: int | None = None
    name: str | None = None
    name_origin: str | None = None
    code: str | None = None
    is_available: bool | None = None
    is_available_live: bool | None = None
    is_visible: bool | None = None
    is_default: bool | None = None
    is_lagrange: bool | None = None
    date_added: int | None = None
    date_modified: int | None = None
    star_system_name: str | None = None
    faction_name: str | None = None
    jurisdiction_name: str | None = None


@dataclass(frozen=True)
class Moon(Model):
    id: int | None = None
    id_star_system: int | None = None
    id_planet: int | None = None
    id_orbit: int | None = None
    id_faction: int | None = None
    id_jurisdiction: int | None = None
    name: str | None = None
    name_origin: str | None = None
    code: str | None = None
    is_available: bool | None = None
    is_available_live: bool | None = None
    is_visible: bool | None = None
    is_default: bool | None = None
    date_added: int | None = None
    date_modified: int | None = None
    star_system_name: str | None = None
    planet_name: str | None = None
    orbit_name: str | None = None
    faction_name: str | None = None
    jurisdiction_name: str | None = None


@dataclass(frozen=True)
class Orbit(Model):
    id: int | None = None
    id_star_system: int | None = None
    id_faction: int | None = None
    id_jurisdiction: int | None = None
    name: str | None = None
    name_origin: str | None = None
    code: str | None = None
    is_available: bool | None = None
    is_available_live: bool | None = None
    is_visible: bool | None = None
    is_default: bool | None = None
    is_lagrange: bool | None = None
    is_man_made: bool | None = None
    is_asteroid: bool | None = None
    is_planet: bool | None = None
    is_star: bool | None = None
    is_jump_point: bool | None = None
    date_added: int | None = None
    date_modified: int | None = None
    star_system_name: str | None = None
    faction_name: str | None = None
    jurisdiction_name: str | None = None


@dataclass(frozen=True)
class OrbitDistance(Model):
    id: int | None = None
    id_star_system: int | None = None
    id_star_system_origin: int | None = None
    id_star_system_destination: int | None = None
    id_orbit_origin: int | None = None
    id_orbit_destination: int | None = None
    distance: float | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    star_system_name: str | None = None
    orbit_origin_name: str | None = None
    orbit_destination_name: str | None = None


@dataclass(frozen=True)
class SpaceStation(Model):
    id: int | None = None
    id_star_system: int | None = None
    id_planet: int | None = None
    id_orbit: int | None = None
    id_moon: int | None = None
    id_city: int | None = None
    id_faction: int | None = None
    id_jurisdiction: int | None = None
    name: str | None = None
    nickname: str | None = None
    is_available: bool | None = None
    is_available_live: bool | None = None
    is_visible: bool | None = None
    is_default: bool | None = None
    is_monitored: bool | None = None
    is_armistice: bool | None = None
    is_landable: bool | None = None
    is_decommissioned: bool | None = None
    is_lagrange: bool | None = None
    is_jump_point: bool | None = None
    has_quantum_marker: bool | None = None
    has_trade_terminal: bool | None = None
    has_habitation: bool | None = None
    has_refinery: bool | None = None
    has_cargo_center: bool | None = None
    has_clinic: bool | None = None
    has_food: bool | None = None
    has_shops: bool | None = None
    has_refuel: bool | None = None
    has_repair: bool | None = None
    has_gravity: bool | None = None
    has_loading_dock: bool | None = None
    has_docking_port: bool | None = None
    has_freight_elevator: bool | None = None
    pad_types: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    star_system_name: str | None = None
    planet_name: str | None = None
    orbit_name: str | None = None
    city_name: str | None = None
    faction_name: str | None = None
    jurisdiction_name: str | None = None


@dataclass(frozen=True)
class City(Model):
    id: int | None = None
    id_star_system: int | None = None
    id_planet: int | None = None
    id_orbit: int | None = None
    id_moon: int | None = None
    id_faction: int | None = None
    id_jurisdiction: int | None = None
    name: str | None = None
    code: str | None = None
    is_available: bool | None = None
    is_available_live: bool | None = None
    is_visible: bool | None = None
    is_default: bool | None = None
    is_monitored: bool | None = None
    is_armistice: bool | None = None
    is_landable: bool | None = None
    is_decommissioned: bool | None = None
    has_quantum_marker: bool | None = None
    has_trade_terminal: bool | None = None
    has_habitation: bool | None = None
    has_refinery: bool | None = None
    has_cargo_center: bool | None = None
    has_clinic: bool | None = None
    has_food: bool | None = None
    has_shops: bool | None = None
    has_refuel: bool | None = None
    has_repair: bool | None = None
    has_gravity: bool | None = None
    has_loading_dock: bool | None = None
    has_docking_port: bool | None = None
    has_freight_elevator: bool | None = None
    pad_types: str | None = None
    wiki: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    star_system_name: str | None = None
    planet_name: str | None = None
    orbit_name: str | None = None
    moon_name: str | None = None
    faction_name: str | None = None
    jurisdiction_name: str | None = None


@dataclass(frozen=True)
class Outpost(Model):
    id: int | None = None
    id_star_system: int | None = None
    id_planet: int | None = None
    id_orbit: int | None = None
    id_moon: int | None = None
    id_faction: int | None = None
    id_jurisdiction: int | None = None
    name: str | None = None
    nickname: str | None = None
    is_available: bool | None = None
    is_available_live: bool | None = None
    is_visible: bool | None = None
    is_default: bool | None = None
    is_monitored: bool | None = None
    is_armistice: bool | None = None
    is_landable: bool | None = None
    is_decommissioned: bool | None = None
    has_quantum_marker: bool | None = None
    has_trade_terminal: bool | None = None
    has_habitation: bool | None = None
    has_refinery: bool | None = None
    has_cargo_center: bool | None = None
    has_clinic: bool | None = None
    has_food: bool | None = None
    has_shops: bool | None = None
    has_refuel: bool | None = None
    has_repair: bool | None = None
    has_gravity: bool | None = None
    has_loading_dock: bool | None = None
    has_docking_port: bool | None = None
    has_freight_elevator: bool | None = None
    pad_types: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    star_system_name: str | None = None
    planet_name: str | None = None
    orbit_name: str | None = None
    moon_name: str | None = None
    faction_name: str | None = None
    jurisdiction_name: str | None = None


@dataclass(frozen=True)
class PointOfInterest(Model):
    id: int | None = None
    id_star_system: int | None = None
    id_planet: int | None = None
    id_orbit: int | None = None
    id_moon: int | None = None
    id_space_station: int | None = None
    id_city: int | None = None
    id_outpost: int | None = None
    id_faction: int | None = None
    id_jurisdiction: int | None = None
    name: str | None = None
    nickname: str | None = None
    is_available: bool | None = None
    is_available_live: bool | None = None
    is_visible: bool | None = None
    is_default: bool | None = None
    is_monitored: bool | None = None
    is_armistice: bool | None = None
    is_landable: bool | None = None
    is_decommissioned: bool | None = None
    is_mining_related: bool | None = None
    has_quantum_marker: bool | None = None
    has_trade_terminal: bool | None = None
    has_habitation: bool | None = None
    has_refinery: bool | None = None
    has_cargo_center: bool | None = None
    has_clinic: bool | None = None
    has_food: bool | None = None
    has_shops: bool | None = None
    has_refuel: bool | None = None
    has_repair: bool | None = None
    has_gravity: bool | None = None
    has_loading_dock: bool | None = None
    has_docking_port: bool | None = None
    has_freight_elevator: bool | None = None
    pad_types: str | None = None
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
    jurisdiction_name: str | None = None


@dataclass(frozen=True)
class JumpPoint(Model):
    id: int | None = None
    id_star_system_origin: int | None = None
    id_star_system_destination: int | None = None
    id_orbit_origin: int | None = None
    id_orbit_destination: int | None = None
    star_system_name_origin: str | None = None
    star_system_name_destination: str | None = None
    orbit_name_origin: str | None = None
    orbit_name_destination: str | None = None
    date_added: int | None = None
    date_modified: int | None = None


@dataclass(frozen=True)
class Jurisdiction(Model):
    id: int | None = None
    id_faction: int | None = None
    name: str | None = None
    nickname: str | None = None
    is_available: bool | None = None
    is_available_live: bool | None = None
    is_visible: bool | None = None
    is_default: bool | None = None
    wiki: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    faction_name: str | None = None


@dataclass(frozen=True)
class Faction(Model):
    id: int | None = None
    ids_star_systems: int | None = None
    ids_factions_friendly: str | None = None
    ids_factions_hostile: str | None = None
    name: str | None = None
    wiki: str | None = None
    is_piracy: bool | None = None
    is_bounty_hunting: bool | None = None
    date_added: int | None = None
    date_modified: int | None = None


@dataclass(frozen=True)
class Company(Model):
    id: int | None = None
    id_faction: int | None = None
    name: str | None = None
    nickname: str | None = None
    wiki: str | None = None
    industry: str | None = None
    is_item_manufacturer: bool | None = None
    is_vehicle_manufacturer: bool | None = None
    date_added: int | None = None
    date_modified: int | None = None


@dataclass(frozen=True)
class Contact(Model):
    id: int | None = None
    id_star_system: int | None = None
    id_planet: int | None = None
    id_orbit: int | None = None
    id_moon: int | None = None
    id_space_station: int | None = None
    id_city: int | None = None
    id_outpost: int | None = None
    id_poi: int | None = None
    id_faction: int | None = None
    id_company: int | None = None
    id_jurisdiction: int | None = None
    name: str | None = None
    description: str | None = None
    is_available: bool | None = None
    is_available_live: bool | None = None
    is_visible: bool | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    star_system_name: str | None = None
    planet_name: str | None = None
    orbit_name: str | None = None
    moon_name: str | None = None
    space_station_name: str | None = None
    city_name: str | None = None
    outpost_name: str | None = None
    poi_name: str | None = None
    faction_name: str | None = None
    company_name: str | None = None
    jurisdiction_name: str | None = None


@dataclass(frozen=True)
class Contract(Model):
    id: int | None = None
    id_parent: int | None = None
    id_star_system: int | None = None
    id_planet: int | None = None
    id_orbit: int | None = None
    id_moon: int | None = None
    id_space_station: int | None = None
    id_city: int | None = None
    id_outpost: int | None = None
    id_poi: int | None = None
    id_faction: int | None = None
    id_company: int | None = None
    id_jurisdiction: int | None = None
    id_contact: int | None = None
    name: str | None = None
    description: str | None = None
    payout: float | None = None
    is_available: bool | None = None
    is_available_live: bool | None = None
    is_visible: bool | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    star_system_name: str | None = None
    planet_name: str | None = None
    orbit_name: str | None = None
    moon_name: str | None = None
    space_station_name: str | None = None
    city_name: str | None = None
    outpost_name: str | None = None
    poi_name: str | None = None
    faction_name: str | None = None
    company_name: str | None = None
    jurisdiction_name: str | None = None
    contact_name: str | None = None
    contact_description: str | None = None
