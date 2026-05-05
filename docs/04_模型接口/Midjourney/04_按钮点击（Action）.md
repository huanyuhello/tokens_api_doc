# 按钮点击（Action）

该接口是用于点击图片下方的按钮，customId通过任务查询接口可以获取到。

## 请求参数
Header 参数生成代码Acceptstring 必需示例:application/jsonAuthorizationstring 必需示例:sk-Content-Typestring 必需示例:application/jsonBody 参数application/json必填生成代码是否选择同一频道下的账号，默认只使用任务关联的账号chooseSameChannelboolean 可选customIdstring 动作标识
必需taskIdstring 任务ID
必需accountFilterobject 可选channelIdstring 频道ID
可选instanceIdstring 账号实例ID
可选modesarray[string]账号模式可选remarkstring 备注可选remixboolean 账号是否remix可选remixAutoConsideredboolean 可选账号过滤时，remix自动提交 视为 账号的remix为false

notifyHookstring 可选回调地址, 为空时使用全局notifyHook

statestring 自定义参数
可选示例
## 返回响应
🟢200成功application/json生成代码Body生成代码codeinteger 可选descriptionstring 可选propertiesobject 可选resultstring 可选请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/mj/submit/action' \
--header 'Accept: application/json' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "customId": "MJ::JOB::upsample::1::0bc41848-dc7f-42f9-893c-9c33b00ebdf3",
    "taskId": "1734937261701345"
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