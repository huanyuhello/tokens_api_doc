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
--header &#x27;Authorization: sk-&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data-raw &#x27;{
    "model": "flux-kontext-pro",
    "prompt": "a beautiful landscape with a river and mountains",
    "size": "1024x1024"
}&#x27;
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