# Gemini 模型接口文档

> **Base URL**：`https://tokens.smartfashionai.cn`
>
> Gemini 模型需使用 **`google-genai` SDK** 或原生 Gemini REST API 调用，不支持通过 OpenAI 兼容格式（`/v1/chat/completions`）调用。

---

## 支持的模型

| 模型 ID | 说明 |
|---------|------|
| `gemini-3.1-pro-preview` | Gemini 3.1 Pro 预览版，适合复杂推理和工具调用任务 |
| `gemini-3.1-flash-image-preview` | Gemini 3.1 Flash 图像预览版，支持图片/视频理解与图片生成 |

!!! tip "模型名称"
    调用时请在「模型广场」复制完整模型名称，名称必须完全一致。

---

## 认证方式

所有接口均需在请求头中携带 API Key：

```http
Authorization: Bearer <YOUR_API_KEY>
Content-Type: application/json
```

或通过 SDK 初始化时传入：

```python
client = genai.Client(
    api_key="YOUR_API_KEY",
    http_options={"base_url": "https://tokens.smartfashionai.cn"},
)
```

---

## 安装依赖

```bash
pip install google-genai
```

---

## 一、文本生成

**POST** `/v1beta/models/{model}:generateContent`

### 请求参数

**Header**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `Authorization` | string | 必需 | `Bearer <YOUR_API_KEY>` |
| `Content-Type` | string | 必需 | `application/json` |

**Body**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `contents` | array | 必需 | 对话消息数组，每项含 `role` 和 `parts` |
| `system_instruction` | object | 可选 | 系统提示词，含 `parts` 数组 |
| `generationConfig` | object | 可选 | 生成配置，含 `maxOutputTokens`、`thinkingConfig` 等 |
| `tools` | array | 可选 | 工具定义数组，用于函数调用 |

### 1.1 基础文本生成

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1beta/models/gemini-3.1-pro-preview:generateContent" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "contents": [
          {"role": "user", "parts": [{"text": "用一句话介绍你自己"}]}
        ]
      }'
    ```

=== "Python"

    ```python
    import google.genai as genai

    client = genai.Client(
        api_key="YOUR_API_KEY",
        http_options={"base_url": "https://tokens.smartfashionai.cn"},
    )

    response = client.models.generate_content(
        model="gemini-3.1-pro-preview",
        contents="用一句话介绍你自己",
    )

    print(response.text)
    ```

**响应示例：**

```json
{
  "candidates": [
    {
      "content": {
        "parts": [{"text": "我是 Gemini，由 Google 训练的大型语言模型。"}],
        "role": "model"
      },
      "finishReason": "STOP"
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 8,
    "candidatesTokenCount": 18,
    "totalTokenCount": 26
  }
}
```

### 1.2 系统提示词

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1beta/models/gemini-3.1-pro-preview:generateContent" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "system_instruction": {
          "parts": [{"text": "你是一个专业的 Python 助手，请用简洁的语言回答。"}]
        },
        "contents": [
          {"role": "user", "parts": [{"text": "如何在 Python 中读取文件？"}]}
        ],
        "generationConfig": {
          "maxOutputTokens": 512
        }
      }'
    ```

=== "Python"

    ```python
    import google.genai as genai
    from google.genai import types

    client = genai.Client(
        api_key="YOUR_API_KEY",
        http_options={"base_url": "https://tokens.smartfashionai.cn"},
    )

    response = client.models.generate_content(
        model="gemini-3.1-pro-preview",
        contents="如何在 Python 中读取文件？",
        config=types.GenerateContentConfig(
            system_instruction="你是一个专业的 Python 助手，请用简洁的语言回答。",
            max_output_tokens=512,
        ),
    )

    print(response.text)
    ```

!!! note "系统提示词说明"
    使用系统提示词时，建议将 `max_output_tokens` 设置为 512 或更大，避免思考模式消耗全部 token 导致响应为空。

### 1.3 流式输出

**POST** `/v1beta/models/{model}:streamGenerateContent`

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1beta/models/gemini-3.1-flash-image-preview:streamGenerateContent?alt=sse" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "contents": [
          {"role": "user", "parts": [{"text": "请用三句话介绍月亮"}]}
        ]
      }'
    ```

=== "Python"

    ```python
    import google.genai as genai

    client = genai.Client(
        api_key="YOUR_API_KEY",
        http_options={"base_url": "https://tokens.smartfashionai.cn"},
    )

    for chunk in client.models.generate_content_stream(
        model="gemini-3.1-flash-image-preview",
        contents="请用三句话介绍月亮",
    ):
        if chunk.text:
            print(chunk.text, end="", flush=True)
    ```

### 1.4 思考模式

Gemini 支持思考模式，通过 `thinkingConfig` 设置思考预算（token 数量）。

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1beta/models/gemini-3.1-pro-preview:generateContent" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "contents": [
          {"role": "user", "parts": [{"text": "请解释为什么天空是蓝色的"}]}
        ],
        "generationConfig": {
          "thinkingConfig": {
            "thinkingBudget": 2000
          },
          "maxOutputTokens": 1024
        }
      }'
    ```

