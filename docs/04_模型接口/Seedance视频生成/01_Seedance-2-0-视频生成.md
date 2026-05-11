# Seedance 2.0 视频生成

> 模型 ID：`seedance-2.0`
>
> 高画质视频生成模型，支持文生视频、图生视频、视频生视频及多模态参考输入。适合正式生产场景，通常 3–5 分钟完成。

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
| `model` | string | 必需 | 固定为 `seedance-2.0` |
| `prompt` | string | 必需 | 视频生成提示词，支持中英文 |
| `duration` | integer | 可选 | 视频时长（秒），可选 `5`（默认）或 `10` |
| `metadata` | object | 可选 | 画面参数对象 |
| `metadata.resolution` | string | 可选 | 分辨率：`480p` / `720p`（默认）/ `1080p` |
| `metadata.ratio` | string | 可选 | 画面比例：`16:9`（默认）/ `9:16` / `1:1` |
| `metadata.content` | array | 可选 | 多模态参考内容（图片 / 视频 / 音频），见下方说明 |

### metadata.content 说明

`content` 为对象数组，支持文本、图片、视频、音频四种类型组合。

**支持的组合方式：**

| 组合 | 说明 |
|------|------|
| 文本 | 纯文生视频 |
| 文本 + 图片 | 图生视频 |
| 文本 + 视频 | 视频生视频 |
| 文本 + 图片 + 音频 | 图片 + 音频参考 |
| 文本 + 图片 + 视频 | 图片 + 视频参考 |
| 文本 + 视频 + 音频 | 视频 + 音频参考 |
| 文本 + 图片 + 视频 + 音频 | 全模态参考 |

> 音频不可单独输入，需至少包含 1 个参考图片或视频。

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
    | 多模态参考图 | 1～9 张 | `reference_image`（必填） |

    **图片格式要求：**

    - 格式：`jpeg`、`png`、`webp`、`bmp`、`tiff`、`gif`
    - 宽高比（宽/高）：(0.4, 2.5)
    - 宽高（px）：(300, 6000)
    - 大小：单张 < 30 MB，请求体 ≤ 64 MB

=== "视频内容"

    | 参数 | 类型 | 必填 | 说明 |
    |------|------|------|------|
    | `type` | string | 必需 | 固定为 `video_url` |
    | `video_url.url` | string | 必需 | 视频公网 URL 或素材 ID（`asset://<ID>`） |
    | `role` | string | 必需 | 固定为 `reference_video` |

    **视频格式要求：**

    - 格式：`mp4`、`mov`
    - 分辨率：480p、720p
    - 单个时长：[2, 15] 秒；最多 3 个，总时长 ≤ 15 秒
    - 宽高比（宽/高）：[0.4, 2.5]
    - 画面像素（宽 × 高）：[409600, 927408]
    - 大小：单个 ≤ 50 MB
    - 帧率：[24, 60] FPS

