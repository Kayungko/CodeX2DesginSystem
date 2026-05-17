# Component Taxonomy

Use this taxonomy as the standard component contract for every generated style page. A source `DESIGN.md` can add theme-specific components, but it must not shrink the standard library.

## Component Tiers

### Tier 1: Required Standard Components

Every style page must include these component sets, even when the source does not explicitly show them. If a component is inferred from tokens instead of directly observed in the source, mark it with a note such as `Source=Inferred`.

#### Actions (5)
| Component | Minimum Variant Axes |
| --- | --- |
| Button | Variant x Size x State |
| Icon Button | Variant x Size x State |
| Link | Tone x State |
| Badge / Tag | Tone x Emphasis x State |
| Button Group | Variant x Size x State |

#### Inputs (11)
| Component | Minimum Variant Axes |
| --- | --- |
| Text Field | Value x State x Validation |
| Search Field | Value x State |
| Select / Dropdown | Value x State |
| Checkbox | Checked x State |
| Radio | Checked x State |
| Switch | Checked x State |
| Slider | Value x State |
| Calendar / Date Picker | Variant x State |
| Combobox | Value x State |
| Input OTP | Value x State |
| Input Group | Variant x State |

#### Navigation (6)
| Component | Minimum Variant Axes |
| --- | --- |
| Navigation Bar | Density x State |
| Sidebar / Rail | Density x State |
| Tabs | Selected x State |
| Segmented Control | Selected x State |
| Breadcrumb | Density x State |
| Pagination | Density x State |

#### Surfaces (9)
| Component | Minimum Variant Axes |
| --- | --- |
| Card | Variant x State |
| Panel | Variant x State |
| Divider | Orientation x Tone |
| Table / Data Row | Density x State |
| Accordion | Variant x State |
| Avatar | Variant x Size x State |
| Carousel | Variant x State |
| Collapsible | State |
| Scroll Area | Variant x State |

#### Feedback (7)
| Component | Minimum Variant Axes |
| --- | --- |
| Tooltip | Placement x Tone |
| Toast / Notification | Tone x State |
| Progress / Loading | Variant x State |
| Empty State | Density x Action |
| Alert | Tone x State |
| Skeleton | Variant x Density |
| Spinner | Size x Tone |

#### Overlays (9)
| Component | Minimum Variant Axes |
| --- | --- |
| Modal / Dialog | Size x State |
| Command Menu | Density x State |
| Menu Item | Selected x State |
| Alert Dialog | Tone x State |
| Context Menu | Density x State |
| Drawer / Sheet | Side x Size x State |
| Dropdown Menu | Density x State |
| Hover Card | Variant x State |
| Popover | Placement x State |

#### Documentation (7)
| Component | Minimum Variant Axes |
| --- | --- |
| Section Header | Density |
| Type Sample | Role |
| Spacing Scale Item | Size |
| Radius Scale Item | Radius |
| Elevation Card | Level |
| Label | Tone x State |
| Kbd | Variant |

### Tier 2: Contextual Standard Components

Include these when the target product category benefits from them. If omitted, record the reason in `Reference Notes`.

| Context | Components |
| --- | --- |
| Developer tools | Code Block, Command Bar, Status Indicator, Log Row |
| Media/content apps | Media Card, Playback Control, Content Grid, Now Playing Bar |
| Dashboard/data apps | Metric Card, Chart Container, Filter Bar, Data Toolbar, Chart |
| Design/editor tools | Toolbar, Inspector Panel, Color Swatch, Property Row, Toggle, Resizable |
| Marketing/product pages | Hero CTA Group, Logo Marquee, Feature Section, Footer / Dark Section, Aspect Ratio |
| E-commerce | Product Card, Price Tag, Cart Row, Checkout Summary, Order Summary |
| AI / Chat | Chat Bubble, Message Input, Model Badge, Thought Process, Token Counter |
| File Management | File Tree, Upload Zone, File Card, File Preview |

### Tier 3: Theme-Specific Components

Use these to preserve source identity. They belong in `Theme-Specific Components` or `Patterns`, not as substitutes for Tier 1.

Examples:

- Spotify Inspired: Play Button, Album Card, Playlist Header, Now Playing Bar.
- VoltAgent Inspired: Command Code Block, Agent Node, Agent Flow Diagram, Logo Marquee.
- Figma Inspired: Product Tab, Toolbar, Inspector Panel, Screenshot Frame.

### Tier 4: Blocks & Compositions

Blocks are multi-component compositions that instantiate master components. They validate the component library by proving components work together in real layouts. Unlike Patterns (which are free-form), Blocks follow a defined composition contract.

Each block must:
- Instance its `requiredComponents` from master component sets (never detach).
- Be placed in the `Blocks` section, distinct from `Patterns` and `Examples`.
- Use Auto Layout for the outer shell; inner instances inherit their own layout.

#### Dashboard
| Block | Required Components | Recommended |
| --- | --- | --- |
| Dashboard Shell | Sidebar / Rail, Navigation Bar, Card, Table / Data Row | Button, Badge / Tag, Chart, Spinner, Avatar |
| Analytics View | Chart Container, Filter Bar, Data Toolbar, Table / Data Row | Card, Segmented Control, Calendar / Date Picker, Button |

#### Authentication
| Block | Required Components | Recommended |
| --- | --- | --- |
| Login Page | Card, Text Field, Button, Label | Checkbox, Link, Divider, Input Group |
| Sign Up Page | Card, Text Field, Button, Label, Checkbox | Input OTP, Input Group, Link, Divider, Toast / Notification |
| Password Reset | Card, Text Field, Button, Label | Alert, Progress / Loading, Link |