=== "Python"

    ```python
    import google.genai as genai
    from google.genai import types

    client = genai.Client(
        api_key="YOUR_API_KEY",
        http_options={"base_url": "https://tokens.smartfashionai.cn"},
    )

    response = client.models.generate_content(
        model="gemini-3.1-pro-preview",
        contents="请解释为什么天空是蓝色的",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=2000),
            max_output_tokens=1024,
        ),
    )

    print(response.text)
    ```

!!! note "思考 token 说明"
    `thinkingBudget` 为思考过程允许使用的最大 token 数，`maxOutputTokens` 必须大于 `thinkingBudget`。

---

## 二、图片理解

Gemini 支持将图片作为输入，通过 `inline_data` 传入原始字节数据（PNG/JPEG 等）。

### 2.1 本地图片理解

=== "cURL"

    ```bash
    # 将图片转为 base64
    IMAGE_BASE64=$(base64 -i image.jpg)

    curl -X POST "https://tokens.smartfashionai.cn/v1beta/models/gemini-3.1-flash-image-preview:generateContent" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d "{
        \"contents\": [
          {
            \"role\": \"user\",
            \"parts\": [
              {\"text\": \"这张图片里有什么？请简短描述。\"},
              {
                \"inline_data\": {
                  \"mime_type\": \"image/jpeg\",
                  \"data\": \"$IMAGE_BASE64\"
                }
              }
            ]
          }
        ]
      }"
    ```

=== "Python"

    ```python
    import google.genai as genai
    from google.genai import types

    client = genai.Client(
        api_key="YOUR_API_KEY",
        http_options={"base_url": "https://tokens.smartfashionai.cn"},
    )

    with open("image.jpg", "rb") as f:
        image_bytes = f.read()

    response = client.models.generate_content(
        model="gemini-3.1-flash-image-preview",
        contents=[
            types.Part(text="这张图片里有什么？请简短描述。"),
            types.Part(
                inline_data=types.Blob(
                    mime_type="image/jpeg",
                    data=image_bytes,
                )
            ),
        ],
    )

    print(response.text)
    ```

### 2.2 通过 URL 获取图片后理解

=== "Python"

    ```python
    import urllib.request
    import google.genai as genai
    from google.genai import types

    client = genai.Client(
        api_key="YOUR_API_KEY",
        http_options={"base_url": "https://tokens.smartfashionai.cn"},
    )

    req = urllib.request.Request(
        "https://example.com/image.jpg",
        headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        image_bytes = resp.read()

    response = client.models.generate_content(
        model="gemini-3.1-flash-image-preview",
        contents=[
            types.Part(text="这张图片里有什么？请简短描述。"),
            types.Part(
                inline_data=types.Blob(
                    mime_type="image/jpeg",
                    data=image_bytes,
                )
            ),
        ],
    )

    print(response.text)
    ```

### 2.3 多图片理解

=== "Python"

    ```python
    import google.genai as genai
    from google.genai import types

    client = genai.Client(
        api_key="YOUR_API_KEY",
        http_options={"base_url": "https://tokens.smartfashionai.cn"},
    )

    with open("image1.jpg", "rb") as f:
        img1 = f.read()
    with open("image2.jpg", "rb") as f:
        img2 = f.read()

    response = client.models.generate_content(
        model="gemini-3.1-flash-image-preview",
        contents=[
            types.Part(text="分别描述这两张图片，各用一句话。"),
            types.Part(inline_data=types.Blob(mime_type="image/jpeg", data=img1)),
            types.Part(inline_data=types.Blob(mime_type="image/jpeg", data=img2)),
        ],
    )

    print(response.text)
    ```

---

## 三、图片生成

使用 `gemini-3.1-flash-image-preview` 模型，设置 `response_modalities` 为 `["IMAGE", "TEXT"]`。

