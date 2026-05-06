# Trae 配置使用 Tokens 教程

## Trae 简介

Trae 是一款基于 VS Code 构建的 AI 驱动 IDE，界面与 VS Code 高度一致，兼容 VS Code 插件生态。

官方下载：[https://www.trae.cn/](https://www.trae.cn/)

---

## 配置步骤

### 第一步：安装 Cline 插件

1. 打开 Trae，进入插件市场（`Ctrl+Shift+X`）
2. 搜索 **Cline**
3. 点击安装，等待完成
4. 左侧活动栏出现 Cline 图标即安装成功

### 第二步：配置 API 信息

点击左侧活动栏的 Cline 图标，在设置界面填写：

| 字段 | 填写内容 |
|------|----------|
| API Provider | OpenAI Compatible |
| Base URL | `http://47.102.134.41:3000/v1` |
| API Key | `sk-...`（你的 Tokens 平台令牌密钥） |
| Model ID | 模型名称，如 `gpt-5.2`（从 Tokens 平台模型广场复制） |

填写完成后保存。

> **注意**：模型名称必须与 Tokens 平台模型广场中的名称完全一致。

### 第三步：开始使用

配置完成后，在 Trae 中点击 Cline 图标即可开始 AI 辅助编程。
