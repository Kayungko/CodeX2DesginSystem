# Multi-Theme Standardization Progress

## Summary

Completed incremental standardization for the existing `Figma Inspired`, `Spotify Inspired`, and `VoltAgent Inspired` pages in Figma file `6OrAjGdiQXjTkvBdJIb0XJ`.

The migration preserved existing master component IDs, added missing Tier 1 standard components, moved theme-specific components into dedicated sections, removed empty legacy `Editor Controls` sections, and adopted page background colors instead of filling structural section frames.

## Page Results

| Page | Sections | Component Sets | Missing Required Components | Layout Warnings |
| --- | ---: | ---: | ---: | ---: |
| Figma Inspired | 10 | 40 | 0 | 0 |
| Spotify Inspired | 10 | 33 | 0 | 0 |
| VoltAgent Inspired | 10 | 34 | 0 | 0 |

## Standard Sections

Each page now contains:

- Overview
- Foundations
- Core Components
- Form & Input Controls
- Navigation & Layout
- Feedback & Overlays
- Theme-Specific Components
- Patterns
- Examples
- Reference Notes

## Component Coverage

- Tier 1 required components: 31 / 31 on all three pages.
- Existing observed components were moved rather than recreated where possible.
- New inferred components were marked with `Source=Inferred` in component descriptions/shared data.
- Theme-specific components remain separate:
  - Figma Inspired: Product Tab, Disclosure.
  - Spotify Inspired: Play Button, Content Card and existing music patterns.
  - VoltAgent Inspired: Command Code Block, Agent Node and existing agent patterns.

## Layout And Visual Rules

- Top-level section overlap: 0.
- Horizontal overflow: 0.
- Menu/list horizontal controls: vertically centered, top/bottom padding 0.
- Structural section/grid/header fills: 0.
- Page backgrounds now carry theme atmosphere:
  - Figma Inspired: light neutral.
  - Spotify Inspired: `#121212`.
  - VoltAgent Inspired: `#050507`.

## Screenshots

Captured screenshots for each page:

- Full page
- Core Components
- Form & Input Controls
- Navigation & Layout
- Feedback & Overlays
- Theme-Specific Components
- Examples

## Local Inventory Files

- `docs/figma-inspired-standard-inventory.json`
- `docs/spotify-inspired-standard-inventory.json`
- `docs/voltagent-inspired-standard-inventory.json`

Inventory schema version: `design-md-system-inventory/v2`.
Contract profile: `tier1-31-no-blocks`.

These inventories are used by `validate_component_contract.py` to verify standard coverage, section order, source status, required variant axes, and blocking layout checks.

## Source Label Cleanup

- Source status is treated as metadata only: component descriptions/shared data and inventory `sourceStatus`.
- Visible `Source=Observed`, `Source=Inferred`, or `Source=Theme-Specific` text inside variants is invalid and should be removed from Figma.
- The local inventories now include `validation.sourceLabelWarnings`; the target value is `[]`.
- Current Figma write tool access is required to remove existing variant-level labels from the live file.

Status on 2026-05-17:

- Confirmed via Figma Dev Mode MCP read tools that `Figma Inspired / Table / Data Row` stores `Source=Inferred` as a visible text child inside each variant.
- Hardened the skill, inventory export template, and validator so future inventories treat visible source labels inside component sets or variants as final-blocking.
- Local baseline inventories validate as `ok=true` with `contractProfile=tier1-31-no-blocks`.
- Live Figma cleanup is still pending because the write-capable `use_figma` tool is currently failing MCP client handshake; rerun the cleanup script once write access is restored.

## Validation Commands

```powershell
python skills/design-md-to-figma-system/scripts/validate_component_contract.py docs/figma-inspired-standard-inventory.json
python skills/design-md-to-figma-system/scripts/validate_component_contract.py docs/spotify-inspired-standard-inventory.json
python skills/design-md-to-figma-system/scripts/validate_component_contract.py docs/voltagent-inspired-standard-inventory.json
```

Latest local results:

- Figma Inspired: `ok=true`, `finalBlocking=[]`, `schemaWarnings=[]`.
- Spotify Inspired: `ok=true`, `finalBlocking=[]`, `schemaWarnings=[]`.
- VoltAgent Inspired: `ok=true`, `finalBlocking=[]`, `schemaWarnings=[]`.

## Screenshot Node IDs

Store screenshot targets in the `screenshots[]` array of each v2 inventory after the next read-only Figma export. Required labels:

- Full page
- Foundations
- Core Components
- Form & Input Controls
- Navigation & Layout
- Feedback & Overlays
- Theme-Specific Components
- Patterns
- Examples
