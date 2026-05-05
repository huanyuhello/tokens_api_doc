# 生成视频（Video）


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
| `prompt` | string |  | 描述文本 必需 |
| `base64Array` |  |  | array[string] 必需 Base64图片数组 |
| `taskId` | string |  | 已有任务ID 可选 |
| `customId` | string |  | 自定义ID 可选 |
| `botType` | string |  | 机器人类型 可选 |
| `notifyHook` | string | 可选 | 回调地址, 为空时使用全局notifyHook |
| `index` | string |  | 索引 可选 |
| `state` | string |  | 自定义参数 可选 |
| `content` | string |  | 内容 可选 |
| `maskBase64` | string |  | 遮罩Base64 可选 示例 |


## 返回响应


## 响应示例

```json
{
"taskId": "existing-task-id-12345",
"prompt": "基于这张图片生成视频，小猫在花园里走动",
"notifyHook": "https://your-domain.com/mj/notify"
}
```
