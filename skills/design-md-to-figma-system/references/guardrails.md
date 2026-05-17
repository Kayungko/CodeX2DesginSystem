# Guardrails

These rules come from issues observed while building the Figma inspired design system.

## Figma MCP Safety

- Always inspect before mutating.
- Never parallelize `use_figma` calls.
- Every mutation call must return created or mutated node IDs.
- Figma scripts are atomic on failure. Read the error before retrying.
- Do not use `figma.currentPage = page`; use `await figma.setCurrentPageAsync(page)`.
- Do not use `figma.notify()`.
- Load fonts before creating or editing text.

## Layout

- Use Auto Layout for controls, rows, cards, menus, and section headers.
- For horizontal controls, set `counterAxisAlignItems = 'CENTER'`.
- For fixed-height menu rows, prefer `paddingTop = 0`, `paddingBottom = 0`, and center alignment.
- Do bounding-box overlap checks for each section.
- Do not hand-place dense controls without a grid.
- Keep top-level section spacing at 240px or more.

## Components

- Variables first, components second.
- Reposition variants after `combineAsVariants`; they may stack at origin.
- Avoid variant explosion. Split by component family if needed.
- Do not create a variant per icon; use icon slots or instance swap in later iterations.
- Keep v1/legacy components separate from v2 production components.
- Do not detach or duplicate master components during migration unless explicitly requested.

## Bindings

- Core components should have variable-bound fills, strokes, radius, spacing, and control sizing.
- Gradients and demonstration art may remain hardcoded.
- Validation should count hardcoded solid fills/strokes for core components.

## Single-Page Style Libraries

- In a multi-style design system file, one page equals one style.
- Restructure existing split pages by moving nodes, not copying.
- Verify key IDs before and after migration.
- Verify instances still have `mainComponent`.

## Naming

- Page: `Style Name`.
- Sections: `Style Name / Overview`, `Style Name / Foundations`, etc.
- Production component sets: `v2 / Component Name`.
- Patterns: descriptive names such as `Command Menu / Quick Actions`.
- Avoid claiming an official design system. Use "inspired" or "reference-based" language.
