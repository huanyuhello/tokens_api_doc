# 图片融合（Blend）


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
| `botType` | string | 可选 |  |
| `base64Array` |  |  | array[string] 必需 垫图base64数组 |
| `dimensions` | string | 必需 | 比例: PORTRAIT(2:3); SQUARE(1:1); LANDSCAPE(3:2) 枚举值:PORTRAIT SQUARE LANDSCAPE 示例值:SQUARE |
| `accountFilter` | object | 可选 |  |
| `channelId` | string |  | 频道ID 可选 |
| `instanceId` | string |  | 账号实例ID 可选 |
| `modes` | string |  | 账号模式 可选 |
| `remark` | string |  | 备注 可选 |
| `remix` | string |  | 账号是否remix 可选 |
| `remixAutoConsidered` | string | 可选 | 账号过滤时，remix自动提交 视为 账号的remix为false |
| `notifyHook` | string | 可选 |  |
| `state` | string | 可选 | 示例 |


## 返回响应
