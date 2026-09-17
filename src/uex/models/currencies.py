"""Generated from the UEX API 2.0 documentation. Scalar fields only;
arrays and nested objects stay reachable through ``raw``.
"""

from __future__ import annotations

from dataclasses import dataclass

from uex.models.base import Model


@dataclass(frozen=True)
class CurrencyIndex(Model):
    id: int | None = None
    currency: str | None = None
    index_value: float | None = None
    basket_value: float | None = None
    methodology: str | None = None
    data_window_days: int | None = None
    date_modified: int | None = None


@dataclass(frozen=True)
class CurrencyIndexSnapshot(Model):
    id: int | None = None
    currency: str | None = None
    index_value: float | None = None
    basket_value: float | None = None
    methodology: str | None = None
    data_window_days: int | None = None
    date_added: int | None = None
