#!/usr/bin/env python3
"""Validate DESIGN.md and Figma URL inputs for the design-md-to-figma-system skill."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


FIGMA_RE = re.compile(
    r"https://(?:www\.)?figma\.com/(?:design|file)/(?P<file_key>[A-Za-z0-9]+)(?:/[^?\s]*)?(?:\?(?P<query>[^\s#]+))?"
)


def parse_figma_url(url: str) -> dict[str, str | None]:
    match = FIGMA_RE.match(url)
    if not match:
        return {"file_key": None, "node_id": None}
    query = match.group("query") or ""
    node_match = re.search(r"(?:^|&)node-id=([^&]+)", query)
    node_id = node_match.group(1).replace("-", ":") if node_match else None
    return {"file_key": match.group("file_key"), "node_id": node_id}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate inputs for DESIGN.md to Figma system generation.")
    parser.add_argument("--design-md", required=True, type=Path, help="Path to DESIGN.md.")
    parser.add_argument("--figma-url", required=True, help="Figma design URL.")
    parser.add_argument("--preview", type=Path, help="Optional preview.html path.")
    parser.add_argument("--preview-dark", type=Path, help="Optional preview-dark.html path.")
    parser.add_argument("--style-name", help="Optional explicit style page name.")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    design_md = args.design_md.resolve()
    if not design_md.exists():
        errors.append(f"DESIGN.md not found: {design_md}")
    elif not design_md.is_file():
        errors.append(f"DESIGN.md path is not a file: {design_md}")
    elif design_md.name != "DESIGN.md":
        warnings.append(f"Expected file named DESIGN.md, got: {design_md.name}")

    preview = args.preview.resolve() if args.preview else design_md.parent / "preview.html"
    preview_dark = args.preview_dark.resolve() if args.preview_dark else design_md.parent / "preview-dark.html"
    if not preview.exists():
        warnings.append(f"preview.html not found: {preview}")
    if not preview_dark.exists():
        warnings.append(f"preview-dark.html not found: {preview_dark}")

    figma = parse_figma_url(args.figma_url)
    if not figma["file_key"]:
        errors.append("Figma URL must be a figma.com/design or figma.com/file URL with a file key.")

    style_name = args.style_name or (design_md.parent.name if design_md.exists() else None)
    result = {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "design_md": str(design_md),
        "preview": str(preview) if preview.exists() else None,
        "preview_dark": str(preview_dark) if preview_dark.exists() else None,
        "figma": figma,
        "style_name": style_name,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
