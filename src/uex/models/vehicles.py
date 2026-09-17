"""Generated from the UEX API 2.0 documentation. Scalar fields only;
arrays and nested objects stay reachable through ``raw``.
"""

from __future__ import annotations

from dataclasses import dataclass

from uex.models.base import Model


@dataclass(frozen=True)
class Vehicle(Model):
    id: int | None = None
    id_company: int | None = None
    id_parent: int | None = None
    ids_vehicles_loaners: str | None = None
    name: str | None = None
    name_full: str | None = None
    slug: str | None = None
    uuid: str | None = None
    scu: float | None = None
    crew: str | None = None
    mass: float | None = None
    width: float | None = None
    height: float | None = None
    length: float | None = None
    fuel_quantum: float | None = None
    fuel_hydrogen: float | None = None
    container_sizes: str | None = None
    is_addon: bool | None = None
    is_boarding: bool | None = None
    is_bomber: bool | None = None
    is_cargo: bool | None = None
    is_carrier: bool | None = None
    is_civilian: bool | None = None
    is_concept: bool | None = None
    is_construction: bool | None = None
    is_datarunner: bool | None = None
    is_docking: bool | None = None
    is_emp: bool | None = None
    is_exploration: bool | None = None
    is_ground_vehicle: bool | None = None
    is_hangar: bool | None = None
    is_industrial: bool | None = None
    is_interdiction: bool | None = None
    is_loading_dock: bool | None = None
    is_medical: bool | None = None
    is_military: bool | None = None
    is_mining: bool | None = None
    is_passenger: bool | None = None
    is_qed: bool | None = None
    is_racing: bool | None = None
    is_refinery: bool | None = None
    is_refuel: bool | None = None
    is_repair: bool | None = None
    is_research: bool | None = None
    is_salvage: bool | None = None
    is_scanning: bool | None = None
    is_science: bool | None = None
    is_showdown_winner: bool | None = None
    is_spaceship: bool | None = None
    is_starter: bool | None = None
    is_stealth: bool | None = None
    is_tractor_beam: bool | None = None
    is_quantum_capable: bool | None = None
    url_photo: str | None = None
    url_store: str | None = None
    url_brochure: str | None = None
    url_hotsite: str | None = None
    url_video: str | None = None
    pad_type: str | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    company_name: str | None = None


@dataclass(frozen=True)
class VehicleLoaner(Model):
    id: int | None = None
    id_company: int | None = None
    id_parent: int | None = None
    ids_vehicles_loaners: str | None = None
    name: str | None = None
    name_full: str | None = None
    uuid: str | None = None
    scu: int | None = None
    crew: str | None = None
    is_addon: bool | None = None
    is_concept: bool | None = None
    is_civilian: bool | None = None
    is_military: bool | None = None
    is_exploration: bool | None = None
    is_passenger: bool | None = None
    is_industrial: bool | None = None
    is_mining: bool | None = None
    is_salvage: bool | None = None
    is_refinery: bool | None = None
    is_cargo: bool | None = None
    is_medical: bool | None = None
    is_racing: bool | None = None
    is_repair: bool | None = None
    is_refuel: bool | None = None
    is_interdiction: bool | None = None
    is_tractor_beam: bool | None = None
    is_qed: bool | None = None
    is_emp: bool | None = None
    is_construction: bool | None = None
    is_datarunner: bool | None = None
    is_science: bool | None = None
    is_boarding: bool | None = None
    is_stealth: bool | None = None
    is_research: bool | None = None
    is_carrier: bool | None = None
    is_ground_vehicle: bool | None = None
    is_spaceship: bool | None = None
    is_showdown_winner: bool | None = None
    url_store: str | None = None
    url_brochure: str | None = None
    url_hotsite: str | None = None
    url_video: str | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    company_name: str | None = None


@dataclass(frozen=True)
class VehiclePrice(Model):
    id: int | None = None
    id_vehicle: int | None = None
    price: float | None = None
    price_warbond: float | None = None
    price_package: float | None = None
    price_concierge: float | None = None
    on_sale: int | None = None
    on_sale_warbond: int | None = None
    on_sale_package: int | None = None
    on_sale_concierge: int | None = None
    currency: str | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    vehicle_name: str | None = None


@dataclass(frozen=True)
class VehiclePurchasePrice(Model):
    id: int | None = None
    id_vehicle: int | None = None
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
    datarunner: str | None = None
    star_system_name: str | None = None
    planet_name: str | None = None
    orbit_name: str | None = None
    moon_name: str | None = None
    space_station_name: str | None = None
    outpost_name: str | None = None
    city_name: str | None = None
    terminal_name: str | None = None
    terminal_code: str | None = None
    terminal_is_player_owned: int | None = None


@dataclass(frozen=True)
class VehiclePurchasePriceSummary(Model):
    id: int | None = None
    id_vehicle: int | None = None
    id_terminal: int | None = None
    price_buy: float | None = None
    date_added: int | None = None
    date_modified: int | None = None
    vehicle_name: str | None = None
    terminal_name: str | None = None


@dataclass(frozen=True)
class VehicleRentalPrice(Model):
    id: int | None = None
    id_vehicle: int | None = None
    id_star_system: int | None = None
    id_planet: int | None = None
    id_orbit: int | None = None
    id_moon: int | None = None
    id_city: int | None = None
    id_outpost: int | None = None
    id_poi: int | None = None
    id_faction: int | None = None
    id_terminal: int | None = None
    price_rent: float | None = None
    price_rent_min: float | None = None
    price_rent_min_week: float | None = None
    price_rent_min_month: float | None = None
    price_rent_max: float | None = None
    price_rent_max_week: float | None = None
    price_rent_max_month: float | None = None
    price_rent_avg: float | None = None
    price_rent_avg_week: float | None = None
    price_rent_avg_month: float | None = None
    faction_affinity: int | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    datarunner: str | None = None
    star_system_name: str | None = None
    planet_name: str | None = None
    orbit_name: str | None = None
    moon_name: str | None = None
    space_station_name: str | None = None
    outpost_name: str | None = None
    city_name: str | None = None
    terminal_name: str | None = None
    terminal_code: str | None = None
    terminal_is_player_owned: int | None = None


@dataclass(frozen=True)
class VehicleRentalPriceSummary(Model):
    id: int | None = None
    id_vehicle: int | None = None
    id_terminal: int | None = None
    price_rent: float | None = None
    date_added: int | None = None
    date_modified: int | None = None
    vehicle_name: str | None = None
    terminal_name: str | None = None
