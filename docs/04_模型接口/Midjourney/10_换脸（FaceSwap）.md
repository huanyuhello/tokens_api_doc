# 换脸（FaceSwap）

提交FaceSwap任务，进行换脸操作。

## 请求参数
Header 参数生成代码Acceptstring 必需示例:application/jsonAuthorizationstring 必需示例:sk-Content-Typestring 必需示例:application/jsonBody 参数application/json必填生成代码sourceBase64string 必需人脸源图片base64

targetBase64string 必需目标图片base64

accountFilterobject 必需instanceIdstring 账号实例ID必需notifyHookstring 必需回调地址, 为空时使用全局notifyHook

statestring 自定义参数必需示例
## 返回响应
🟢200成功application/json生成代码Body生成代码codeinteger 可选descriptionstring 可选resultstring 可选请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/mj/insight-face/swap' \
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
    "result": "string"
}
```