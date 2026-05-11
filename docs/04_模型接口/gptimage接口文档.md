# GPT Image 模型接口文档

> **Base URL**：`https://tokens.smartfashionai.cn`
>
> 使用标准 OpenAI 图像接口格式，现有 OpenAI SDK 无需修改代码，只需替换 `base_url` 和 `api_key`。

---

## 支持的模型

| 模型 ID | 说明 |
|---------|------|
| `gpt-image-2` | GPT Image 2，支持文生图与图像编辑，最高 4K 分辨率 |

!!! tip "模型名称"
    调用时请在「模型广场」复制完整模型名称，名称必须完全一致。

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
| `POST` | `/v1/images/generations` | 文生图（根据提示词生成图片） |
| `POST` | `/v1/images/edits` | 图像编辑（基于参考图修改/重绘） |

---

## 一、文生图

**POST** `/v1/images/generations`

### 请求参数

**Header**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `Authorization` | string | 必需 | `Bearer <YOUR_API_KEY>` |
| `Content-Type` | string | 必需 | `application/json` |

**Body**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `model` | string | 必需 | 固定填 `gpt-image-2` |
| `prompt` | string | 必需 | 图像描述提示词，最大 1000 字符 |
| `n` | integer | 可选 | 生成图片数量，范围 1–10，默认 1 |
| `size` | string | 可选 | 图片尺寸，见下方说明，默认 `auto` |
| `quality` | string | 可选 | `auto`（默认）/ `low` / `medium` / `high` |
| `background` | string | 可选 | `auto`（默认）/ `opaque`，不支持 `transparent` |
| `response_format` | string | 可选 | `b64_json`（默认，返回 base64）/ `url`（返回图片 URL） |
| `output_format` | string | 可选 | `png`（默认）/ `jpeg` / `webp` |
| `output_compression` | integer | 可选 | jpeg/webp 压缩率，范围 0–100 |
| `stream` | boolean | 可选 | `true` 时启用 SSE 流式返回 |
| `partial_images` | integer | 可选 | 仅流式生效，非流式传入会被忽略 |
| `instructions` | string | 可选 | 系统级提示词，透传给模型，如 `"Always render in pixel art style"` |
| `moderation` | string | 可选 | `auto`（默认）/ `low` |

**size 可选值：**

| 值 | 说明 |
|----|------|
| `auto` | 模型自动选择（默认） |
| `1024x1024` | 正方形 |
| `1536x1024` | 横版 |
| `1024x1536` | 竖版 |
| `2048x2048` | 高清正方形 |
| `2048x1152` | 宽屏横版 |
| `3840x2160` | 4K 横版 |
| `2160x3840` | 4K 竖版 |

### 1.1 基础文生图

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/images/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "gpt-image-2",
        "prompt": "一只在樱花树下打盹的橘猫，水彩画风格",
        "n": 1,
        "size": "1024x1024"
      }'
    ```

=== "Python"

    ```python
    import base64
    from openai import OpenAI

    client = OpenAI(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn/v1"
    )

    response = client.images.generate(
        model="gpt-image-2",
        prompt="一只在樱花树下打盹的橘猫，水彩画风格",
        n=1,
        size="1024x1024"
    )

    # 保存 base64 图片
    image_data = base64.b64decode(response.data[0].b64_json)
    with open("output.png", "wb") as f:
        f.write(image_data)
    print("图片已保存为 output.png")
    ```

**响应示例（b64_json）：**

```json
{
  "created": 1746940000,
  "data": [
    {
      "b64_json": "/9j/4AAQSkZJRgAB..."
    }
  ]
}
```

**响应示例（url）：**

```json
{
  "created": 1746940000,
  "data": [
    {
      "url": "data:image/png;base64,/9j/4AAQSkZJRgAB..."
    }
  ]
}
```

### 1.2 高清生成

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/images/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "gpt-image-2",
        "prompt": "未来城市夜景，赛博朋克风格，霓虹灯倒映在雨后街道",
        "size": "3840x2160",
        "quality": "high",
        "output_format": "png"
      }'
    ```

