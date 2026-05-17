# Multi-Theme Standardization Progress

## Summary

Completed incremental standardization for the existing `Figma Inspired`, `Spotify Inspired`, and `VoltAgent Inspired` pages in Figma file `6OrAjGdiQXjTkvBdJIb0XJ`.

The migration preserved existing master component IDs, added missing Tier 1 standard components, moved theme-specific components into dedicated sections, removed empty legacy `Editor Controls` sections, and adopted page background colors instead of filling structural section frames.

For a fresh-machine or new-Codex handoff, start with `docs/NEXT_HANDOFF_PLAN.md`.

## Page Results

| Page | Sections | Component Sets | Missing Required Components | Layout Warnings |
| --- | ---: | ---: | ---: | ---: |
| Figma Inspired | 11 | 41 | 0 | 0 |
| Spotify Inspired | 10 | 33 | 0 | 0 |
| VoltAgent Inspired | 10 | 34 | 0 | 0 |

## Standard Sections

The `Spotify Inspired` and `VoltAgent Inspired` baseline pages contain:

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

`Figma Inspired` additionally contains `Blocks` between `Theme-Specific Components` and `Patterns` because it is the active `full-blocks-v3` trial page.

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
- Live Figma cleanup completed after plugin authorization recovered.
- Removed 24 visible `Source=Inferred` text layers from component variants across the three pages: 8 in Figma Inspired, 8 in Spotify Inspired, and 8 in VoltAgent Inspired.
- Verified by read-only scan that all three pages now have `totalSourceTexts=0` and `insideCount=0`.
- Verified `Figma Inspired / Table / Data Row` now has only the visible row title in each variant; `Source=Inferred` remains in component and variant descriptions.

## Blocks v3 Trial

Status on 2026-05-17:

- Enabled `contractProfile=full-blocks-v3` for `Figma Inspired` only. `Spotify Inspired` and `VoltAgent Inspired` remain on `tier1-31-no-blocks`.
- Inserted `Figma Inspired / Blocks` between `Theme-Specific Components` and `Patterns`; moved `Patterns`, `Examples`, and `Reference Notes` down by 2840px.
- Structural section frame has no fill; block cards use content surface styling only.
- Created 5 trial blocks from existing master component instances:
  - Dashboard Shell: `203:39`
  - Settings Layout: `203:61`
  - Mail Shell: `203:75`
  - Feature Grid: `203:89`
  - Empty State Pattern: `203:119`
- Verified via read-only Figma scan: section overlaps `[]`, `sourceLabelWarnings=[]`, `instanceDetachWarnings=[]`.
- Recorded the remaining 13 contract blocks as omitted warnings with `omittedReason`; they are not final-blocking for this trial.
- Hardened `validate_component_contract.py` so block dependencies use exact `standardName` from `requiredComponentInstances[]`; substring matches such as `Feature Card` -> `Card` are rejected.

## Blocks v3 Phase 2

Status on 2026-05-17:

- Continued only on `Figma Inspired`; `Spotify Inspired` and `VoltAgent Inspired` remain on `tier1-31-no-blocks`.
- Added dependency component sets:
  - `Figma Inspired / Label`: `209:74`
  - `Figma Inspired / Button Group`: `209:85`
- Added 6 more block frames:
  - Login Page: `209:86`
  - Password Reset: `209:106`
  - Notification Settings: `209:122`
  - Pricing Table: `209:147`
  - Error Page: `209:178`
  - Onboarding Stepper: `209:188`
- Blocks section height expanded from 2600 to 3600; `Patterns`, `Examples`, and `Reference Notes` moved down by 1000px.
- Verified via read-only Figma scan: 11 present blocks, section overlaps `[]`, `sourceLabelWarnings=[]`, `instanceDetachWarnings=[]`.
- Remaining omitted blocks reduced from 13 to 7. They require contextual/broader dependencies and stay warnings, not final-blocking.

## Validation Commands

```powershell
python skills/design-md-to-figma-system/scripts/validate_component_contract.py docs/figma-inspired-standard-inventory.json
python skills/design-md-to-figma-system/scripts/validate_component_contract.py docs/figma-inspired-standard-inventory.json --profile full-blocks-v3
python skills/design-md-to-figma-system/scripts/validate_component_contract.py docs/spotify-inspired-standard-inventory.json
python skills/design-md-to-figma-system/scripts/validate_component_contract.py docs/voltagent-inspired-standard-inventory.json
```

Latest local results:

- Figma Inspired: `ok=true`, `contractProfile=full-blocks-v3`, `finalBlocking=[]`, `schemaWarnings=[]`, `present_blocks=11`, `omitted_blocks=7`.
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

Additional source-label cleanup QA targets:

- `Table / Data Row`: `169:107`
- `Navigation & Layout`: `169:38`
- `Feedback & Overlays`: `169:42`

Additional Blocks v3 QA targets:

- `Blocks`: `203:34`
- `Dashboard Shell`: `203:39`
- `Settings Layout`: `203:61`
- `Mail Shell`: `203:75`
- `Feature Grid`: `203:89`
- `Empty State Pattern`: `203:119`
- `Login Page`: `209:86`
- `Password Reset`: `209:106`
- `Notification Settings`: `209:122`
- `Pricing Table`: `209:147`
- `Error Page`: `209:178`
- `Onboarding Stepper`: `209:188`
