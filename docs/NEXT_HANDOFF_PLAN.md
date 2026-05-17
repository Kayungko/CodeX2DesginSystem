# Next Handoff Plan

## 当前状态

仓库当前主线已经完成三件事：

- `design-md-to-figma-system` skill 已创建并通过 `quick_validate.py`。
- `Figma Inspired`、`Spotify Inspired`、`VoltAgent Inspired` 三个页面已完成 31 个 Tier 1 标准组件基线补齐。
- `Figma Inspired` 已进入 `full-blocks-v3` 试点：11 个 present blocks，7 个 omitted blocks。

最新已推送提交：

- `7f2cbc1 扩展 Figma Blocks 二阶段组件`

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
- 机器可读 contract：`skills/design-md-to-figma-system/references/standard-component-contract.json`

## 下一轮建议：扩展组件补齐

下一轮优先补组件，不继续直接堆 Blocks。原因是剩余 7 个 omitted blocks 依赖更广，如果继续临时拼 block，会削弱组件库的系统性。

建议先在 `Figma Inspired` 补齐这些扩展组件：

- Actions / Documentation：`Kbd`
- Inputs：`Calendar / Date Picker`、`Combobox`、`Input Group`、`Input OTP`
- Navigation：`Breadcrumb`、`Pagination`
- Surfaces：`Accordion`、`Avatar`、`Carousel`、`Collapsible`、`Scroll Area`
- Feedback：`Alert`、`Skeleton`、`Spinner`
- Overlays：`Alert Dialog`、`Context Menu`、`Drawer / Sheet`、`Dropdown Menu`、`Hover Card`、`Popover`
- Contextual：`Chart Container`、`Filter Bar`、`Data Toolbar`、`Chart`、`Chat Bubble`、`Message Input`、`Hero CTA Group`、`Footer / Dark Section`、`Upload Zone`、`File Card`

第一批建议范围控制在 12-16 个组件：

- `Avatar`
- `Alert`
- `Skeleton`
- `Spinner`
- `Calendar / Date Picker`
- `Combobox`
- `Input Group`
- `Input OTP`
- `Breadcrumb`
- `Pagination`
- `Drawer / Sheet`
- `Popover`
- `Carousel`
- `Hero CTA Group`
- `Footer / Dark Section`
- `Upload Zone`

## 下一轮成功标准

- `Figma Inspired` 新增扩展组件均为 component set，不能只画普通 frame。
- 每个新增组件至少有最小可用 variants，并写入 `standardName`、`sourceStatus=Inferred`。
- 新增组件放入正确标准 section，不放入 `Theme-Specific Components`。
- 结构性 section / grid / layout wrapper 默认透明；非必要不填充颜色。
- 组件内部横向控件保持垂直居中，避免 `Menu Item` 曾出现的贴边问题。
- 不重建已有 master component，不破坏现有 block instance 的 `mainComponent`。
- 更新 `figma-inspired-standard-inventory.json`，记录新增 component sets 与截图 node ids。
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

扩展组件补齐后，再按依赖成熟度解锁剩余 blocks：

1. `Sign Up Page`：依赖 `Input OTP`、`Input Group`、`Alert`
2. `Hero Section`：依赖 `Hero CTA Group`
3. `Footer Section`：依赖 `Footer / Dark Section`、`Kbd`
4. `Testimonial Carousel`：依赖 `Carousel`、`Avatar`
5. `Analytics View`：依赖 `Chart Container`、`Filter Bar`、`Data Toolbar`
6. `Chat Interface`：依赖 `Chat Bubble`、`Message Input`、`Scroll Area`
7. `File Upload Zone`：依赖 `Upload Zone`、`File Card`

## 提交规则

- 使用 PowerShell，不使用 `rg`。
- 计划和进度必须及时写入 `docs/`。
- 提交信息使用中文。
- 完成后推送到 `origin/main`。
