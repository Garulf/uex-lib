"""Generated from the UEX API 2.0 documentation. Scalar fields only;
arrays and nested objects stay reachable through ``raw``.
"""

from __future__ import annotations

from dataclasses import dataclass

from uex.models.base import Model


@dataclass(frozen=True)
class GameVersions(Model):
    live: str | None = None
    ptu: str | None = None


@dataclass(frozen=True)
class GameVersionEntry(Model):
    id: int | None = None
    game_version: str | None = None
    date_added: int | None = None
