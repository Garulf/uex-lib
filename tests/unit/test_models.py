from __future__ import annotations

from uex.models import MODELS, Commodity, GameVersions, ResultMeta, Vehicle
from uex.models.base import Model


def test_every_registered_model_builds_from_empty_payload() -> None:
    for model_cls in MODELS.values():
        obj = model_cls.from_payload({})
        assert isinstance(obj, Model)
        assert obj.raw == {}


def test_unknown_keys_are_tolerated_and_kept_in_raw() -> None:
    v = Vehicle.from_payload({"slug": "orig-100i", "brand_new_field": 1})
    assert v.slug == "orig-100i"
    assert v.raw["brand_new_field"] == 1


def test_int_bool_and_float_coercion() -> None:
    v = Vehicle.from_payload(
        {
            "id": 1,
            "is_civilian": 1,
            "is_military": 0,
            "scu": 2.0,
            "name": "100i",
        }
    )
    assert v.id == 1
    assert v.is_civilian is True
    assert v.is_military is False
    assert v.scu == 2.0
    assert v.name == "100i"


def test_null_fields_stay_none() -> None:
    c = Commodity.from_payload({"id": 1, "uuid": None, "code": "AGRI"})
    assert c.uuid is None
    assert c.code == "AGRI"


def test_game_versions_is_flat_single_object() -> None:
    gv = GameVersions.from_payload({"live": "4.10.1", "ptu": None})
    assert gv.live == "4.10.1"
    assert gv.ptu is None


def test_empty_string_numeric_fields_become_none() -> None:
    v = Vehicle.from_payload({"id": "", "scu": "", "name": "100i"})
    assert v.id is None
    assert v.scu is None
    assert v.name == "100i"


def test_meta_is_attached() -> None:
    meta = ResultMeta(endpoint="vehicles", cached=True)
    v = Vehicle.from_payload({}, meta)
    assert v.meta.endpoint == "vehicles"
    assert v.meta.cached is True
