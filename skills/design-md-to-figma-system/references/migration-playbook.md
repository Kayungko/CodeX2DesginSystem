# Migration Playbook

Use this when restructuring an existing Figma design system page or converting old split pages into the single-page style format.

## 1. Snapshot Before Moving

- Export inventory with `references/figma-inventory-export.md`.
- Save page IDs, section IDs, component set IDs, and key instance `mainComponent` IDs.
- Record current variable collection names and counts.
- Stop if component sets cannot be identified by stable IDs.

## 2. Plan The Target Structure

- Target one style page with ten sections in contract order.
- Rename existing sections when that preserves identity.
- Create only missing sections.
- Decide where each component set moves before mutating the file.
- Keep theme-specific component sets in `Theme-Specific Components`.

## 3. Move, Do Not Clone

- Move existing master component sets into the new section containers.
- Do not copy and delete master components, because that can break IDs and examples.
- Do not detach examples; examples should remain instances of master components.
- If a Figma Section node cannot host a component safely, use a named frame as the section container.

## 4. Layout Recovery Rules

- Re-grid component sets after moving them.
- Keep at least 240px between top-level sections.
- Use Auto Layout for section body rows and grids.
- Set horizontal control rows to vertical center alignment.
- Avoid structural frame fills unless they communicate an actual surface; prefer page background for theme atmosphere.

## 5. Post-Migration Diff

- Export inventory again.
- Compare pre/post component set IDs; existing masters should keep the same IDs.
- Check examples for `mainComponent` references.
- Run `validate_component_contract.py` against the new inventory.
- Treat non-empty `finalBlocking` as a stop condition.

## 6. Delete Old Sections Or Pages

Delete an old section or split page only when:

- Its content was moved, not copied.
- Its master component IDs still exist on the target page.
- Its instances still point to `mainComponent`.
- Its old container is empty or contains only intentional notes.
- The latest inventory has no section/component/layout blocking errors.

## 7. Recovery

- If IDs changed, stop and restore from the previous stable state instead of continuing with detached copies.
- If variants stack or collapse, rebuild only the variant layout grid, not the component set identity.
- If overlap remains after two local adjustments, reflow the whole section grid instead of nudging individual nodes.
- If standard coverage is missing, add inferred components and mark `Source=Inferred` rather than letting a theme-specific component stand in for them.
