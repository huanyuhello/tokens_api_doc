# Seedance Fast 2.0 视频生成

> 模型 ID：`seedance-2.0-fast`
>
> 轻量快速视频生成模型，速度快、成本低，适合快速预览与迭代。通常 1–3 分钟完成。支持文生视频和图生视频，最高分辨率 720p。

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
| `POST` | `/v1/video/generations` | 提交视频生成任务 |
| `GET` | `/v1/video/generations/{task_id}` | 查询任务状态与结果 |

---

## 一、提交视频生成任务

**POST** `/v1/video/generations`

### 请求参数

#### Header

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `Authorization` | string | 必需 | `Bearer <YOUR_API_KEY>` |
| `Content-Type` | string | 必需 | `application/json` |

#### Body（application/json）

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `model` | string | 必需 | 固定为 `seedance-2.0-fast` |
| `prompt` | string | 必需 | 视频生成提示词，支持中英文 |
| `duration` | integer | 可选 | 视频时长（秒），可选 `5`（默认）或 `10` |
| `metadata` | object | 可选 | 画面参数对象 |
| `metadata.resolution` | string | 可选 | 分辨率：`480p` / `720p`（默认），**不支持 1080p** |
| `metadata.ratio` | string | 可选 | 画面比例：`16:9`（默认）/ `9:16` / `1:1` |
| `metadata.content` | array | 可选 | 多模态参考内容（图片），见下方说明 |

!!! warning "与 Seedance 2.0 的差异"
    - 最高分辨率为 **720p**，不支持 1080p
    - **不支持**视频输入（`video_url`）和音频输入（`audio_url`）
    - 如需视频生视频、音频参考或 1080p 输出，请使用 [Seedance 2.0](01_Seedance-2-0-视频生成.md)

### metadata.content 说明

`content` 为对象数组，Fast 版本仅支持图片输入。

**支持的组合方式：**

| 组合 | 说明 |
|------|------|
| 文本 | 纯文生视频 |
| 文本 + 图片 | 图生视频（首帧 / 首尾帧） |

---

=== "文本内容"

    | 参数 | 类型 | 必填 | 说明 |
    |------|------|------|------|
    | `type` | string | 必需 | 固定为 `text` |
    | `text` | string | 必需 | 提示词，建议中文 ≤500 字，英文 ≤1000 词 |

=== "图片内容"

    | 参数 | 类型 | 必填 | 说明 |
    |------|------|------|------|
    | `type` | string | 必需 | 固定为 `image_url` |
    | `image_url.url` | string | 必需 | 图片 URL、Base64（`data:image/<格式>;base64,<数据>`）或素材 ID（`asset://<ID>`） |
    | `role` | string | 条件必填 | 图片用途，见下表 |

    **图片 role 取值：**

    | 场景 | 图片数量 | role |
    |------|---------|------|
    | 图生视频（首帧） | 1 张 | `first_frame`（或不填） |
    | 首尾帧（首帧） | 2 张中的首帧 | `first_frame`（必填） |
    | 首尾帧（尾帧） | 2 张中的尾帧 | `last_frame`（必填） |

    **图片格式要求：**

    - 格式：`jpeg`、`png`、`webp`、`bmp`、`tiff`、`gif`
    - 宽高比（宽/高）：(0.4, 2.5)
    - 宽高（px）：(300, 6000)
    - 大小：单张 < 30 MB，请求体 ≤ 64 MB

---

### 响应

