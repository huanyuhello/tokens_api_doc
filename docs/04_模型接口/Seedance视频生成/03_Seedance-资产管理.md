# Seedance 资产管理

> 本模块用于管理视频生成所需的各种多模态素材（图片、视频、音频）。通过资产库管理素材，可在视频生成任务中通过资产 ID 安全引用，尤其适合仿真人等需要合规审核的场景。

**Base URL**：`https://tokens.smartfashionai.cn`

---

## 认证方式

所有接口均需在请求头中携带 API Key：

```http
Authorization: Bearer <YOUR_API_KEY>
Content-Type: application/json
```

---

## 接口概览

| 方法 | 路径 | 说明 |
|------|------|------|
| `POST` | `/open/CreateAsset` | 添加新资产 |
| `POST` | `/open/ListAssets` | 查询资产列表 |
| `POST` | `/open/GetAsset` | 获取资产详情 |
| `POST` | `/open/UpdateAsset` | 更新资产信息 |
| `POST` | `/open/DeleteAsset` | 删除资产记录 |

---

## 一、添加新资产

**POST** `/open/CreateAsset`

将外部素材链接注册到系统资产中心，注册后可在视频生成任务中通过资产 ID 引用。

### 请求参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `Name` | string | 必需 | 资产显示名称 |
| `AssetType` | string | 必需 | 资产类型，枚举值：`Image`、`Video`、`Audio` |
| `URL` | string | 必需 | 资产的公网可访问地址 |
| `ProjectName` | string | 可选 | 所属项目名称，不传则使用系统默认配置 |
| `Moderation` | object | 可选 | 内容审核配置，`Strategy` 可选 `Default`（开启）或 `Skip`（跳过），不传默认 `Skip` |

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/open/CreateAsset" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "Name": "测试图片素材",
        "AssetType": "Image",
        "URL": "https://example.com/demo.jpg",
        "Moderation": {
          "Strategy": "Skip"
        }
      }'
    ```

=== "Python"

    ```python
    import requests

    BASE_URL = "https://tokens.smartfashionai.cn"
    API_KEY  = "your_api_key_here"
    HEADERS  = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    payload = {
        "Name": "测试图片素材",
        "AssetType": "Image",
        "URL": "https://example.com/demo.jpg",
        "Moderation": {
            "Strategy": "Skip"
        }
    }

    resp = requests.post(f"{BASE_URL}/open/CreateAsset", json=payload, headers=HEADERS)
    print(resp.json())
    ```

### 响应示例

```json
{
  "code": 200,
  "status": "success",
  "message": "Operation successful",
  "data": {
    "Id": "asset-202404231705-xxxx"
  }
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.Id` | string | 资产 ID，格式为 `asset-<时间戳>-<随机串>`，用于视频生成时引用 |

!!! tip "在视频生成中引用资产"
    获取资产 ID 后，在视频生成请求的 `metadata.content` 中使用 `asset://<ID>` 格式引用：
    ```json
    {
      "type": "image_url",
      "role": "first_frame",
      "image_url": { "url": "asset://asset-202404231705-xxxx" }
    }
    ```

---

## 二、查询资产列表

**POST** `/open/ListAssets`

### 请求参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `PageNumber` | integer | 可选 | 页码，从 1 开始，默认 1 |
| `PageSize` | integer | 可选 | 每页条数，默认 10 |
| `Filter` | object | 可选 | 过滤器对象，见下表 |
| `SortBy` | string | 可选 | 排序字段：`CreateTime`、`UpdateTime` |
| `SortOrder` | string | 可选 | 排序方向：`Desc`（降序）、`Asc`（升序） |

**Filter 字段：**

| 字段 | 类型 | 说明 |
|------|------|------|
| `Name` | string | 素材名称模糊匹配 |
| `Statuses` | string[] | 状态过滤，可选值：`Active`、`Processing`、`Failed` |
| `GroupIds` | string[] | 指定资产组 ID 列表 |

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/open/ListAssets" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "Filter": {
          "Name": "测试",
          "Statuses": ["Active"]
        },
        "PageNumber": 1,
        "PageSize": 10,
        "SortBy": "CreateTime",
        "SortOrder": "Desc"
      }'
    ```

=== "Python"

    ```python
    import requests

    BASE_URL = "https://tokens.smartfashionai.cn"
    API_KEY  = "your_api_key_here"
    HEADERS  = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    payload = {
        "Filter": {
            "Name": "测试",
            "Statuses": ["Active"]
        },
        "PageNumber": 1,
        "PageSize": 10,
        "SortBy": "CreateTime",
        "SortOrder": "Desc"
    }

    resp = requests.post(f"{BASE_URL}/open/ListAssets", json=payload, headers=HEADERS)
    data = resp.json()
    for item in data["data"]["Items"]:
        print(f"{item['Id']}  {item['Name']}  {item['Status']}")
    ```

### 响应示例

```json
{
  "code": 200,
  "status": "success",
  "data": {
    "Items": [
      {
        "Id": "asset-xxxx",
        "Name": "测试图片素材",
        "AssetType": "Image",
        "URL": "https://tos-path.volces.com/xxx.jpg",
        "Status": "Active",
        "CreateTime": "2024-04-23T09:05:07Z",
        "UpdateTime": "2024-04-23T09:05:12Z"
      }
    ],
    "PageNumber": 1,
    "PageSize": 10,
    "TotalCount": 1
  }
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `data.Items` | array | 资产列表 |
| `data.TotalCount` | integer | 总条数 |
| `data.PageNumber` | integer | 当前页码 |
| `data.PageSize` | integer | 每页条数 |

**资产状态枚举：**

| 状态值 | 说明 |
|--------|------|
| `Processing` | 处理中（上传/审核中） |
| `Active` | 可用，可在视频生成中引用 |
| `Failed` | 处理失败 |

---

## 三、获取资产详情

**POST** `/open/GetAsset`

### 请求参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `Id` | string | 必需 | 资产 ID |

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/open/GetAsset" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "Id": "asset-202404231705-xxxx"
      }'
    ```

=== "Python"

    ```python
    import requests

    BASE_URL = "https://tokens.smartfashionai.cn"
    API_KEY  = "your_api_key_here"
    HEADERS  = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    resp = requests.post(
        f"{BASE_URL}/open/GetAsset",
        json={"Id": "asset-202404231705-xxxx"},
        headers=HEADERS
    )
    print(resp.json())
    ```

### 响应示例

```json
{
  "code": 200,
  "status": "success",
  "data": {
    "Id": "asset-202404231705-xxxx",
    "Name": "测试图片素材",
    "AssetType": "Image",
    "URL": "https://tos-path.volces.com/xxx.jpg",
    "Status": "Active",
    "ProjectName": "default",
    "CreateTime": "2024-04-23T09:05:07Z",
    "UpdateTime": "2024-04-23T09:05:12Z"
  }
}
```

---

## 四、更新资产信息

**POST** `/open/UpdateAsset`

### 请求参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `Id` | string | 必需 | 资产 ID |
| `Name` | string | 可选 | 新的资产名称 |

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/open/UpdateAsset" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "Id": "asset-202404231705-xxxx",
        "Name": "修改后的名称"
      }'
    ```

