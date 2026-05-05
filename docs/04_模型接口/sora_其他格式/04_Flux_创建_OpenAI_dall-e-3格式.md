# Flux 创建（OpenAI dall-e-3格式）

图片
给定提示和/或输入图像，模型将生成新图像。
相关指南：图像生成
根据提示创建图像。

## 请求参数
Authorization在 Header 添加参数 Authorization，其值为在 Bearer 之后拼接 Token示例：`Authorization: Bearer ********************`Header 参数生成代码Authorizationstring 可选示例:Bearer {{YOUR_API_KEY}}Body 参数application/json必填生成代码promptstring 必需所需图像的文本描述。最大长度为 1000 个字符。

modelstring 必需用于图像生成的模型。

ninteger 必需要生成的图像数。必须介于 1 和 10 之间。

qualitystring 必需将生成的图像的质量。hd创建具有更精细细节和更高一致性的图像。此参数仅支持dall-e-3.

response_formatstring 必需返回生成的图像的格式。必须是 或url之一b64_json。

stylestring 风格必需userstring 必需生成图像的风格。必须是 或vivid之一natural。生动使模型倾向于生成超真实和戏剧性的图像。自然使模型生成更自然、不太真实的图像。此参数仅支持dall-e-3.

sizestring 必需生成图像的大小。必须是256x256、512x512或 1024x1024之一。

aspect_ratiostring 必需图片比例: 枚举值Possible enum values: 21:9, 16:9, 4:3, 3:2, 1:1, 2:3, 3:4, 9:16, 9:21

示例
## 返回响应
🟢200成功application/json生成代码Body生成代码createdinteger 必需dataobject 必需urlstring 必需请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/v1/images/generations' \
--header 'Authorization: Bearer ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model": "flux-kontext-pro",
    "prompt": "a beautiful landscape with a river and mountains",
    // "size": "1024x1524",
    "n": 1,
    "aspect_ratio": "21:9"
}'
```
响应示例响应示例
```
{
    "created": 0,
    "data": {
        "url": "string"
    }
}
```