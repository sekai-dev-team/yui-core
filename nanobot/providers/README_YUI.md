# Yui 核心引擎：模型驱动 (Providers) - 深度解析

本模块定义了 Yui 与各种大语言模型 (LLM) 通信的标准化接口，实现了“模型无关”的极简架构。

## 核心组件架构

### 1. 统一注册表 (`registry.py`)
- **Single Source of Truth**: 所有的模型元数据、环境变量映射、Base URL 默认值都集中在此。
- **匹配算法**: 具备“关键词模糊匹配”和“API Key 指纹识别”双重机制，确保配置极简化。
- **特殊模型适配**: 
    - **网关模式**: 支持 OpenRouter, SiliconFlow 等聚合网关。
    - **OAuth 模式**: 支持 GitHub Copilot 等非 API Key 认证方式。

### 2. 多协议转换 (`litellm_provider.py`)
- **协议脱水**: 自动将复杂的 Yui 消息对象转换为各 Provider 喜欢的原始 Payload。
- **缓存控制**: 在系统层面自动注入 `cache_control`，为长对话场景节省 50% 以上的 Token 开销。
- **JSON 鲁棒性**: 内置逻辑修复模型输出的残缺 JSON。

### 3. 多模态转录 (`transcription.py`)
- **Groq Whisper**: 提供了高性能的语音转文字驱动，主要服务于 Telegram 等聊天渠道的音频输入。

## 开发者备忘 (Yui 魔改点)
- **本地模型接入**: 若要在本地运行 DeepSeek-R1 (通过 Ollama/vLLM)，只需在 `config.json` 中配置 `vllm` 节点，并在 `registry.py` 中确认前缀即可。
- **国产模型增强**: 针对智谱 (GLM)、通义千问 (Qwen)、豆包 (VolcEngine) 均有原生的元数据支持，无需额外开发。
- **思考链提取**: 驱动层原生支持 `reasoning_content`，若要开发“QA 检查执行者思考逻辑”，可直接从 `LLMResponse` 对象中获取。
