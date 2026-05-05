# 编辑图片（Edit）

执行edit接口，可以编辑外部传入的图片，可以进行局部重绘，也可以直接改图

## 请求参数
Header 参数生成代码Acceptstring 必需示例:application/jsonAuthorizationstring 必需示例:sk-Content-Typestring 必需示例:application/jsonBody 参数application/json必填生成代码actionstring 必需固定 "EDITS"

promptstring 提示词必需base64Arrayarray[string]必需目标图片base64

maskBase64string 必需蒙版图（Base64，黑白/透明区域作为编辑区域）

notifyHookstring 可选回调地址, 为空时使用全局notifyHook

statestring 自定义参数可选remixboolean 可选示例
## 返回响应
🟢200成功application/json生成代码Body生成代码object 请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/mj/submit/edits' \
--header 'Accept: application/json' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "action": "EDITS",
    "prompt": "将图片转为吉卜力风格",
    "maskBase64": "data:image/png;base64,iVBORw0KGgoAAAAlFTkSuQmCC",
    "base64Array": [
        "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSQ=="
    ]
}'
```
响应示例响应示例
```
{}
```