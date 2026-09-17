"""Generated from the UEX API 2.0 documentation. Scalar fields only;
arrays and nested objects stay reachable through ``raw``.
"""

from __future__ import annotations

from dataclasses import dataclass

from uex.models.base import Model


@dataclass(frozen=True)
class Poll(Model):
    id: str | None = None
    id_item: int | None = None
    id_vehicle: int | None = None
    id_commodity: int | None = None
    question: str | None = None
    type: str | None = None
    category: str | None = None
    slug: str | None = None
    game_version: str | None = None
    user_username: str | None = None
    total_votes: int | None = None
    total_voters: int | None = None
    is_featured: bool | None = None
    is_official: bool | None = None
    is_recurring: bool | None = None
    is_active: bool | None = None
    date_opened: int | None = None
    date_closed: int | None = None


@dataclass(frozen=True)
class PollAuditEntry(Model):
    voter: str | None = None
    option: str | None = None
    date_added: int | None = None
