# doubao-seedream-4-0-250828-文生图

给定提示和/或输入图像，模型将生成新图像。

## 请求参数
Header 参数生成代码Acceptstring 必需示例:application/jsonAuthorizationstring 必需示例:sk-Content-Typestring 必需示例:application/jsonBody 参数application/json必填生成代码modelstring 必需本次请求使用模型的 Model ID。

promptstring 必需用于生成图像的提示词，支持中英文。

sizestring 必需指定生成图像的尺寸信息，支持以下两种方式，不可混用。
方式1 |指定生成图像的分辨率，可选值：1K、2K、4K
方式2 |指定生成图像的宽高像素值：默认值：2048x2048
面积取值范围：[1024x1024, 4096x4096]
宽高比取值范围：[1/16, 16]

sequential_image_generationstring 必需控制是否关闭组图功能。默认值 disabled
取值范围：
auto：自动判断模式，模型会根据用户提供的提示词自主判断是否返回组图以及组图包含的图片数量。
disabled：关闭组图功能，模型只会生成一张图。

streamstring 必需控制是否开启流式输出模式。默认值 false

response_formatstring 必需指定生成图像的返回格式。默认值 url
生成的图片为 jpeg 格式，支持以下两种返回方式：
url：返回图片下载链接；链接在图片生成后24小时内有效，请及时下载图片。
b64_json：以 Base64 编码字符串的 JSON 格式返回图像数据。

watermarkstring 必需是否在生成的图片中添加水印。默认值 true
false：不添加水印。
true：在图片右下角添加“AI生成”字样的水印标识。

示例
## 返回响应
🟢200成功application/json生成代码Body生成代码object 请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/v1/images/generations' \
--header 'Accept: application/json' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model": "doubao-seedream-4-0-250828",
    "prompt": "星际穿越，黑洞，黑洞里冲出一辆快支离破碎的复古列车，抢视觉冲击力，电影大片，末日既视感，动感，对比色，oc渲染，光线追踪，动态模糊，景深，超现实主义，深蓝，画面通过细腻的丰富的色彩层次塑造主体与场景，质感真实，暗黑风背景的光影效果营造出氛围，整体兼具艺术幻想感，夸张的广角透视效果，耀光，反射，极致的光影，强引力，吞噬",
    "size": "1728x2304",
    "sequential_image_generation": "disabled",
    "stream": false,
    "response_format": "url",
    "watermark": true
}'
```
响应示例响应示例
```
{
    "data": [
        {
            "url": "https://ark-content-generation-v2-cn-beijing.tos-cn-beijing.volces.com/doubao-seedream-4-0/0217574690542070fa6ef8c2347680bd87fd8d357bb16f1e5ca0f_0.jpeg?X-Tos-Algorithm=TOS4-HMAC-SHA256&X-Tos-Credential=REDACTED&X-Tos-Date=20250910T015107Z&X-Tos-Expires=86400&X-Tos-Signature=fbc5369be594d6e21be983ed1ec32463b5f82cf0c18c4349e477c11e51e55fa0&X-Tos-SignedHeaders=host"
        }
    ],
    "created": 1757469067,
    "usage": {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 15908,
        "prompt_tokens_details": {
            "cached_tokens_details": {}
        },
        "completion_tokens_details": {},
        "output_tokens": 15908
    }
}
```