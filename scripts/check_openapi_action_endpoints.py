#!/usr/bin/env python3
"""Quick check that every endpoint in openapi_action.json returns HTTP 200."""
from __future__ import annotations

import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

SPEC_PATH = Path(__file__).resolve().parents[1] / "openapi_action.json"


def main() -> int:
    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    servers = spec.get("servers") or []
    if not servers:
        raise SystemExit("No servers configured in openapi_action.json")
    base_url = (servers[0].get("url") or "").rstrip("/")
    if not base_url:
        raise SystemExit("Invalid base URL in openapi_action.json")

    failures: list[str] = []

    for path, operations in spec.get("paths", {}).items():
        if "get" not in operations:
            continue
        url = f"{base_url}{path}"
        req = Request(url, method="GET")
        try:
            with urlopen(req) as response:  # noqa: S310 - urllib is fine here
                status = response.status
                if status != 200:
                    failures.append(f"{url} -> HTTP {status}")
                    continue
        except HTTPError as exc:
            failures.append(f"{url} -> HTTPError: {exc.code}")
            continue
        except URLError as exc:
            failures.append(f"{url} -> URLError: {exc.reason}")
            continue

    if failures:
        print("Some endpoints failed:")
        for failure in failures:
            print(f"  - {failure}")
        return 1

    print("All GET endpoints in openapi_action.json returned HTTP 200.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
