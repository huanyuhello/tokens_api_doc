# 图片编辑（Nano-banana） base64格式

OpenAI兼容接口（推荐）
图片编辑（Nano-banana） base64格式
**POST** `https://4sapi.com/v1/chat/completions`

## 请求参数

### Header 参数

| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `Accept` | string | 必需 | Authorization |  |
| `Content-Type` | string | 必需 | application/json |  |

### Body 参数

## 返回响应

## 请求示例

```bash
curl --location --request POST 'https://4sapi.com/v1/chat/completions' \
--header 'Accept: application/json' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model": "gemini-2.5-flash-image-preview",
    "stream": false,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "add a dog"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwA......"
                    }
                }
            ]
        }
    ]
}'
```

## 响应示例

```json
{
    "id": "string",
    "object": "string",
    "created": 0,
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "string",
                "content": "string"
            },
            "finish_reason": "string"
        }
    ],
    "usage": {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0
    }
}
```