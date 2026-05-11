# Chat GPT 模型接口文档

> **Base URL**：`https://tokens.smartfashionai.cn`
>
> 使用标准 OpenAI 兼容格式（`/v1/chat/completions`）调用，现有 OpenAI SDK 无需修改代码，只需替换 `base_url` 和 `api_key`。

---

## 支持的模型

| 模型 ID | 说明 |
|---------|------|
| `gpt-5.4` | GPT-5.4，强推理与复杂任务处理 |
| `gpt-5.5` | GPT-5.5，最新旗舰版本，综合能力最强 |

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

## 接口概览

| 方法 | 路径 | 说明 |
|------|------|------|
| `POST` | `/v1/chat/completions` | 文本生成（主接口） |
| `POST` | `/v1/responses` | Responses 通用接口 |

---

## 一、文本生成

**POST** `/v1/chat/completions`

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
| `n` | integer | 可选 | 每次请求生成的候选数量，默认 1 |
| `stream` | boolean | 可选 | 是否启用流式输出，默认 `false` |
| `stop` | string/array | 可选 | 停止生成的序列，最多 4 个 |
| `presence_penalty` | number | 可选 | 话题多样性惩罚，范围 -2.0–2.0 |
| `frequency_penalty` | number | 可选 | 重复惩罚，范围 -2.0–2.0 |
| `user` | string | 可选 | 终端用户唯一标识符 |

### 1.1 基础文本生成

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "gpt-5.4",
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
        model="gpt-5.4",
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
  "model": "gpt-5.4",
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

### 1.2 带系统提示词

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "gpt-5.5",
        "messages": [
          {"role": "system", "content": "你是一位专业的代码审查工程师，请用简洁专业的语言回答问题。"},
          {"role": "user", "content": "如何避免 SQL 注入攻击？"}
        ],
        "max_tokens": 2048,
        "temperature": 0.7
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
        model="gpt-5.5",
        messages=[
            {"role": "system", "content": "你是一位专业的代码审查工程师，请用简洁专业的语言回答问题。"},
            {"role": "user", "content": "如何避免 SQL 注入攻击？"}
        ],
        max_tokens=2048,
        temperature=0.7
    )
    print(response.choices[0].message.content)
    ```

### 1.3 流式输出

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "gpt-5.4",
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
        model="gpt-5.4",
        messages=[
            {"role": "user", "content": "写一首关于秋天的短诗"}
        ],
        max_tokens=512,
        stream=True
    )

    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
    print()
    ```

流式响应格式（SSE）：

```
data: {"id":"chatcmpl-abc123","object":"chat.completion.chunk","choices":[{"delta":{"content":"秋"},"index":0}]}

data: {"id":"chatcmpl-abc123","object":"chat.completion.chunk","choices":[{"delta":{"content":"风"},"index":0}]}

data: [DONE]
```

### 1.4 多轮对话

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "gpt-5.4",
        "messages": [
          {"role": "user", "content": "Python 中列表和元组有什么区别？"},
          {"role": "assistant", "content": "列表是可变的，元组是不可变的。列表用方括号 [] 定义，元组用圆括号 () 定义。"},
          {"role": "user", "content": "那什么时候应该用元组？"}
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
        model="gpt-5.4",
        messages=[
            {"role": "user", "content": "Python 中列表和元组有什么区别？"},
            {"role": "assistant", "content": "列表是可变的，元组是不可变的。列表用方括号 [] 定义，元组用圆括号 () 定义。"},
            {"role": "user", "content": "那什么时候应该用元组？"}
        ],
        max_tokens=1024
    )
    print(response.choices[0].message.content)
    ```

---

## 二、图片理解

支持通过 URL 或 Base64 传入图片，适用于 `gpt-5.4` 和 `gpt-5.5`。

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "gpt-5.5",
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
        model="gpt-5.5",
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

**Base64 传图：**

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "gpt-5.5",
        "messages": [
          {
            "role": "user",
            "content": [
              {
                "type": "image_url",
                "image_url": {
                  "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgAB..."
                }
              },
              {
                "type": "text",
                "text": "图中有哪些文字？"
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
        model="gpt-5.5",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgAB..."
                        }
                    },
                    {
                        "type": "text",
                        "text": "图中有哪些文字？"
                    }
                ]
            }
        ],
        max_tokens=1024
    )
    print(response.choices[0].message.content)
    ```

