# Validation Checklist

Run these checks before finalizing.

## Figma Structure

- Export `design-md-system-inventory/v2` using `references/figma-inventory-export.md`.
- Current baseline inventories declare `contractProfile=tier1-31-no-blocks`; Blocks v3 inventories declare `contractProfile=full-blocks-v3` and validate the 31-component baseline plus Blocks.
- Target style exists as exactly one page.
- Expected sections exist in order.
- Current baseline builds use: Overview, Foundations, Core Components, Form & Input Controls, Navigation & Layout, Feedback & Overlays, Theme-Specific Components, Patterns, Examples, Reference Notes.
- Full Blocks v3 builds insert Blocks between Theme-Specific Components and Patterns.
- Section `standardName` values are unique and appear in contract order.
- Old split pages are removed after migration, when applicable.
- Local variable collections have expected names, counts, and modes.
- Local text/effect styles were created or preserved.

## Components

- All Tier 1 required components from `standard-component-contract.json` exist.
- Missing required components are final-blocking unless the user explicitly approves a reduced library.
- Required component matching uses `componentSets[].standardName`; legacy `name` matching is exact after removing the style namespace only.
- `Feature Card` must not satisfy `Card`, and `Icon Button` must not satisfy `Button`.
- Required axes from the contract are covered by `variantProperties`.
- `sourceStatus` is one of `Observed`, `Inferred`, or `Theme-Specific`.
- Inferred components are documented as `Source=Inferred`.
- Theme-specific components are documented separately from standard coverage.
- Standard components are not placed in `Theme-Specific Components`.
- Theme-specific components never replace required standard components.
- Every expected component set exists.
- Variant counts match the plan.
- Variant properties have stable names.
- Component set bounds are nonzero and readable.
- Horizontal row controls are vertically centered.
- Instances in examples still have `mainComponent`.
- Source-status labels are metadata or separate annotations, not text inside component sets or variant cards.
- Visible source-status annotations sit outside the variant grid with at least 16px spacing.

## Blocks

- Skip this section for `contractProfile=tier1-31-no-blocks`.
- For `full-blocks-v3`, all required blocks from `standard-component-contract.json` are either present in the `Blocks` section or explicitly omitted with a reason.
- Missing blocks are final-blocking unless the category is out of scope for the product type (record the reason in `Reference Notes`).
- Every block's required components are present as master component instances; no detached local copies.
- Inventory uses `blocks[].requiredComponentInstances[]` as the authoritative list, with exact `standardName`, `instanceId`, `mainComponentId`, and `mainComponentName`.
- Block component matching is exact by `standardName`; `Feature Card` must not satisfy `Card`.
- Dependency-only components such as Label or Button Group can support active blocks without increasing the 31-component baseline required count.
- Block content is contained within its own Auto Layout frame.
- Blocks do not appear in `Patterns` or `Examples` sections.
- Omitted contextual blocks are documented with reasons.
- Block instances pass `mainComponent` reference check.

## Layout

- No bounding-box overlaps inside each section, excluding intentional nested children.
- Top-level sections have at least 240px vertical separation.
- Section title text is not clipped.
- Blocks use a fixed card width, wrapping grid, and enough section height for all rows.
- `validation.sourceLabelWarnings` is empty.
- Dense controls and overlays do not overlap product sections.

## Bindings

- Count bound vs hardcoded fills/strokes for core components.
- Core components should have zero hardcoded solid fills/strokes unless explicitly justified.
- Gradients and decorative demos are allowed exceptions.

## Visual QA

Capture screenshots for:

- full style page
- Foundations
- Core Components
- Form & Input Controls
- Navigation & Layout
- Feedback & Overlays
- Theme-Specific Components
- Patterns
- Examples

Also capture Blocks when the full Blocks v3 contract is active.

Check screenshots for clipping, collapsed variants, top-edge text alignment, and incoherent overlap.

## Documentation

- Update product documentation with page structure, component scope, and non-goals.
- Update progress documentation with counts, screenshot node IDs, inventory schema version, validation commands, warnings, and known follow-ups.
- Report `finalBlocking`, `warnings`, and `schemaWarnings`; do not deliver with non-empty `finalBlocking`.
- In final response, report validation status and any unresolved risks.
