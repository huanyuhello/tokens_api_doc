# MJ视频 chat格式

openai兼容/chat格式
MJ视频 （chat格式）
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
  "model": "chat_fast_video",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "飞机冒烟，准备撞击大厦，超人突然出现，救下飞机"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://cdn.pixabay.com/photo/2020/05/01/08/33/building-5115897_1280.jpg"
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
    "id": "chatcmpl-e958087762724a59a3b6d4931bae3fee",
    "object": "chat.completion.chunk",
    "serviceTier": "default",
    "created": 1753957765,
    "model": "chat_fast_video",
    "choices": [
        {
            "index": 0,
            "finishReason": "stop",
            "delta": {
                "role": "assistant",
                "content": "✅ 图片生成完成！\n\n**视频1:**\n[![视频1](https://video1.mid。。。。。。"
            }
        }
    ]
}
```