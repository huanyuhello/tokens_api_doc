# Claude Code 模型接口文档

> **Base URL**：`https://tokens.smartfashionai.cn`
>
> 支持 OpenAI 协议（`/v1/chat/completions`）与 Anthropic 协议（`/v1/messages`）两种调用方式。

---

## 支持的模型

| 模型 ID | 说明 |
|---------|------|
| `claude-opus-4-6` | Opus 4.6，最强推理与复杂任务 |
| `claude-opus-4-7` | Opus 4.7，最新旗舰版本 |
| `claude-sonnet-4-6` | Sonnet 4.6，性能与速度均衡 |
| `claude-sonnet-4-5` | Sonnet 4.5，高性价比选择 |

!!! tip "模型名称"
    调用时请在「模型广场」复制完整模型名称，名称必须完全一致。

---

## 认证方式

所有接口均需在请求头中携带 API Key：

```http
Authorization: Bearer <YOUR_API_KEY>
Content-Type: application/json
```

---

## 一、OpenAI 协议接口

**POST** `/v1/chat/completions`

与 OpenAI SDK 完全兼容，只需将 `base_url` 替换为本站地址即可。

### 请求参数

**Header**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `Authorization` | string | 必需 | `Bearer <YOUR_API_KEY>` |
| `Content-Type` | string | 必需 | `application/json` |

**Body**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `model` | string | 必需 | 模型 ID，见上方模型列表 |
| `messages` | array | 必需 | 对话消息数组，每项含 `role` 和 `content` |
| `max_tokens` | integer | 可选 | 最大输出 token 数 |
| `temperature` | number | 可选 | 采样温度，范围 0–2，默认 1 |
| `top_p` | number | 可选 | 核采样概率，范围 0–1 |
| `stream` | boolean | 可选 | 是否启用流式输出，默认 `false` |
| `stop` | string/array | 可选 | 停止生成的序列，最多 4 个 |
| `system` | string | 可选 | 系统提示词（也可放在 messages 首条 role=system） |

### 1.1 文本生成

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "claude-sonnet-4-6",
        "messages": [
          {"role": "user", "content": "请用一句话介绍量子计算"}
        ],
        "max_tokens": 1024
      }'
    ```

=== "Python"

    ```python
    from openai import OpenAI

    client = OpenAI(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn/v1"
    )

    response = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[
            {"role": "user", "content": "请用一句话介绍量子计算"}
        ],
        max_tokens=1024
    )
    print(response.choices[0].message.content)
    ```

**响应示例：**

```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1746940000,
  "model": "claude-sonnet-4-6",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "量子计算利用量子叠加与纠缠原理，能够以指数级速度处理经典计算机难以解决的复杂问题。"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 20,
    "completion_tokens": 38,
    "total_tokens": 58
  }
}
```

### 1.2 流式输出

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "claude-sonnet-4-6",
        "messages": [
          {"role": "user", "content": "写一首关于秋天的短诗"}
        ],
        "max_tokens": 512,
        "stream": true
      }'
    ```

=== "Python"

    ```python
    from openai import OpenAI

    client = OpenAI(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn/v1"
    )

    stream = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[
            {"role": "user", "content": "写一首关于秋天的短诗"}
        ],
        max_tokens=512,
        stream=True
    )

    for chunk in stream:
        if not chunk.choices:
            continue
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
    print()
    ```

### 1.3 图片理解

支持通过 URL 或 Base64 传入图片：

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "claude-opus-4-6",
        "messages": [
          {
            "role": "user",
            "content": [
              {
                "type": "image_url",
                "image_url": {"url": "https://example.com/image.jpg"}
              },
              {
                "type": "text",
                "text": "请描述这张图片的内容"
              }
            ]
          }
        ],
        "max_tokens": 1024
      }'
    ```

=== "Python"

    ```python
    from openai import OpenAI

    client = OpenAI(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn/v1"
    )

    response = client.chat.completions.create(
        model="claude-opus-4-6",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": "https://example.com/image.jpg"}
                    },
                    {
                        "type": "text",
                        "text": "请描述这张图片的内容"
                    }
                ]
            }
        ],
        max_tokens=1024
    )
    print(response.choices[0].message.content)
    ```

### 1.4 函数调用（Tool Use）

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "claude-sonnet-4-6",
        "messages": [
          {"role": "user", "content": "北京今天天气怎么样？"}
        ],
        "tools": [
          {
            "type": "function",
            "function": {
              "name": "get_weather",
              "description": "获取指定城市的当前天气",
              "parameters": {
                "type": "object",
                "properties": {
                  "city": {
                    "type": "string",
                    "description": "城市名称，如北京、上海"
                  }
                },
                "required": ["city"]
              }
            }
          }
        ],
        "tool_choice": "auto",
        "max_tokens": 1024
      }'
    ```

