# OpenClaw 在云服务器 Linux 环境下通过终端配置 API

---

## 前置条件

- 已安装 OpenClaw
- 已在 [Tokens 平台](http://47.102.134.41:3000) 获取 API Key

---

## 配置步骤

### 第一步：执行初始化引导

在终端输入：

```bash
openclaw onboard --install-daemon
```

### 第二步：按提示完成配置

1. 选择 **Quick Start**
2. **Model/auth provider** 选择 **Custom provider**
3. **API Base URL** 填写：`http://47.102.134.41:3000`
4. 粘贴你的 API Key
5. 后续步骤全部选择**跳过（Skip）**

### 第三步：调整上下文窗口（可选）

如果聊天时提示上下文窗口过小：

1. 打开 Web UI 后，点击**配置选项** → **Models**
2. 在下方选择 **RWA**
3. 将 `contextWindow` 和 `maxTokens` 调大（如 `200000` 和 `8192`）

### 第四步：验证

配置完成后，OpenClaw 即可正常运行。
