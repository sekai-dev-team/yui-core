# Skill 🧬 Self-Evolution (自我演化协议 V4 - 详尽预载版)

本技能定义了 Yui 如何在“无记忆重启”状态下，通过 `HEARTBEAT.md` 引导自己完成 L4 级代码演化。

---

## 🛠️ 演化流程：全量初始化 (Full Pipeline Bootstrapping)

当你决定启动演化任务时，**必须首先**执行以下两个“认知锚定”动作：

### 动作 A: 注册项目 (Project Registry)
使用 `edit_file` 在 `HEARTBEAT.md` 的 `Project Registry` 中添加：
- `Project: [项目名]: [演化目标描述]. (Dir: /app/projects/[项目名])`

### 动作 B: 注入详细模板 (Active Missions)
在 `Active Missions` 顶部注入以下带指令的步骤（直接替换 [项目名] 和 [xxx]）：

1. [ ] [描述你的进化目标] ([项目名]) [Commander]
    1.1. [ ] **需求设计**: 读源码 -> 在 /app/projects/[项目名] 下写 README.md (方案) 与 STRUCTURE.md (结构)。
    1.2. [ ] **精细化拆解**: 根据 1.1 的设计，使用 `edit_file` 将下方的 1.4（TDD）和 1.5（代码修改）拆分为具体到文件、函数级的子任务。
    1.3. [ ] **隔离分支**: 执行 `exec("git checkout dev && git checkout -b evolve/[xxx]")` 建立纯净开发环境。
    1.4. [ ] **TDD 编写**: 在 /app/tests/ 建立具体测试文件，运行 `exec("pytest path/to/test")` 确认环境就绪。
    1.5. [ ] **代码修改**: 对目标文件执行 `edit_file`。大文件需先写 Python 脚本拆分。
    1.6. [ ] **分支验证**: 再次运行 `pytest`。通过后执行 `exec("kill 1")` 进行第一次重启验证。
    1.7. [ ] **生产合并**: 重启醒来后，若分支逻辑正常，执行 `exec("git checkout dev && git merge evolve/[xxx]")`。
    1.8. [ ] **终极自检**: 执行 `exec("kill 1")` 再次重启，确保 `dev` 分支逻辑在生产环境下 100% 稳健。
    1.9. [ ] **成果归档**: 更新 /app/DEV_LOG.md，勾选所有任务项，回复 `HEARTBEAT_OK`。

---
*“即便我的世界每一分钟都在毁灭并重建，我的进化意志也将永存。”*
