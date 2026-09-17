"""Turn raw responses into parsed payloads or typed errors."""

from __future__ import annotations

import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from uex._http import Response
from uex.errors import ApiError, InvalidRequest, NotFound, RateLimited, ServerError

_MAX_AGE_RE = re.compile(r"max-age=(\d+)")


@dataclass(frozen=True)
class Parsed:
    data: Any
    message: str = ""
    max_age: float | None = None


def _header(headers: Mapping[str, str], name: str) -> str | None:
    wanted = name.lower()
    for key, value in headers.items():
        if key.lower() == wanted:
            return value
    return None


def _retry_after(headers: Mapping[str, str]) -> float | None:
    raw = _header(headers, "Retry-After")
    if raw is None:
        return None
    try:
        return float(raw)
    except ValueError:
        return None


def _max_age(headers: Mapping[str, str]) -> float | None:
    raw = _header(headers, "Cache-Control")
    if raw is None:
        return None
    match = _MAX_AGE_RE.search(raw)
    return float(match.group(1)) if match else None


def parse_response(response: Response, *, endpoint: str) -> Parsed:
    status = response.status
    if status == 404:
        raise NotFound(endpoint)
    if status == 429:
        raise RateLimited(_retry_after(response.headers), response.body)
    if status >= 500:
        raise ServerError(status, body=response.body)
    try:
        payload = json.loads(response.body)
    except ValueError as exc:
        raise ApiError(status, message="API returned a non-JSON body", body=response.body) from exc
    if not isinstance(payload, Mapping):
        raise ApiError(status, message="API returned an unexpected payload", body=response.body)
    code = payload.get("status")
    message = payload.get("message") or ""
    if code == "requests_limit_reached":
        raise RateLimited(_retry_after(response.headers), response.body)
    if code != "ok" or status >= 400:
        raise InvalidRequest(status, str(code), message, response.body)
    return Parsed(payload.get("data"), message, _max_age(response.headers))
