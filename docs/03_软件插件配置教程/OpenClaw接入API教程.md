# OpenClaw 接入 Tokens 教程

## 前置条件

- 已在 [Tokens 平台](http://47.102.134.41:3000) 获取 API Key（令牌）
- 已安装 [Node.js](https://nodejs.org/) 24 或更高版本

---

## 第一步：安装 OpenClaw

=== "npm 安装（推荐）"

    ```bash
    npm install -g openclaw
    ```

=== "一键脚本安装"

    ```bash
    curl -fsSL https://openclaw.ai/install.sh | bash
    ```

---

## 第二步：执行初始化引导

```bash
openclaw onboard --install-daemon
```

按提示操作：

1. 选择 **Quick Start**
2. 模型提供商选择 **Custom Provider**
3. 填写 API Base URL：`http://47.102.134.41:3000`（或 `http://47.102.134.41:3000/v1`）
4. 粘贴你的 API Key
5. 选择兼容端点：
    - **Claude 模型**：选择 `anthropic-messages`
    - **GPT / Gemini 模型**：选择 `openai-completions`
6. 填写模型名称（从 Tokens 平台模型广场复制）
7. 后续步骤选择 **Skip**
8. 最后重启网关

---

## 第三步：访问 Web UI

初始化完成后，在浏览器访问：

```
http://127.0.0.1:18789/?token=...
```

> Token 值在 `C:\Users\用户名\.clawdbot\clawdbot.json` 文件中查找。

---

## 第四步：手动配置模型（可选）

如需手动添加模型，在 Web UI 中进入「模型供应商」页面：

**Claude 模型配置示例：**

```json
{
  "models": {
    "providers": {
      "custom-1": {
        "baseUrl": "http://47.102.134.41:3000",
        "apiKey": "sk-...",
        "api": "anthropic-messages",
        "models": [
          {
            "id": "claude-sonnet-4-6",
            "name": "claude-sonnet-4-6",
            "api": "anthropic-messages",
            "reasoning": true,
            "input": ["text", "image"],
            "contextWindow": 200000,
            "maxTokens": 8192
          }
        ]
      }
    }
  }
}
```

**GPT / Gemini 模型配置示例：**

```json
{
  "models": {
    "providers": {
      "custom-2": {
        "baseUrl": "http://47.102.134.41:3000",
        "apiKey": "sk-...",
        "api": "openai-completions",
        "models": [
          {
            "id": "gpt-5.2",
            "name": "gpt-5.2",
            "api": "openai-completions",
            "contextWindow": 200000,
            "maxTokens": 8192
          }
        ]
      }
    }
  }
}
```

---

## 第五步：设置默认模型

在 Web UI 的 Agents 配置中，设置 Primary Model，格式为 `供应商名/模型ID`：

```
custom-1/claude-sonnet-4-6
custom-2/gpt-5.2
```

---

## 常见问题

**网关无法启动？** 手动执行：

```bash
openclaw gateway run
openclaw dashboard
```

**上下文窗口过小警告？** 在 `.openclaw/openclaw.json` 中修改 `contextWindow` 和 `maxTokens` 参数。

**忘记 Web UI Token？** 查看 `C:\Users\用户名\.clawdbot\clawdbot.json` 文件中的 token 字段。
