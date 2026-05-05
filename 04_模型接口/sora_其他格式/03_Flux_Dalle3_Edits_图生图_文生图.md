# Flux(Dalle3 Edits(图生图&amp;文生图))

仅支持 flux-kontext pro、max ，支持多图参考

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
curl --location --request POST &#x27;http://47.102.134.41:3000/v1/images/edits&#x27; \
--header &#x27;Accept: application/json&#x27; \
--header &#x27;Authorization: sk-&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data-raw &#x27;{
    "prompt": "string",
    "model": "string",
    "size": "string",
    "aspect_ratio": "string",
    "image": "string"
}&#x27;
```
响应示例响应示例
```
{}
```