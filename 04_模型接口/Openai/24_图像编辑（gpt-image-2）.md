# 图像编辑（gpt-image-2）

原图（支持 PNG/JPEG/WebP/GIF），可**同名多次**传入 1-6 张参考图

maskfile 可选可选 mask，**必须 PNG 或 WebP**（需 alpha 通道）。透明区 = 需要重绘，不透明区 = 保持原样

sizestring 可选auto（默认，模型自选）1024x1024、1536x1024、1024x1536、2048x2048、2048x1152、3840x2160、2160x3840

qualitystring 可选low（快，推荐草稿）/ medium / high（实际质量由 Codex 上游决定，可能降级）/ auto（默认）

backgroundstring 可选auto（默认）/ opaque。不支持 transparent，传入会被 Codex 拒绝

ninteger 可选要生成的图像数。必须介于 1 和 10 之间。

response_formatstring 可选b64_json/ url

streamstring 可选true / 1/ yes/ on → 走 SSE

instructionsstring 可选system prompt

output_formatstring 可选png / jpeg / webp

output_compressionstring 0-100可选partial_imagesstring 仅流式可选moderationstring 可选auto / low

input_fidelitystring 可选参考图保真度（Codex 扩展字段）

## 返回响应
🟢200成功application/json生成代码Body生成代码createinteger 必需dataarray[string]必需请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/v1/images/edits' \
--header 'Accept: application/json' \
--header 'Authorization;' \
--form 'model="gpt-image-2"' \
--form 'prompt="提示词"' \
--form 'image=@""'
```
响应示例响应示例
```
{
    "created": 1776935730,
    "data": [
        {
            "url": "https://oss.filenest.top/uploads/3fe1f778-9aa6-469c-b69f-a8897243c740.png"
        }
    ],
    "usage": {
        "total_tokens": 1140,
        "input_tokens": 580,
        "output_tokens": 560,
        "input_tokens_details": {
            "text_tokens": 20,
            "image_tokens": 560
        }
    }
}
```