"""Model base class and payload coercion.

Models type the fields most callers need and keep the untouched payload in
``raw`` so a new API field is reachable before the model catches up. Field
coercion is driven by each field's declared type: ``bool | None`` truthy-casts
an int, ``int``/``float``/``str`` cast directly, and anything else (arrays,
nested objects) is left for callers to read from ``raw``.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass, field, fields
from typing import Any, ClassVar, TypeVar, Union, get_args, get_origin, get_type_hints

M = TypeVar("M", bound="Model")


@dataclass(frozen=True)
class ResultMeta:
    endpoint: str = ""
    cached: bool = False
    stale: bool = False
    fetched_at: float = 0.0


_HINTS_CACHE: dict[type[Any], Mapping[str, Any]] = {}


def _hints(cls: type[Any]) -> Mapping[str, Any]:
    cached = _HINTS_CACHE.get(cls)
    if cached is None:
        cached = get_type_hints(cls)
        _HINTS_CACHE[cls] = cached
    return cached


def _scalar(hint: Any) -> Any:
    if get_origin(hint) is Union:
        args = [a for a in get_args(hint) if a is not type(None)]
        return args[0] if len(args) == 1 else None
    return hint


def _coerce(hint: Any, value: Any) -> Any:
    if value is None:
        return None
    target = _scalar(hint)
    if target in (bool, int, float) and value == "":
        return None
    if target is bool:
        return value if isinstance(value, bool) else bool(int(value))
    if target is int:
        return int(value)
    if target is float:
        return float(value)
    if target is str:
        return str(value)
    return value


@dataclass(frozen=True)
class Model:
    """Top-level API resource. Subclasses declare typed fields and, when the
    generic coercion above is not enough, a ``_derive`` map."""

    raw: Mapping[str, Any] = field(default_factory=dict, repr=False, compare=False)
    meta: ResultMeta = field(default_factory=ResultMeta, repr=False, compare=False)

    _derive: ClassVar[Mapping[str, Callable[[Mapping[str, Any]], Any]]] = {}

    @classmethod
    def from_payload(cls: type[M], data: Mapping[str, Any], meta: ResultMeta | None = None) -> M:
        hints = _hints(cls)
        values: dict[str, Any] = {}
        for f in fields(cls):
            if f.name in ("raw", "meta") or not f.init:
                continue
            derive = cls._derive.get(f.name)
            if derive is not None:
                values[f.name] = derive(data)
            else:
                values[f.name] = _coerce(hints.get(f.name), data.get(f.name))
        return cls(raw=data, meta=meta or ResultMeta(), **values)
