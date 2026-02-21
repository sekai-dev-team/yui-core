# Yui 核心引擎：命令行接口 (CLI) - 深度解析

本模块是用户操控 Yui 的总控制台，负责初始化、单机调试及网关服务的拉起。

## 核心指令集

### 1. 引导与诊断 (`onboard` & `status`)
- **`onboard`**: 自动化部署。创建 `~/.nanobot/config.json` 和工作区 MD 模板。
- **`status`**: 一键诊断。显示模型配置状态、API Key 是否缺失以及工作区路径是否正确。

### 2. 交互引擎 (`agent`)
- **本地调试**: 在没有接入 Telegram/飞书前，可以直接在终端与 Yui 对话。
- **Rich 渲染**: 自动将 Agent 返回的 Markdown 在终端进行语法高亮展示。
- **历史回溯**: 支持上下箭头翻找之前的对话指令。

### 3. 网关中枢 (`gateway`) —— **Yui 生产运行的核心**
- **多任务聚合**: 这是一个长驻进程，它在一个 `asyncio.run` 中并行驱动：
    - `AgentLoop`: 思考循环。
    - `ChannelManager`: 渠道收发。
    - `CronService`: 定时任务调度。
    - `HeartbeatService`: 周期性自省。

### 4. 外部登录 (`login`)
- **扫码接入**: 用于处理 WhatsApp 等需要交互式登录的渠道。
- **OAuth 认证**: 实现了 GitHub Copilot 等模型的设备流认证。

## 开发者备忘 (Yui 魔改点)
- **增加新指令**: 可以通过 `app.command()` 增加如 `yui setup-rss` 这样的快捷配置命令。
- **启动逻辑魔改**: 若要实现“多 Agent 协作”，我们可能需要修改 `gateway` 命令，让其启动多个带不同 Identity 的 `AgentLoop`。
- **UI 自定义**: 终端的提示符 (`You:`) 和 Logo (`__logo__`) 均可在此模块进行个性化修改。
