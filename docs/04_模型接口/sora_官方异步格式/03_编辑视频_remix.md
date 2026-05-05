# 编辑视频(remix)

string
修改视频的想法描述
必需

示例
## 返回响应
🟢200成功application/json生成代码Body生成代码object 请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/v1/videos/sora-2:task_01k76rbx40e7p9gzexm129v1z2/remix' \
--header 'Authorization: Bearer ' \
--header 'Content-Type: application/json' \
--data-raw '{
    "prompt": "让这个视频背景变成蓝天白云"
}'
```
响应示例响应示例
```
{}
```