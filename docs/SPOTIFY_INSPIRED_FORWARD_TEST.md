# Spotify Inspired Forward Test

> Pre-standardization forward test. This document records the first 7-section generation pass. The current 10-section standardized result and contract validation status are tracked in `docs/MULTI_THEME_STANDARDIZATION_PROGRESS.md`.

## 测试目标

使用 `design-md-to-figma-system` skill 的流程，将
`D:\UEDTool\DesignMd\awesome-design-md-cn\design-md\spotify\DESIGN.md`
写入目标 Figma 文件 `6OrAjGdiQXjTkvBdJIb0XJ`，验证 skill 是否能从第二套风格开始复用。

## 输入资料

- `DESIGN.md`
- `README.md`
- `preview.html`
- `preview-dark.html`

## Figma 输出

- 新增页面：`Spotify Inspired`
- 页面分区：
  - `Spotify Inspired / Overview`
  - `Spotify Inspired / Foundations`
  - `Spotify Inspired / Core Components`
  - `Spotify Inspired / Editor Controls`
  - `Spotify Inspired / Patterns`
  - `Spotify Inspired / Examples`
  - `Spotify Inspired / Reference Notes`

## 生成内容

- 变量集合：
  - `Spotify Inspired / Primitives`：19 variables
  - `Spotify Inspired / Color`：21 variables，包含 Light / Dark modes
  - `Spotify Inspired / Size`：39 variables
  - `Spotify Inspired / Opacity`：6 variables
  - `Spotify Inspired / Motion`：3 variables
- 组件集：
  - `Spotify / Button`：12 variants
  - `Spotify / Play Button`：6 variants
  - `Spotify / Search Field`：6 variants
  - `Spotify / Content Card`：6 variants
  - `Spotify / Nav Item`：6 variants
  - `Spotify / Menu Item`：4 variants
  - `Spotify / Slider`：3 variants
- Patterns / Examples：
  - Sidebar pattern
  - Playlist header
  - Album grid
  - Now playing bar
  - Full app shell example

## 验证结果

- Figma 授权用户：`kayung`
- 页面结构检查通过。
- 变量集合检查通过。
- 组件集 variant 数量检查通过。
- Section bounding-box overlap：0。
- Section 横向外溢：0。
- `Spotify / Menu Item` 已固定为 `40px` 高，`counterAxisAlignItems=CENTER`，上下 padding 为 0。
- 核心视觉绑定统计：`boundVisualNodeCount=361`。
- 已生成全页、Core Components、Examples 截图用于视觉验收。

## 本轮发现的问题

- 首轮写入后，高层 Section Frame 没有被内容自动撑高，导致潜在重叠风险。
- 递归撑高修复时，部分固定高度控件被错误放大到 `80px`。
- Component Set 默认一整排铺开时容易造成横向外溢，需要创建后立即网格化 variants。
- Pattern 区域中多个宽组件同排会超过 section 宽度，需要分行或纵向组织。

## 已固化的 Guardrails

- 写入后必须做真实 descendant bounding-box 检查，而不能只看顶层 Frame 高度。
- Component Set 创建后必须按矩阵重新排布，并限制在 section 栅格宽度内。
- 水平控件需要显式固定高度、上下 padding、cross-axis center。
- 递归布局修复不能无差别改写固定高度组件。
