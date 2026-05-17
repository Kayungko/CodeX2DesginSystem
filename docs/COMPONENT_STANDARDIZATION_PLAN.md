# Component Standardization Plan

## 背景

前向测试中发现不同主题页面的组件覆盖不一致：

- Spotify Inspired 强调播放器、内容卡片和 Now Playing。
- VoltAgent Inspired 强调代码块、Agent 节点和工程图。
- Figma Inspired 强调编辑器控件和产品界面组件。

这种差异能保留主题特征，但会让多主题设计系统缺少横向一致性。例如 A 主题有 Panel，B 主题没有 Panel，使用者就无法稳定比较、替换或复用组件。

## 决策

从下一轮生成开始，skill 采用「标准组件契约 + 主题特色组件」结构。

每个主题都必须生成完整 Tier 1 标准组件库。若源 `DESIGN.md` 没有直接出现某个组件，也要根据 token、布局语法和相邻组件推导生成，并标记为 `Source=Inferred`。

主题特色组件继续保留，但只能作为补充，不能替代标准组件。

## 标准页面结构

- Overview
- Foundations
- Core Components
- Form & Input Controls
- Navigation & Layout
- Feedback & Overlays
- Theme-Specific Components
- Patterns
- Examples
- Reference Notes

## 标准组件覆盖

标准组件清单维护在：

- `skills/design-md-to-figma-system/references/component-taxonomy.md`
- `skills/design-md-to-figma-system/references/standard-component-contract.json`

核心覆盖包括：

- Actions：Button、Icon Button、Link、Badge / Tag
- Inputs：Text Field、Search Field、Select / Dropdown、Checkbox、Radio、Switch、Slider
- Navigation：Navigation Bar、Sidebar / Rail、Tabs、Segmented Control
- Surfaces：Card、Panel、Divider、Table / Data Row
- Feedback：Tooltip、Toast / Notification、Progress / Loading、Empty State
- Overlays：Modal / Dialog、Command Menu、Menu Item
- Documentation：Section Header、Type Sample、Spacing Scale Item、Radius Scale Item、Elevation Card

## 验收要求

- 所有 Tier 1 required components 必须存在。
- 组件命名中的核心名词必须跨主题稳定，例如始终使用 `Panel`，不能在不同主题里变成 `Container`、`Surface Box` 等不可比名称。
- 每个组件记录来源状态：`Observed`、`Inferred` 或 `Theme-Specific`。
- 非必要情况下不给结构性 Frame 填充颜色；主题氛围优先使用 Figma 页面背景色表达，section / grid / layout wrapper 默认透明。
- Figma 验证必须输出缺失组件清单，缺失标准组件默认阻塞最终交付。
- 主题特色组件放入 `Theme-Specific Components` 或 `Patterns`，不混入标准覆盖统计。

## 迁移影响

已有 `Figma Inspired`、`Spotify Inspired`、`VoltAgent Inspired` 页面是早期前向测试产物，组件覆盖不完全一致。后续可按新契约做一轮补齐迁移，而不是立即删除重建。

## 下一步

1. 用新 contract 生成下一套主题，验证标准覆盖是否稳定。
2. 给已有三个主题补齐缺失标准组件。
3. 将 Figma 验证脚本升级为读取 `standard-component-contract.json` 后自动检查组件覆盖。
