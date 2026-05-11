# GPT Codex 配置教程

> 适用平台：Windows / macOS / Linux

---

## 前置条件

- 已注册并获取 API 密钥：[https://tokens.smartfashionai.cn/](https://tokens.smartfashionai.cn/)
- 已安装 [Node.js](https://nodejs.org/)（建议 v18+）

---

## 第一步：安装 GPT Codex

在终端中执行以下命令全局安装：

```bash
npm i -g @openai/codex
```

---

## 第二步：创建配置文件

在项目目录下创建 `.codex/config.toml` 文件：

```bash
code .codex/config.toml
```

将以下内容粘贴到文件中，并根据需求修改模型名称：

```toml
# 全局默认配置
model_provider = "Tokens"
model = "gpt-5"  # 调用的模型，请确保该模型 ID 在控制台中存在

# Tokens 模型供应商配置
[model_providers.Tokens]
name = "Tokens"
base_url = "https://tokens.smartfashionai.cn/v1"
env_key = "4SAPI_API_KEY"   # 请勿在此处填写密钥，保持不变
wire_api = "responses"
query_params = {}
request_max_retries = 3
stream_max_retries = 8
```

> `env_key` 字段指定了读取 API Key 的环境变量名称，密钥通过环境变量传入，不要直接写在配置文件中。

---

## 第三步：配置 API Key 环境变量（二选一）

### 方法一：命令行（CMD / PowerShell）

使用 `setx` 永久写入环境变量（需重新打开终端生效）：

```bash
setx 4SAPI_API_KEY "sk-..."
```

![命令行设置环境变量](../resource/616773.png)

> 设置完成后，关闭当前终端，重新打开新窗口才会生效。

---

### 方法二：图形界面（GUI，推荐）

1. 按 `Win + R`，输入 `sysdm.cpl` 回车

    ```
    sysdm.cpl
    ```

    ![打开系统属性](../resource/615268.png)

2. 切换到「高级」选项卡，点击「环境变量...」

    ![进入环境变量设置](../resource/617957.png)

3. 在「用户变量」区域点击「新建」，填入：

    | 变量名 | 变量值 |
    |--------|--------|
    | `4SAPI_API_KEY` | `sk-...`（你的密钥） |

    ![新建用户变量](../resource/617955.png)

    ![填写变量值](../resource/617981.png)

4. 点击「确定」保存，关闭所有终端窗口后重新打开生效。

---

## 第四步：启动 GPT Codex

打开新终端，进入项目目录后运行：

```bash
cd your-project
codex
```

首次运行可用以下命令测试是否配置成功：

```bash
codex "你好"
```

![启动 GPT Codex 成功](../resource/616777.png)
