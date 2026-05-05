# Flux 创建 OpenAI dall-e-3格式


## 请求参数


### Header 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `Authorization` | string | 可选 | 示例: Bearer {{YOUR_API_KEY}} |


### Body 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `必填` |  |  |  |
| `prompt` | string | 必需 | 所需图像的文本描述。最大长度为 1000 个字符。 |
| `model` | string | 必需 | 用于图像生成的模型。 |
| `n` | integer | 必需 | 要生成的图像数。必须介于 1 和 10 之间。 |
| `quality` | string | 必需 | 将生成的图像的质量。hd创建具有更精细细节和更高一致性的图像。此参数仅支持dall-e-3. |
| `response_format` | string | 必需 | 返回生成的图像的格式。必须是 或url之一b64_json。 |
| `style` | string |  | 风格 必需 |
| `user` | string | 必需 | 生成图像的风格。必须是 或vivid之一natural。生动使模型倾向于生成超真实和戏剧性的图像。自然使模型生成更自然、不太真实的图像。此参数仅支持dall-e-3. |
| `size` | string | 必需 | 生成图像的大小。必须是256x256、512x512或 1024x1024之一。 |
| `aspect_ratio` | string | 必需 | 图片比例: 枚举值Possible enum values: 21:9, 16:9, 4:3, 3:2, 1:1, 2:3, 3:4, 9:16, 9:21 示例 |


## 返回响应
