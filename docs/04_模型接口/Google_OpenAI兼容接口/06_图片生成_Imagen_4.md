# 图片生成 / Imagen 4

Gemini 绘图和视频生成指引
​
Imagen 绘图
Imagen 是 Google 推出的先进图像生成 AI 模型系列，能够根据文本提示创建高质量、逼真的图像。本指南将帮助您了解如何使用 Imagen 系列 API 生成图像，包括参数设置、模型选择和代码示例。
可用模型列表：
imagen-4.0-generate-preview-05-20：最新的正式预览版
imagen-4.0-ultra-generate-exp-05-20：更高级的 4.0 实验款
imagen-3.0-generate-002：3.0 正式版
目前 Imagen 仅支持英文提示词（prompt），集成时建议增加自动翻译，让用户能够无障碍使用
绘制大量文本的表现不稳定，建议只绘制重点关键词
抢先体验期间，Imagen 系列模型同价，后续可能会按官方正式价格调整。
模型参数
Imagen 目前仅支持英文提示词，并提供以下参数：
numberOfImages: 要生成的图像数量，范围从 1 到 4（含）。默认值为 4。另外注意 imagen-4.0-ultra-generate-exp-05-20 单次只能生成 1 张。
aspectRatio: 更改生成图像的宽高比。支持的值有 “1:1”、“3:4”、“4:3”、“9:16” 和 “16:9”。默认值为 “1:1”。
personGeneration: 允许模型生成人物图像。支持以下值：
“DONT_ALLOW”: 阻止生成人物图像。
“ALLOW_ADULT”: 生成成人图像，但不生成儿童图像。这是默认值。

## 请求参数
Header 参数生成代码
### 

- 
- 
- 
Body 参数application/json生成代码
### 

- 
- 
- 
示例
## 返回响应
🟢200成功application/json生成代码Body生成代码
### 

- 
- 
- 
请求示例请求示例ShellJavaScriptJavaSwiftcURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST &#x27;http://47.102.134.41:3000/v1/images/generations&#x27; \
--header &#x27;Accept: application/json&#x27; \
--header &#x27;Authorization: sk-&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data-raw &#x27;{
    "model": "imagen-4.0-generate-preview-06-06",
    "prompt": "a portrait of a sheepadoodle wearing a cape",
    "response_format": "b64_json",
    "n": 1
}&#x27;
```
响应示例响应示例
```
{
    "id": "string",
    "object": "string",
    "created": 0,
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "string",
                "content": "string"
            },
            "finish_reason": "string"
        }
    ],
    "usage": {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0
    }
}
```