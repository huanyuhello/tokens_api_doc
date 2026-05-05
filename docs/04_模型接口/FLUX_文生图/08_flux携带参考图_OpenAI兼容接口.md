# flux携带参考图 / OpenAI兼容接口

仅部分模型支持 图片 参考
例如：
seededit
flux-kontext

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
    "prompt": "https://replicate.delivery/pbxt/N55l5TWGh8mSlNzW8usReoaNhGbFwvLeZR3TX1NL4pd2Wtfv/replicate-prediction-f2d25rg6gnrma0cq257vdw2n4c.png Make this a 90s cartoon",
    "n": 1,
    "model": "flux-kontext-pro",
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