---

## 三、函数调用（Tool Use）

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "gpt-5.4",
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
                  },
                  "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "温度单位"
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
                        "city": {"type": "string", "description": "城市名称"},
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                    },
                    "required": ["city"]
                }
            }
        }
    ]

    response = client.chat.completions.create(
        model="gpt-5.4",
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
            # 此处执行实际函数逻辑，然后将结果回传给模型
    ```

**响应示例（模型决定调用函数）：**

```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": null,
        "tool_calls": [
          {
            "id": "call_abc123",
            "type": "function",
            "function": {
              "name": "get_weather",
              "arguments": "{\"city\": \"北京\"}"
            }
          }
        ]
      },
      "finish_reason": "tool_calls"
    }
  ]
}
```

---

## 四、联网搜索（Web Search）

通过 `web_search` 工具让模型实时搜索网络信息：

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "gpt-5.5",
        "messages": [
          {"role": "user", "content": "2025年最新的AI大模型有哪些？"}
        ],
        "tools": [{"type": "web_search"}],
        "max_tokens": 2048
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
        model="gpt-5.5",
        messages=[
            {"role": "user", "content": "2025年最新的AI大模型有哪些？"}
        ],
        tools=[{"type": "web_search"}],
        max_tokens=2048
    )
    print(response.choices[0].message.content)
    ```

---

## 五、多轮对话（含函数结果回传）

=== "cURL"

    ```bash
    # 第一轮：发送请求，模型决定调用函数
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "gpt-5.4",
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
                  "city": {"type": "string"}
                },
                "required": ["city"]
              }
            }
          }
        ],
        "tool_choice": "auto",
        "max_tokens": 1024
      }'

    # 第二轮：将函数结果回传给模型
    curl -X POST "https://tokens.smartfashionai.cn/v1/chat/completions" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "gpt-5.4",
        "messages": [
          {"role": "user", "content": "北京今天天气怎么样？"},
          {"role": "assistant", "content": null, "tool_calls": [{"id": "call_abc123", "type": "function", "function": {"name": "get_weather", "arguments": "{\"city\": \"北京\"}"}}]},
          {"role": "tool", "tool_call_id": "call_abc123", "content": "北京今天晴，气温 22°C，微风"}
        ],
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

    def get_weather(city: str) -> str:
        # 模拟天气查询
        return f"{city}今天晴，气温 22°C，微风"

    messages = [{"role": "user", "content": "北京今天天气怎么样？"}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "获取指定城市的当前天气",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"}
                    },
                    "required": ["city"]
                }
            }
        }
    ]

    # 第一轮：模型决定调用函数
    response = client.chat.completions.create(
        model="gpt-5.4",
        messages=messages,
        tools=tools,
        tool_choice="auto",
        max_tokens=1024
    )

    assistant_message = response.choices[0].message
    messages.append(assistant_message)

    # 执行函数并回传结果
    if assistant_message.tool_calls:
        for tool_call in assistant_message.tool_calls:
            args = json.loads(tool_call.function.arguments)
            result = get_weather(**args)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result
            })

    # 第二轮：模型根据函数结果生成最终回答
    final_response = client.chat.completions.create(
        model="gpt-5.4",
        messages=messages,
        max_tokens=1024
    )
    print(final_response.choices[0].message.content)
    ```

---

## 六、注意事项

- **模型名称**：调用时请从「模型广场」复制完整模型 ID，名称必须完全一致
- **图片格式**：支持 `jpeg`、`png`、`gif`、`webp`，URL 需可公网访问；Base64 格式为 `data:image/<格式>;base64,<数据>`
- **流式输出**：设置 `stream: true` 后，响应以 SSE 格式返回，以 `data: [DONE]` 结束
- **函数调用**：`tool_choice` 可设为 `"auto"`（模型自行决定）、`"none"`（禁用）或指定函数名强制调用
- **temperature 与 top_p**：建议只调整其中一个，不要同时修改两者
