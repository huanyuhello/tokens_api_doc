# 窗口执行（Modal）

当执行其他任务，code返回21时，需要执行modal接口，传入新的提示词用来修改细节。

## 请求参数
Header 参数生成代码Acceptstring 必需示例:application/jsonAuthorizationstring 必需示例:sk-Content-Typestring 必需示例:application/jsonBody 参数application/json必填生成代码maskBase64string 可选局部重绘的蒙版base64

promptstring 提示词可选taskIdstring 任务ID必需示例
## 返回响应
🟢200成功application/json生成代码Body生成代码codeinteger 必需状态码: 1(提交成功), 22(排队中), other(错误)

descriptionstring 描述必需propertiesobject 扩展字段
可选resultstring 任务ID
可选请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/mj/submit/modal' \
--header 'Accept: application/json' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "maskBase64": "data:image/png;base64,xxx1",
    "prompt": "Cat",
    "taskId": "1712204995849324"
}'
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