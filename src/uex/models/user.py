"""Generated from the UEX API 2.0 documentation. Scalar fields only;
arrays and nested objects stay reachable through ``raw``.
"""

from __future__ import annotations

from dataclasses import dataclass

from uex.models.base import Model


@dataclass(frozen=True)
class User(Model):
    id: int | None = None
    ids_factions: str | None = None
    ids_star_systems: str | None = None
    name: str | None = None
    username: str | None = None
    email: str | None = None
    avatar: str | None = None
    bio: str | None = None
    website_url: str | None = None
    timezone: str | None = None
    language: str | None = None
    discord_username: str | None = None
    twitch_username: str | None = None
    day_availability: str | None = None
    time_availability: str | None = None
    specializations: str | None = None
    languages: str | None = None
    archetypes: str | None = None
    is_datarunner: bool | None = None
    is_datarunner_banned: bool | None = None
    is_staff: bool | None = None
    is_away_game: bool | None = None
    date_added: int | None = None
    date_modified: int | None = None
    date_disabled: int | None = None
    date_rsi_verified: int | None = None
    date_twitch_verified: int | None = None


@dataclass(frozen=True)
class UserNotification(Model):
    id: int | None = None
    message: str | None = None
    redir: str | None = None
    code: str | None = None
    date_added: int | None = None
    date_read: int | None = None


@dataclass(frozen=True)
class UserTrade(Model):
    id: int | None = None
    id_terminal: int | None = None
    id_commodity: int | None = None
    id_user_fleet: int | None = None
    id_vehicle: int | None = None
    id_organization: int | None = None
    operation: str | None = None
    scu: int | None = None
    price: float | None = None
    date_added: int | None = None
    date_modified: int | None = None
    user_name: str | None = None
    user_username: str | None = None
    commodity_name: str | None = None
    terminal_name: str | None = None
    user_fleet_name: str | None = None
    user_fleet_serial: str | None = None
    user_fleet_screenshot: str | None = None
    vehicle_name: str | None = None
    organization_name: str | None = None


@dataclass(frozen=True)
class UserRefineryJob(Model):
    id: int | None = None
    id_terminal: int | None = None
    id_refinery_method: int | None = None
    cost: float | None = None
    time_minutes: int | None = None
    date_added: int | None = None
    date_modified: int | None = None
    date_expiration: int | None = None
    terminal_name: str | None = None


@dataclass(frozen=True)
class FleetVehicle(Model):
    id: int | None = None
    id_organization: int | None = None
    id_vehicle: int | None = None
    name: str | None = None
    serial: str | None = None
    description: str | None = None
    date_added: int | None = None
    organization_name: str | None = None
    model_name: str | None = None
    is_hidden: bool | None = None
    is_pledged: bool | None = None


@dataclass(frozen=True)
class WalletBalance(Model):
    balance: float | None = None


@dataclass(frozen=True)
class Organization(Model):
    id: int | None = None
    slug: str | None = None
    name: str | None = None
    description: str | None = None
    logo: str | None = None
    date_added: int | None = None
    date_modified: int | None = None
