# Yui 核心引擎：工具系统 (Tools) - 深度解析

本模块定义了 Yui 与物理世界、网络及外部协议交互的“手”。

## 工具集概览

### 1. 文件系统 (`filesystem.py`)
- **`read_file` / `write_file`**: 基础读写。
- **`edit_file`**: **差异化编辑**。它要求 LLM 提供 `old_text` 和 `new_text`。如果 `old_text` 不唯一或未找到，它会计算编辑距离并给出最佳匹配建议，这比全量覆盖更安全。
- **`list_dir`**: 带有 Emoji 标识（📁/📄）的目录列表。

### 2. 命令执行 (`shell.py`)
- **`exec`**: 强大的 Shell 接口。
- **安全拦截器**: 硬编码了危险指令黑名单（如 `rm -rf`, `mkfs`, `dd` 等）。
- **超时保护**: 默认 60 秒限制，防止任务挂起。

### 3. 网络能力 (`web.py`)
- **`web_search`**: 基于 Brave Search API。
- **`web_fetch`**: **网页脱水机**。内置 HTML 语义提取（Readability 算法），自动剔除脚本和样式，产出高纯度 Markdown。支持 JSON 自动格式化。

### 4. 外部协议 (`mcp.py`)
- **MCP 适配器**: 实现了 Model Context Protocol 客户端。
- **动态注册**: 可以实时连接远程或本地 MCP Server，将其工具无感地注入到 Yui 的可用工具列表中。

### 5. 协作能力 (`spawn.py`)
- **`spawn`**: 派生背景子代理。它并不直接执行，而是调用 `SubagentManager` 启动异步任务。

## 开发者备忘 (Yui 扩展点)
- **野蛮生长与安全**: `shell.py` 的 `deny_patterns` 是我们可以根据需要精简或增强的地方。
- **新工具开发**: 继承 `base.py` 的 `Tool` 基类，只需定义 `parameters` (JSON Schema) 和 `execute` (异步) 即可快速扩展。
- **MCP Server 集成**: 这是 Yui “吸收全网能力”的核心。我们可以通过配置文件快速接入谷歌或 Anthropic 的 MCP 资源。
