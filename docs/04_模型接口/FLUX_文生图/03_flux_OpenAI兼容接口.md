# flux / OpenAI兼容接口

image_size Available options: 1024x1024, 512x1024, 768x512, 768x1024, 1024x576, 576x1024
seed Required range: 0 < x < 9999999999
prompt_enhancement: default: false(Rewrite prompts into detailed, model-friendly versions when switched on.)

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
    "model": "black-forest-labs/flux-schnell",
    "prompt": "black forest gateau cake spelling out the words \"FLUX SCHNELL\", tasty, food photography, dynamic shot",
    "go_fast": true,
    "num_outputs": 1,
    "aspect_ratio": "1:1",
    "output_format": "webp",
    "output_quality": 80
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