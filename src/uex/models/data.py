"""Generated from the UEX API 2.0 documentation. Scalar fields only;
arrays and nested objects stay reachable through ``raw``.
"""

from __future__ import annotations

from dataclasses import dataclass

from uex.models.base import Model


@dataclass(frozen=True)
class DataParameters(Model):
    is_accepting_reports: bool | None = None
    is_accepting_ptu_reports: bool | None = None
    is_datacenter_enabled: bool | None = None
    game_version: str | None = None
    game_version_ptu: str | None = None
    is_accepted: bool | None = None
    is_temporary_enabled: bool | None = None
    price_variation: int | None = None
    scu_variation: int | None = None
    ttl: int | None = None
    notification: str | None = None


@dataclass(frozen=True)
class DataMonitorEntry(Model):
    id_terminal: int | None = None
    type: str | None = None
    terminal_name: str | None = None
    terminal_nickname: str | None = None
    terminal_code: str | None = None
    terminal_slug: str | None = None
    id_star_system: int | None = None
    star_system_name: str | None = None
    orbit_name: str | None = None
    orbit_nickname: str | None = None
    orbit_code: str | None = None
    game_version: str | None = None
    prices_total: int | None = None
    prices_updated: int | None = None
    prices_updated_percentage: int | None = None
    last_update_days_limit: int | None = None
    last_update_days: int | None = None
    last_update_days_percentage: int | None = None
    last_update: int | None = None
    id_report: int | None = None
    has_recent_reports: bool | None = None
    has_ptu_reports: bool | None = None


@dataclass(frozen=True)
class DataInfo(Model):
    id: int | None = None
    type: str | None = None
    status: str | None = None
    id_user: int | None = None
    username: str | None = None
    id_terminal: int | None = None
    id_commodity: int | None = None
    id_item: int | None = None
    id_category: int | None = None
    id_vehicle: int | None = None
    name: str | None = None
    price_buy: float | None = None
    price_sell: float | None = None
    price_rent: float | None = None
    scu_buy: int | None = None
    scu_sell: int | None = None
    status_buy: int | None = None
    status_sell: int | None = None
    quality: int | None = None
    container_sizes: str | None = None
    faction_affinity: int | None = None
    details: str | None = None
    game_version: str | None = None
    is_missing: bool | None = None
    is_new_item: bool | None = None
    is_new_at_location: bool | None = None
    is_ptu_report: bool | None = None
    is_contested: bool | None = None
    is_owner: bool | None = None
    is_editable: bool | None = None
    has_attachments: bool | None = None
    has_comments: bool | None = None
    date_added: int | None = None
    date_modified: int | None = None
    date_checked: int | None = None
    date_approved: int | None = None
    date_declined: int | None = None
    date_consolidated: int | None = None
    date_expired: int | None = None
    date_queued: int | None = None
