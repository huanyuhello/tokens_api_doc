# /fal-ai/nano-banana 文生图

官方文档: [https://fal.ai/models/fal-ai/nano-banana](https://fal.ai/models/fal-ai/nano-banana)

## 请求参数
Header 参数生成代码Authorizationstring 必需示例:sk-Body 参数application/json必填生成代码promptstring 生成图片的提示词。必需num_imagesstring 必需生成图片数量。范围值1-4。默认值：1

示例
## 返回响应
🟢200成功application/json生成代码Body生成代码statusstring 必需request_idstring 必需response_urlstring 必需status_urlstring 必需cancel_urlstring 必需logsstring 必需metricsstring 必需queue_positionstring 必需请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/fal-ai/nano-banana' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "prompt": "An action shot of a black lab swimming in an inground suburban swimming pool. The camera is placed meticulously on the water line, dividing the image in half, revealing both the dogs head above water holding a tennis ball in it'\''s mouth, and it'\''s paws paddling underwater.",
    "num_images": 1
}'
```
响应示例响应示例
```
{
    "status": "IN_QUEUE",
    "request_id": "e7e9202c-efb8-40f2-81c3-13b3f7aaa4ca",
    "response_url": "https://queue.fal.run/fal-ai/nano-banana/requests/e7e9202c-efb8-40f2-81c3-13b3f7aaa4ca",
    "status_url": "https://queue.fal.run/fal-ai/nano-banana/requests/e7e9202c-efb8-40f2-81c3-13b3f7aaa4ca/status",
    "cancel_url": "https://queue.fal.run/fal-ai/nano-banana/requests/e7e9202c-efb8-40f2-81c3-13b3f7aaa4ca/cancel",
    "logs": null,
    "metrics": {},
    "queue_position": 0
}
```