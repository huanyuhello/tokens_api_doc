# doubao-seedream-4-0-文生图


## 请求参数


### Header 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `Accept` | string | 必需 | 示例: application/json |
| `Authorization` | string | 必需 | 示例: |
| `sk-` |  |  |  |
| `Content-Type` | string | 必需 | 示例: application/json |


### Body 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `必填` |  |  |  |
| `model` | string | 必需 | 本次请求使用模型的 Model ID。 |
| `prompt` | string | 必需 | 用于生成图像的提示词，支持中英文。 |
| `size` | string | 必需 | 指定生成图像的尺寸信息，支持以下两种方式，不可混用。 方式1 \|指定生成图像的分辨率，可选值：1K、2K、4K 方式2 \|指定生成图像的宽高像素值：默认值：2048x2048 面积取值范围：[1024x1024, 4096x4096] 宽高比取值范围：[1/16, 16] |
| `sequential_image_generation` | string | 必需 | 控制是否关闭组图功能。默认值 disabled 取值范围： auto：自动判断模式，模型会根据用户提供的提示词自主判断是否返回组图以及组图包含的图片数量。 disabled：关闭组图功能，模型只会生成一张图。 |
| `stream` | string | 必需 | 控制是否开启流式输出模式。默认值 false |
| `response_format` | string | 必需 | 指定生成图像的返回格式。默认值 url 生成的图片为 jpeg 格式，支持以下两种返回方式： url：返回图片下载链接；链接在图片生成后24小时内有效，请及时下载图片。 b64_json：以 Base64 编码字符串的 JSON 格式返回图像数据。 |
| `watermark` | string | 必需 | 是否在生成的图片中添加水印。默认值 true false：不添加水印。 true：在图片右下角添加“AI生成”字样的水印标识。 示例 |


## 返回响应
