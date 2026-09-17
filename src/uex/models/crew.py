"""Generated from the UEX API 2.0 documentation. Scalar fields only;
arrays and nested objects stay reachable through ``raw``.
"""

from __future__ import annotations

from dataclasses import dataclass

from uex.models.base import Model


@dataclass(frozen=True)
class CrewMember(Model):
    name: str | None = None
    username: str | None = None
    twitch_username: str | None = None
    day_availability: str | None = None
    time_availability: str | None = None
    specializations: str | None = None
    languages: str | None = None
    archetypes: str | None = None
    timezone: str | None = None
    avatar: str | None = None
    bio: str | None = None
    date_added: int | None = None