=== "Python"

    ```python
    import base64
    from openai import OpenAI

    client = OpenAI(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn/v1"
    )

    response = client.images.generate(
        model="gpt-image-2",
        prompt="未来城市夜景，赛博朋克风格，霓虹灯倒映在雨后街道",
        size="2048x1152",
        quality="high",
        extra_body={
            "output_format": "webp",
            "output_compression": 85
        }
    )

    image_data = base64.b64decode(response.data[0].b64_json)
    with open("output.webp", "wb") as f:
        f.write(image_data)
    ```

### 1.3 流式生成（SSE）

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/images/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "gpt-image-2",
        "prompt": "山间云雾缭绕的古寺，中国水墨画风格",
        "stream": true,
        "partial_images": 3
      }'
    ```

=== "Python"

    ```python
    from openai import OpenAI

    client = OpenAI(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn/v1"
    )

    # 流式生成需通过 extra_body 传入 stream 和 partial_images
    response = client.images.generate(
        model="gpt-image-2",
        prompt="山间云雾缭绕的古寺，中国水墨画风格",
        extra_body={
            "stream": True,
            "partial_images": 3
        }
    )
    # 流式响应以 SSE 格式返回，最终帧 type 为 image_generation.completed
    print(response)
    ```

流式响应格式（SSE）：

```
data: {"type":"image_generation.partial","partial_image_index":0,"b64_json":"..."}

data: {"type":"image_generation.partial","partial_image_index":1,"b64_json":"..."}

data: {"type":"image_generation.completed","b64_json":"..."}

data: [DONE]
```

---

## 二、图像编辑

**POST** `/v1/images/edits`

支持基于参考图进行局部重绘或风格迁移，请求格式为 `multipart/form-data`。

### 请求参数

#### Header

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| `Authorization` | string | 必需 | `Bearer <YOUR_API_KEY>` |
| `Content-Type` | string | 必需 | `multipart/form-data` |

#### Body（multipart/form-data）

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `model` | string | 必需 | 固定填 `gpt-image-2` |
| `prompt` | string | 必需 | 编辑指令提示词 |
| `image` | file | 必需 | 原图，支持 PNG/JPEG/WebP/GIF，可同名多次传入 1–6 张参考图 |
| `mask` | file | 可选 | 遮罩图，必须为 PNG 或 WebP（需含 alpha 通道）。透明区域 = 需要重绘，不透明区域 = 保持原样 |
| `n` | integer | 可选 | 生成图片数量，范围 1–10 |
| `size` | string | 可选 | 同文生图 size 参数 |
| `quality` | string | 可选 | `auto`（默认）/ `low` / `medium` / `high` |
| `background` | string | 可选 | `auto`（默认）/ `opaque` |
| `response_format` | string | 可选 | `b64_json` / `url` |
| `output_format` | string | 可选 | `png` / `jpeg` / `webp` |
| `output_compression` | integer | 可选 | jpeg/webp 压缩率，范围 0–100 |
| `stream` | string | 可选 | `true` / `1` / `yes` / `on` 均可启用 SSE |
| `instructions` | string | 可选 | 系统级提示词 |
| `input_fidelity` | string | 可选 | 参考图保真度 |
| `moderation` | string | 可选 | `auto`（默认）/ `low` |

### 2.1 基础图像编辑

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/images/edits" \
      -H "Authorization: Bearer $API_KEY" \
      -F "model=gpt-image-2" \
      -F "prompt=将背景替换为日落时分的海滩" \
      -F "image=@/path/to/original.png"
    ```

=== "Python"

    ```python
    import base64
    from openai import OpenAI

    client = OpenAI(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn/v1"
    )

    with open("original.png", "rb") as image_file:
        response = client.images.edit(
            model="gpt-image-2",
            image=image_file,
            prompt="将背景替换为日落时分的海滩",
            size="1024x1024"
        )

    image_data = base64.b64decode(response.data[0].b64_json)
    with open("edited.png", "wb") as f:
        f.write(image_data)
    print("编辑后图片已保存为 edited.png")
    ```

