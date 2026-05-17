# DemoDesignSystem Figma 组件库产品文档

## 项目背景

本组件库用于在 Figma 文件 `DemoDesignSystem` 中沉淀一套基于 `design-md/figma/DESIGN.md` 的可复用设计语言。它不是 Figma 官方设计系统复刻，而是依据公开页面提炼出的 Figma inspired 风格组件库，用于快速搭建页面、原型和 AI 生成 UI 的视觉基准。

## 设计目标

- 建立可复用的基础变量、文字样式、效果样式和组件。
- 保持 Figma inspired 的黑白界面层、彩色内容层、药丸按钮、圆形图标按钮和虚线焦点语言。
- 让组件库适合后续扩展，不把所有内容写死在单一画板中。
- 在多风格 `DesignSystem` 文件中采用“一个页面 = 一个风格”的结构，用页内分区清楚呈现 foundations、components、patterns 和 usage examples。

## 设计语言来源

主要来源：

- `design-md/figma/DESIGN.md`
- `design-md/figma/preview.html`
- `design-md/figma/preview-dark.html`

核心原则：

- 界面 chrome 只使用黑白与透明玻璃层。
- 彩色只用于 hero gradient、产品展示和内容占位。
- 交互控件使用 `50px` 药丸或 `50%` 圆形几何。
- 焦点态使用 `2px dashed` 虚线轮廓。
- 字体层级通过细微字重变化和紧凑字距建立。

## v2 增强范围

### Foundations

- `Figma Inspired / Primitives`：21 个基础色与渐变 stop。
- `Figma Inspired / Color`：34 个语义色变量，包含 Light / Dark 两个模式。
- `Figma Inspired / Size`：44 个尺寸变量，覆盖 spacing、radius、stroke、icon、control height、container width。
- `Figma Inspired / Opacity`：8 个透明度变量，覆盖 glass、overlay、muted text、disabled。
- `Figma Inspired / Motion`：4 个动效时长变量，用于后续 prototype / handoff 说明。
- Typography styles：15 个 `Figma Inspired` 文字样式，覆盖 display、section、body、mono、control 和 mobile fallback。
- Effect styles：5 个 `Figma Inspired` 效果样式，覆盖 elevated、dark、hover lift、product window 和 focus reference。
- `Figma Inspired / Foundations` 分区展示 Color、Typography、Spacing、Radius、Elevation 五类 token。

### Page Structure

当前 Figma 文件中，Figma inspired 风格已迁移为单页结构：

- `Figma Inspired / Overview`：风格封面、Getting Started 和使用入口。
- `Figma Inspired / Foundations`：完整 token 展示。
- `Figma Inspired / Core Components`：v2 核心组件、v1 兼容组件和基础 utility 组件。
- `Figma Inspired / Editor Controls`：UI2-inspired 编辑器级控件。
- `Figma Inspired / Patterns`：primitive patterns、产品区块、overlay 与 panels。
- `Figma Inspired / Examples`：完整页面组合示例。
- `Figma Inspired / Reference Notes`：迁移记录和维护约定。

### Components

- `v2 / Button`：36 variants，属性为 `Size` / `Variant` / `State`。
- `v2 / Icon Button`：24 variants，属性为 `Size` / `Variant` / `State`。
- `v2 / Product Tab`：16 variants，属性为 `Item` / `State`。
- `v2 / Card`：6 variants，属性为 `Variant`。
- `v2 / Text Field`：8 variants，属性为 `Kind` / `Value` / `State`。
- `v2 / Search Field`：8 variants，属性为 `Kind` / `Value` / `State`。
- 保留 v1 组件集作为兼容参考：`Button`、`Icon Button`、`Product Tab`、`Card`、`Text Field`、`Search Field`、`Badge / Mono Label`。
- 核心 v2 组件的 fill、stroke、radius、尺寸、间距等主要视觉属性已尽量绑定 Figma 变量。

### UI2 参考补充

参考 `UI2 - Figma's Design System - Community Copy` 后，确认它最值得吸收的是编辑器级产品界面的密集控件、菜单、浮层和面板模式。当前库不直接复制 UI2 视觉资产，而是将这些模式重画为符合本库变量体系的 Figma inspired 组件。

新增组件集：

- `v2 / Checkbox`：9 variants，属性为 `Value` / `State`。
- `v2 / Radio`：6 variants，属性为 `Value` / `State`。
- `v2 / Switch`：9 variants，属性为 `Value` / `State`。
- `v2 / Disclosure`：6 variants，属性为 `Opened` / `State`。
- `v2 / Segmented Control Item`：8 variants，属性为 `Selected` / `State`。
- `v2 / Menu Item`：8 variants，属性为 `Leading Icon` / `State`。

新增 UI2-inspired patterns：

- `Tooltip / Editor Hint`
- `Toast / Notification`
- `Command Menu / Quick Actions`
- `Editor Side Panel / Dense Controls`

### Patterns

`Figma Inspired / Patterns` 分区用于沉淀更接近产品搭建场景的组合模式：

- `Link`
- `Divider`
- `Gradient Preview`
- `Type Sample`
- `Weight Spectrum Row`
- `Spacing Scale Item`
- `Radius Scale Item`
- `Elevation Card`
- `Product Window / Screenshot Frame`
- `Product Showcase Card`
- `Product Showcase Section`
- `Hero CTA Group`
- `Responsive Navigation Bar`
- `Footer / Dark Section`
- `Tooltip / Editor Hint`
- `Toast / Notification`
- `Command Menu / Quick Actions`
- `Editor Side Panel / Dense Controls`

### Examples

`Figma Inspired / Examples` 分区提供一套完整页面组合示例，用于验证 hero、navigation、product showcase、window frame、dark footer 在同一页面中的节奏、对比度和间距关系。

## 非目标

- 不导入 Material、SDS 等第三方库作为基础实现。
- 不声明这是官方 Figma Design System。
- 不做复杂交互动效或 Code Connect 映射。
- 不引入彩色 chrome 或多套品牌主题。

## 交付标准

- Figma 文件中保留 `Figma Inspired` 单页作为该风格的完整来源。
- 页内分区之间保持清晰间距，分区内组件无重叠。
- 组件命名稳定，便于后续 Code Connect 或设计系统发布。
- 组件以模块化方式创建，避免互相硬耦合。
- 文档和进度记录同步更新。

## 验收记录

- Figma 结构验证 warnings 为空。
- v2 核心组件集 variant 数量符合计划。
- 变量集合包含 Light / Dark 模式和新增 opacity / motion 集合。
- 核心 v2 组件主要视觉属性绑定变量，结构验证中未发现 hardcoded fill / stroke 告警。
- UI2-inspired 新增控件与模式结构验证 warnings 为空，新增组件集主要 fill / stroke 绑定变量，hardcoded fill / stroke 统计为 0。
- 单页迁移后仅保留 `Figma Inspired` 页面，旧拆分页已移除；关键组件 ID、变量数量、实例引用和页内重叠检查均通过。
