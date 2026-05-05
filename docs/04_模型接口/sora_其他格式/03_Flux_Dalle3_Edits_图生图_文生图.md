# Flux(Dalle3 Edits(图生图&amp;文生图))

仅支持 flux-kontext pro、max ，支持多图参考

## 请求参数
Header 参数生成代码Acceptstring 必需示例:application/jsonAuthorizationstring 必需示例:sk-Content-Typestring 必需示例:application/jsonBody 参数application/json必填生成代码promptstring 可选string
可选
示例值:
带上眼镜

modelstring 可选string
可选
示例值:
flux-kontext-pro

sizestring 可选string
可选
最终会转换成比例，建议直接使用 aspect_ratio
示例值:
1024x1024

aspect_ratiostring 可选string
可选
21:9, 16:9, 4:3, 3:2, 1:1, 2:3, 3:4, 9:16, 9:21
示例值:
1:1

imagestring 可选file
可选
参考图片，支持多个

示例
## 返回响应
🟢200成功application/json生成代码Body生成代码object 请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/v1/images/edits' \
--header 'Accept: application/json' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "prompt": "string",
    "model": "string",
    "size": "string",
    "aspect_ratio": "string",
    "image": "string"
}'
```
响应示例响应示例
```
{}
```