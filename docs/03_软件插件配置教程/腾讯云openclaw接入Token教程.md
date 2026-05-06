# 腾讯云 OpenClaw 接入 Tokens 配置 QQ 机器人教程

---

## 第一步：配置模型

在 OpenClaw 中配置 Tokens 平台的模型：

| 字段 | 填写内容 |
|------|----------|
| API Base URL | `http://47.102.134.41:3000` |
| API Key | `sk-...`（你的 Tokens 平台 API Key） |
| 模型名称 | 如 `claude-opus-4-6` |

配置完成后，绿灯亮起表示连接正常。

---

## 第二步：配置 QQ 机器人通道

### 2.1 创建 QQ 机器人

前往以下地址创建机器人：

[https://q.qq.com/qqbot/openclaw/index.html](https://q.qq.com/qqbot/openclaw/index.html)

### 2.2 在 OpenClaw 中添加机器人

回到腾讯云 OpenClaw，填写机器人的 **ID** 和 **Key**。

---

## 第三步：测试 QQ 机器人

配置完成后，向机器人发送消息测试是否正常响应。

参考文档：[https://clawd.org.cn/channels/qqbot](https://clawd.org.cn/channels/qqbot)
