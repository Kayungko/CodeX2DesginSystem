#!/usr/bin/env python3
"""List DESIGN.md style sources under a root directory."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def scan(root: Path) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for design_md in sorted(root.rglob("DESIGN.md")):
        if ".git" in design_md.parts:
            continue
        folder = design_md.parent
        results.append(
            {
                "name": folder.name,
                "folder": str(folder),
                "design_md": str(design_md),
                "readme": str(folder / "README.md") if (folder / "README.md").exists() else None,
                "preview": str(folder / "preview.html") if (folder / "preview.html").exists() else None,
                "preview_dark": str(folder / "preview-dark.html")
                if (folder / "preview-dark.html").exists()
                else None,
            }
        )
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan a directory for DESIGN.md style sources.")
    parser.add_argument("root", type=Path, help="Root directory to scan.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON.")
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.exists():
        parser.error(f"root does not exist: {root}")
    if not root.is_dir():
        parser.error(f"root is not a directory: {root}")

    data = {"root": str(root), "count": 0, "styles": scan(root)}
    data["count"] = len(data["styles"])
    print(json.dumps(data, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