=== "音频内容"

    | 参数 | 类型 | 必填 | 说明 |
    |------|------|------|------|
    | `type` | string | 必需 | 固定为 `audio_url` |
    | `audio_url.url` | string | 必需 | 音频 URL、Base64（`data:audio/<格式>;base64,<数据>`）或素材 ID（`asset://<ID>`） |
    | `role` | string | 必需 | 固定为 `reference_audio` |

    **音频格式要求：**

    - 格式：`wav`、`mp3`
    - 单段时长：[2, 15] 秒；最多 3 段，总时长 ≤ 15 秒
    - 大小：单个 ≤ 15 MB，请求体 ≤ 64 MB

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
        "finish_time": 1746940120
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
        "model": "seedance-2.0",
        "prompt": "城市夜景延时摄影，霓虹灯倒映在雨后街道",
        "duration": 5,
        "metadata": {
          "resolution": "1080p",
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
                     resolution: str = "1080p", ratio: str = "16:9") -> str:
        payload = {
            "model": "seedance-2.0",
            "prompt": prompt,
            "duration": duration,
            "metadata": {"resolution": resolution, "ratio": ratio},
        }
        resp = requests.post(f"{BASE_URL}/v1/video/generations", json=payload, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()["task_id"]


    def poll_task(task_id: str, interval: int = 5, timeout: int = 600) -> dict:
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
        task_id = submit_video("城市夜景延时摄影，霓虹灯倒映在雨后街道")
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
        "model": "seedance-2.0",
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
        "model": "seedance-2.0",
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
        "model": "seedance-2.0",
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
        "model": "seedance-2.0",
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

### B. 创意视频

适用于社交媒体、短视频创作，强调动作控制与风格统一。

#### 首尾帧控制

指定首尾帧，让角色完成从"惊讶"到"开怀大笑"的过渡。

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/video/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "seedance-2.0",
        "prompt": "角色表情从惊讶迅速变为灿烂的笑容，光影自然过渡",
        "duration": 5,
        "metadata": {
          "resolution": "720p",
          "ratio": "9:16",
          "content": [
            {
              "type": "image_url",
              "role": "first_frame",
              "image_url": { "url": "https://example.com/surprised.jpg" }
            },
            {
              "type": "image_url",
              "role": "last_frame",
              "image_url": { "url": "https://example.com/happy.jpg" }
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
        "model": "seedance-2.0",
        "prompt": "角色表情从惊讶迅速变为灿烂的笑容，光影自然过渡",
        "duration": 5,
        "metadata": {
            "resolution": "720p",
            "ratio": "9:16",
            "content": [
                {
                    "type": "image_url",
                    "role": "first_frame",
                    "image_url": {"url": "https://example.com/surprised.jpg"}
                },
                {
                    "type": "image_url",
                    "role": "last_frame",
                    "image_url": {"url": "https://example.com/happy.jpg"}
                }
            ]
        }
    }

    resp = requests.post(f"{BASE_URL}/v1/video/generations", json=payload, headers=HEADERS)
    print(resp.json())
    ```

#### 视频换风格

基于现有视频的运动轨迹，替换场景风格。

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/video/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "seedance-2.0",
        "prompt": "保持原视频的运镜轨迹，将原本的现代街道改为1920年代的复古老上海街头，黄包车、老式路灯，黑白色调",
        "duration": 5,
        "metadata": {
          "resolution": "720p",
          "ratio": "16:9",
          "content": [
            {
              "type": "video_url",
              "role": "reference_video",
              "video_url": { "url": "https://example.com/modern_street.mp4" }
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
        "model": "seedance-2.0",
        "prompt": "保持原视频的运镜轨迹，将原本的现代街道改为1920年代的复古老上海街头，黄包车、老式路灯，黑白色调",
        "duration": 5,
        "metadata": {
            "resolution": "720p",
            "ratio": "16:9",
            "content": [
                {
                    "type": "video_url",
                    "role": "reference_video",
                    "video_url": {"url": "https://example.com/modern_street.mp4"}
                }
            ]
        }
    }

    resp = requests.post(f"{BASE_URL}/v1/video/generations", json=payload, headers=HEADERS)
    print(resp.json())
    ```

#### 视频转动漫

利用参考视频锁定动作，通过 prompt 改变全局渲染风格。

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/video/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "seedance-2.0",
        "prompt": "将视频转换为宫崎骏动漫风格，清新明亮的色彩，手绘笔触，天空中飘着大朵的白云",
        "duration": 5,
        "metadata": {
          "resolution": "720p",
          "ratio": "16:9",
          "content": [
            {
              "type": "video_url",
              "role": "reference_video",
              "video_url": { "url": "https://example.com/hiking_video.mp4" }
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
        "model": "seedance-2.0",
        "prompt": "将视频转换为宫崎骏动漫风格，清新明亮的色彩，手绘笔触，天空中飘着大朵的白云",
        "duration": 5,
        "metadata": {
            "resolution": "720p",
            "ratio": "16:9",
            "content": [
                {
                    "type": "video_url",
                    "role": "reference_video",
                    "video_url": {"url": "https://example.com/hiking_video.mp4"}
                }
            ]
        }
    }

    resp = requests.post(f"{BASE_URL}/v1/video/generations", json=payload, headers=HEADERS)
    print(resp.json())
    ```

---

### C. 建筑装修

适用于建筑设计、室内装修的效果展示。

#### 效果图动效

让静态的建筑渲染图"活"起来，模拟黄昏到夜晚的灯光切换。

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/video/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "seedance-2.0",
        "prompt": "镜头缓慢推向别墅，时间从黄昏变为夜晚，窗户内的灯光依次亮起，水池倒影波动",
        "duration": 5,
        "metadata": {
          "resolution": "1080p",
          "ratio": "16:9",
          "content": [
            {
              "type": "image_url",
              "role": "first_frame",
              "image_url": { "url": "https://example.com/villa_day.jpg" }
            },
            {
              "type": "image_url",
              "role": "last_frame",
              "image_url": { "url": "https://example.com/villa_night.jpg" }
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
        "model": "seedance-2.0",
        "prompt": "镜头缓慢推向别墅，时间从黄昏变为夜晚，窗户内的灯光依次亮起，水池倒影波动",
        "duration": 5,
        "metadata": {
            "resolution": "1080p",
            "ratio": "16:9",
            "content": [
                {
                    "type": "image_url",
                    "role": "first_frame",
                    "image_url": {"url": "https://example.com/villa_day.jpg"}
                },
                {
                    "type": "image_url",
                    "role": "last_frame",
                    "image_url": {"url": "https://example.com/villa_night.jpg"}
                }
            ]
        }
    }

    resp = requests.post(f"{BASE_URL}/v1/video/generations", json=payload, headers=HEADERS)
    print(resp.json())
    ```

---

### D. 高级用法

#### 多素材编排

综合利用视频参考、多图片参考及音频同步生成。

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/video/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "seedance-2.0",
        "prompt": "使用[视频1]的奔跑动作，角色穿着[图片1]中的盔甲，在[图片2]的冰原背景中穿行，伴随厚重的脚步声和风雪声",
        "duration": 10,
        "metadata": {
          "resolution": "720p",
          "ratio": "16:9",
          "content": [
            {
              "type": "video_url",
              "role": "reference_video",
              "video_url": { "url": "https://example.com/run_cycle.mp4" }
            },
            {
              "type": "image_url",
              "role": "reference_image",
              "image_url": { "url": "https://example.com/armor.jpg" }
            },
            {
              "type": "image_url",
              "role": "reference_image",
              "image_url": { "url": "https://example.com/ice_field.png" }
            },
            {
              "type": "audio_url",
              "role": "reference_audio",
              "audio_url": { "url": "https://example.com/footsteps_wind.mp3" }
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
        "model": "seedance-2.0",
        "prompt": "使用[视频1]的奔跑动作，角色穿着[图片1]中的盔甲，在[图片2]的冰原背景中穿行，伴随厚重的脚步声和风雪声",
        "duration": 10,
        "metadata": {
            "resolution": "720p",
            "ratio": "16:9",
            "content": [
                {
                    "type": "video_url",
                    "role": "reference_video",
                    "video_url": {"url": "https://example.com/run_cycle.mp4"}
                },
                {
                    "type": "image_url",
                    "role": "reference_image",
                    "image_url": {"url": "https://example.com/armor.jpg"}
                },
                {
                    "type": "image_url",
                    "role": "reference_image",
                    "image_url": {"url": "https://example.com/ice_field.png"}
                },
                {
                    "type": "audio_url",
                    "role": "reference_audio",
                    "audio_url": {"url": "https://example.com/footsteps_wind.mp3"}
                }
            ]
        }
    }

    resp = requests.post(f"{BASE_URL}/v1/video/generations", json=payload, headers=HEADERS)
    print(resp.json())
    ```

#### 资产库引用

对于仿真人场景，为满足安全合规要求，建议先将人物素材上传至资产库，再通过资产 ID 引用。直接使用外部 URL 可能触发安全过滤。

!!! warning
    若直接使用外部 URL 传递仿真人图片，系统可能拦截并提示：`The request failed because the input image may contain real person`。请务必先通过管理后台上传资产，获取资产 ID 后再调用。

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/video/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "seedance-2.0",
        "prompt": "参考[图片1]生成连贯的视频，女孩微笑着看向镜头，背景是繁华的都市街道",
        "duration": 10,
        "metadata": {
          "resolution": "720p",
          "ratio": "9:16",
          "content": [
            {
              "type": "image_url",
              "role": "first_frame",
              "image_url": { "url": "asset://asset-20260511104758-spszr" }
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
        "model": "seedance-2.0",
        "prompt": "参考[图片1]生成连贯的视频，女孩微笑着看向镜头，背景是繁华的都市街道",
        "duration": 10,
        "metadata": {
            "resolution": "720p",
            "ratio": "9:16",
            "content": [
                {
                    "type": "image_url",
                    "role": "first_frame",
                    # 使用资产 ID 格式：asset://<ID>
                    "image_url": {"url": "asset://asset-20260511104758-spszr"}
                }
            ]
        }
    }

    resp = requests.post(f"{BASE_URL}/v1/video/generations", json=payload, headers=HEADERS)
    print(resp.json())
    ```

#### 视频续写

基于已有视频素材，向后延续 5–10 秒的内容，保持角色与环境的逻辑连贯。

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/video/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "seedance-2.0",
        "prompt": "视频中的角色继续向前走，穿过一道传送门，进入一个充满未来感的实验室",
        "duration": 5,
        "metadata": {
          "resolution": "720p",
          "ratio": "16:9",
          "content": [
            {
              "type": "video_url",
              "role": "reference_video",
              "video_url": { "url": "https://example.com/segment_1.mp4" }
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
        "model": "seedance-2.0",
        "prompt": "视频中的角色继续向前走，穿过一道传送门，进入一个充满未来感的实验室",
        "duration": 5,
        "metadata": {
            "resolution": "720p",
            "ratio": "16:9",
            "content": [
                {
                    "type": "video_url",
                    "role": "reference_video",
                    "video_url": {"url": "https://example.com/segment_1.mp4"}
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
- **超时建议**：Seedance 2.0 通常需要 3–5 分钟，建议设置至少 600 秒超时
- **1080p 分辨率**：仅 Seedance 2.0 支持，Seedance Fast 最高 720p
- **首尾帧**：`first_frame` 与 `last_frame` 必须同时提供，且两张图片的宽高比需一致
- **仿真人素材**：建议通过资产库上传后使用 `asset://<ID>` 引用，避免安全过滤
- **`metadata.content` 优先级**：参考图/视频必须放在 `metadata.content` 内，不要与顶层 `images` 字段混用
- **竖屏视频**：使用 `ratio: "9:16"`
