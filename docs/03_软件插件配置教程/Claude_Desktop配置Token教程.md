# Claude Desktop 配置 Tokens 教程

!!! warning "重要前提"
    - 必须使用**最新版** Claude Desktop
    - 建议**未登录**状态下配置（已登录请先退出）
    - 需要支持 Anthropic-compatible 的 API（即支持 `/v1/messages` 请求）
    - Gateway base URL 需为 **HTTPS 地址**

> 本教程以 Windows 环境为例。

---

## 第一步：启用开发者模式

1. 打开 Claude Desktop，**不要登录**官方账号
2. 在顶部菜单栏选择 **Help（帮助）** → **Troubleshooting（疑难解答）**
3. 点击 **Enable Developer Mode（启用开发者模式）**

启用成功后，顶部菜单栏会新增 **Developer（开发者）** 菜单。

---

## 第二步：进入第三方 API 配置页面

1. 点击顶部 **Developer** 菜单
2. 选择 **Configure Third-Party Inference…（配置第三方推理）**

---

## 第三步：填写配置信息

在配置窗口中按如下填写：

| 字段 | 填写内容 |
|------|----------|
| Use this configuration | **开启**（必须） |
| Gateway | `Anthropic-compatible` |
| Gateway base URL | `http://47.102.134.41:3000` |
| Gateway API key | 你的 Tokens 平台 API Key（`sk-...`） |
| Gateway auth scheme | 保持默认 |
| Gateway extra headers | 留空 |

填写完成后，点击右下角 **Apply locally（本地应用）**，然后重启软件。

---

## 第四步：选择模型并验证

重启后，在界面中选择模型，输入一个简单问题测试。模型能正常响应即配置成功。
