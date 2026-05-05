# 图像编辑（gpt-image-2）


## 请求参数


### Header 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `Accept` | string | 可选 | 示例: application/json |
| `Authorization` | string | 可选 |  |
| `Content-Type` | string | 可选 | 示例: application/json |


### Body 参数 (multipart/form-data)

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `model` | string |  | 模型 ID 必需 示例: |
| `gpt-image-2` | prompt |  |  |
| `string` | 编辑指提示词 | 必需 | 示例: 提示词 |
| `image` | file | 必需 | 原图（支持 PNG/JPEG/WebP/GIF），可同名多次传入 1-6 张参考图 |
| `mask` | file | 可选 | 可选 mask，必须 PNG 或 WebP（需 alpha 通道）。透明区 = 需要重绘，不透明区 = 保持原样 |
| `size` | string | 可选 | auto（默认，模型自选）1024x1024、1536x1024、1024x1536、2048x2048、2048x1152、3840x2160、2160x3840 |
| `quality` | string | 可选 | low（快，推荐草稿）/ medium / high（实际质量由 Codex 上游决定，可能降级）/ auto（默认） |
| `background` | string | 可选 | auto（默认）/ opaque。不支持 transparent，传入会被 Codex 拒绝 |
| `n` | integer | 可选 | 要生成的图像数。必须介于 1 和 10 之间。 |
| `response_format` | string | 可选 | b64_json/ url |
| `stream` | string | 可选 | true / 1/ yes/ on → 走 SSE |
| `instructions` | string | 可选 | system prompt |
| `output_format` | string | 可选 | png / jpeg / webp |
| `output_compression` | string |  | 0-100 可选 |
| `partial_images` | string |  | 仅流式 可选 |
| `moderation` | string | 可选 | auto / low |
| `input_fidelity` | string | 可选 | 参考图保真度（Codex 扩展字段） |


## 返回响应
