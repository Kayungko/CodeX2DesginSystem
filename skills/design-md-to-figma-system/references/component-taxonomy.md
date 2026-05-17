# Component Taxonomy

Use this as the MVP component map unless the source DESIGN.md strongly suggests another structure.

## Core Components

| Component | Minimum Variants |
| --- | --- |
| Button | Size x Variant x State |
| Icon Button | Size x Variant x State |
| Product Tab / Tab | Item or Label x State |
| Card | Standard, Elevated, Glass, Media, Content, Dark |
| Text Field | Value x State |
| Search Field | Value x State |
| Badge / Label | Subtle, Solid |
| Navigation Bar | One reusable pattern/component |
| Section Header | One reusable component |

## Editor Controls

Use these when the style targets productivity, design, developer tooling, dashboards, or dense product surfaces.

| Component | Minimum Variants |
| --- | --- |
| Checkbox | Value x State |
| Radio | Value x State |
| Switch | Value x State |
| Disclosure | Opened x State |
| Segmented Control Item | Selected x State |
| Menu Item | Leading Icon x State |

## Patterns

Group patterns by usage:

- Primitive patterns: Link, Divider, Gradient Preview, Type Sample, spacing/radius/elevation samples.
- Product sections: Product Showcase Card, Product Showcase Section, Hero CTA Group, Responsive Navigation Bar, Footer / Dark Section.
- Overlay and panels: Tooltip, Toast, Command Menu, Side Panel, Window / Screenshot Frame.

## Variant States

Default state set:

- Default
- Hover
- Focus
- Disabled
- Pressed or Selected when the source calls for it
- Error for inputs

Use dashed focus rings when the design language calls for visible keyboard focus.
