# Figma Inventory Export

Use this reference after the read-only Figma inspection phase and again before final delivery. The export is a contract-facing inventory, not a design artifact. It must not mutate the Figma file.

## When To Export

- Before restructuring an existing page, to capture section and component IDs.
- After creating or migrating components, before running local contract validation.
- After final layout cleanup, to capture validation arrays and screenshot node IDs.

## Required Schema

Write the result as JSON with:

- `schemaVersion`: `design-md-system-inventory/v2`
- `contractProfile`: `tier1-31-no-blocks` for the current 31-component baseline, or omit/use `full` after Blocks v3 is implemented.
- `styleName`, `fileKey`, `pageId`, `pageName`
- `sections[]`: `name`, `standardName`, `index`, `id`, `bounds`
- `componentSets[]`: `name`, `standardName`, `section`, `sourceStatus`, `variantCount`, `variantProperties`, `id`
- `blocks[]`: `name`, `category`, `section`, `id`, `instanceCount`, `requiredComponents`, `omittedReason`
- `validation`: `overlaps`, `overWidth`, `structuralFrameFills`, `sourceLabelWarnings`, `menuAlignmentWarnings`, `instanceDetachWarnings`, `bindingSummary`, plus optional `hardcodedFillWarnings`, `bindingWarnings`, `screenshotWarnings`
- `screenshots[]`: label and node ID for each captured area

`standardName` is authoritative for standard sections and Tier 1 components. For theme-specific component sets, set `sourceStatus` to `Theme-Specific` and leave `standardName` null unless it is also a standard component, which should normally be avoided.

Source status must be metadata. `Source=Observed`, `Source=Inferred`, or `Source=Theme-Specific` text inside a component set or variant is a blocking `sourceLabelWarnings` item.

## Read-Only `use_figma` Template

Load `figma-use` first, then run a read-only script shaped like this:

