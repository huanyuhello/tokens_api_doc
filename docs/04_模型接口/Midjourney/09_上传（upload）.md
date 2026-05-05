# 上传（upload）


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
| `base64Array` |  |  | array[string] base64数组 必需 |
| `filter` | object | 必需 |  |
| `channelId` | string |  | 频道ID 必需 |
| `instanceId` | string |  | 账号实例ID 必需 |
| `remark` | string |  | 备注包含 必需 示例 |


## 返回响应
