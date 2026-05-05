# Flux Dalle3 Edits 图生图 文生图


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
| `prompt` | string | 可选 |  |
| `string` | 可选 |  | 示例值: 带上眼镜 |
| `model` | string | 可选 |  |
| `string` | 可选 |  | 示例值: |
| `flux-kontext-pro` | size |  |  |
| `string` | 可选 |  |  |
| `string` | 可选 |  | 最终会转换成比例，建议直接使用 aspect_ratio 示例值: 1024x1024 |
| `aspect_ratio` | string | 可选 |  |
| `string` | 可选 |  | 21:9, 16:9, 4:3, 3:2, 1:1, 2:3, 3:4, 9:16, 9:21 示例值: 1:1 |
| `image` | string | 可选 |  |
| `file` | 可选 |  | 参考图片，支持多个 示例 |


## 返回响应
