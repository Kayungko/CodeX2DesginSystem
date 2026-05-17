#!/usr/bin/env python3
"""Validate Figma inventory JSON against the standard component contract.

Preferred inventory schema:

{
  "schemaVersion": "design-md-system-inventory/v2",
  "sections": [
    {"name": "Style / Overview", "standardName": "Overview", "index": 0}
  ],
  "componentSets": [
    {
      "name": "Style / Button",
      "standardName": "Button",
      "section": "Core Components",
      "sourceStatus": "Inferred",
      "variantCount": 4,
      "variantProperties": ["Variant", "Size", "State"]
    }
  ],
    "validation": {
    "overlaps": [],
    "overWidth": [],
    "structuralFrameFills": [],
    "sourceLabelWarnings": [],
    "menuAlignmentWarnings": [],
    "instanceDetachWarnings": []
  }
}

Legacy inventories with only `name` are still accepted for basic coverage checks,
but they emit `schemaWarnings` and skip strict axes/source/layout validation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


DEFAULT_CONTRACT = (
    Path(__file__).resolve().parents[1]
    / "references"
    / "standard-component-contract.json"
)
SCHEMA_VERSION = "design-md-system-inventory/v2"
BASELINE_31_PROFILE = "tier1-31-no-blocks"
BASELINE_31_SECTIONS = [
    "Overview",
    "Foundations",
    "Core Components",
    "Form & Input Controls",
    "Navigation & Layout",
    "Feedback & Overlays",
    "Theme-Specific Components",
    "Patterns",
    "Examples",
    "Reference Notes",
]
BASELINE_31_COMPONENTS = {
    "Button",
    "Icon Button",
    "Link",
    "Badge / Tag",
    "Text Field",
    "Search Field",
    "Select / Dropdown",
    "Checkbox",
    "Radio",
    "Switch",
    "Slider",
    "Navigation Bar",
    "Sidebar / Rail",
    "Tabs",
    "Segmented Control",
    "Card",
    "Panel",
    "Divider",
    "Table / Data Row",
    "Tooltip",
    "Toast / Notification",
    "Progress / Loading",
    "Empty State",
    "Modal / Dialog",
    "Command Menu",
    "Menu Item",
    "Section Header",
    "Type Sample",
    "Spacing Scale Item",
    "Radius Scale Item",
    "Elevation Card",
}


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def tail_name(value: str) -> str:
    parts = [part.strip() for part in value.split("/") if part.strip()]
    if len(parts) >= 2:
        return " / ".join(parts[1:])
    return parts[0] if parts else value.strip()


def legacy_standard_name(value: str, allowed: set[str]) -> str | None:
    """Return an exact standard-name match from a legacy node name.

    This intentionally avoids fuzzy suffix/contains matching so a name like
    "Feature Card" cannot satisfy the required standard component "Card".
    """

    tail = normalize(tail_name(value))
    for name in allowed:
        if normalize(name) == tail:
            return name
    return None


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def collect_section_map(
    inventory: dict[str, Any], required_sections: list[str], schema_warnings: list[str]
) -> dict[str, dict[str, Any]]:
    allowed = set(required_sections)
    result: dict[str, dict[str, Any]] = {}

    for index, item in enumerate(inventory.get("sections", [])):
        if not isinstance(item, dict):
            continue
        standard_name = item.get("standardName")
        if not standard_name:
            standard_name = legacy_standard_name(item.get("name", ""), allowed)
            schema_warnings.append(
                f"section '{item.get('name', '')}' uses legacy name-only matching"
            )
        if not standard_name:
            continue
        copy = dict(item)
        copy.setdefault("index", index)
        copy["standardName"] = standard_name
        result.setdefault(standard_name, copy)
    return result


def collect_component_map(
    inventory: dict[str, Any], required_components: list[str], schema_warnings: list[str]
) -> dict[str, dict[str, Any]]:
    allowed = set(required_components)
    result: dict[str, dict[str, Any]] = {}

    for item in inventory.get("componentSets", []):
        if not isinstance(item, dict):
            continue
        if "standardName" in item:
            standard_name = item.get("standardName")
            if not standard_name and item.get("sourceStatus") == "Theme-Specific":
                continue
            if not standard_name:
                schema_warnings.append(
                    f"component set '{item.get('name', '')}' missing standardName"
                )
                continue
        else:
            standard_name = legacy_standard_name(item.get("name", ""), allowed)
            schema_warnings.append(
                f"component set '{item.get('name', '')}' uses legacy name-only matching"
            )
        if not standard_name:
            continue
        copy = dict(item)
        copy["standardName"] = standard_name
        result.setdefault(standard_name, copy)
    return result


def list_names(items: list[dict[str, Any]]) -> list[str]:
    return [str(item.get("name", "")) for item in items if isinstance(item, dict)]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Figma inventory against the DESIGN.md standard component contract."
    )
    parser.add_argument("inventory", type=Path, help="Path to inventory JSON exported from Figma validation.")
    parser.add_argument(
        "--contract",
        type=Path,
        default=DEFAULT_CONTRACT,
        help=f"Path to component contract JSON. Defaults to {DEFAULT_CONTRACT}",
    )
    args = parser.parse_args()

    contract = load_json(args.contract)
    inventory = load_json(args.inventory)

    contract_profile = inventory.get("contractProfile", "full")
    if contract_profile == BASELINE_31_PROFILE:
        required_sections = BASELINE_31_SECTIONS
        required_components = [
            item for item in contract["required_components"]
            if item["name"] in BASELINE_31_COMPONENTS
        ]
        required_blocks = []
    else:
        required_sections = contract["required_sections"]
        required_components = contract["required_components"]
        required_blocks = contract.get("blocks", [])
    required_component_names = [item["name"] for item in required_components]
    allowed_statuses = set(contract.get("source_status", []))

    schema_warnings: list[str] = []
    final_blocking: list[str] = []
    warnings: list[str] = []

    # ----- blocks -----
    required_block_names = [item["name"] for item in required_blocks]
    inventory_blocks = inventory.get("blocks", [])

    block_map: dict[str, dict[str, Any]] = {}
    for item in inventory_blocks:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if not name:
            continue
        block_map.setdefault(name, item)

    missing_blocks = [name for name in required_block_names if name not in block_map]
    omitted_blocks = [
        name for name in required_block_names
        if name in block_map and block_map[name].get("omittedReason")
    ]
    present_blocks = [
        name for name in required_block_names
        if name in block_map and not block_map[name].get("omittedReason")
    ]

    for name in missing_blocks:
        warnings.append(f"missing block: {name} (not final-blocking; record reason if out of scope)")
    for name in omitted_blocks:
        warnings.append(f"block '{name}' omitted: {block_map[name].get('omittedReason')}")

    for contract_block in required_blocks:
        name = contract_block["name"]
        block = block_map.get(name)
        if not block or block.get("omittedReason"):
            continue

        if block.get("section") != "Blocks":
            final_blocking.append(f"block '{name}' must be placed in 'Blocks' section, got '{block.get('section')}'")

        required_children = contract_block.get("requiredComponents", [])
        block_present = set(block.get("requiredComponents", []))
        missing_children = [
            child for child in required_children
            if not any(child in bp or bp in child for bp in block_present)
        ]
        if missing_children:
            final_blocking.append(
                f"block '{name}' missing required component instances: {', '.join(missing_children)}"
            )

        instance_count = block.get("instanceCount")
        if instance_count is None:
            schema_warnings.append(f"block '{name}' missing instanceCount")
        elif not isinstance(instance_count, int) or instance_count <= 0:
            final_blocking.append(f"block '{name}' has no master component instances")

    # ----- core validation -----

    if inventory.get("schemaVersion") != SCHEMA_VERSION:
        schema_warnings.append(
            f"inventory schemaVersion is '{inventory.get('schemaVersion', 'legacy')}', expected '{SCHEMA_VERSION}'"
        )

    section_map = collect_section_map(inventory, required_sections, schema_warnings)
    component_map = collect_component_map(inventory, required_component_names, schema_warnings)

    missing_sections = [name for name in required_sections if name not in section_map]
    missing_components = [name for name in required_component_names if name not in component_map]

    for name in missing_sections:
        final_blocking.append(f"missing section: {name}")
    for name in missing_components:
        final_blocking.append(f"missing required component: {name}")

    section_sequence = [item.get("standardName") for item in inventory.get("sections", []) if isinstance(item, dict)]
    if all(section_sequence):
        if section_sequence != required_sections:
            final_blocking.append("standard sections are missing, duplicated, or out of order")
    elif not missing_sections:
        schema_warnings.append("section order could not be strictly validated without sections[].standardName")

    duplicate_sections = sorted(
        name for name in set(section_sequence) if section_sequence.count(name) > 1 and name
    )
    for name in duplicate_sections:
        final_blocking.append(f"duplicate section: {name}")

    for item in inventory.get("componentSets", []):
        if not isinstance(item, dict):
            continue
        source_status = item.get("sourceStatus")
        if source_status is None:
            schema_warnings.append(f"component set '{item.get('name', '')}' missing sourceStatus")
        elif source_status not in allowed_statuses:
            final_blocking.append(
                f"component set '{item.get('name', '')}' has invalid sourceStatus '{source_status}'"
            )

        standard_name = item.get("standardName")
        if source_status == "Theme-Specific" and standard_name in required_component_names:
            final_blocking.append(
                f"theme-specific component '{item.get('name', standard_name)}' cannot replace standard component '{standard_name}'"
            )
        if standard_name in required_component_names and item.get("section") == "Theme-Specific Components":
            final_blocking.append(
                f"standard component '{standard_name}' is placed in Theme-Specific Components"
            )

    for contract_item in required_components:
        name = contract_item["name"]
        component = component_map.get(name)
        if not component:
            continue

        source_status = component.get("sourceStatus")
        if source_status is None:
            schema_warnings.append(f"component '{component.get('name', name)}' missing sourceStatus")
        elif source_status not in allowed_statuses:
            final_blocking.append(
                f"component '{component.get('name', name)}' has invalid sourceStatus '{source_status}'"
            )

        if source_status == "Theme-Specific":
            final_blocking.append(f"standard component '{name}' cannot be Source=Theme-Specific")

        variant_properties = component.get("variantProperties")
        if variant_properties is None:
            schema_warnings.append(f"component '{component.get('name', name)}' missing variantProperties")
        else:
            missing_axes = [
                axis for axis in contract_item.get("axes", []) if axis not in variant_properties
            ]
            if missing_axes:
                final_blocking.append(
                    f"component '{name}' missing variant axes: {', '.join(missing_axes)}"
                )

        variant_count = component.get("variantCount")
        if variant_count is None:
            schema_warnings.append(f"component '{component.get('name', name)}' missing variantCount")
        elif not isinstance(variant_count, int) or variant_count <= 0:
            final_blocking.append(f"component '{name}' has invalid variantCount '{variant_count}'")

    validation = inventory.get("validation", {})
    for field in [
        "overlaps",
        "overWidth",
        "structuralFrameFills",
        "sourceLabelWarnings",
        "menuAlignmentWarnings",
        "instanceDetachWarnings",
    ]:
        value = validation.get(field)
        if value is None:
            schema_warnings.append(f"validation.{field} missing")
        elif value:
            final_blocking.append(f"validation.{field} is not empty")

    for field in ["hardcodedFillWarnings", "bindingWarnings", "screenshotWarnings"]:
        value = validation.get(field)
        if value:
            warnings.append(f"validation.{field} is not empty")

    result = {
        "ok": not final_blocking,
        "schemaVersion": inventory.get("schemaVersion", "legacy"),
        "contractProfile": contract_profile,
        "finalBlocking": final_blocking,
        "warnings": warnings,
        "schemaWarnings": schema_warnings,
        "missing_sections": missing_sections,
        "missing_components": missing_components,
        "missing_blocks": missing_blocks,
        "omitted_blocks": omitted_blocks,
        "present_blocks": present_blocks,
        "section_count": len(list_names(inventory.get("sections", []))),
        "component_set_count": len(list_names(inventory.get("componentSets", []))),
        "required_component_count": len(required_components),
        "required_block_count": len(required_blocks),
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
