# 导出令牌每日消耗（XLSX）

**GET** `https://tokens.smartfashionai.cn/api/log/self/token_daily/export`

将令牌每日消耗数据导出为 XLSX 文件。

---

## 请求参数

### Header

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `Authorization` | string | 可选 | 系统访问令牌 |
| `New-Api-User` | string | 可选 | 用户 ID（数字） |

### Query

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `start_timestamp` | integer | 可选 | 开始时间戳（秒） |
| `end_timestamp` | integer | 可选 | 结束时间戳（秒） |
| `keyword` | string | 可选 | 关键词过滤 |
| `sort_field` | string | 可选 | 排序字段：`total` 或日期时间戳 |
| `sort_order` | string | 可选 | 排序方向：`asc` / `desc` |
| `page` | string | 可选 | 页码 |
| `page_size` | string | 可选 | 每页条数 |

---

## 请求示例

```bash
curl --location --request GET 'https://tokens.smartfashionai.cn/api/log/self/token_daily/export?start_timestamp=1773974400&end_timestamp=1774032510&keyword=&sort_field=&sort_order=&page=&page_size=' \
--header 'Authorization: user-token' \
--header 'New-Api-User: user-id'
```

---

## 响应说明

成功时返回 XLSX 文件流，HTTP 状态码 200。

---
