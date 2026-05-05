# 图片融合（Blend）

执行Blend操作，提交融图任务。

## 请求参数
Header 参数生成代码Acceptstring 必需示例:application/jsonAuthorizationstring 必需示例:sk-Content-Typestring 必需示例:application/jsonBody 参数application/json必填生成代码botTypestring 可选base64Arrayarray[string]必需垫图base64数组

dimensionsstring 必需比例: PORTRAIT(2:3); SQUARE(1:1); LANDSCAPE(3:2)
枚举值:PORTRAIT SQUARE LANDSCAPE
示例值:SQUARE

accountFilterobject 可选channelIdstring 频道ID
可选instanceIdstring 账号实例ID
可选modesstring 账号模式
可选remarkstring 备注可选remixstring 账号是否remix可选remixAutoConsideredstring 可选账号过滤时，remix自动提交 视为 账号的remix为false

notifyHookstring 可选statestring 可选示例
## 返回响应
🟢200成功application/json生成代码Body生成代码codeinteger 可选descriptionstring 可选propertiesobject 可选resultstring 可选请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/mj/submit/blend' \
--header 'Accept: application/json' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "mode": "RELAX",
    "base64Array": [
        "data:image/png;base64,xxx1",
        "data:image/png;base64,xxx2"
    ],
    "dimensions": "SQUARE"
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