```js
const STYLE_NAME = "Spotify Inspired";
const STANDARD_SECTIONS = [
  "Overview",
  "Foundations",
  "Core Components",
  "Form & Input Controls",
  "Navigation & Layout",
  "Feedback & Overlays",
  "Theme-Specific Components",
  "Blocks",
  "Patterns",
  "Examples",
  "Reference Notes",
];
const REQUIRED_COMPONENTS = new Set([
  "Button",
  "Icon Button",
  "Link",
  "Badge / Tag",
  "Text Field",
  "Search Field",
  "Select / Dropdown",
  "Checkbox",
  "Radio",
  "Switch",
  "Slider",
  "Navigation Bar",
  "Sidebar / Rail",
  "Tabs",
  "Segmented Control",
  "Card",
  "Panel",
  "Divider",
  "Table / Data Row",
  "Tooltip",
  "Toast / Notification",
  "Progress / Loading",
  "Empty State",
  "Modal / Dialog",
  "Command Menu",
  "Menu Item",
  "Section Header",
  "Type Sample",
  "Spacing Scale Item",
  "Radius Scale Item",
  "Elevation Card",
]);

function bounds(node) {
  return {
    x: node.absoluteBoundingBox?.x ?? node.x ?? 0,
    y: node.absoluteBoundingBox?.y ?? node.y ?? 0,
    width: node.absoluteBoundingBox?.width ?? node.width ?? 0,
    height: node.absoluteBoundingBox?.height ?? node.height ?? 0,
  };
}

function stripStylePrefix(name) {
  return name.replace(new RegExp(`^${STYLE_NAME}\\s*/\\s*`), "").trim();
}

function standardSectionName(name) {
  const tail = stripStylePrefix(name);
  return STANDARD_SECTIONS.includes(tail) ? tail : null;
}

function standardComponentName(name) {
  const parts = name.split("/").map((part) => part.trim()).filter(Boolean);
  const tail = parts.length > 1 ? parts.slice(1).join(" / ") : name.trim();
  return REQUIRED_COMPONENTS.has(tail) ? tail : null;
}

function variantProperties(componentSet) {
  const firstVariant = componentSet.children?.find((child) => child.type === "COMPONENT");
  return Object.keys(firstVariant?.variantProperties ?? {});
}

function sourceStatus(node, standardName) {
  const raw = node.description || "";
  const match = raw.match(/Source=(Observed|Inferred|Theme-Specific)/);
  if (match) return match[1];
  return standardName ? "Inferred" : "Theme-Specific";
}

const page = figma.root.children.find((child) => child.name === STYLE_NAME);
if (!page) throw new Error(`Page not found: ${STYLE_NAME}`);

const sectionNodes = page.children
  .filter((node) => node.type === "SECTION" || node.type === "FRAME")
  .map((node, index) => ({
    name: node.name,
    standardName: standardSectionName(node.name),
    index,
    id: node.id,
    bounds: bounds(node),
  }))
  .filter((node) => node.standardName);

const sectionForNode = (node) => {
  const box = bounds(node);
  const containing = sectionNodes.find((section) => {
    const s = section.bounds;
    return box.x >= s.x && box.y >= s.y && box.x < s.x + s.width && box.y < s.y + s.height;
  });
  return containing?.standardName ?? null;
};

const componentSets = page.findAll((node) => node.type === "COMPONENT_SET").map((node) => {
  const standardName = standardComponentName(node.name);
  return {
    name: node.name,
    standardName,
    section: sectionForNode(node),
    sourceStatus: sourceStatus(node, standardName),
    variantCount: node.children.filter((child) => child.type === "COMPONENT").length,
    variantProperties: variantProperties(node),
    id: node.id,
  };
});

function hasAncestor(node, predicate) {
  let parent = node.parent;
  while (parent && parent.type !== "PAGE") {
    if (predicate(parent)) return parent;
    parent = parent.parent;
  }
  return null;
}

function intersects(a, b) {
  return !(a.x + a.width <= b.x || b.x + b.width <= a.x || a.y + a.height <= b.y || b.y + b.height <= a.y);
}

function edgeDistance(a, b) {
  if (intersects(a, b)) return 0;
  const dx = Math.max(b.x - (a.x + a.width), a.x - (b.x + b.width), 0);
  const dy = Math.max(b.y - (a.y + a.height), a.y - (b.y + b.height), 0);
  return Math.sqrt(dx * dx + dy * dy);
}

const sourceTextNodes = page.findAll(
  (node) =>
    node.type === "TEXT" &&
    /^Source=(Observed|Inferred|Theme-Specific)$/.test((node.characters || "").trim())
);

const componentSetNodes = page.findAll((node) => node.type === "COMPONENT_SET");
const sourceLabelWarnings = [];
for (const textNode of sourceTextNodes) {
  const owner = hasAncestor(textNode, (node) => node.type === "COMPONENT" || node.type === "COMPONENT_SET");
  if (owner) {
    sourceLabelWarnings.push({
      id: textNode.id,
      ownerId: owner.id,
      ownerName: owner.name,
      reason: "source status text is inside a component set or variant; use description/shared data instead",
    });
    continue;
  }
  const textBounds = bounds(textNode);
  const tooClose = componentSetNodes.find((set) => edgeDistance(textBounds, bounds(set)) < 16);
  if (tooClose) {
    sourceLabelWarnings.push({
      id: textNode.id,
      ownerId: tooClose.id,
      ownerName: tooClose.name,
      reason: "visible source status annotation is less than 16px from the variant grid",
    });
  }
}

const blocksSection = sectionNodes.find((s) => s.standardName === "Blocks");
const blockFrames = blocksSection
  ? page.findAll(
      (node) =>
        (node.type === "FRAME" || node.type === "SECTION") &&
        node.parent?.id === blocksSection.id &&
        node.name.startsWith(`${STYLE_NAME} / `)
    )
  : [];

const blocks = blockFrames.map((frame) => ({
  name: frame.name,
  category: (frame.description || "").match(/Category=(\w[\w\s]*)/)?.[1] || null,
  section: "Blocks",
  id: frame.id,
  instanceCount: frame.findAll((node) => node.type === "INSTANCE").length,
  requiredComponents: frame.findAll((node) => node.type === "INSTANCE").map((inst) => inst.name),
  omittedReason: (frame.description || "").match(/Omitted=(.+)/)?.[1] || null,
}));

return {
  schemaVersion: "design-md-system-inventory/v2",
  contractProfile: "tier1-31-no-blocks",
  styleName: STYLE_NAME,
  pageId: page.id,
  pageName: page.name,
  sections: sectionNodes,
  componentSets,
  blocks,
  validation: {
    overlaps: [],
    overWidth: [],
    structuralFrameFills: [],
    sourceLabelWarnings,
    menuAlignmentWarnings: [],
    instanceDetachWarnings: [],
    bindingSummary: {},
    hardcodedFillWarnings: [],
    bindingWarnings: [],
    screenshotWarnings: [],
  },
  screenshots: [],
};
```

## Local Validation

Save the inventory under `docs/*-standard-inventory.json`, then run:

```powershell
python skills/design-md-to-figma-system/scripts/validate_component_contract.py docs/spotify-inspired-standard-inventory.json
```

Delivery is blocked when `finalBlocking` is not empty. `schemaWarnings` are acceptable only for old inventories during migration; final v2 inventories should have no `schemaWarnings`.
