# CC Switch 使用教程

## 工具简介

CC Switch 是一个基于 Rust 和 Tauri 构建的轻量级桌面应用（约 6MB），用于一键切换 Claude Code、Codex、Gemini CLI、OpenCode、OpenClaw 等 CLI 工具的 API 配置。

| 特性 | 说明 |
|------|------|
| 支持工具 | Claude Code、Codex、Gemini CLI、OpenCode、OpenClaw 等 |
| 支持系统 | Windows 10+、macOS 12+、Linux（Ubuntu/Debian/Fedora） |
| 核心功能 | 一键切换配置、系统托盘快速操作、云同步、MCP 协议支持 |

项目地址：[https://github.com/farion1231/cc-switch](https://github.com/farion1231/cc-switch)

---

## 第一步：下载安装

前往 [Releases 页面](https://github.com/farion1231/cc-switch/releases) 下载适合你系统的版本并安装。

---

## 第二步：配置 Claude Code 接入 Tokens

打开 CC Switch，点击 Claude 图标，新建配置：

| 字段 | 填写内容 |
|------|----------|
| ANTHROPIC_AUTH_TOKEN | `sk-...`（你的 Tokens 平台 API Key） |
| ANTHROPIC_BASE_URL | `http://47.102.134.41:3000` |
| ANTHROPIC_MODEL | `claude-opus-4-6` |

填写完成后点击**保存**，一键切换即可生效。

---

## 第三步：配置 Gemini CLI 接入 Tokens

点击顶部 Gemini 图标，点击右上角加号，选择**自定义供应商**：

| 字段 | 填写内容 |
|------|----------|
| API Base URL | `http://47.102.134.41:3000/v1` |
| API Key | `sk-...` |
| 模型名称 | 如 `gemini-2.5-pro-all` |

保存后，打开终端输入 `gemini` 即可开始使用。
