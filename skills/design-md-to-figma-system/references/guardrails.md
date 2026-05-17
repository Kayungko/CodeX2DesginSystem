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
- Do not fill structural frames unless the fill communicates a required surface. Prefer setting the Figma page background for theme atmosphere and keeping sections/layout wrappers transparent.
- For horizontal controls, set `counterAxisAlignItems = 'CENTER'`.
- For fixed-height menu rows, prefer `paddingTop = 0`, `paddingBottom = 0`, and center alignment.
- Do bounding-box overlap checks for each section.
- Check annotation-label proximity: source/status labels must not touch, overlap, or visually attach to variant cards.
- Do not hand-place dense controls without a grid.
- Keep top-level section spacing at 240px or more.

## Components

- Variables first, components second.
- Every style must include the Tier 1 standard component contract from `component-taxonomy.md`.
- Do not let source-specific components replace standard components. For example, `Now Playing Bar` does not replace `Panel`, and `Command Code Block` does not replace `Text Field`.
- If the source does not show a required component, infer it and mark it as `Inferred`.
- Store source status as component metadata first: component description/shared data and inventory `sourceStatus`. Do not place visible `Source=Inferred` text inside a component set or variant card.
- If a visible source-status note is useful for documentation, place it in a separate annotation row or caption outside the component set with at least 16px spacing from the variant grid, and make it visually secondary.
- Keep theme-specific components in their own section so cross-theme coverage remains comparable.
- Reposition variants after `combineAsVariants`; they may stack at origin.
- Avoid variant explosion. Split by component family if needed.
- Do not create a variant per icon; use icon slots or instance swap in later iterations.
- Keep v1/legacy components separate from v2 production components.
- Do not detach or duplicate master components during migration unless explicitly requested.

## Blocks

- Every block must instance its `requiredComponents` from master component sets. Detached local copies break the contract.
- A block must not replace or stand in for a missing standard component. If a required component is absent, generate it first.
- Blocks belong in the `Blocks` section, not in `Patterns` or `Examples`.
- Block variant exploration (sidebar-left vs sidebar-right, compact vs relaxed) is done with separate block frames, not by parameterizing the block as a component set.
- Contextual blocks (E-commerce, AI/Chat, File Management) are optional. Record omitted blocks and the reason in `Reference Notes`.
- Block inner instances must still reference `mainComponent` after layout adjustments. Run an instance check on every block before delivery.
- Do not overstyle block backgrounds. Blocks should use the page background and rely on inner component surfaces for contrast.

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
- Production component sets: `Style Name / Component Name` or the file's established prefix. Keep the component noun stable across themes.
- Standard component names must stay comparable across themes: `Panel` is always `Panel`, not `Spotify Container` or `Volt Surface`.
- Theme-specific components may use source nouns: `Spotify / Now Playing Bar`, `VoltAgent / Agent Node`.
- Patterns: descriptive names such as `Command Menu / Quick Actions`.
- Avoid claiming an official design system. Use "inspired" or "reference-based" language.
