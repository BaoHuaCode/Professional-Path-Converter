# 🚀 Professional Path Converter | 路径转换器专业版

[English Version Below | 中文版见下文]

---

#English Description
A specialized automation tool for cross-platform developers. It monitors the clipboard in real-time and automatically converts file paths between **Windows (backslashes `\`)** and **Mac/Linux (slashes `/`)** formats.

# Key Features
* **Real-time Monitoring**: Uses a low-power polling mechanism to listen for clipboard changes instantly.
* **Smart Bidirectional Conversion**: 
    * Automatically converts `\` to `/` for Mac terminals or Python code.
    * Automatically converts `/` to `\` for Windows-specific software requirements.
* **Anti-Duplication**: Built-in state recorder prevents redundant processing of the same path.
* **Graceful Exit**: Integrated `KeyboardInterrupt` handling for a clean `Ctrl+C` shutdown without error logs.

# Tech Stack
* **Python 3.x**
* **Libraries**: `pyperclip`, `time`

---

# 中文说明
这是一款专为跨平台开发者设计的自动化路径转换工具。它能实时监控剪贴板，自动识别并将 Windows 风格路径（反斜杠 `\`）与 Mac/Linux 风格路径（斜杠 `/`）进行双向智能互转。

# 功能特性
* **实时监控**：利用低功耗轮询机制，后台实时监听剪贴板变化，响应迅速。
* **智能双向转换**：
    * 自动将 `\` 转换为 `/`（适用于 Mac 终端或 Python 代码粘贴）。
    * 自动将 `/` 转换为 `\`（满足 Windows 特定软件路径格式需求）。
* **防重复处理**：内置状态记录器，确保同一路径内容不会被循环重复转换。
* **优雅退出**：集成 `KeyboardInterrupt` 异常处理，支持 `Ctrl+C` 丝滑退出，不抛出报错信息。

#技术栈
* **Python 3.x**
* **核心库**: `pyperclip` (剪贴板操作), `time` (频率控制)

---

# My Learning | 学习收获
By developing this project, I deepened my understanding of **Daemon Processes** (background monitoring) and **Exception Handling** in Python. It's a bridge from writing "scripts" to creating "utility tools."
通过这个项目，我深入理解了 Python 中的**守护进程（后台监控）**逻辑和**异常处理**。这是我从编写“简单脚本”向开发“实用小工具”迈出的重要一步。
