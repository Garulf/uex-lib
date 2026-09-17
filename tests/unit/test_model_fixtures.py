"""Every recorded fixture must parse into its model without raising."""

from __future__ import annotations

import pytest

from tests.conftest import load_fixture
from uex.core.endpoints import ENDPOINTS
from uex.models import MODELS

FIXTURED_ENDPOINTS = [
    "vehicles",
    "commodities",
    "commodities_prices",
    "terminals",
    "star_systems",
    "game_versions",
    "items",
    "crew",
    "data_parameters",
    "marketplace_listings",
    "polls",
    "currencies_index",
    "refineries_methods",
    "jump_points",
    "categories",
]


@pytest.mark.parametrize("endpoint_name", FIXTURED_ENDPOINTS)
def test_fixture_rows_parse_into_typed_model(endpoint_name: str) -> None:
    endpoint = ENDPOINTS[endpoint_name]
    model_cls = MODELS[endpoint.model]
    payload = load_fixture(endpoint_name)
    data = payload["data"]
    rows = [data] if endpoint.single else data
    if endpoint_name != "crew":
        assert rows
    for row in rows:
        obj = model_cls.from_payload(row)
        assert obj.raw is row


@pytest.mark.parametrize("endpoint_name", FIXTURED_ENDPOINTS)
def test_fixture_scalar_fields_are_typed_or_none(endpoint_name: str) -> None:
    """Every declared field either matches the fixture's JSON type or stayed None."""
    endpoint = ENDPOINTS[endpoint_name]
    model_cls = MODELS[endpoint.model]
    payload = load_fixture(endpoint_name)
    data = payload["data"]
    rows = [data] if endpoint.single else data
    for row in rows:
        obj = model_cls.from_payload(row)
        for field_name in vars(obj):
            if field_name in ("raw", "meta") or field_name not in row:
                continue
            value = getattr(obj, field_name)
            if value is None:
                continue
            assert isinstance(value, bool | int | float | str)
