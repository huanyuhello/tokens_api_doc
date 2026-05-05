# 图片生成（gpt-image-1）


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
| `model` | string | 必需 | 要使用的模型的 ID。有关哪些模型适用于聊天 API 的详细信息 |
| `prompt` | string | 必需 | 所需图像的文本描述。最大长度为 1000 个字符。 |
| `n` | string | 可选 | 要生成的图像数。必须介于 1 和 10 之间。 |
| `size` | string | 可选 | 生成图像的大小。必须是256x256、512x512或 1024x1024之一。 示例 |


## 返回响应
