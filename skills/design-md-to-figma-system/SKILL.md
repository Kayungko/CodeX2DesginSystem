---
name: design-md-to-figma-system
description: Build or update a complete single-page Figma design system from a DESIGN.md style source, awesome-design-md reference folder, brand design language, or preview.html using Figma MCP. Use when the user asks to generate variables/tokens, styles, component libraries, patterns, examples, validation screenshots, or documentation from DESIGN.md with Figma MCP.
---

# DESIGN.md to Figma System

Use this skill to turn a `DESIGN.md` source into a Figma design system page. The default output is a complete single-page style library: tokens, text/effect styles, core components, editor controls, patterns, examples, validation, and documentation.

## Mandatory Companion Skills

- Load `figma-use` before every `use_figma` call.
- Load `figma-generate-library` for design system generation, variables, components, and validation.
- Load `awesome-design-md` when the source is inside `awesome-design-md-cn` or another VoltAgent/awesome-design-md style folder.

## Quick Start

1. Resolve inputs with `scripts/validate_skill_inputs.py`.
2. Read the selected `DESIGN.md`; optionally inspect `preview.html` and `preview-dark.html`.
3. Inspect the target Figma file before writing anything.
4. Follow `references/workflow.md` for the generation sequence.
5. Keep `references/guardrails.md` open when writing or migrating Figma nodes.
6. Validate with `references/validation-checklist.md` before final response.

## Default Output Contract

- One Figma page per style. Use the style name as the page name.
- Inside the page, create sections named:
  - `Style Name / Overview`
  - `Style Name / Foundations`
  - `Style Name / Core Components`
  - `Style Name / Editor Controls`
  - `Style Name / Patterns`
  - `Style Name / Examples`
  - `Style Name / Reference Notes`
- Build variables before components.
- Build components before examples.
- Move existing master components when restructuring; do not duplicate them unless the user asks for a fork.
- Update product and progress docs at the end of every generation or migration task.

## References

- `references/workflow.md`: exact Figma MCP workflow and phase order.
- `references/guardrails.md`: failure modes to avoid, including overlap, variant stacking, instance breakage, and menu item vertical alignment.
- `references/component-taxonomy.md`: MVP components, pattern groups, and variant guidance.
- `references/validation-checklist.md`: final checks and report shape.
- `references/figma-inspired-case-study.md`: case study from the Figma inspired system built from `design-md/figma`.

## Scripts

- `scripts/scan_design_md.py <root>` lists available DESIGN.md style folders.
- `scripts/validate_skill_inputs.py --design-md <path> --figma-url <url>` validates required inputs and extracts the Figma file key.

Do not put Figma mutation logic into scripts. Figma writes must stay in MCP calls so the agent can inspect, validate, and recover incrementally.
