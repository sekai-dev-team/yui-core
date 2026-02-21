# Yui 核心引擎：总线与会话 (Bus & Session) - 深度解析

本模块负责消息在各个组件间的路由、分发以及会话状态的持久化。

## 核心架构

### 1. 消息总线 (`nanobot/bus/`)
- **解耦核心**: `MessageBus` 是 Yui 内部的“信息高速公路”。它将各种通信渠道（如 Telegram, Web, OneBot）与核心 Agent 引擎彻底解耦。
- **异步驱动**: 基于 `asyncio.Queue` 实现非阻塞的消息收发。
- **消息定义 (`events.py`)**:
    - **`InboundMessage`**: 输入消息，携带 `channel`, `chat_id`, `media`, `metadata`。
    - **`OutboundMessage`**: 输出响应，支持 `reply_to` 引用回复。

### 2. 会话管理 (`nanobot/session/`)
- **持久化格式**: 采用 `.jsonl` 文件存储在 `workspace/sessions/` 目录下。
- **存储结构**:
    - 第一行：`_type: "metadata"`，存储会话创建时间、更新时间、整理进度 (`last_consolidated`)。
    - 后续行：每一行一个 JSON 消息，完整记录角色、内容、时间戳及工具调用详情。
- **缓存机制**: `SessionManager` 维护了一层内存缓存，减少频繁的 IO 操作。
- **数据迁移**: 自动将旧版的全局配置 (`~/.nanobot/sessions`) 迁移至当前工作区。

## 开发者备忘 (Yui 扩展点)
- **多平台同步**: 由于采用了 `channel:chat_id` 的 Key 机制，我们可以轻易实现跨平台的统一用户画像关联。
- **高性能历史检索**: 随着 `.jsonl` 文件增大，可以通过 `Session.get_history` 的 `max_messages` 参数灵活控制喂给 LLM 的上下文长度。
- **监控与审计**: 通过监听 `MessageBus` 的出入队列，可以非常简单地实现第三方监控面板或安全审计日志。
