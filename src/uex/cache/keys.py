"""Deterministic cache keys that are stable across processes."""

from __future__ import annotations

from collections.abc import Mapping


def make_key(endpoint: str, params: Mapping[str, str]) -> str:
    joined = "&".join(f"{k}={v}" for k, v in sorted(params.items()))
    return f"{endpoint}|{joined}"
