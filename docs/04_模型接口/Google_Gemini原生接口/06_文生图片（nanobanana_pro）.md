# 文生图片（nanobanana pro）


## 请求参数


### Header 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `Authorization` | string | 必需 | 示例: sk-*********** |
| `Content-Type` | string | 必需 | 示例: application/json |


### Body 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `必填` |  |  |  |
| `contents` |  |  | array [object] 必需 |
| `role` | string | 可选 |  |
| `parts` |  |  | array [object] 可选 |
| `generationConfig` | object | 必需 |  |
| `responseModalities` |  |  | array[string] 必需 示例 |


## 返回响应
