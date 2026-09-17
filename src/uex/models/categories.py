"""Generated from the UEX API 2.0 documentation. Scalar fields only;
arrays and nested objects stay reachable through ``raw``.
"""

from __future__ import annotations

from dataclasses import dataclass

from uex.models.base import Model


@dataclass(frozen=True)
class Category(Model):
    id: int | None = None
    type: str | None = None
    section: str | None = None
    name: str | None = None
    is_game_related: bool | None = None
    is_mining: bool | None = None
    date_added: int | None = None
    date_modified: int | None = None


@dataclass(frozen=True)
class CategoryAttribute(Model):
    id: int | None = None
    id_category: int | None = None
    name: str | None = None
    category_name: int | None = None
    description: str | None = None
    is_lower_better: bool | None = None
    date_added: int | None = None
    date_modified: int | None = None
