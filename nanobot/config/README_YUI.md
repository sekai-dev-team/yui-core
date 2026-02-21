# Yui 核心引擎：配置与驱动 (Config & Providers) - 深度解析

本模块定义了 Yui 的基础代谢系统，负责配置的动态加载及与全球大模型 API 的无缝对接。

## 核心组件架构

### 1. 声明式配置 (`nanobot/config/`)
- **Pydantic 驱动 (`schema.py`)**: 所有配置项（从 API Key 到渠道参数）都经过严格的类型校验。
- **动态加载 (`loader.py`)**: 支持配置文件、环境变量双重注入。具备配置版本迁移能力，确保平滑升级。
- **环境隔离**: 默认工作区位于 `~/.nanobot/`，但也支持工作区局部化，方便实现“野蛮生长”下的多实例并行。

### 2. 万能驱动层 (`nanobot/providers/`)
- **LiteLLM 集成 (`litellm_provider.py`)**: 
    - **全协议支持**: 覆盖了 OpenAI, Anthropic, Google, DeepSeek, 以及 SiliconFlow, OpenRouter 等聚合平台。
    - **参数脱水**: 自动针对不同 Provider 的癖好清洗消息格式（如剔除多余的元数据）。
    - **容错机制**: 内置 `json_repair`，极大提升了模型调用工具时的成功率。
- **Prompt 缓存**: 自动处理 `cache_control`，显著降低长对话场景下的 Token 成本。
- **推理过程支持**: 能够捕获并存储模型生成的推理链（Reasoning Content），方便后续审计和分析。

## 开发者备忘 (Yui 扩展点)
- **接入新模型**: 绝大多数情况下，只需在 `config.json` 中配置 API Key 即可。特殊模型可通过修改 `registry.py` 的关键词映射来支持。
- **自定义驱动**: 若 LiteLLM 不支持某特殊模型，可继承 `base.py` 编写自定义 Provider。
- **多模型负载均衡**: 可以在配置层面实现主备模型切换（如：DeepSeek 宕机时自动切到 Gemini）。
