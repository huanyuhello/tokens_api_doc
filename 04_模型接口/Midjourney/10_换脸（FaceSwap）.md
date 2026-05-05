# 换脸（FaceSwap）

提交FaceSwap任务，进行换脸操作。

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
curl --location --request POST &#x27;http://47.102.134.41:3000/mj/insight-face/swap&#x27; \
--header &#x27;Accept: application/json&#x27; \
--header &#x27;Authorization: sk-&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data-raw &#x27;{
    "mode": "RELAX",
    "sourceBase64": "data:image/png;base64,xxx1",
    "targetBase64": "data:image/png;base64,xxx2"
}&#x27;
```
响应示例响应示例
```
{
    "code": 0,
    "description": "string",
    "result": "string"
}
```