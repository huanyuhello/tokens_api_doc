# 创建视频任务 Copy

枚举值:
sora-2
sora-2-hd
示例值:
sora_video2

promptstring 可选示例值:
画面动起来

secondsstring 可选string
可选
只允许设置这三个值：10、15、25，其他值无效。并且25s需要sora-2-pro才有效
示例值:
10

input_referenceinteger 必需图片
可选
示例值:
file:///Users/xiangsx/Downloads/RHTtTcBrlY5wGxop9ux8DqRckyIKxd.png

sizestring 可选
enum
可选
宽x高，会忽略具体数据 宽>高 为横屏，宽watermarkboolean 可选boolean
可选
是否需要水印，不传默认无水印（测试中）
示例值:
false

示例
## 返回响应
🟢200成功application/json生成代码Body生成代码object 请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/v1/videos' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model": "reprehenderit ut dolore adipisicing",
    "prompt": "amet sunt ea eu tempor",
    "seconds": "velit",
    "input_reference": "eiusmod est",
    "size": "voluptate in tempor ea magna",
    "watermark": false
}'
```
响应示例响应示例
```
{
    "id": "sora-2:task_01k7e89xwmfr1vjp42w574zbdb",
    "object": "video",
    "model": "sora-2",
    "status": "queued",
    "progress": 0,
    "created_at": 1760341326742,
    "seconds": "10"
}
```