### 3.1 生成并保存图片

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1beta/models/gemini-3.1-flash-image-preview:generateContent" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "contents": [
          {"role": "user", "parts": [{"text": "画一只可爱的卡通猫咪"}]}
        ],
        "generationConfig": {
          "responseModalities": ["IMAGE", "TEXT"]
        }
      }'
    ```

=== "Python"

    ```python
    import google.genai as genai
    from google.genai import types

    client = genai.Client(
        api_key="YOUR_API_KEY",
        http_options={"base_url": "https://tokens.smartfashionai.cn"},
    )

    response = client.models.generate_content(
        model="gemini-3.1-flash-image-preview",
        contents="画一只可爱的卡通猫咪",
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
        ),
    )

    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            with open("generated.png", "wb") as f:
                f.write(part.inline_data.data)
            print(f"图片已保存: {part.inline_data.mime_type}, {len(part.inline_data.data)} bytes")
            break
    ```

### 3.2 获取 Base64 格式图片

=== "Python"

    ```python
    import base64
    import google.genai as genai
    from google.genai import types

    client = genai.Client(
        api_key="YOUR_API_KEY",
        http_options={"base_url": "https://tokens.smartfashionai.cn"},
    )

    response = client.models.generate_content(
        model="gemini-3.1-flash-image-preview",
        contents="画一幅简单的风景画",
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
        ),
    )

    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            b64_data = base64.b64encode(part.inline_data.data).decode()
            print(f"Base64 图片: {part.inline_data.mime_type}, {len(b64_data)} chars")
            break
    ```

---

## 四、视频理解

Gemini 支持视频理解，通过 `file_data` 传入公网可访问的视频 URL。

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1beta/models/gemini-3.1-flash-image-preview:generateContent" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "contents": [
          {
            "role": "user",
            "parts": [
              {"text": "这段视频展示了什么？请简短描述。"},
              {
                "file_data": {
                  "mime_type": "video/mp4",
                  "file_uri": "https://example.com/video.mp4"
                }
              }
            ]
          }
        ]
      }'
    ```

=== "Python"

    ```python
    import google.genai as genai
    from google.genai import types

    client = genai.Client(
        api_key="YOUR_API_KEY",
        http_options={"base_url": "https://tokens.smartfashionai.cn"},
    )

    response = client.models.generate_content(
        model="gemini-3.1-flash-image-preview",
        contents=[
            types.Part(text="这段视频展示了什么？请简短描述。"),
            types.Part(
                file_data=types.FileData(
                    mime_type="video/mp4",
                    file_uri="https://example.com/video.mp4",
                )
            ),
        ],
    )

    print(response.text)
    ```

---

## 五、工具调用（Function Calling）

Gemini 支持工具调用，通过 `FunctionDeclaration` 定义函数供模型调用。

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1beta/models/gemini-3.1-pro-preview:generateContent" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "contents": [
          {"role": "user", "parts": [{"text": "北京今天天气怎么样？"}]}
        ],
        "tools": [
          {
            "functionDeclarations": [
              {
                "name": "get_weather",
                "description": "获取指定城市的当前天气",
                "parameters": {
                  "type": "OBJECT",
                  "properties": {
                    "city": {
                      "type": "STRING",
                      "description": "城市名称"
                    },
                    "unit": {
                      "type": "STRING",
                      "description": "温度单位",
                      "enum": ["celsius", "fahrenheit"]
                    }
                  },
                  "required": ["city"]
                }
              }
            ]
          }
        ]
      }'
    ```

=== "Python"

    ```python
    import google.genai as genai
    from google.genai import types

    client = genai.Client(
        api_key="YOUR_API_KEY",
        http_options={"base_url": "https://tokens.smartfashionai.cn"},
    )

    get_weather = types.FunctionDeclaration(
        name="get_weather",
        description="获取指定城市的当前天气",
        parameters=types.Schema(
            type="OBJECT",
            properties={
                "city": types.Schema(type="STRING", description="城市名称"),
                "unit": types.Schema(
                    type="STRING",
                    description="温度单位",
                    enum=["celsius", "fahrenheit"],
                ),
            },
            required=["city"],
        ),
    )

    response = client.models.generate_content(
        model="gemini-3.1-pro-preview",
        contents="北京今天天气怎么样？",
        config=types.GenerateContentConfig(
            tools=[types.Tool(function_declarations=[get_weather])],
        ),
    )

    for part in response.candidates[0].content.parts:
        if part.function_call is not None:
            fc = part.function_call
            print(f"调用工具: {fc.name}")
            print(f"参数: {dict(fc.args)}")
    ```

**响应示例：**

```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "functionCall": {
              "name": "get_weather",
              "args": {
                "city": "北京",
                "unit": "celsius"
              }
            }
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP"
    }
  ]
}
```

---

## 六、注意事项

- **必须使用 `google-genai` SDK 或原生 Gemini API**，不支持 OpenAI 格式（`/v1/chat/completions`）调用 Gemini 模型
- **模型名称**：调用时请从「模型广场」复制完整模型 ID，名称必须完全一致
- **图片传入**：通过 `inline_data`（字节数据）传入，不支持直接传 URL；图片大小建议不超过 20MB
- **视频传入**：通过 `file_data.file_uri` 传入公网可访问的 URL；视频时长建议不超过 1 小时
- **思考模式**：`thinkingBudget` 建议设置为 1000–16000，`maxOutputTokens` 必须大于 `thinkingBudget`
- **系统提示词**：`max_output_tokens` 建议设置为 512 或更大
- **工具调用**：工具调用后需要将工具结果返回模型以获取最终响应
