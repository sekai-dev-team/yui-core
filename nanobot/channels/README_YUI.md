# Yui 核心引擎：渠道接入 (Channels) - 深度解析

本模块是 Yui 的“感官”，负责与各大通讯平台进行协议转换与双向通信。

## 核心组件架构

### 1. 渠道管理器 (`manager.py`)
- **动态加载**: 根据配置文件动态初始化 Telegram, Feishu, QQ, Discord 等渠道。
- **中心调度**: 维护 `_dispatch_outbound` 循环，将 Agent 生成的响应精准路由回最初的消息来源。

### 2. 基础协议 (`base.py`)
- **权限哨兵**: `is_allowed()` 检查 `allow_from` 白名单，支持用户 ID 和用户名匹配。
- **标准化总线对接**: 自动将各平台的原始 Payload 封装为统一的 `InboundMessage` 丢入消息总线。

### 3. 典型渠道实现
- **Telegram (`telegram.py`)**:
    - **Markdown 适配**: 将 MD 转换为 Telegram 兼容的 HTML，保护代码块不被转义。
    - **多模态转录**: 接收语音消息后自动调用 Groq 进行文本转录。
    - **输入状态反馈**: 自动模拟“正在输入...”状态，提升交互感。
- **飞书/Lark (`feishu.py`)**:
    - **极致视觉**: 采用 **交互式卡片 (Interactive Cards)** 格式。
    - **表格增强**: 自动将 MD 表格转换为飞书原生的高级表格组件。
    - **长连接**: 采用 WebSocket 模式，无需内网穿透即可从外网访问。
- **QQ (`qq.py`)**:
    - **官方 SDK 接入**: 支持腾讯官方的 `botpy` 协议，主要针对 C2C 私聊场景。

## 开发者备忘 (Yui 扩展点)
- **接入 OneBot**: 参照 `feishu.py` 的 WebSocket 模式，可以轻松编写 `onebot.py` 来接入 QQ 群及其他支持该协议的平台。
- **多模态扩展**: 目前 Telegram 已支持语音转录，可将其逻辑抽象到 `base.py`，让所有支持音频输入的渠道都具备此能力。
- **野蛮生长建议**: 对于不带身份验证的渠道，务必在 `config` 中配置 `allow_from`，以防止 Agent 的 Token 被非法消耗。