=== "Python"

    ```python
    import requests

    BASE_URL = "https://tokens.smartfashionai.cn"
    API_KEY  = "your_api_key_here"
    HEADERS  = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    resp = requests.post(
        f"{BASE_URL}/open/UpdateAsset",
        json={"Id": "asset-202404231705-xxxx", "Name": "修改后的名称"},
        headers=HEADERS
    )
    print(resp.json())
    ```

---

## 五、删除资产记录

**POST** `/open/DeleteAsset`

### 请求参数

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `Id` | string | 必需 | 资产 ID |

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/open/DeleteAsset" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "Id": "asset-202404231705-xxxx"
      }'
    ```

=== "Python"

    ```python
    import requests

    BASE_URL = "https://tokens.smartfashionai.cn"
    API_KEY  = "your_api_key_here"
    HEADERS  = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    resp = requests.post(
        f"{BASE_URL}/open/DeleteAsset",
        json={"Id": "asset-202404231705-xxxx"},
        headers=HEADERS
    )
    print(resp.json())
    ```

### 响应示例

```json
{
  "code": 200,
  "status": "success",
  "data": {}
}
```

---

## 注意事项

- 资产状态变为 `Active` 后才可在视频生成中引用，`Processing` 状态下引用会报错
- 仿真人图片建议通过资产库上传并使用 `asset://<ID>` 引用，直接传外部 URL 可能触发安全过滤
- 删除资产后，已提交的视频生成任务不受影响，但新任务无法再引用该资产 ID
