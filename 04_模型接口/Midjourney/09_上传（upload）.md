# 上传（upload）

提交FaceSwap任务，进行换脸操作。

## 请求参数
Header 参数生成代码Acceptstring 必需示例:application/jsonAuthorizationstring 必需示例:sk-Content-Typestring 必需示例:application/jsonBody 参数application/json必填生成代码base64Arrayarray[string]base64数组必需filterobject 必需channelIdstring 频道ID必需instanceIdstring 账号实例ID必需remarkstring 备注包含必需示例
## 返回响应
🟢200成功application/json生成代码Body生成代码codeinteger 可选descriptionstring 可选resultstring 可选请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/mj/submit/upload-discord-images' \
--header 'Accept: application/json' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "mode": "RELAX",
    "sourceBase64": "data:image/png;base64,xxx1",
    "targetBase64": "data:image/png;base64,xxx2"
}'
```
响应示例响应示例
```
{
    "code": 0,
    "description": "string",
    "result": [
        "string"
    ]
}
```