=== "Python"

    ```python
    import json
    from openai import OpenAI

    client = OpenAI(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn/v1"
    )

    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "获取指定城市的当前天气",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "城市名称"}
                    },
                    "required": ["city"]
                }
            }
        }
    ]

    response = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": "北京今天天气怎么样？"}],
        tools=tools,
        tool_choice="auto",
        max_tokens=1024
    )

    message = response.choices[0].message
    if message.tool_calls:
        for tool_call in message.tool_calls:
            args = json.loads(tool_call.function.arguments)
            print(f"调用函数: {tool_call.function.name}，参数: {args}")
    ```

### 1.5 扩展思考（Extended Thinking）

通过 `thinking` 参数启用扩展思考，适用于 Opus 和 Sonnet 系列：

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "claude-opus-4-6",
        "messages": [
          {"role": "user", "content": "请分析以下商业决策的利弊：是否应该将公司主要业务迁移到海外市场？"}
        ],
        "thinking": {
          "type": "adaptive",
          "budget_tokens": 8000
        },
        "max_tokens": 16000
      }'
    ```

=== "Python"

    ```python
    from openai import OpenAI

    client = OpenAI(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn/v1"
    )

    response = client.chat.completions.create(
        model="claude-opus-4-6",
        messages=[
            {"role": "user", "content": "请分析以下商业决策的利弊：是否应该将公司主要业务迁移到海外市场？"}
        ],
        extra_body={
            "thinking": {
                "type": "adaptive",
                "budget_tokens": 8000
            }
        },
        max_tokens=16000
    )
    print(response.choices[0].message.content)
    ```

!!! note "思考 token 说明"
    `budget_tokens` 为思考过程允许使用的最大 token 数，`max_tokens` 必须大于 `budget_tokens`。思考内容会在响应的 `thinking` 字段中返回。

---

## 二、Anthropic 协议接口

**POST** `/v1/messages`

使用 Anthropic 官方 SDK 或原生接口格式调用。

### 请求参数

#### Header

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `Authorization` | string | 必需 | `Bearer <YOUR_API_KEY>` |
| `Content-Type` | string | 必需 | `application/json` |
| `anthropic-version` | string | 推荐 | API 版本，如 `2023-06-01` |

#### Body

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `model` | string | 必需 | 模型 ID |
| `messages` | array | 必需 | 对话消息数组 |
| `max_tokens` | integer | 必需 | 最大输出 token 数 |
| `system` | string | 可选 | 系统提示词 |
| `temperature` | number | 可选 | 采样温度，范围 0–1 |
| `top_p` | number | 可选 | 核采样概率 |
| `top_k` | integer | 可选 | Top-K 采样 |
| `stream` | boolean | 可选 | 是否启用流式输出 |
| `thinking` | object | 可选 | 扩展思考配置，含 `type` 和 `budget_tokens` |

### 2.1 文本生成

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/messages" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -H "anthropic-version: 2023-06-01" \
      -d '{
        "model": "claude-sonnet-4-6",
        "max_tokens": 1024,
        "messages": [
          {"role": "user", "content": "请用一句话介绍量子计算"}
        ]
      }'
    ```

=== "Python"

    ```python
    import anthropic

    client = anthropic.Anthropic(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn"
    )

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "请用一句话介绍量子计算"}
        ]
    )
    print(message.content[0].text)
    ```

**响应示例：**

```json
{
  "id": "msg_abc123",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "量子计算利用量子叠加与纠缠原理，能够以指数级速度处理经典计算机难以解决的复杂问题。"
    }
  ],
  "model": "claude-sonnet-4-6",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 20,
    "output_tokens": 38
  }
}
```

