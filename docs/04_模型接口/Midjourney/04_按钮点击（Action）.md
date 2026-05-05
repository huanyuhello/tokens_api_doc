# 按钮点击（Action）


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
| `chooseSameChannel` | boolean | 可选 |  |
| `customId` | string |  | 动作标识 必需 |
| `taskId` | string |  | 任务ID 必需 |
| `accountFilter` | object | 可选 |  |
| `channelId` | string |  | 频道ID 可选 |
| `instanceId` | string |  | 账号实例ID 可选 |
| `modes` |  |  | array[string] 账号模式 可选 |
| `remark` | string |  | 备注 可选 |
| `remix` | boolean |  | 账号是否remix 可选 |
| `remixAutoConsidered` | boolean | 可选 | 账号过滤时，remix自动提交 视为 账号的remix为false |
| `notifyHook` | string | 可选 | 回调地址, 为空时使用全局notifyHook |
| `state` | string |  | 自定义参数 可选 示例 |


## 返回响应
