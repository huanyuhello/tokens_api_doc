# GPT-Codex 安装教程

## 前置条件

- 已在 [Tokens 平台](http://47.102.134.41:3000) 获取 API Key（令牌）
- 已安装 [Node.js](https://nodejs.org/) 18 或更高版本

---

## 第一步：安装 GPT-Codex

适用于 macOS、Linux、WSL、Windows PowerShell、Windows CMD：

```bash
npm i -g @openai/codex
```

---

## 第二步：创建配置文件

在 `.codex` 目录下创建 `config.toml` 文件：

```bash
code ~/.codex/config.toml
```

写入以下配置（根据需要修改模型名称）：

```toml
# 全局默认配置
model_provider = "Tokens"
model = "gpt-5"  # 调用的模型，确保该模型 ID 在 Tokens 控制台中存在

# Tokens 模型供应商配置
[model_providers.Tokens]
name = "Tokens"
base_url = "http://47.102.134.41:3000/v1"
env_key = "TOKENS_API_KEY"
wire_api = "responses"
query_params = {}
request_max_retries = 3
stream_max_retries = 8
```

---

## 第三步：配置 API Key 环境变量

=== "Windows（命令行）"

    ```cmd
    setx TOKENS_API_KEY "sk-..."
    ```

    > 设置完成后需**重新打开**终端窗口才能生效。

=== "Windows（图形界面）"

    1. 按 `Win + R`，输入 `sysdm.cpl` 回车
    2. 切换到「高级」选项卡，点击「环境变量」
    3. 在「用户变量」中点击「新建」：
        - 变量名：`TOKENS_API_KEY`
        - 变量值：`sk-...`（你的 API Key）
    4. 点击确定，重新打开终端

=== "macOS/Linux"

    在 `~/.bashrc` 或 `~/.zshrc` 中添加：

    ```bash
    export TOKENS_API_KEY="sk-..."
    ```

    然后执行：

    ```bash
    source ~/.bashrc
    ```

---

## 第四步：验证安装

打开新终端，输入以下命令测试：

```bash
codex "你好"
```

出现正常响应即配置成功。

---

## 第五步：开始使用

进入项目目录后运行：

```bash
cd your-project
codex
```
