# Validation Checklist

Run these checks before finalizing.

## Figma Structure

- Target style exists as exactly one page.
- Expected sections exist in order.
- Old split pages are removed after migration, when applicable.
- Local variable collections have expected names, counts, and modes.
- Local text/effect styles were created or preserved.

## Components

- Every expected component set exists.
- Variant counts match the plan.
- Variant properties have stable names.
- Component set bounds are nonzero and readable.
- Horizontal row controls are vertically centered.
- Instances in examples still have `mainComponent`.

## Layout

- No bounding-box overlaps inside each section, excluding intentional nested children.
- Top-level sections have at least 240px vertical separation.
- Section title text is not clipped.
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
- Editor Controls
- Patterns
- Examples

Check screenshots for clipping, collapsed variants, top-edge text alignment, and incoherent overlap.

## Documentation

- Update product documentation with page structure, component scope, and non-goals.
- Update progress documentation with counts, screenshots taken, warnings, and known follow-ups.
- In final response, report validation status and any unresolved risks.
