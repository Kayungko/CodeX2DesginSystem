# Workflow

Use this sequence for every DESIGN.md to Figma system build. Do not skip inspection or validation.

## 1. Source Discovery

- Validate inputs with `scripts/validate_skill_inputs.py`.
- Read `DESIGN.md` first.
- Read `README.md`, `preview.html`, and `preview-dark.html` only when present and useful.
- Extract the style name, audience, density, color roles, typography, components, layout rules, and anti-patterns.
- Record non-goals such as "do not recreate the official design system" or "do not import third-party component libraries."

## 2. Figma Inspection

- Use `use_figma` read-only scripts before writing.
- Inspect pages, variables, local styles, components, component sets, and existing naming.
- Use `get_libraries` / `search_design_system` only for discovery; do not import remote UI kits unless the user explicitly wants that.
- If updating an existing style page, identify stable master component IDs and plan to move nodes instead of copying.

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
- Use these sections in order:
  - Overview
  - Foundations
  - Core Components
  - Editor Controls
  - Patterns
  - Examples
  - Reference Notes
- Keep at least 240px between top-level sections.
- Prefer Figma Section nodes if they are reliable; otherwise use named frames.
- Give each section a title, short description, and content count.

## 5. Component Generation

- Build atoms before molecules and patterns.
- Use Auto Layout for containers and controls.
- After `combineAsVariants`, manually lay out variants in a grid.
- Cap variant matrices. If a component exceeds roughly 36 variants, split it into subcomponents.
- Use `componentPropertyDefinitions` when useful, but do not block MVP completion on advanced instance properties.
- Bind fill, stroke, radius, padding, gap, and control dimensions to variables where possible.

## 6. Patterns And Examples

- Patterns should be reusable composition blocks, not full pages.
- Examples should be placed at the end and should instantiate master components.
- Do not mix examples with master component sets.
- For multi-style files, never spread one style across multiple pages.

## 7. Validation And Documentation

- Run structure validation after every major phase.
- Screenshot Foundations, Core Components, Editor Controls, Patterns, and Examples.
- Check overlap before finalizing.
- Update product docs and progress docs with exact counts and validation results.
