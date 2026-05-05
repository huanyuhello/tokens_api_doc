# doubao-seedream-4-0-250828-图生图

给定提示和/或输入图像，模型将生成新图像。

## 请求参数
Header 参数生成代码
### 

- 
- 
- 
Body 参数application/json必填生成代码
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
    "model": "doubao-seedream-4-0-250828",
    "prompt": "生成狗狗趴在草地上的近景画面",
    "image": "https://ark-project.tos-cn-beijing.volces.com/doc_image/seedream4_imageToimage.png",
    "size": "1728x2304",
    "sequential_image_generation": "disabled",
    "stream": false,
    "response_format": "url",
    "watermark": true
}&#x27;
```
响应示例响应示例
```
{
    "data": [
        {
            "url": "https://ark-content-generation-v2-cn-beijing.tos-cn-beijing.volces.com/doubao-seedream-4-0/0217574690542070fa6ef8c2347680bd87fd8d357bb16f1e5ca0f_0.jpeg?X-Tos-Algorithm=TOS4-HMAC-SHA256&X-Tos-Credential=<REDACTED>&X-Tos-Date=20250910T015107Z&X-Tos-Expires=86400&X-Tos-Signature=fbc5369be594d6e21be983ed1ec32463b5f82cf0c18c4349e477c11e51e55fa0&X-Tos-SignedHeaders=host"
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