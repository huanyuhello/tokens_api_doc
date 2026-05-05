# 图生文（Describe）

执行Describe操作，提交图生文任务。

## 请求参数
Header 参数生成代码Acceptstring 必需示例:application/jsonAuthorizationstring 必需示例:sk-Content-Typestring 必需示例:application/jsonBody 参数application/json必填生成代码botTypestring 可选base64string 图片base64必需dimensionsstring 必需比例: PORTRAIT(2:3); SQUARE(1:1); LANDSCAPE(3:2)
枚举值:PORTRAIT SQUARE LANDSCAPE
示例值:SQUARE

accountFilterobject 可选channelIdstring 频道ID可选instanceIdstring 账号实例ID可选modesarray[string]账号模式必需remarkstring 备注可选remixstring 账号是否remix可选remixAutoConsideredboolean 可选账号过滤时，remix自动提交 视为 账号的remix为false

notifyHookstring 可选statestring 可选示例
## 返回响应
🟢200成功application/json生成代码Body生成代码codeinteger 可选descriptionstring 可选propertiesobject 可选resultstring 可选请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/mj/submit/describe' \
--header 'Accept: application/json' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "mode": "RELAX",
    "base64": "data:image/png;base64,xxx"
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