# Yui 核心引擎：Agent 模块 (大脑) - 深度解析

本模块定义了 Yui 的核心思维逻辑、上下文构建、记忆管理及多智能体协作机制。

## 核心组件深度解析

### 1. `loop.py` (中央处理器)
- **PTA 循环控制**: 严格管理 `max_iterations`（默认 20 次），防止 LLM 进入无限死循环。
- **思考块处理**: 自动识别并过滤 `<think>` 标签（支持 DeepSeek-R1 等模型），通过 `_strip_think` 保持最终输出纯净。
- **指令系统**: 内置 `/new`（触发异步记忆整理并重置会话）和 `/help`。
- **系统消息处理**: 能够解析来自 `subagent` 通道的系统级反馈，将其无缝集成到当前会话中。

### 2. `subagent.py` (背景执行器)
- **工具隔离**: 子代理仅拥有文件操作、Shell 执行和 Web 访问权限，**禁用了消息工具和递归派生工具**，防止系统失控。
- **异步通知**: 子代理完成后，通过 `system` 通道发送经过格式化的任务报告给主 Agent。

### 3. `memory.py` (记忆生命周期)
- **触发机制**: 当会话长度超过 `memory_window` 时，自动触发异步 `consolidate`。
- **Save Memory Tool**: 使用一个专门的 JSON Schema 工具让 LLM 执行整理工作，产出 `history_entry` (历史日志) 和 `memory_update` (事实更新)。
- **持久化**: 事实存入 `MEMORY.md`，原始路径/细节存入 `HISTORY.md`。

### 4. `skills.py` (能力加载器)
- **前置检查**: 自动检查 `SKILL.md` 中定义的 `bins` (如是否安装了 tmux) 和 `env` (是否配置了 API Key)。
- **加载策略**: 
    - **Always-loaded**: 核心技能始终在 System Prompt 中展示全量内容。
    - **Progressive-loading**: 普通技能仅展示描述，由 Agent 自主决定是否通过 `read_file` 加载详细文档。

### 5. `context.py` (环境组装)
- **Bootstrap 机制**: 实时聚合工作区中的 `SOUL.md`, `USER.md`, `TOOLS.md` 等身份定义文件。
- **多模态支持**: 自动处理本地媒体文件的 Base64 编码，支持视觉交互。

## 开发者备忘 (Yui 魔改点)
- **野蛮生长控制**: 若要提升执行力，可适当放宽 `loop.py` 的迭代限制。
- **L3 协作优化**: 可以通过修改 `_build_subagent_prompt` 来强化子代理的汇报模版，使其更符合“执行者”或“QA”的身份。
- **内存优化**: 可以在 `MemoryStore` 中引入更强的 RAG 检索策略，替代简单的全量读取。
