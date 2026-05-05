# 图片编辑（nanobanana pro）

Google Gemini接口
图片编辑（nanobanana pro）
**POST** `https://4sapi.com/v1beta/models/gemini-3-pro-image-preview:generateContent`

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
| `contents` | object | 必需 | parts |  |
| `generationConfig` | object | 必需 | responseModalities |  |

## 返回响应

## 请求示例

```bash
curl --location --request POST 'https://4sapi.com/v1beta/models/gemini-3-pro-image-preview:generateContent' \
--header 'Authorization: Bearer <token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "contents": [
        {
            "role": "user",
            "parts": [
                {
                    "text": "将背景修改为炸鸡店"
                },
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": "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w+6jf/Wn7sMf/gP3wb/6fffuj/yue/1fvcW97MOvc895/4vcL//+S92v/f6vuLe9/43ube99o3vD777RvfKPftO99JNvda9Y+QP344O3u+8avtw9uP4096AzT3b+Xx90+MOqw99d6XDLE5239SwX9Z7vvLWfcdPNZ7tDgxe4B3Vf4A4tP915132vk68/3s1s/rxbGL3SHRj8mnvk1pvdwz73Ivfg1z3JPfmlT3W/8EvPcK/+pee4txP/D/3qi92XXvtyd8srX+Bued7PuWt/7qnuIz/1A+6D9Cvf9awfd+940bPd2170HPf+V/2y++gbX+M+//bXuc+88WXun17/i+7rv/lMd/q3nu2Gv/0CN3zZzzj3gh9zyc8/xTV+7glu5b/9gLv76T/gvv7Mp7gvPfsn3F/8zI+61z/2e9xzH/1d7uee8AT3E0/5IfeMpz/LvfBFpMVrfsO9/nVvcr/6qte6F/33l7gXPP/F7hUv+xX3yy9+mXvxC1/ifvXVr3VveiPp9/JfcU968o+4yx/8EBeXK86PC84EoQuKEw624mw84y6/hn7hTzzLvfilv+5+443vcL/19ve4173h7e6FL3+de+Yvvto9/qm/6C575I+6yQf/hNv7hDe4Bz3zL9yjfu069/2/c9o9+j3r7pHv2XYPe1fdfee7W+4xb9t2P/imRfdfXnGd+6ln/S/39Ce90j3jmh9wL7zkQe5N1+xzf/WUy93nnvFw97UXP8Hd+pqfcrf85rPc7e98qbvj997gbv3jd7sv/o93u798y2+5977619xvvuRV7pee91L3X//L0901D32Mm913lZs78LAcrrj80e5hD/0+9/BHPtlddvVj3X9/xdvcZ798xJ1c7LpNynKP9nD
```

## 响应示例

```json
{}
```