# Hermes Agent Linux 安装接入 Tokens 教程

## Hermes Agent 简介

Hermes Agent 是 Nous Research 开发的开源自主 AI 智能体，支持 Linux、macOS 和 WSL2，运行越久能力越强。一条命令即可安装，无需前置依赖。

---

## 第一步：安装 Hermes Agent

```bash
curl -fsSL https://res1.hermesagent.org.cn/install.sh | bash
```

---

## 第二步：配置接入 Tokens

安装完成后，执行引导配置：

1. 在选项中选择 **Custom endpoint**（通常为选项 28）
2. 填写以下信息：

| 字段 | 填写内容 |
|------|----------|
| URL | `http://47.102.134.41:3000` |
| API Key | `sk-...`（你的 Tokens 平台 API Key） |
| 模型 ID | 如 `claude-opus-4-6` |

---

## 第三步：加载环境变量

```bash
cd ~
source ~/.bashrc
```

---

## 第四步：开始使用

配置完成后，Hermes Agent 即可通过 Tokens 平台调用模型，运行时间越长，智能体能力越强。
