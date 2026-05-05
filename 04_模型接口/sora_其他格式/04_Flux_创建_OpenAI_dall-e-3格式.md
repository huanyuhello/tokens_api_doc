# Flux 创建（OpenAI dall-e-3格式）

图片
给定提示和/或输入图像，模型将生成新图像。
相关指南：图像生成
根据提示创建图像。

## 请求参数
Authorization在 Header 添加参数 Authorization，其值为在 Bearer 之后拼接 Token示例：`Authorization: Bearer ********************`Header 参数生成代码
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
--header &#x27;Authorization: Bearer &#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data-raw &#x27;{
    "model": "flux-kontext-pro",
    "prompt": "a beautiful landscape with a river and mountains",
    // "size": "1024x1524",
    "n": 1,
    "aspect_ratio": "21:9"
}&#x27;
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