```json
{
  "task_id": "task_0a1b2c3d4e5f6789",
  "status": "queued"
}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `task_id` | string | 任务 ID，用于后续查询 |
| `status` | string | 初始状态，固定为 `queued` |

---

## 二、查询任务状态

**GET** `/v1/video/generations/{task_id}`

### 路径参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `task_id` | string | 提交任务时返回的 `task_id` |

### 响应字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `code` | string | 网关返回码，`success` 表示成功 |
| `data.task_id` | string | 任务 ID |
| `data.status` | string | 任务状态，见下表 |
| `data.progress` | string | 进度，如 `"60%"` |
| `data.result_url` | string | 成功时的视频地址 |
| `data.fail_reason` | string | 失败原因（仅失败时有值） |
| `data.submit_time` | integer | 提交时间戳（秒） |
| `data.finish_time` | integer | 完成时间戳（秒） |

### 任务状态枚举

| 状态值 | 说明 |
|--------|------|
| `QUEUED` | 排队中 |
| `IN_PROGRESS` | 生成中 |
| `SUCCESS` | 生成成功 |
| `FAILURE` | 生成失败 |
| `CANCELLED` | 已取消 |
| `EXPIRED` | 已过期 |

### 响应示例

=== "提交成功"

    ```json
    {
      "task_id": "task_0a1b2c3d4e5f6789",
      "status": "queued"
    }
    ```

=== "生成中"

    ```json
    {
      "code": "success",
      "data": {
        "task_id": "task_0a1b2c3d4e5f6789",
        "status": "IN_PROGRESS",
        "progress": "60%",
        "result_url": "",
        "fail_reason": "",
        "submit_time": 1746940000,
        "finish_time": 0
      }
    }
    ```

=== "生成成功"

    ```json
    {
      "code": "success",
      "data": {
        "task_id": "task_0a1b2c3d4e5f6789",
        "status": "SUCCESS",
        "progress": "100%",
        "result_url": "https://cdn.example.com/videos/output_0a1b2c3d.mp4",
        "fail_reason": "",
        "submit_time": 1746940000,
        "finish_time": 1746940090
      }
    }
    ```

=== "生成失败"

    ```json
    {
      "code": "success",
      "data": {
        "task_id": "task_0a1b2c3d4e5f6789",
        "status": "FAILURE",
        "progress": "0%",
        "result_url": "",
        "fail_reason": "prompt contains sensitive content",
        "submit_time": 1746940000,
        "finish_time": 1746940010
      }
    }
    ```

---

## 三、场景示例

### A. 基础用法

#### 文生视频

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/video/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "seedance-2.0-fast",
        "prompt": "一只猫在草地上奔跑，阳光明媚，镜头缓慢推进",
        "duration": 5,
        "metadata": {
          "resolution": "720p",
          "ratio": "16:9"
        }
      }'
    ```

=== "Python"

    ```python
    import time
    import requests

    BASE_URL = "https://tokens.smartfashionai.cn"
    API_KEY  = "your_api_key_here"
    HEADERS  = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


    def submit_video(prompt: str, duration: int = 5,
                     resolution: str = "720p", ratio: str = "16:9") -> str:
        payload = {
            "model": "seedance-2.0-fast",
            "prompt": prompt,
            "duration": duration,
            "metadata": {"resolution": resolution, "ratio": ratio},
        }
        resp = requests.post(f"{BASE_URL}/v1/video/generations", json=payload, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()["task_id"]


    def poll_task(task_id: str, interval: int = 5, timeout: int = 300) -> dict:
        deadline = time.time() + timeout
        while time.time() < deadline:
            resp = requests.get(f"{BASE_URL}/v1/video/generations/{task_id}", headers=HEADERS)
            resp.raise_for_status()
            result = resp.json()
            status = result["data"]["status"]
            print(f"  状态: {status}")
            if status in ("SUCCESS", "SUCCEEDED", "COMPLETED"):
                return result
            if status in ("FAILURE", "FAILED", "CANCELLED", "EXPIRED"):
                raise RuntimeError(f"任务失败: {result['data'].get('fail_reason')}")
            time.sleep(interval)
        raise TimeoutError(f"任务 {task_id} 超时（{timeout}s）")


    if __name__ == "__main__":
        task_id = submit_video("一只狐狸在雪地里跳舞，4K，慢动作")
        print(f"已提交，task_id = {task_id}")
        result = poll_task(task_id)
        print(f"完成！视频地址: {result['data']['result_url']}")
    ```

#### 图生视频

!!! tip "参数说明"
    | 场景 | 图片数量 | role |
    |------|---------|------|
    | 图生视频（首帧） | 1 张 | `first_frame`（或不填） |
    | 首尾帧（首帧） | 2 张中的首帧 | `first_frame`（必填） |
    | 首尾帧（尾帧） | 2 张中的尾帧 | `last_frame`（必填） |
    | 多模态参考图 | 1～9 张 | `reference_image`（必填） |


=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/video/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "seedance-2.0-fast",
        "prompt": "人物缓缓转身，微风吹动头发",
        "duration": 5,
        "metadata": {
          "resolution": "720p",
          "ratio": "9:16",
          "content": [
            {
              "type": "image_url",
              "role": "first_frame",
              "image_url": { "url": "https://example.com/reference.jpg" }
            }
          ]
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
        "model": "seedance-2.0-fast",
        "prompt": "人物优雅地转身，微风吹起裙摆",
        "duration": 5,
        "metadata": {
            "resolution": "720p",
            "ratio": "9:16",
            "content": [
                {
                    "type": "image_url",
                    "role": "first_frame",
                    "image_url": {"url": "https://example.com/reference.jpg"}
                }
            ]
        }
    }

    resp = requests.post(f"{BASE_URL}/v1/video/generations", json=payload, headers=HEADERS)
    print(resp.json())
    ```


#### 视频生视频

以一段已有视频为参考，生成风格或内容延续的新视频。

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/video/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "seedance-2.0-fast",
        "prompt": "延续视频风格，继续向前行驶，保持同样的运镜节奏",
        "duration": 5,
        "metadata": {
          "resolution": "720p",
          "ratio": "16:9",
          "content": [
            {
              "type": "video_url",
              "role": "reference_video",
              "video_url": { "url": "https://example.com/source_video.mp4" }
            }
          ]
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
        "model": "seedance-2.0-fast",
        "prompt": "延续视频风格，继续向前行驶，保持同样的运镜节奏",
        "duration": 5,
        "metadata": {
            "resolution": "720p",
            "ratio": "16:9",
            "content": [
                {
                    "type": "video_url",
                    "role": "reference_video",
                    "video_url": {"url": "https://example.com/source_video.mp4"}
                }
            ]
        }
    }

    resp = requests.post(f"{BASE_URL}/v1/video/generations", json=payload, headers=HEADERS)
    print(resp.json())
    ```

