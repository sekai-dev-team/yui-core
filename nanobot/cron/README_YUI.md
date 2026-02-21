# Yui 核心引擎：自动化 (Cron & Heartbeat) - 深度解析

本模块为 Yui 提供了主动触发和定时任务的能力，使其不再仅仅是一个“被动响应”的聊天机器人。

## 核心组件架构

### 1. 定时任务 (`nanobot/cron/`)
- **多维度调度**:
    - `at`: 指定毫秒时间戳执行（一次性）。
    - `every`: 固定时间间隔执行。
    - `cron`: 支持标准 Cron 表达式（如 `0 9 * * *` 表示每天早 9 点）。
- **主动推送**: 通过设置 `payload.deliver=True`，任务结果可以直接穿透消息总线发往 Telegram、飞书等渠道。
- **持久化存储**: 所有任务配置保存在 `cron.json` 中，支持服务重启后的任务恢复。

### 2. 心跳自省 (`nanobot/heartbeat/`)
- **工作流**: 
    1. 定时扫描 `HEARTBEAT.md`。
    2. 若发现非空指令，向 Agent 发送 `HEARTBEAT_PROMPT`。
    3. Agent 介入处理，完成后通过回复 `HEARTBEAT_OK` 结束本次心跳。
- **设计理念**: “以文件为中心”。用户或外部程序只需向 `HEARTBEAT.md` 写入 Markdown 任务，Agent 就会在下一个心跳周期自动执行。

## 开发者备忘 (Yui 扩展点)
- **RSS 自动化**: 可以编写一个 Cron 任务定时抓取 RSS，并将更新内容写入 `HEARTBEAT.md` 触发 Yui 阅读总结。
- **深夜记忆沉淀**: 配置一个凌晨 3 点的任务，强制触发 `MemoryStore.consolidate()`，实现 L4 级的自我演化。
- **主动健康监控**: 利用心跳机制让 Yui 定期检查本地服务状态，并在出现异常时主动报警。
