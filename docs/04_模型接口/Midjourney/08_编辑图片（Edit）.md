# 编辑图片（Edit）


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
| `action` | string | 必需 | 固定 "EDITS" |
| `prompt` | string |  | 提示词 必需 |
| `base64Array` |  |  | array[string] 必需 目标图片base64 |
| `maskBase64` | string | 必需 | 蒙版图（Base64，黑白/透明区域作为编辑区域） |
| `notifyHook` | string | 可选 | 回调地址, 为空时使用全局notifyHook |
| `state` | string |  | 自定义参数 可选 |
| `remix` | boolean | 可选 | 示例 |


## 返回响应
