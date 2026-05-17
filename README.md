# CodeX2DesignSystem

用于沉淀“DESIGN.md + Figma MCP”生成 Figma 设计系统的参考资料、产品文档与后续 skill 实现。

## 当前内容

- `skills/design-md-to-figma-system/`：第一版 Codex skill，用于根据 `DESIGN.md` 与 Figma MCP 生成单页设计系统。
- `references/awesome-design-md-cn/`：来自本地 `awesome-design-md-cn` 的设计风格资料库。
- `references/awesome-design-md-cn/design-md/`：多套网站/产品风格的 `DESIGN.md`、`preview.html` 与 `preview-dark.html`。
- `references/awesome-design-md-cn/design-md/figma/`：本轮 Figma inspired 设计系统的主要设计语言来源。
- `references/awesome-design-md-cn/docs/FIGMA_COMPONENT_LIBRARY_PRODUCT_DOC.md`：DemoDesignSystem 产品文档。
- `references/awesome-design-md-cn/docs/FIGMA_COMPONENT_LIBRARY_PROGRESS.md`：DemoDesignSystem 开发与迁移进度。
- `docs/SPOTIFY_INSPIRED_FORWARD_TEST.md`：Spotify DESIGN.md 写入 Figma 的 skill 前向测试记录。
- `docs/VOLTAGENT_INSPIRED_FORWARD_TEST.md`：VoltAgent DESIGN.md 写入 Figma 的 skill 前向测试记录。
- `docs/COMPONENT_STANDARDIZATION_PLAN.md`：多主题设计系统组件覆盖统一方案。
- `docs/MULTI_THEME_STANDARDIZATION_PROGRESS.md`：三套现有主题补齐标准组件后的迁移进度与验证记录。
- `docs/*-standard-inventory.json`：三套主题的 v2 Figma inventory，本地用于 contract 验收。

## Skill 使用方式

当前 skill 尚未安装到本机 Codex skills 目录，默认作为仓库内版本管理资产维护。开发或测试时可显式引用：

```text
Use the skill at skills/design-md-to-figma-system to turn references/awesome-design-md-cn/design-md/figma/DESIGN.md into a single-page Figma design system.
```

辅助脚本：

```powershell
python skills/design-md-to-figma-system/scripts/scan_design_md.py references/awesome-design-md-cn/design-md
python skills/design-md-to-figma-system/scripts/validate_skill_inputs.py --design-md references/awesome-design-md-cn/design-md/figma/DESIGN.md --figma-url https://www.figma.com/design/6OrAjGdiQXjTkvBdJIb0XJ/DesignSystem?m=dev
python skills/design-md-to-figma-system/scripts/validate_component_contract.py docs/figma-inspired-standard-inventory.json
python skills/design-md-to-figma-system/scripts/test_validate_component_contract.py
```

## 后续方向

继续扩展为 Figma inventory 自动导出、多风格批量生成、Code Connect 映射、移动端 variants、现有系统增量更新。
