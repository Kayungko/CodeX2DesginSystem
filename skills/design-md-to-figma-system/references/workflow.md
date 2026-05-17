# Workflow

Use this sequence for every DESIGN.md to Figma system build. Do not skip inspection or validation.

## 1. Source Discovery

- Validate inputs with `scripts/validate_skill_inputs.py`.
- Read `DESIGN.md` first.
- Read `README.md`, `preview.html`, and `preview-dark.html` only when present and useful.
- Extract the style name, audience, density, color roles, typography, components, layout rules, and anti-patterns.
- Classify source components as `Observed`, then list which standard components must be `Inferred`.
- Read `references/component-taxonomy.md` and `references/standard-component-contract.json` before locking component scope.
- Record non-goals such as "do not recreate the official design system" or "do not import third-party component libraries."

## 2. Figma Inspection

- Use `use_figma` read-only scripts before writing.
- Inspect pages, variables, local styles, components, component sets, and existing naming.
- Export a v2 inventory with `references/figma-inventory-export.md` when updating or validating an existing page.
- Use `get_libraries` / `search_design_system` only for discovery; do not import remote UI kits unless the user explicitly wants that.
- If updating an existing style page, identify stable master component IDs and plan to move nodes instead of copying.
- If restructuring split pages or old sections, follow `references/migration-playbook.md` before any mutation.

## 3. Token Extraction

- Create primitive variables first.
- Create semantic variables second and alias them to primitives where practical.
- Include modes when the source has light/dark guidance.
- Minimum token groups:
  - primitives
  - semantic color
  - size/spacing/radius/stroke/icon/control
  - opacity
  - motion
- Set scopes and code syntax for every variable.

## 4. Page Structure

- Use one Figma page per style.
- For the current validated baseline, use `contractProfile=tier1-31-no-blocks` and these sections in order:
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
- Use the additional `Blocks` section only when implementing `contractProfile=full-blocks-v3`.
- Keep at least 240px between top-level sections.
- Prefer Figma Section nodes if they are reliable; otherwise use named frames.
- Give each section a title, short description, and content count.

## 5. Component Generation

- Build atoms before molecules and patterns.
- Build the complete Tier 1 standard component contract for every style.
- Do not omit a standard component only because the source lacks an explicit example; infer it from tokens and nearest style grammar.
- Place broad reusable components in standard sections and source-identity components in `Theme-Specific Components`.
- Treat `Source=Observed|Inferred|Theme-Specific` as metadata. Put it in component descriptions/shared data and inventory `sourceStatus`, never as text inside a component set or variant.
- Use Auto Layout for containers and controls.
- After `combineAsVariants`, manually lay out variants in a grid.
- Cap variant matrices. If a component exceeds roughly 36 variants, split it into subcomponents.
- Use `componentPropertyDefinitions` when useful, but do not block MVP completion on advanced instance properties.
- Bind fill, stroke, radius, padding, gap, and control dimensions to variables where possible.

## 6. Block Generation

- Skip this phase for `contractProfile=tier1-31-no-blocks`.
- Generate blocks after master components are complete and before free-form patterns when using `contractProfile=full-blocks-v3`.
- Read the `blocks` section of `references/standard-component-contract.json` to scope which blocks to generate for the target product category.
- Blocks must instance their `requiredComponents` from master component sets; never detach or copy locally.
- Record block dependencies in inventory as `requiredComponentInstances[]` with exact `standardName`, `instanceId`, `mainComponentId`, and `mainComponentName`.
- Required component matching for blocks is exact by `standardName`; do not accept substring or display-name matches.
- If a block references a missing Tier 1 component, generate that component first before the block.
- Each block is a self-contained Auto Layout frame placed in the `Blocks` section.
- Block variants (e.g. sidebar position, density) are handled as separate block frames, not component variants.
- Give each block a title, short description, and component count label.
- Contextual blocks (e.g. E-commerce, AI/Chat) are optional; record which were omitted and why in `Reference Notes`.

## 7. Patterns And Examples

- Patterns should be reusable composition blocks, not full pages.
- Examples should be placed at the end and should instantiate master components.
- Do not mix examples with master component sets.
- For multi-style files, never spread one style across multiple pages.

## 8. Validation And Documentation

- Run structure validation after every major phase.
- Export the final v2 inventory before delivery.
- Validate required sections, required component sets, source labels, and required blocks when active with `scripts/validate_component_contract.py`.
- Final delivery is blocked when `finalBlocking` is not empty.
- Final v2 inventories should have empty `schemaWarnings`; legacy inventories may warn only during migration.
- Report `Observed`, `Inferred`, and `Theme-Specific` component counts.
- Report Block coverage only when using `contractProfile=full-blocks-v3`.
- Screenshot Foundations, Core Components, Form & Input Controls, Navigation & Layout, Feedback & Overlays, Theme-Specific Components, Patterns, and Examples; include Blocks only when that section exists.
- Check overlap before finalizing.
- Update product docs and progress docs with exact counts and validation results.