#### Settings
| Block | Required Components | Recommended |
| --- | --- | --- |
| Settings Layout | Sidebar / Rail, Tabs, Text Field, Button | Switch, Select / Dropdown, Segmented Control, Divider, Avatar |
| Notification Settings | Switch, Section Header, Divider | Radio, Segmented Control, Label, Card |

#### Layout Shells
| Block | Required Components | Recommended |
| --- | --- | --- |
| Mail Shell | Sidebar / Rail, Table / Data Row, Panel | Search Field, Button, Icon Button, Badge / Tag, Avatar, Divider |
| Chat Interface | Chat Bubble, Message Input, Scroll Area | Avatar, Spinner, Empty State, Icon Button, Divider |

#### Landing Page
| Block | Required Components | Recommended |
| --- | --- | --- |
| Hero Section | Hero CTA Group, Button, Button Group | Badge / Tag, Carousel, Logo Marquee |
| Feature Grid | Card, Icon Button, Section Header | Badge / Tag, Link |
| Pricing Table | Segmented Control, Card, Button, Divider | Badge / Tag, Checkbox, Tooltip |
| Testimonial Carousel | Carousel, Card, Avatar | Badge / Tag, Icon Button |
| Footer Section | Footer / Dark Section, Link, Icon Button, Divider | Badge / Tag, Kbd |

#### Utility
| Block | Required Components | Recommended |
| --- | --- | --- |
| Empty State Pattern | Empty State, Button | Link, Icon Button |
| Error Page | Empty State, Button | Link, Kbd |
| File Upload Zone | Upload Zone, Progress / Loading, File Card | Button, Icon Button, Toast / Notification, Empty State |
| Onboarding Stepper | Progress / Loading, Text Field, Button, Button Group | Select / Dropdown, Checkbox, Radio, Card, Alert |

## Page Sections

Use this section structure for every style:

- `Overview`
- `Foundations`
- `Core Components`
- `Form & Input Controls`
- `Navigation & Layout`
- `Feedback & Overlays`
- `Theme-Specific Components`
- `Blocks`
- `Patterns`
- `Examples`
- `Reference Notes`

For older pages that still use `Editor Controls`, place editor controls inside `Form & Input Controls` or `Navigation & Layout` during the next migration.

Block placement rules:
- Blocks go in `Blocks`, after `Theme-Specific Components` and before `Patterns`.
- Every block must be a self-contained composition frame.
- Block content must reference master component instances, not local copies.
- If a block's required component is missing from Tier 1, generate that component first.

## Standard Variant Axes

Keep variant matrices comparable across styles. Use source-specific names for visual variants, but keep the axis names stable.

| Component | Minimum Variant Axes |
| --- | --- |
| Button | Variant x Size x State |
| Icon Button | Variant x Size x State |
| Link | Tone x State |
| Badge / Tag | Tone x Emphasis x State |
| Button Group | Variant x Size x State |
| Text Field | Value x State x Validation |
| Search Field | Value x State |
| Select / Dropdown | Value x State |
| Checkbox | Checked x State |
| Radio | Checked x State |
| Switch | Checked x State |
| Slider | Value x State |
| Calendar / Date Picker | Variant x State |
| Combobox | Value x State |
| Input OTP | Value x State |
| Input Group | Variant x State |
| Navigation Bar | Density x State |
| Sidebar / Rail | Density x State |
| Tabs | Selected x State |
| Segmented Control | Selected x State |
| Breadcrumb | Density x State |
| Pagination | Density x State |
| Card | Variant x State |
| Panel | Variant x State |
| Divider | Orientation x Tone |
| Table / Data Row | Density x State |
| Accordion | Variant x State |
| Avatar | Variant x Size x State |
| Carousel | Variant x State |
| Collapsible | State |
| Scroll Area | Variant x State |
| Tooltip | Placement x Tone |
| Toast / Notification | Tone x State |
| Progress / Loading | Variant x State |
| Empty State | Density x Action |
| Alert | Tone x State |
| Skeleton | Variant x Density |
| Spinner | Size x Tone |
| Modal / Dialog | Size x State |
| Command Menu | Density x State |
| Menu Item | Selected x State |
| Alert Dialog | Tone x State |
| Context Menu | Density x State |
| Drawer / Sheet | Side x Size x State |
| Dropdown Menu | Density x State |
| Hover Card | Variant x State |
| Popover | Placement x State |
| Section Header | Density |
| Type Sample | Role |
| Spacing Scale Item | Size |
| Radius Scale Item | Radius |
| Elevation Card | Level |
| Label | Tone x State |
| Kbd | Variant |

## State Set

Default state set:

- Default
- Hover
- Focus
- Disabled
- Pressed or Selected when applicable
- Error for validation components
- Loading when async behavior is relevant

## Inferred Component Rule

When the source lacks an explicit component, infer it from:

1. Source token roles: surface, border, text, accent, semantic states.
2. Source layout grammar: radius, density, shadow, border weight, motion.
3. Closest sibling component in the same style.

Do not leave the component out merely because the source page did not show it.

Record inferred status in machine-readable metadata:

- Set inventory `componentSets[].sourceStatus = "Inferred"`.
- Add `Source=Inferred` to the component description or shared plugin data when useful.
- Do not add `Source=Inferred` as a text child inside the component set or inside a variant frame.
- If a visible status label is needed in the documentation canvas, put it in a separate caption/annotation frame outside the component set, at least 16px from the variant bounds.
- Treat source labels that touch or sit inside the variant grid as `validation.sourceLabelWarnings`.

## Machine-Readable Contract

Use `references/standard-component-contract.json` as the stable checklist for generation and validation scripts. The Markdown file explains intent; the JSON file defines required names, minimum axes, and block composition contracts.
