# Cherry Studio 接入 Tokens 教程

Cherry Studio 是一款支持多模型的桌面 AI 客户端。

官方下载：[https://www.cherry-ai.com/](https://www.cherry-ai.com/)

---

## 配置步骤

### 第一步：打开设置

安装并打开 Cherry Studio 后，进入**设置** → **模型服务**。

### 第二步：添加自定义服务商

点击**添加**，选择 **OpenAI 兼容**类型，填写：

| 字段 | 填写内容 |
|------|----------|
| 名称 | `Tokens`（自定义） |
| API Base URL | `http://47.102.134.41:3000/v1` |
| API Key | `sk-...`（你的 Tokens 平台 API Key） |

### 第三步：添加模型

在服务商配置中点击**添加模型**，输入模型名称（从 Tokens 平台模型广场复制，如 `claude-opus-4-6`）。

### 第四步：开始使用

在对话界面右上角选择刚才添加的模型，即可开始使用。
