"""Re-record a sample response per fixtured endpoint into tests/fixtures.

Only endpoints with a recorded sample query in SAMPLES are refreshed; adding
one there is enough to bring a new endpoint under the fixture-parsing tests.
"""

from __future__ import annotations

import json
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from uex import __version__

BASE = "https://api.uexcorp.space/2.0"
OUT = Path(__file__).resolve().parents[1] / "tests" / "fixtures"
HEADERS = {"Accept": "application/json", "User-Agent": f"uex-lib/{__version__} fixtures"}
MAX_ROWS = 3

SAMPLES: dict[str, str] = {
    "vehicles": "vehicles?id_company=195",
    "commodities": "commodities",
    "commodities_prices": "commodities_prices?id_terminal=1",
    "terminals": "terminals?id_star_system=68",
    "star_systems": "star_systems",
    "game_versions": "game_versions",
    "items": "items?id_category=1",
    "crew": "crew?specialization=trade",
    "data_parameters": "data_parameters",
    "marketplace_listings": "marketplace_listings",
    "polls": "polls",
    "currencies_index": "currencies_index",
    "refineries_methods": "refineries_methods",
    "jump_points": "jump_points",
    "categories": "categories",
}


def get(url: str) -> Any:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as fh:
        return json.load(fh)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, path in SAMPLES.items():
        payload = get(f"{BASE}/{path}")
        data = payload.get("data")
        if isinstance(data, list):
            payload["data"] = data[:MAX_ROWS]
        (OUT / f"{name}.json").write_text(json.dumps(payload, indent=1) + "\n")
        print(name)
        time.sleep(0.3)


if __name__ == "__main__":
    main()
