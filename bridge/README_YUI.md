# Yui 核心引擎：桥接层 (Bridge) - 深度解析

本模块是一个独立的 Node.js 项目，专门用于处理复杂的第三方通讯协议（如 WhatsApp）。它通过 WebSocket 将这些能力“借”给 Python 核心。

## 核心架构

### 1. 技术栈
- **运行时**: Node.js (>= 20.0.0)。
- **核心库**: `@whiskeysockets/baileys` (WhatsApp 协议实现)。
- **通信**: `ws` (WebSocket Server)。

### 2. 桥接机制 (`server.ts`)
- **双向通信**: 
    - **Inbound**: 接收 WhatsApp 消息 -> 封装为 JSON -> 通过 WebSocket 广播给 Python 客户端。
    - **Outbound**: Python 客户端发送指令 -> `BridgeServer` 调度 WhatsApp 发送消息。
- **安全加固**: 
    - 强制绑定 `127.0.0.1`。
    - 握手协议：连接后必须在 5 秒内发送正确的 `BRIDGE_TOKEN` 进行身份验证。

### 3. WhatsApp 适配 (`whatsapp.ts`)
- **登录流**: 首次启动时会在终端打印二维码（QR Code），扫描后凭证持久化在 `authDir`。
- **消息脱水**: 将复杂的富媒体消息（图片、视频、语音）转换为简化的文本描述（如 `[Image] caption`），降低 Python 端处理复杂度。

## 开发者备忘 (Yui 扩展点)
- **增加新桥接**: 若后续需要接入如 iMessage 或其他 Node.js 独占的协议，可参照此模式在 `bridge/` 下新增模块。
- **部署说明**: 运行 `npm run dev` 即可启动桥接服务。Python 端的 `whatsapp` 渠道会自动尝试连接此服务的 WebSocket 端口（默认 3001）。
- **多实例**: 虽然目前只针对 WhatsApp，但其架构完全可以扩展为通用的“非 Python 驱动渠道”网关。
