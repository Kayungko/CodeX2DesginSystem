#!/usr/bin/env python3
"""Regression tests for validate_component_contract.py."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "references" / "standard-component-contract.json"
VALIDATOR = ROOT / "scripts" / "validate_component_contract.py"
SCHEMA_VERSION = "design-md-system-inventory/v2"


def load_contract() -> dict:
    with CONTRACT_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def section_for(area: str) -> str:
    return {
        "Actions": "Core Components",
        "Documentation": "Core Components",
        "Inputs": "Form & Input Controls",
        "Navigation": "Navigation & Layout",
        "Surfaces": "Navigation & Layout",
        "Feedback": "Feedback & Overlays",
        "Overlays": "Feedback & Overlays",
    }[area]


def full_inventory() -> dict:
    contract = load_contract()
    return {
        "schemaVersion": SCHEMA_VERSION,
        "sections": [
            {
                "name": f"Test / {name}",
                "standardName": name,
                "index": index,
                "id": f"section-{index}",
                "bounds": {"x": 0, "y": index * 1000, "width": 1200, "height": 800},
            }
            for index, name in enumerate(contract["required_sections"])
        ],
        "componentSets": [
            {
                "name": f"Test / {component['name']}",
                "standardName": component["name"],
                "section": section_for(component["area"]),
                "sourceStatus": "Inferred",
                "variantCount": 1,
                "variantProperties": component["axes"],
                "id": f"component-{index}",
            }
            for index, component in enumerate(contract["required_components"])
        ],
        "validation": {
            "overlaps": [],
            "overWidth": [],
            "structuralFrameFills": [],
            "sourceLabelWarnings": [],
            "menuAlignmentWarnings": [],
            "instanceDetachWarnings": [],
            "bindingSummary": {},
        },
        "contractProfile": "full-blocks-v3",
        "blocks": [
            {
                "name": block["name"],
                "category": block.get("category", ""),
                "section": "Blocks",
                "id": f"block-{index}",
                "instanceCount": 1,
                "requiredComponentInstances": [
                    {
                        "standardName": component_name,
                        "instanceId": f"block-{index}-instance-{component_index}",
                        "mainComponentId": f"component-main-{component_index}",
                        "mainComponentName": component_name,
                    }
                    for component_index, component_name in enumerate(block.get("requiredComponents", []))
                ],
            }
            for index, block in enumerate(contract.get("blocks", []))
        ],
    }


def run_validator(inventory: dict) -> tuple[int, dict]:
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as file:
        json.dump(inventory, file)
        temp_path = Path(file.name)

    try:
        completed = subprocess.run(
            [sys.executable, str(VALIDATOR), str(temp_path)],
            check=False,
            capture_output=True,
            text=True,
        )
        return completed.returncode, json.loads(completed.stdout)
    finally:
        temp_path.unlink(missing_ok=True)


def assert_blocking_contains(result: dict, needle: str) -> None:
    if not any(needle in item for item in result["finalBlocking"]):
        raise AssertionError(f"Expected finalBlocking to contain {needle!r}, got {result['finalBlocking']}")


def test_icon_button_does_not_match_button() -> None:
    inventory = full_inventory()
    inventory["componentSets"] = [
        item for item in inventory["componentSets"] if item["standardName"] != "Button"
    ]
    code, result = run_validator(inventory)
    assert code == 1
    assert_blocking_contains(result, "missing required component: Button")


def test_feature_card_does_not_match_card() -> None:
    inventory = full_inventory()
    inventory["componentSets"] = [
        item for item in inventory["componentSets"] if item["standardName"] != "Card"
    ]
    inventory["componentSets"].append({"name": "Test / Feature Card"})
    code, result = run_validator(inventory)
    assert code == 1
    assert_blocking_contains(result, "missing required component: Card")


def test_missing_axes_fail() -> None:
    inventory = full_inventory()
    for item in inventory["componentSets"]:
        if item["standardName"] == "Button":
            item["variantProperties"] = ["Variant"]
    code, result = run_validator(inventory)
    assert code == 1
    assert_blocking_contains(result, "component 'Button' missing variant axes: Size, State")


def test_section_order_and_duplicate_fail() -> None:
    inventory = full_inventory()
    inventory["sections"][0], inventory["sections"][1] = inventory["sections"][1], inventory["sections"][0]
    inventory["sections"].append(dict(inventory["sections"][0]))
    code, result = run_validator(inventory)
    assert code == 1
    assert_blocking_contains(result, "standard sections are missing, duplicated, or out of order")
    assert_blocking_contains(result, "duplicate section")


def test_block_missing_required_components_fails() -> None:
    inventory = full_inventory()
    if inventory["blocks"]:
        inventory["blocks"][0]["requiredComponentInstances"] = []
    code, result = run_validator(inventory)
    if inventory["blocks"]:
        assert code == 1
        assert any("missing required component instances" in item for item in result["finalBlocking"])


def test_block_required_components_are_exact() -> None:
    inventory = full_inventory()
    if inventory["blocks"]:
        inventory["blocks"][0]["requiredComponentInstances"] = [
            {
                "standardName": "Sidebar / Rail Item",
                "instanceId": "bad-1",
                "mainComponentId": "bad-main-1",
                "mainComponentName": "Sidebar / Rail Item",
            },
            {
                "standardName": "Navigation Bar Copy",
                "instanceId": "bad-2",
                "mainComponentId": "bad-main-2",
                "mainComponentName": "Navigation Bar Copy",
            },
            {
                "standardName": "Feature Card",
                "instanceId": "bad-3",
                "mainComponentId": "bad-main-3",
                "mainComponentName": "Feature Card",
            },
            {
                "standardName": "Table / Data Row Expanded",
                "instanceId": "bad-4",
                "mainComponentId": "bad-main-4",
                "mainComponentName": "Table / Data Row Expanded",
            },
        ]
    code, result = run_validator(inventory)
    if inventory["blocks"]:
        assert code == 1
        assert_blocking_contains(result, "block 'Dashboard Shell' missing required component instances")


def test_block_detached_instance_fails() -> None:
    inventory = full_inventory()
    if inventory["blocks"]:
        inventory["blocks"][0]["requiredComponentInstances"][0]["mainComponentId"] = None
    code, result = run_validator(inventory)
    if inventory["blocks"]:
        assert code == 1
        assert_blocking_contains(result, "missing mainComponentId")


def test_source_label_warning_fails() -> None:
    inventory = full_inventory()
    inventory["validation"]["sourceLabelWarnings"] = [
        {
            "componentSet": "Test / Table / Data Row",
            "reason": "Source label is inside or too close to the variant grid",
        }
    ]
    code, result = run_validator(inventory)
    assert code == 1
    assert_blocking_contains(result, "validation.sourceLabelWarnings is not empty")


def test_full_inventory_with_blocks_passes() -> None:
    inventory = full_inventory()
    code, result = run_validator(inventory)
    assert code == 0
    assert result["required_block_count"] == len(inventory["blocks"])
    assert result["missing_blocks"] == []


def test_legacy_inventory_warns_but_runs() -> None:
    contract = load_contract()
    inventory = {
        "sections": [{"name": f"Test / {name}"} for name in contract["required_sections"]],
        "componentSets": [{"name": f"Test / {item['name']}"} for item in contract["required_components"]],
        "validation": {},
    }
    code, result = run_validator(inventory)
    assert code == 0
    assert result["schemaWarnings"]


def main() -> int:
    tests = [
        test_icon_button_does_not_match_button,
        test_feature_card_does_not_match_card,
        test_missing_axes_fail,
        test_section_order_and_duplicate_fail,
        test_block_missing_required_components_fails,
        test_block_required_components_are_exact,
        test_block_detached_instance_fails,
        test_source_label_warning_fails,
        test_full_inventory_with_blocks_passes,
        test_legacy_inventory_warns_but_runs,
    ]
    for test in tests:
        test()
    print(f"ok - {len(tests)} validate_component_contract regression tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
