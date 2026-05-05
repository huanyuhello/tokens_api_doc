# 获取种子（Seed）接口

原生接口
获取种子（Seed）接口
**GET** `https://4sapi.com/mj/task/{id}/image-seed`

## 请求参数

### Path 参数

| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `id` | string | 必需 |  |  |

### Header 参数

| 参数名 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| `Accept` | string | 必需 | Authorization |  |
| `Content-Type` | string | 必需 | application/json |  |

## 返回响应

## 请求示例

```bash
curl --location --request GET 'https://4sapi.com/mj/task//image-seed' \
--header 'Accept: application/json' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json'
```

## 响应示例

```json
{
    "code": 0,
    "description": "string",
    "result": "string"
}
```