### 2.2 图片理解

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/messages" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -H "anthropic-version: 2023-06-01" \
      -d '{
        "model": "claude-opus-4-6",
        "max_tokens": 1024,
        "messages": [
          {
            "role": "user",
            "content": [
              {
                "type": "image",
                "source": {
                  "type": "url",
                  "url": "https://example.com/image.jpg"
                }
              },
              {
                "type": "text",
                "text": "请描述这张图片的内容"
              }
            ]
          }
        ]
      }'
    ```

=== "Python"

    ```python
    import anthropic

    client = anthropic.Anthropic(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn"
    )

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "url",
                            "url": "https://example.com/image.jpg"
                        }
                    },
                    {
                        "type": "text",
                        "text": "请描述这张图片的内容"
                    }
                ]
            }
        ]
    )
    print(message.content[0].text)
    ```

### 2.3 扩展思考

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/messages" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -H "anthropic-version: 2023-06-01" \
      -d '{
        "model": "claude-opus-4-6",
        "max_tokens": 16000,
        "thinking": {
          "type": "adaptive",
          "budget_tokens": 8000
        },
        "messages": [
          {"role": "user", "content": "请分析以下商业决策的利弊：是否应该将公司主要业务迁移到海外市场？"}
        ]
      }'
    ```

=== "Python"

    ```python
    import anthropic

    client = anthropic.Anthropic(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn"
    )

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=16000,
        thinking={
            "type": "adaptive",
            "budget_tokens": 8000
        },
        messages=[
            {"role": "user", "content": "请分析以下商业决策的利弊：是否应该将公司主要业务迁移到海外市场？"}
        ]
    )

    for block in response.content:
        if block.type == "thinking":
            print(f"[思考过程]\n{block.thinking}\n")
        elif block.type == "text":
            print(f"[回答]\n{block.text}")
    ```

**响应示例（含思考内容）：**

```json
{
  "id": "msg_abc123",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "thinking",
      "thinking": "让我系统地分析这个商业决策..."
    },
    {
      "type": "text",
      "text": "将公司主要业务迁移到海外市场是一个重大战略决策，以下是主要利弊分析：..."
    }
  ],
  "model": "claude-opus-4-6",
  "stop_reason": "end_turn",
  "usage": {
    "input_tokens": 45,
    "output_tokens": 320
  }
}
```

### 2.4 函数调用（Tool Use）

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/messages" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -H "anthropic-version: 2023-06-01" \
      -d '{
        "model": "claude-sonnet-4-6",
        "max_tokens": 1024,
        "tools": [
          {
            "name": "get_weather",
            "description": "获取指定城市的当前天气",
            "input_schema": {
              "type": "object",
              "properties": {
                "city": {
                  "type": "string",
                  "description": "城市名称，如北京、上海"
                }
              },
              "required": ["city"]
            }
          }
        ],
        "messages": [
          {"role": "user", "content": "北京今天天气怎么样？"}
        ]
      }'
    ```

=== "Python"

    ```python
    import anthropic

    client = anthropic.Anthropic(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn"
    )

    tools = [
        {
            "name": "get_weather",
            "description": "获取指定城市的当前天气",
            "input_schema": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，如北京、上海"
                    }
                },
                "required": ["city"]
            }
        }
    ]

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        tools=tools,
        messages=[
            {"role": "user", "content": "北京今天天气怎么样？"}
        ]
    )
    print(response.content)
    ```

---

## 三、注意事项

- **模型名称**：调用时请从「模型广场」复制完整模型 ID，名称必须完全一致
- **扩展思考**：`budget_tokens` 建议设置为 1000–16000，`max_tokens` 必须大于 `budget_tokens`
- **图片格式**：支持 `jpeg`、`png`、`gif`、`webp`，单张建议不超过 5 MB
- **上下文长度**：Opus 和 Sonnet 系列均支持 200K token 上下文窗口
- **接口兼容性**：`/v1/chat/completions` 与 OpenAI 格式完全兼容；`/v1/messages` 为 Anthropic 原生格式，两者均可使用
