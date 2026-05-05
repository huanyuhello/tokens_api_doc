# stable-diffusion / OpenAI兼容接口

image_size Available options: 1024x1024, 512x1024, 768x512, 768x1024, 1024x576, 576x1024
batch_size Required range: 1 < x < 4
num_inference_steps Required range: 1 < x < 100
guidance_scale Required range: 0 < x < 100
seed Required range: 0 < x < 9999999999

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
    "model": "stable-diffusion-api",
    "messages": [
        {
            "role": "user",
            "content": "striking poses, stunning backdrop of rocky coastline and golden hour lighting, fashion-forward wardrobe, eye-catching accessories, warm and inviting color palette, sharp and detailed digital rendering, stunning high definition finish, on eye level, scenic, masterpiece"
        }
    ]
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