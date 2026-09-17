"""Generated from the UEX API 2.0 documentation. Scalar fields only;
arrays and nested objects stay reachable through ``raw``.
"""

from __future__ import annotations

from dataclasses import dataclass

from uex.models.base import Model


@dataclass(frozen=True)
class Item(Model):
    id: int | None = None
    id_parent: int | None = None
    id_category: int | None = None
    id_company: int | None = None
    id_vehicle: int | None = None
    name: str | None = None
    section: str | None = None
    category: str | None = None
    company_name: str | None = None
    vehicle_name: str | None = None
    slug: str | None = None
    size: str | None = None
    uuid: str | None = None
    color: str | None = None
    color2: str | None = None
    url_store: str | None = None
    wiki: str | None = None
    quality: int | None = None
    is_exclusive_pledge: bool | None = None
    is_exclusive_subscriber: bool | None = None
    is_exclusive_concierge: bool | None = None
    is_commodity: bool | None = None
    is_harvestable: bool | None = None
    screenshot: str | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_modified: int | None = None


@dataclass(frozen=True)
class ItemAttribute(Model):
    id: int | None = None
    id_item: int | None = None
    id_category: int | None = None
    id_category_attribute: int | None = None
    category_name: str | None = None
    item_name: str | None = None
    item_uuid: str | None = None
    item_wiki: str | None = None
    attribute_name: str | None = None
    value: str | None = None
    unit: str | None = None
    date_added: int | None = None
    date_modified: int | None = None


@dataclass(frozen=True)
class ItemPrice(Model):
    id: int | None = None
    id_item: int | None = None
    id_parent: int | None = None
    id_category: int | None = None
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
    price_sell: float | None = None
    price_sell_min: float | None = None
    price_sell_min_week: float | None = None
    price_sell_min_month: float | None = None
    price_sell_max: float | None = None
    price_sell_max_week: float | None = None
    price_sell_max_month: float | None = None
    price_sell_avg: float | None = None
    price_sell_avg_week: float | None = None
    price_sell_avg_month: float | None = None
    durability: float | None = None
    durability_min: float | None = None
    durability_min_week: float | None = None
    durability_min_month: float | None = None
    durability_max: float | None = None
    durability_max_week: float | None = None
    durability_max_month: float | None = None
    durability_avg: float | None = None
    durability_avg_week: float | None = None
    durability_avg_month: float | None = None
    faction_affinity: int | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    item_name: str | None = None
    item_wiki: str | None = None
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
class ItemPriceSummary(Model):
    id: int | None = None
    id_item: int | None = None
    id_terminal: int | None = None
    id_category: int | None = None
    price_buy: float | None = None
    price_sell: float | None = None
    date_added: int | None = None
    date_modified: int | None = None
    item_name: str | None = None
    item_uuid: str | None = None
    terminal_name: str | None = None
