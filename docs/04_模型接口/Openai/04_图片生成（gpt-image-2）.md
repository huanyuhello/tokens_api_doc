# 图片生成（gpt-image-2）


## 请求参数


### Header 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `Accept` | string | 可选 | 示例: application/json |
| `Authorization` | string | 可选 | 示例: |
| `sk-` |  |  |  |
| `Content-Type` | string | 可选 | 示例: application/json |


### Body 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `必填` |  |  |  |
| `model` | string | 必需 | 要使用的模型的 ID。有关哪些模型适用于聊天 API 的详细信息 |
| `prompt` | string | 必需 | 所需图像的文本描述。最大长度为 1000 个字符。 |
| `n` | integer | 可选 | 要生成的图像数。必须介于 1 和 10 之间。 |
| `size` | string | 可选 | auto（默认，模型自选）1024x1024、1536x1024、1024x1536、2048x2048、2048x1152、3840x2160、2160x3840 |
| `quality` | string | 可选 | low（快，推荐草稿）/ medium / high（实际质量由 Codex 上游决定，可能降级）/ auto（默认） |
| `background` | string | 可选 | auto（默认）/ opaque。不支持 transparent，传入会被 Codex 拒绝 |
| `response_format` | string | 可选 | b64_json（默认，data[0].b64_json 返 base64）/ url（返 data[0].url形如 data:image/png;base64,...） |
| `stream` | boolean | 可选 | 可选，true 时走 SSE 流 |
| `instructions` | string | 可选 | 作为 system prompt 透传（对齐 Codex 官方契约），示例："Always render in pixel art style" |
| `output_format` | string | 可选 | 可选，png / jpeg / webp，默认 png |
| `output_compression` | integer | 可选 | 可选，jpeg/webp 压缩率 0..100 |
| `partial_images` | integer | 可选 | 仅流式生效；非流式传了会被强制置 0 |
| `moderation` | string | 可选 | 可选，auto / low 示例 |


## 返回响应
