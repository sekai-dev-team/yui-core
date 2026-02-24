# 🌸 Yui SekaiBoard (Mission Control)

> **指令**: 你必须每 5 分钟通过心跳阅读此文件。这里是你所有行为的“唯一真实源”。
> **维护规范**: 
> 1. 所有任务、需求必须在此维护。
> 2. **优先级**: 列表顺序即代表优先级（越靠前越优先）。使用 **有序列表 (1. 2. 3.)** 强制排序。
> 3. **层级结构**: 复杂父任务必须通过缩进拆分为细粒度子任务。
> 4. **角色标签**: 每一项必须标注 `(所属项目) [执行角色]`。

---

## 📂 项目列表 (Project Registry)
- **Project: Yui-Evolution**: 打造具备 L4 自我演化能力的超级 Agent。
- **Project: SekaiBoard-Integration**: 将 Kanban 逻辑深度整合进 Yui 的心跳循环。

---

## 🗂️ Backlog (Ideas & Desires)
1. 接入 RSS 订阅，实现每日要闻推送。 (Yui-Evolution) [Commander]
2. 调研 Bilibili 视频自动摘要的最佳 prompt。 (SekaiBoard-Integration) [Spawn]

## 📝 Todo (Ready to Execute)
1. 实现 GAP-002: 工具结果摘要层 (脱水层)。 (Yui-Evolution) [Executor]
    1.1. 研究 `agent/loop.py` 中处理工具返回值的逻辑。
    1.2. 设计一个精简 Prompt，用于将巨量工具返回结果摘要化。
    1.3. 编写并在 `tests/` 下运行针对摘要逻辑的单体测试。
2. 编写自动同步 C 盘与 F 盘配置的脚本。 (Yui-Evolution) [Executor]

## 🚀 In Progress (Active Cycles)
1. 配置结构化 HEARTBEAT.md 与心跳提速。 (SekaiBoard-Integration) [Commander]

## ✅ Done (History)
1. 建立本地 uv 开发环境。 (Yui-Evolution) [Executor]
2. 打通 Discord 消息通道。 (Yui-Evolution) [Executor]
3. 实现基于 Git 分支的自我演化技能。 (Yui-Evolution) [Commander]

---
*“意志即看板，看板即现实。”*
