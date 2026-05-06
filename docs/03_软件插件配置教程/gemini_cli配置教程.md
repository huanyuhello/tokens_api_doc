# Gemini CLI 配置教程

## 前置条件

- 已在 [Tokens 平台](http://47.102.134.41:3000) 获取 API Key（令牌）
- 已安装 [Node.js](https://nodejs.org/) 18 或更高版本

---

## 第一步：安装 Gemini CLI

```bash
npm install -g @google/gemini-cli
```

macOS 如遇权限问题：

```bash
sudo npm install -g @google/gemini-cli
```

---

## 第二步：通过 CC Switch 配置接入（推荐）

CC Switch 可以方便地管理 Gemini CLI 的 API 配置。

1. 下载安装 [CC Switch](https://github.com/farion1231/cc-switch/releases)
2. 打开 CC Switch，点击顶部 **Gemini** 图标
3. 点击右上角加号，选择**自定义供应商**
4. 填写以下信息：

| 字段 | 填写内容 |
|------|----------|
| API Base URL | `http://47.102.134.41:3000/v1` |
| API Key | `sk-...`（你的 Tokens 平台 API Key） |
| 模型名称 | 如 `gemini-2.5-pro-all` |

5. 保存配置

---

## 第三步：开始使用

打开终端，输入：

```bash
gemini
```

出现交互界面即配置成功。