### 2.2 局部重绘（带 mask）

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/images/edits" \
      -H "Authorization: Bearer $API_KEY" \
      -F "model=gpt-image-2" \
      -F "prompt=在透明区域添加一只白色的猫" \
      -F "image=@/path/to/original.png" \
      -F "mask=@/path/to/mask.png"
    ```

=== "Python"

    ```python
    import base64
    from openai import OpenAI

    client = OpenAI(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn/v1"
    )

    with open("original.png", "rb") as image_file, \
         open("mask.png", "rb") as mask_file:
        response = client.images.edit(
            model="gpt-image-2",
            image=image_file,
            mask=mask_file,
            prompt="在透明区域添加一只白色的猫",
            size="1024x1024"
        )

    image_data = base64.b64decode(response.data[0].b64_json)
    with open("inpainted.png", "wb") as f:
        f.write(image_data)
    ```

!!! note "mask 说明"
    mask 图片中透明（alpha=0）的区域会被重新生成，不透明区域保持原图不变。mask 尺寸必须与原图一致。

### 2.3 多参考图融合

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/images/edits" \
      -H "Authorization: Bearer $API_KEY" \
      -F "model=gpt-image-2" \
      -F "prompt=将两张图片的风格融合，生成统一风格的新图" \
      -F "image=@/path/to/image1.png" \
      -F "image=@/path/to/image2.png"
    ```

=== "Python"

    ```python
    import base64
    from openai import OpenAI

    client = OpenAI(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn/v1"
    )

    with open("image1.png", "rb") as f1, open("image2.png", "rb") as f2:
        response = client.images.edit(
            model="gpt-image-2",
            image=[f1, f2],
            prompt="将两张图片的风格融合，生成统一风格的新图"
        )

    image_data = base64.b64decode(response.data[0].b64_json)
    with open("merged.png", "wb") as f:
        f.write(image_data)
    ```

---

## 三、批量生成多张图片

=== "cURL"

    ```bash
    curl -X POST "https://tokens.smartfashionai.cn/v1/images/generations" \
      -H "Authorization: Bearer $API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "gpt-image-2",
        "prompt": "极简风格的产品展示图，白色背景，专业摄影",
        "n": 4,
        "size": "1024x1024",
        "quality": "medium"
      }'
    ```

=== "Python"

    ```python
    import base64
    from openai import OpenAI

    client = OpenAI(
        api_key="your_api_key_here",
        base_url="https://tokens.smartfashionai.cn/v1"
    )

    response = client.images.generate(
        model="gpt-image-2",
        prompt="极简风格的产品展示图，白色背景，专业摄影",
        n=4,
        size="1024x1024",
        quality="medium"
    )

    for i, image in enumerate(response.data):
        image_data = base64.b64decode(image.b64_json)
        with open(f"output_{i+1}.png", "wb") as f:
            f.write(image_data)
        print(f"图片 {i+1} 已保存")
    ```

---

## 四、注意事项

- **模型名称**：调用时请从「模型广场」复制完整模型 ID，名称必须完全一致
- **图片格式**：生成接口支持输出 `png` / `jpeg` / `webp`；编辑接口输入支持 PNG/JPEG/WebP/GIF
- **mask 要求**：mask 图片必须为 PNG 或 WebP 格式，且包含 alpha 通道，尺寸需与原图完全一致
- **background 参数**：不支持 `transparent`，传入会被拒绝，请使用 `auto` 或 `opaque`
- **流式输出**：设置 `stream: true` 后，响应以 SSE 格式返回，可通过 `partial_images` 控制中间帧数量
- **response_format**：默认返回 `b64_json`（base64 编码），设为 `url` 时返回的 URL 格式为 `data:image/png;base64,...`
- **多参考图**：图像编辑接口支持同时传入 1–6 张参考图，模型会综合参考图内容进行生成
