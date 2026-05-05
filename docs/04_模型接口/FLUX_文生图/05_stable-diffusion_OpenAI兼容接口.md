# stable-diffusion / OpenAI兼容接口

image_size Available options: 1024x1024, 512x1024, 768x512, 768x1024, 1024x576, 576x1024
batch_size Required range: 1 < x < 4
num_inference_steps Required range: 1 < x < 100
guidance_scale Required range: 0 < x < 100
seed Required range: 0 < x < 9999999999

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
    "model": "stable-diffusion-api",
    "messages": [
        {
            "role": "user",
            "content": "striking poses, stunning backdrop of rocky coastline and golden hour lighting, fashion-forward wardrobe, eye-catching accessories, warm and inviting color palette, sharp and detailed digital rendering, stunning high definition finish, on eye level, scenic, masterpiece"
        }
    ]
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