# Cursor 接入 Tokens 教程

## 前置条件

- 已在 [Tokens 平台](http://47.102.134.41:3000) 获取 API Key（令牌）
- 已安装 [Node.js](https://nodejs.org/) 18 或更高版本
- 已安装 [Cursor](https://www.cursor.com/)

---

## 第一步：安装 Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

---

## 第二步：配置 Claude Code 接入 Tokens

修改 settings.json 文件：

- **Windows**：`C:\Users\用户名\.claude\settings.json`
- **macOS/Linux**：`~/.claude/settings.json`

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-...",
    "ANTHROPIC_BASE_URL": "http://47.102.134.41:3000",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "claude-opus-4-6",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "claude-opus-4-6",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "claude-opus-4-6",
    "ANTHROPIC_MODEL": "claude-opus-4-6",
    "ANTHROPIC_REASONING_MODEL": "claude-opus-4-6"
  },
  "includeCoAuthoredBy": false
}
```

---

## 第三步：验证 Claude Code

打开新终端，输入 `claude` 回车，能正常对话即配置成功。

> **注意**：建议在空文件夹中测试，避免 Claude Code 自动读取大量文件消耗 Token。

---

## 第四步：在 Cursor 中安装 Claude Code 插件

1. 打开 Cursor，进入扩展市场（`Ctrl+Shift+X`）
2. 搜索 **Claude Code**
3. 点击安装，等待完成
4. 重启 Cursor，左侧活动栏出现 Claude Code 图标即安装成功

---

## 第五步：在 Cursor 中使用

安装插件后，Claude Code 会自动读取上面配置的环境变量，直接在 Cursor 中点击 Claude Code 图标即可开始使用。
