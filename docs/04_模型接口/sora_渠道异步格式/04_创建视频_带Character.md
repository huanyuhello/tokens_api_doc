# 创建视频(带 Character)

默认值:
{{Authorization}}

Body 参数application/x-www-form-urlencoded必填生成代码modelfile 必需
enum
必需
枚举值:
sora-2
sora-2-hd
示例:sora-2promptstring 画面动起来必需secondsstring 10可选input_referencestring 可选示例:file:///Users/xiangsx/Downloads/RHTtTcBrlY5wGxop9ux8DqRckyIKxd.pngsizestring 可选
宽x高，会忽略具体数据 宽>高 为横屏，宽示例:16x9watermarkstring 可选是否需要水印，不传默认无水印

示例:trueprivatestring 可选是否隐藏视频，true-视频不会发布，同时视频无法进行 remix(二次编辑)， 默认为 false

示例:falsecharacter_urlstring 可选创建角色需要的视频链接，注意视频中一定不能出现真人，否则会失败

示例:https://filesystem.site/cdn/20251030/javYrU4etHVFDqg8by7mViTWHlMOZy.mp4character_timestampsstring 可选视频角色出现的秒数范围，格式 {start},{end}, 注意 end-start 的范围 1～3秒

示例:1,3character_from_taskstring 可选已完成的任务 id,可以根据已经生成的任务 id，来创建角色

## 返回响应
🟢200成功application/json生成代码Body生成代码object 请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/v1/videos' \
--header 'Authorization: Bearer ' \
--data-urlencode 'model=sora-2' \
--data-urlencode 'prompt=' \
--data-urlencode 'seconds=' \
--data-urlencode 'input_reference=file:///Users/xiangsx/Downloads/RHTtTcBrlY5wGxop9ux8DqRckyIKxd.png' \
--data-urlencode 'size=16x9' \
--data-urlencode 'watermark=true' \
--data-urlencode 'private=false' \
--data-urlencode 'character_url=https://filesystem.site/cdn/20251030/javYrU4etHVFDqg8by7mViTWHlMOZy.mp4' \
--data-urlencode 'character_timestamps=1,3' \
--data-urlencode 'character_from_task='
```
响应示例响应示例
```
{}
```