---

### B. 快速预览迭代

适合在正式生产前用 Fast 版本快速验证 prompt 效果，满意后再切换到 Seedance 2.0 出高清版本。

#### 竖屏短视频预览

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/video/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "seedance-2.0-fast",
        "prompt": "年轻女性在咖啡馆窗边阅读，暖光，浅景深，电影感",
        "duration": 5,
        "metadata": {
          "resolution": "720p",
          "ratio": "9:16"
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
        "model": "seedance-2.0-fast",
        "prompt": "年轻女性在咖啡馆窗边阅读，暖光，浅景深，电影感",
        "duration": 5,
        "metadata": {"resolution": "720p", "ratio": "9:16"},
    }

    resp = requests.post(f"{BASE_URL}/v1/video/generations", json=payload, headers=HEADERS)
    print(resp.json())
    ```

#### 首尾帧控制预览

快速验证首尾帧过渡效果，确认满意后再用 Seedance 2.0 生成高清版本。

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/video/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "seedance-2.0-fast",
        "prompt": "角色表情从平静自然过渡到开心微笑，光影柔和",
        "duration": 5,
        "metadata": {
          "resolution": "720p",
          "ratio": "9:16",
          "content": [
            {
              "type": "image_url",
              "role": "first_frame",
              "image_url": { "url": "https://example.com/calm.jpg" }
            },
            {
              "type": "image_url",
              "role": "last_frame",
              "image_url": { "url": "https://example.com/smile.jpg" }
            }
          ]
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
        "model": "seedance-2.0-fast",
        "prompt": "角色表情从平静自然过渡到开心微笑，光影柔和",
        "duration": 5,
        "metadata": {
            "resolution": "720p",
            "ratio": "9:16",
            "content": [
                {
                    "type": "image_url",
                    "role": "first_frame",
                    "image_url": {"url": "https://example.com/calm.jpg"}
                },
                {
                    "type": "image_url",
                    "role": "last_frame",
                    "image_url": {"url": "https://example.com/smile.jpg"}
                }
            ]
        }
    }

    resp = requests.post(f"{BASE_URL}/v1/video/generations", json=payload, headers=HEADERS)
    print(resp.json())
    ```

---

### C. 电商与产品展示

适合快速生成产品展示视频，低成本批量预览多个角度或风格。

#### 产品展示动效

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/video/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "seedance-2.0-fast",
        "prompt": "香水瓶在白色背景上缓慢旋转，光线从侧面打入，高端质感",
        "duration": 5,
        "metadata": {
          "resolution": "720p",
          "ratio": "1:1",
          "content": [
            {
              "type": "image_url",
              "role": "first_frame",
              "image_url": { "url": "https://example.com/product.jpg" }
            }
          ]
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
        "model": "seedance-2.0-fast",
        "prompt": "香水瓶在白色背景上缓慢旋转，光线从侧面打入，高端质感",
        "duration": 5,
        "metadata": {
            "resolution": "720p",
            "ratio": "1:1",
            "content": [
                {
                    "type": "image_url",
                    "role": "first_frame",
                    "image_url": {"url": "https://example.com/product.jpg"}
                }
            ]
        }
    }

    resp = requests.post(f"{BASE_URL}/v1/video/generations", json=payload, headers=HEADERS)
    print(resp.json())
    ```

---

## 注意事项

- **轮询间隔**：建议每 5 秒查询一次，避免触发限流（429）
- **超时建议**：Seedance Fast 通常 1–3 分钟完成，建议设置至少 300 秒超时
- **不支持 1080p**：最高分辨率为 720p；如需 1080p，请使用 Seedance 2.0
- **不支持视频/音频输入**：如需视频生视频或音频参考，请使用 Seedance 2.0
- **首尾帧**：`first_frame` 与 `last_frame` 必须同时提供，且两张图片的宽高比需一致
- **竖屏视频**：使用 `ratio: "9:16"`
