# UI2 Editor Workbench Analysis

## Source

- UI2 component library: `8iEzdFqojLjUkZPZ3FwgOT`, node `0:11724`
- UI2 editor template: `8iEzdFqojLjUkZPZ3FwgOT`, node `448:1`
- DesignSystem target: `6OrAjGdiQXjTkvBdJIb0XJ`

## UI2 Component Map

The UI2 source is organized by product-interface regions rather than marketing UI. The useful groups for future workbench development are:

- Panels: transform controls, style rows, paint mixer, export settings, layout grid settings, color mixer, layer list rows, separators, sliders, empty panels, modal rows.
- Sidebar: page navigator, page list items, asset grid, layer list, layer rows for frame/group/text/slice/vector/mask/component/instance, right-sidebar prototype rows.
- Toolbar: edit/view toolbar, tool buttons, file title, share/sign-in actions, multiplayer avatars, prototype options, viewport controls.
- Controls: disclosure, label, radio, paint, option menu, style selector, option strip, checkbox, switch, value input, progress indicator.
- Menus: menu base, simple action rows, submenu rows, on/off rows, separators, Windows-style menu examples.
- Overlay and Windows: tooltip, notification, visual bell, modal/non-modal dialog templates, window background/title bar/close states.
- Desktop app: tab strip, file tabs, file browser states, macOS menu chrome.
- Navigation bars, Cards, Banners: higher-level browse/community shells that are useful later, but lower priority than editor workbench primitives.

## Editor Template Anatomy

The `Editor template` frame is a 1680 x 880 desktop workbench. Its durable structure is:

- Top toolbar: 40px high, left tool cluster, centered file/title region, right collaboration/prototype/share controls.
- Left sidebar: 240px wide, page navigator at top and dense layer list below.
- Center canvas: large neutral workspace that frames artboards rather than content cards.
- Right inspector: dense property rows and grouped controls for design/prototype settings.
- Interaction language: 32/40px icon cells, compact rows, low-radius panels, selected rows with subtle fill or accent stroke, no decorative hero treatment.

## DesignSystem Implementation

Implemented a derived `UI2 Workbench` kit in each existing style page, under `Patterns` only. No new standard top-level section was added, so the existing component contract section order remains intact.

Per style page:

- `Workbench Toolbar`: `Mode=Design|Prototype`, `State=Default`
- `Workbench Sidebar`: `Side=Left|Right`, `Density=Compact|Default`
- `Workbench Layer Row`: `Kind=Frame|Group|Text|Component`, `State=Default|Selected`
- `Workbench Control Row`: `Kind=Value|Option|Toggle|Color`, `State=Default|Focus`
- `Workbench Shell`: `Mode=Design|Prototype`, `Density=Desktop`
- `UI2 Editor Template Reference`: exact P4 clone of the UI2 editor template structure, 1680 x 880

Node IDs:

| Page | Toolbar | Sidebar | Layer Row | Control Row | Shell | P4 Reference |
| --- | --- | --- | --- | --- | --- | --- |
| Figma Inspired | `228:444` | `228:445` | `228:446` | `228:447` | `228:448` | `233:122` |
| Spotify Inspired | `228:821` | `228:822` | `228:823` | `228:824` | `228:825` | `233:142` |
| VoltAgent Inspired | `228:1198` | `228:1199` | `228:1200` | `228:1201` | `228:1202` | `233:162` |

The first pass used a simplified themed example. After reviewing `Page 4` in the DesignSystem file, the examples were replaced with exact P4 template clones to preserve the real UI2 workbench proportions: 40px top toolbar, 240px sidebars, right inspector panel stack, and central paint mixer.

## Follow-Up

- Add deeper inspector primitives: property row, color swatch row, slider row, token picker row.
- Add menu/overlay variants: context menu, command palette, notification, tooltip, non-modal dialog.
- Add workbench blocks after primitives stabilize: design editor shell, asset browser, code inspector, prototype review mode.
- Consider a future `workbench-v1` contract profile if these patterns become required across every theme.
