# flux / OpenAI兼容接口

image_size Available options: 1024x1024, 512x1024, 768x512, 768x1024, 1024x576, 576x1024
seed Required range: 0 < x < 9999999999
prompt_enhancement: default: false(Rewrite prompts into detailed, model-friendly versions when switched on.)

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
    "model": "black-forest-labs/flux-schnell",
    "prompt": "black forest gateau cake spelling out the words \"FLUX SCHNELL\", tasty, food photography, dynamic shot",
    "go_fast": true,
    "num_outputs": 1,
    "aspect_ratio": "1:1",
    "output_format": "webp",
    "output_quality": 80
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