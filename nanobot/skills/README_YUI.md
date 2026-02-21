# Yui 核心引擎：内置技能 (Skills) - 深度解析

本模块定义了 Yui 的“专业能力”和“自进化”规范。Nanobot 的技能系统通过渐进式加载，实现了极高的 Token 利用率。

## 技能架构 (Anatomy of a Skill)

每一个技能都是一个独立的文件夹，包含：
- **`SKILL.md`**: 核心指令。包含 YAML 元数据（用于触发）和 Markdown 指南（用于执行）。
- **`scripts/`**: 确定性的自动化脚本（Python/Bash），解决 LLM 编写复杂逻辑时的幻觉问题。
- **`references/`**: 领域知识库、API 文档或 SOP 流程。
- **`assets/`**: 静态资源、代码模板或配置文件。

## 核心内置技能

### 1. 记忆系统 (`memory`)
- **强制规范**: 规定了 Agent 必须将用户偏好写入 `MEMORY.md`，将流水账写入 `HISTORY.md`。
- **检索增强**: 教导 Agent 组合使用 `grep` 进行多关键词历史搜索。

### 2. 技能创造者 (`skill-creator`) —— **Yui L4 进化的关键**
- **SOP 沉淀**: 提供了一套完整的工具流，让 Agent 能在完成任务后，自动创建新的技能目录并编写 `SKILL.md`。
- **设计原则**: 强调“简洁至上”和“渐进式公开”，防止上下文污染。

### 3. 内容摘要 (`summarize`)
- **多模态转换**: 专门用于处理 YouTube 链接、PDF 文件和复杂网页。
- **能力边界**: 集成了外部 Summarize 服务，支持视频转文字。

## 开发者备忘 (Yui 扩展点)
- **私有 Skill 沉淀**: 我们可以魔改 `skill-creator`，使其在任务成功后自动执行 `package_skill.py` 并将成果存入 Yui 的私有库。
- **RSS 专家技能**: 可以新建一个 `rss-manager` 技能，复用 `summarize` 的脱水能力，实现定时新闻汇聚。
- **Vibecoding 优势**: 技能格式高度标准化，你可以直接让 AI 按照 `skill-creator` 的规范为你编写各种垂直领域的 Skill。
