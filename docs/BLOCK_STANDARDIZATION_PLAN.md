# Block Standardization Plan

## 背景

shadcn/ui 除了 56 个核心组件外，官方维护了 50+ 个 **blocks**（页面级组件组合），涵盖 Dashboard、Sidebar、Login、Charts、Calendar、Mail、Tasks、Music 等类别。社区生态（blocks.so、Shadcnblocks、Shadcn Space）更是扩展到了 1,100+ 个 block，包括 Settings、Pricing、Chat、Empty States、File Upload、Onboarding 等领域。

当前 skill 只有自由形式的 `Patterns` 和 `Examples`，缺少结构化的 block 契约，导致多主题设计系统缺少页面级组合的可比性。

## 决策

从当前版本开始，skill 在 Tier 1/2/3 组件之上新增 **Tier 4: Blocks & Compositions** 层。正式 profile 名称为 `full-blocks-v3`，含义是“31 个 Tier 1 基线组件 + Blocks v3 验证层”；现有无 Blocks 基线继续使用 `tier1-31-no-blocks`。

Block 的定义：
- Block 是一个自包含的 Auto Layout frame，放在 `Blocks` section 中
- Block 必须实例化其 `requiredComponents` 从 master component 集，不 detach
- Block inventory 必须记录 `requiredComponentInstances[]`，每项包含 `standardName`、`instanceId`、`mainComponentId`、`mainComponentName`
- Block 依赖只按 `standardName` 精确匹配，禁止使用 substring/includes；例如 `Feature Card` 不等于 `Card`
- Block 是组件库的"验证层"：证明 Tier 1 组件能协同工作
- Block 不同于 Patterns（自由组合），Block 遵循契约中定义的组合结构

## Figma Inspired 试点范围

第一轮只在 `Figma Inspired` 页面启用 `full-blocks-v3`，并生成 5 个低风险 block：

- Dashboard Shell
- Settings Layout
- Mail Shell
- Feature Grid
- Empty State Pattern

其余 block 暂以 `omittedReason` 记录，保持 warning，不作为本轮 final-blocking。

第二阶段继续只处理 `Figma Inspired`：

- 新增依赖组件：Label、Button Group
- 新增 block：Login Page、Password Reset、Notification Settings、Pricing Table、Error Page、Onboarding Stepper
- `present_blocks` 从 5 扩展到 11，剩余 7 个 block 继续以 `omittedReason` 记录

Blocks v3 阶段性策略：只补当前 block 必需依赖，不批量补全 54 个扩展组件。依赖组件可先作为 Blocks dependency component 存在，不改变 31 个 Tier 1 baseline required count。

## 标准 Page Sections

新增 `Blocks` section，位置在 `Theme-Specific Components` 之后、`Patterns` 之前：

- Overview
- Foundations
- Core Components
- Form & Input Controls
- Navigation & Layout
- Feedback & Overlays
- Theme-Specific Components
- **Blocks** ← 新增
- Patterns
- Examples
- Reference Notes

## Block 契约（18 个）

### Dashboard (2)
| Block | Required Components |
|-------|-------------------|
| Dashboard Shell | Sidebar / Rail, Navigation Bar, Card, Table / Data Row |
| Analytics View | Chart Container, Filter Bar, Data Toolbar, Table / Data Row |

### Authentication (3)
| Block | Required Components |
|-------|-------------------|
| Login Page | Card, Text Field, Button, Label |
| Sign Up Page | Card, Text Field, Button, Label, Checkbox |
| Password Reset | Card, Text Field, Button, Label |

### Settings (2)
| Block | Required Components |
|-------|-------------------|
| Settings Layout | Sidebar / Rail, Tabs, Text Field, Button |
| Notification Settings | Switch, Section Header, Divider |

### Layout Shells (2)
| Block | Required Components |
|-------|-------------------|
| Mail Shell | Sidebar / Rail, Table / Data Row, Panel |
| Chat Interface | Chat Bubble, Message Input, Scroll Area |

### Landing Page (5)
| Block | Required Components |
|-------|-------------------|
| Hero Section | Hero CTA Group, Button, Button Group |
| Feature Grid | Card, Icon Button, Section Header |
| Pricing Table | Segmented Control, Card, Button, Divider |
| Testimonial Carousel | Carousel, Card, Avatar |
| Footer Section | Footer / Dark Section, Link, Icon Button, Divider |

### Utility (4)
| Block | Required Components |
|-------|-------------------|
| Empty State Pattern | Empty State, Button |
| Error Page | Empty State, Button |
| File Upload Zone | Upload Zone, Progress / Loading, File Card |
| Onboarding Stepper | Progress / Loading, Text Field, Button, Button Group |

## 上下文 Block

以下 block 类别为上下文相关，如果产品类型不需要可跳过，在 `Reference Notes` 中记录原因：
- E-commerce（需要 Product Card、Cart Row 等 Tier 2 组件）
- AI/Chat（需要 Chat Bubble、Message Input 等 Tier 2 组件）
- File Management（需要 File Tree、Upload Zone 等 Tier 2 组件）

## 验收要求

- `Blocks` section 存在且在正确位置
- 所有适用 block 已生成（missing blocks 记录为 warning，非 final-blocking）
- 每个 block 的 `requiredComponents` 已作为 master component 实例存在于 block frame 内
- Block frame 的 `instanceCount > 0`
- Block 内部实例的 `mainComponent` 引用完好
- 已截图 Blocks section 用于视觉 QA

## 验证

```powershell
python skills/design-md-to-figma-system/scripts/validate_component_contract.py docs/<style>-standard-inventory.json --profile full-blocks-v3
```

- `missing_blocks`：block 不在 inventory 中 → warning
- `omitted_blocks`：block 存在但有 `omittedReason` → warning
- block `requiredComponentInstances` 精确 standardName 缺失 → finalBlocking
- block instance 缺少 `mainComponentId` / `mainComponentName` → finalBlocking
- block `instanceCount` 为 0 → finalBlocking
- block 不在 `Blocks` section 中 → finalBlocking

## 后续

1. 在已有 Figma 主题中生成 Blocks section
2. 扩展更多 block 类别（E-commerce、AI/Chat、File Management）
3. Block 变体探索（sidebar-left vs sidebar-right、compact vs relaxed）
4. Block 与 Code Connect 的映射关系
