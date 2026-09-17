"""Build transport-neutral requests from endpoint definitions and query values."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from urllib.parse import urlencode

from uex._http import Request
from uex.core.endpoints import SECRET, TOKEN, Endpoint
from uex.errors import AuthRequired, MissingParameter

MAX_MULTI_IDS = 10


def _join_multi(name: str, value: object) -> str:
    if isinstance(value, str) or not isinstance(value, Sequence):
        return str(value)
    values = [str(v) for v in value]
    if len(values) > MAX_MULTI_IDS:
        raise ValueError(f"{name} accepts at most {MAX_MULTI_IDS} ids, got {len(values)}")
    return ",".join(values)


def normalize_params(endpoint: Endpoint, values: Mapping[str, object]) -> dict[str, str]:
    """Drop ``None`` values, join multi-id sequences, and stringify the rest."""
    out: dict[str, str] = {}
    for key, value in values.items():
        if value is None:
            continue
        if key in endpoint.multi:
            out[key] = _join_multi(key, value)
        elif isinstance(value, bool):
            out[key] = "1" if value else "0"
        else:
            out[key] = str(value)
    return out


def check_requirements(endpoint: Endpoint, params: Mapping[str, str]) -> None:
    if not endpoint.requires:
        return
    mode, *names = endpoint.requires
    present = [n for n in names if n in params]
    if mode == "any" and not present:
        raise MissingParameter(endpoint.name, "any", tuple(names))
    if mode == "all" and len(present) != len(names):
        raise MissingParameter(endpoint.name, "all", tuple(names))


def check_auth(endpoint: Endpoint, *, token: str | None, secret_key: str | None) -> None:
    if endpoint.auth == TOKEN and token is None:
        raise AuthRequired(endpoint.name, "token")
    if endpoint.auth == SECRET:
        if token is None:
            raise AuthRequired(endpoint.name, "token")
        if secret_key is None:
            raise AuthRequired(endpoint.name, "secret_key")


def build_request(
    base_url: str,
    endpoint: Endpoint,
    params: Mapping[str, str],
    *,
    user_agent: str,
    token: str | None,
    secret_key: str | None,
) -> Request:
    url = f"{base_url.rstrip('/')}/{endpoint.path}"
    if params:
        url = f"{url}?{urlencode(sorted(params.items()))}"
    headers = {"Accept": "application/json", "User-Agent": user_agent}
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"
    if secret_key is not None:
        headers["secret-key"] = secret_key
    return Request("GET", url, headers)
