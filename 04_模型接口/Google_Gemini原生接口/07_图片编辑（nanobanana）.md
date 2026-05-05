# 图片编辑（nanobanana）

Google Gemini接口
图片编辑（nanobanana）
**POST** `https://4sapi.com/v1beta/models/gemini-2.5-flash-image-preview:generateContent`

## 请求参数

Authorization
在 Header 添加参数 Authorization，其值为在 Bearer 之后拼接 Token
示例：
Authorization: Bearer ********************
### Header 参数

| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `Authorization` | string | 必需 | Content-Type |  |

### Body 参数

| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `role` | string | 可选 | array [object] |  |
| `generationConfig` | object | 必需 | array[string] |  |

## 返回响应

## 请求示例

```bash
curl --location --request POST 'https://4sapi.com/v1beta/models/gemini-2.5-flash-image-preview:generateContent' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "'\''Hi, This is a picture of me. Can you add a llama next to me"
        },
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "iVBOR3fabzK5CYII=。。base64。。。。"
          }
        }
      ]
    }
  ],
  "generationConfig": {
    "responseModalities": [
      "TEXT",
      "IMAGE"
    ]
  }
}'
```

## 响应示例

```json
{}
```