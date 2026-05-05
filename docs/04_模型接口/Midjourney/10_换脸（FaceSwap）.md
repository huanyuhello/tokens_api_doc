# 换脸（FaceSwap）


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
| `sourceBase64` | string | 必需 | 人脸源图片base64 |
| `targetBase64` | string | 必需 | 目标图片base64 |
| `accountFilter` | object | 必需 |  |
| `instanceId` | string |  | 账号实例ID 必需 |
| `notifyHook` | string | 必需 | 回调地址, 为空时使用全局notifyHook |
| `state` | string |  | 自定义参数 必需 示例 |


## 返回响应
