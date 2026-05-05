# flux-kontext-pro / OpenAI兼容接口

Flux AI 文生图模型，效果堪比 Midjourney，碾压 StableDiffusion；生成图片接口
size 支持
1024x512
1024x1024
1024x576
1024x768
1024x512
512x1024
512x768
1280x960
1280x960
960x1280
960x1280
768x1366
768x512
1366x768
1344x576

## 请求参数
Header 参数生成代码Authorizationstring 必需示例:sk-Body 参数application/json必填生成代码promptstring 必需所需图像的文本描述。最大长度为 1000 个字符。

nstring 必需要生成的图像数。必须介于 1 和 10 之间。

sizestring 必需生成图像的大小。必须是256x256、512x512或 1024x1024之一。

示例
## 返回响应
🟢200成功application/json生成代码Body生成代码object 请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/v1/images/generations' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model": "flux-kontext-pro",
    "prompt": "a beautiful landscape with a river and mountains",
    "size": "1024x1024"
}'
```
响应示例响应示例
```
{
    "created": 1589478378,
    "data": [
        {
            "url": "https://..."
        },
        {
            "url": "https://..."
        }
    ]
}
```