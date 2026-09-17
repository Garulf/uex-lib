"""Generated from the UEX API 2.0 documentation. Scalar fields only;
arrays and nested objects stay reachable through ``raw``.
"""

from __future__ import annotations

from dataclasses import dataclass

from uex.models.base import Model


@dataclass(frozen=True)
class MarketplaceListing(Model):
    id: int | None = None
    id_category: int | None = None
    id_item: int | None = None
    id_star_system: int | None = None
    id_terminal: int | None = None
    id_organization: int | None = None
    operation: str | None = None
    type: str | None = None
    slug: str | None = None
    title: str | None = None
    description: str | None = None
    unit: str | None = None
    price: float | None = None
    price_old: float | None = None
    currency: str | None = None
    language: str | None = None
    location: str | None = None
    source: str | None = None
    availability: str | None = None
    durability: str | None = None
    quality: str | None = None
    in_stock: int | None = None
    is_sold_out: bool | None = None
    user_name: str | None = None
    user_username: str | None = None
    user_avatar: str | None = None
    total_views: int | None = None
    total_negotiations: int | None = None
    votes: int | None = None
    photos: str | None = None
    video_url: str | None = None
    hours_expiration: int | None = None
    date_added: int | None = None
    date_approved: int | None = None
    date_expiration: int | None = None


@dataclass(frozen=True)
class MarketplaceAverage(Model):
    id: int | None = None
    id_item: int | None = None
    id_category: int | None = None
    quality_tier: int | None = None
    quality_count: int | None = None
    currency: str | None = None
    price_buy: float | None = None
    price_buy_week: float | None = None
    price_buy_month: float | None = None
    price_sell: float | None = None
    price_sell_week: float | None = None
    price_sell_month: float | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    item_name: str | None = None


@dataclass(frozen=True)
class MarketplaceAverageSummary(Model):
    id: int | None = None
    id_item: int | None = None
    id_category: int | None = None
    quality_tier: int | None = None
    quality_count: int | None = None
    currency: str | None = None
    price_buy: float | None = None
    price_sell: float | None = None
    date_added: int | None = None
    date_modified: int | None = None
    item_name: str | None = None
    item_uuid: str | None = None


@dataclass(frozen=True)
class MarketplaceFavorite(Model):
    id: int | None = None
    id_listing: int | None = None
    date_added: int | None = None
    operation: str | None = None
    type: str | None = None
    slug: str | None = None
    category: str | None = None
    title: str | None = None
    description: str | None = None
    unit: str | None = None
    price: float | None = None
    in_stock: int | None = None
    advertiser_name: str | None = None
    advertiser_username: str | None = None
    advertiser_avatar: str | None = None


@dataclass(frozen=True)
class MarketplaceNegotiation(Model):
    id: int | None = None
    id_listing: int | None = None
    hash: str | None = None
    price: float | None = None
    unit: str | None = None
    currency: str | None = None
    deal_value: float | None = None
    deal_value_currency: str | None = None
    listing_title: str | None = None
    listing_slug: str | None = None
    advertiser_name: str | None = None
    advertiser_username: str | None = None
    advertiser_avatar: str | None = None
    client_name: str | None = None
    client_username: str | None = None
    client_avatar: str | None = None
    is_listing_advertiser: bool | None = None
    date_added: int | None = None
    date_modified: int | None = None
    date_closed: int | None = None
    date_closed_client: int | None = None


@dataclass(frozen=True)
class MarketplaceNegotiationMessage(Model):
    id: int | None = None
    id_listing: int | None = None
    id_negotiation: int | None = None
    event: str | None = None
    message: str | None = None
    listing_title: str | None = None
    listing_slug: str | None = None
    negotiation_hash: str | None = None
    user_name: str | None = None
    user_username: str | None = None
    user_avatar: str | None = None
    api_name: str | None = None
    date_added: int | None = None
    date_read: int | None = None


@dataclass(frozen=True)
class MarketplacePriceAverage(Model):
    id: int | None = None
    id_item: int | None = None
    id_category: int | None = None
    item_uuid: str | None = None
    item_slug: str | None = None
    item_name: str | None = None
    quality_tier: int | None = None
    operation: str | None = None
    currency: str | None = None
    unit: str | None = None
    listings_count: int | None = None
    price_avg: float | None = None
    price_avg_week: float | None = None
    price_avg_month: float | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_modified: int | None = None


@dataclass(frozen=True)
class MarketplacePriceAverageSummary(Model):
    id: int | None = None
    id_item: int | None = None
    quality_tier: int | None = None
    operation: str | None = None
    currency: str | None = None
    unit: str | None = None
    listings_count: int | None = None
    price_avg: float | None = None
    price_avg_week: float | None = None
    price_avg_month: float | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
    item_name: str | None = None
    item_uuid: str | None = None
    item_slug: str | None = None


@dataclass(frozen=True)
class MarketplacePriceHistory(Model):
    id: int | None = None
    id_item: int | None = None
    id_listing: int | None = None
    id_terminal: int | None = None
    id_star_system: int | None = None
    id_category: int | None = None
    item_id_category: int | None = None
    item_uuid: str | None = None
    item_slug: str | None = None
    item_name: str | None = None
    operation: str | None = None
    price: float | None = None
    unit: str | None = None
    currency: str | None = None
    quality: int | None = None
    quality_tier: int | None = None
    game_version: str | None = None
    date_added: int | None = None
    date_removed: int | None = None
    terminal_name: str | None = None
    terminal_nickname: str | None = None
    terminal_slug: str | None = None
    star_system_name: str | None = None
    star_system_code: str | None = None


@dataclass(frozen=True)
class MarketplaceTrend(Model):
    id_item: int | None = None
    item_name: str | None = None
    item_slug: str | None = None
    currency: str | None = None
    price_avg_sell: float | None = None
    price_avg_month_sell: float | None = None
    price_min_sell: float | None = None
    price_max_sell: float | None = None
    listings_count_sell: int | None = None
    price_avg_buy: float | None = None
    price_avg_month_buy: float | None = None
    price_min_buy: float | None = None
    price_max_buy: float | None = None
    listings_count_buy: int | None = None
    total_listings_count: int | None = None
    negotiations_count: int | None = None
    negotiations_open: int | None = None
    negotiations_success: int | None = None
    link_prices: str | None = None
    link_prices_history: str | None = None
