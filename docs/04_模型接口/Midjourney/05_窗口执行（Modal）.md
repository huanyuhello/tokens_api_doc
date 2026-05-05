# 窗口执行（Modal）

当执行其他任务，code返回21时，需要执行modal接口，传入新的提示词用来修改细节。

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
curl --location --request POST &#x27;http://47.102.134.41:3000/mj/submit/modal&#x27; \
--header &#x27;Accept: application/json&#x27; \
--header &#x27;Authorization: sk-&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data-raw &#x27;{
    "maskBase64": "data:image/png;base64,xxx1",
    "prompt": "Cat",
    "taskId": "1712204995849324"
}&#x27;
```
响应示例响应示例
```
{
    "code": 1,
    "description": "提交成功",
    "properties": {},
    "result": 1320098173412546
}
```