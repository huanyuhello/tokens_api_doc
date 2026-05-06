# Claude Code 安装教程（Win/Mac）

## 前置条件

- 已在 [Tokens 平台](http://47.102.134.41:3000) 获取 API Key（令牌）
- 已安装 [Node.js](https://nodejs.org/) 18 或更高版本

---

## 第一步：安装 Claude Code

适用于 macOS、Linux、WSL、Windows PowerShell、Windows CMD：

```bash
npm install -g @anthropic-ai/claude-code
```

---

## 第二步：配置接入（二选一）

### 方法一：修改 settings.json（推荐）

文件路径：

- **Windows**：`C:\Users\用户名\.claude\settings.json`
- **macOS/Linux**：`~/.claude/settings.json`

写入以下内容（替换 `sk-...` 为你的 API Key）：

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

### 方法二：配置环境变量

=== "Windows（命令行）"

    ```cmd
    setx ANTHROPIC_AUTH_TOKEN "sk-..."
    setx ANTHROPIC_BASE_URL "http://47.102.134.41:3000"
    ```

    > 设置完成后需**重新打开**终端窗口才能生效。

=== "Windows（图形界面）"

    1. 按 `Win + R`，输入 `sysdm.cpl` 回车
    2. 切换到「高级」选项卡，点击「环境变量」
    3. 在「用户变量」中点击「新建」，依次添加：
        - 变量名：`ANTHROPIC_AUTH_TOKEN`，变量值：`sk-...`
        - 变量名：`ANTHROPIC_BASE_URL`，变量值：`http://47.102.134.41:3000`
    4. 点击确定保存，重新打开终端

=== "macOS/Linux"

    在 `~/.bashrc` 或 `~/.zshrc` 中添加：

    ```bash
    export ANTHROPIC_AUTH_TOKEN="sk-..."
    export ANTHROPIC_BASE_URL="http://47.102.134.41:3000"
    ```

    然后执行：

    ```bash
    source ~/.bashrc  # 或 source ~/.zshrc
    ```

---

## 第三步：验证安装

打开新终端，进入任意项目目录后运行：

```bash
cd your-project
claude
```

出现交互界面即表示配置成功。

> **注意**：Claude Code 会自动读取当前目录下的文件，建议先在空文件夹中测试，避免消耗大量 Token。

---

## Claude Code 能做什么

| 功能 | 说明 |
|------|------|
| 构建功能 | 用自然语言描述需求，自动制定计划、编写代码 |
| 调试修复 | 粘贴报错信息，自动分析并修复问题 |
| 代码导航 | 询问任何关于代码库的问题，获得准确答案 |
| 自动化任务 | 修复 lint 问题、解决合并冲突、编写发布说明 |
