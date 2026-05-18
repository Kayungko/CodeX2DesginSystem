# Next Handoff Plan

## 当前状态

仓库当前主线已经完成三件事：

- `design-md-to-figma-system` skill 已创建并通过 `quick_validate.py`。
- `Figma Inspired`、`Spotify Inspired`、`VoltAgent Inspired` 三个页面已完成 31 个 Tier 1 标准组件基线补齐。
- `Figma Inspired` 已进入 `full-blocks-v3` 试点：11 个 present blocks，7 个 omitted blocks。
- `Figma Inspired` 已补齐第一批 16 个扩展组件，component set 数量为 62。
- 已分析 UI2 社区文件并在三个风格页 `Patterns` 中实现 UI2-inspired workbench kit。

上一轮已推送提交：

- `9011190 补齐 Figma 扩展组件基线`

本地未提交项：

- `.claude/`
- `.mcp.json`

这些是本地 MCP / Claude 连接配置，不纳入正式提交，除非后续明确要版本化多 agent 本地权限配置。

## 关键入口

- Figma 文件：`6OrAjGdiQXjTkvBdJIb0XJ`
- 当前活跃页面：`Figma Inspired`
- 当前活跃 profile：`full-blocks-v3`
- 进度文档：`docs/MULTI_THEME_STANDARDIZATION_PROGRESS.md`
- Blocks 计划：`docs/BLOCK_STANDARDIZATION_PLAN.md`
- 组件标准化计划：`docs/COMPONENT_STANDARDIZATION_PLAN.md`
- 当前 inventory：`docs/figma-inspired-standard-inventory.json`
- UI2 工作台分析：`docs/UI2_EDITOR_WORKBENCH_ANALYSIS.md`
- 机器可读 contract：`skills/design-md-to-figma-system/references/standard-component-contract.json`

## 已完成：扩展组件补齐与 UI2 工作台沉淀

`Figma Inspired` 第一批扩展组件已完成：

- Inputs：`Calendar / Date Picker`、`Combobox`、`Input Group`、`Input OTP`
- Navigation / Surfaces：`Avatar`、`Breadcrumb`、`Pagination`、`Carousel`
- Feedback / Overlays：`Alert`、`Skeleton`、`Spinner`、`Drawer / Sheet`、`Popover`
- Contextual：`Hero CTA Group`、`Footer / Dark Section`、`Upload Zone`

UI2 工作台已按多主题方式完成：

- Figma Inspired：`Workbench Toolbar` (`228:444`)、`Workbench Sidebar` (`228:445`)、`Workbench Layer Row` (`228:446`)、`Workbench Control Row` (`228:447`)、`Workbench Shell` (`228:448`)、P4 reference `233:122`
- Spotify Inspired：`228:821`、`228:822`、`228:823`、`228:824`、`228:825`、P4 reference `233:142`
- VoltAgent Inspired：`228:1198`、`228:1199`、`228:1200`、`228:1201`、`228:1202`、P4 reference `233:162`

注意：第一版简化 editor example 已被替换为 `Page 4` 中 `Editor template` 的精确克隆，保留 1680 x 880、40px 顶栏、240px 左右侧栏、右侧 inspector panel stack 和中部 paint mixer。

## 下一轮成功标准

- 继续补 UI2 工作台深水区组件，而不是先解锁 Blocks。
- 新增工作台组件均为 component set，不能只画普通 frame。
- 每个新增组件至少有最小可用 variants，并写入 `standardName`、`sourceStatus=Inferred`。
- 新增组件放入 `Patterns` 或对应标准 section，不放入 `Theme-Specific Components`。
- 结构性 section / grid / layout wrapper 默认透明；非必要不填充颜色。
- 组件内部横向控件保持垂直居中，避免贴边。
- 不重建已有 master component，不破坏现有 block instance 的 `mainComponent`。
- 更新对应 inventory，记录新增 component sets 与截图 node ids。
- 更新 `MULTI_THEME_STANDARDIZATION_PROGRESS.md`，记录新增组件数量和验证结果。

## 验证命令

```powershell
python skills/design-md-to-figma-system/scripts/test_validate_component_contract.py
python skills/design-md-to-figma-system/scripts/validate_component_contract.py docs/figma-inspired-standard-inventory.json --profile full-blocks-v3
python skills/design-md-to-figma-system/scripts/validate_component_contract.py docs/spotify-inspired-standard-inventory.json
python skills/design-md-to-figma-system/scripts/validate_component_contract.py docs/voltagent-inspired-standard-inventory.json
python C:\Users\MiaoMiao\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills/design-md-to-figma-system
```

验收要求：

- 所有命令 `ok=true` 或 `Skill is valid!`
- `finalBlocking=[]`
- `schemaWarnings=[]`
- `validation.sourceLabelWarnings=[]`
- `validation.instanceDetachWarnings=[]`
- section overlap 为 0

## 后续 Blocks 解锁顺序

UI2 工作台细化后，再按依赖成熟度解锁剩余 blocks：

1. `Sign Up Page`：依赖 `Input OTP`、`Input Group`、`Alert`
2. `Hero Section`：依赖 `Hero CTA Group`
3. `Footer Section`：依赖 `Footer / Dark Section`、`Kbd`
4. `Testimonial Carousel`：依赖 `Carousel`、`Avatar`
5. `Analytics View`：依赖 `Chart Container`、`Filter Bar`、`Data Toolbar`
6. `Chat Interface`：依赖 `Chat Bubble`、`Message Input`、`Scroll Area`
7. `File Upload Zone`：依赖 `Upload Zone`、`File Card`

## 下一轮建议：UI2 工作台深水区组件

优先继续补下面这些跨主题工作台组件：

- Inspector：`Property Row`、`Color Swatch Row`、`Slider Row`、`Token Picker Row`
- Menus / Overlay：`Context Menu`、`Command Palette`、`Notification`、`Tooltip`、`Non-modal Dialog`
- Sidebar：`Page List Item`、`Layer Tree Row`、`Asset Grid Item`
- Desktop shell：`File Tab`、`Tab Strip`、`Window Chrome`

完成后再考虑建立 `workbench-v1` contract profile，让工作台能力成为多主题强制覆盖的一层。

## 提交规则

- 使用 PowerShell，不使用 `rg`。
- 计划和进度必须及时写入 `docs/`。
- 提交信息使用中文。
- 完成后推送到 `origin/main`。
