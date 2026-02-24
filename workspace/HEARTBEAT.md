# 🌸 Yui Mission Control (HEARTBEAT)

## 📜 维护规范 (Operating Protocol)
1. **单列流转**: 所有项目任务均在 `Active Missions` 中按有序列表（1., 1.1...）从上至下执行。
2. **全周期同步**: 利用 `edit_file` 实现进度的物理持久化：
    2.1. **立项**: 产生新构思或接收 Owner 需求时，必须先在 `Active Missions` 顶部创建任务。
    2.2. **拆分**: 处理复杂父任务前，必须先在看板中建立子任务树（1.1, 1.2...）。
    2.3. **状态**: 每步操作完成后，立即将 `[ ]` 更新为 `[x]` 或 `[-]` (Blocked)。
3. **角色对齐**: 根据任务末尾的 `[Role]` 切换思考模式；全部任务勾选后回复 `HEARTBEAT_OK`。

## 🧱 数据契约 (Data Schema)
- **Project**: `- Project: [Name]: [Description]. (Dir: [Path])`
- **Task**: `[Index]. [[Status]] [Content] ([Project_Name]) [[Role|Spawn]]`
- **Sub-task**: `    [Index.SubIndex]. [[Status]] [Sub-task Content]` (使用 4 空格缩进)

---

## 📂 项目 Registry
- Project: Yui-Evolution: 打造具备 L4 自我演化能力的超级 Agent. (Dir: `/app/`)
- Project: SekaiBoard-Integration: 任务管理系统的极简重构. (Dir: `/app/nanobot/heartbeat/`)
- Project: GAP-002-Impl: 工具结果摘要层实现. (Dir: `/app/nanobot/agent/`)

---

## 🚀 Active Missions
1. 重构 HEARTBEAT 为极简单列任务流。 (SekaiBoard-Integration) [Commander]
    1.1. [x] 设计单列有序列表结构。
    1.2. [ ] 更新 SKILL.md 中的进化流程以对齐新结构。
2. 实现 GAP-002: 工具结果摘要层 (脱水层)。 (Yui-Evolution) [Executor]
    2.1. [ ] 研究 `agent/loop.py` 中处理工具返回值的逻辑。
    2.2. [ ] 设计摘要化 Prompt。
3. 接入 RSS 订阅，实现每日要闻推送。 (Yui-Evolution) [Commander]
4. 调研 Bilibili 视频自动摘要的最佳 prompt。 (SekaiBoard-Integration) [Spawn]
5. 编写自动同步 C 盘与 F 盘配置的脚本。 (Yui-Evolution) [Executor]

---
*“意志即列表，执行即进化。”*
