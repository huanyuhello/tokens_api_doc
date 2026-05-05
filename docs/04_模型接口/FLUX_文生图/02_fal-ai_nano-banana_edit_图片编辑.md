# /fal-ai/nano-banana/edit 图片编辑

官方文档: [https://fal.ai/models/fal-ai/nano-banana/edit](https://fal.ai/models/fal-ai/nano-banana/edit)

## 请求参数
Header 参数生成代码Authorizationstring 必需示例:sk-Body 参数application/json必填生成代码promptstring 图像编辑的提示词。必需image_urlsstring 必需需要编辑的图片url。

num_imagesstring 必需生成图片数量。范围值1-4。默认值：1

示例
## 返回响应
🟢200成功application/json生成代码Body生成代码statusstring 必需request_idstring 必需response_urlstring 必需status_urlstring 必需cancel_urlstring 必需logsstring 必需metricsstring 必需queue_positionstring 必需请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/fal-ai/nano-banana/edit' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "prompt": "make a photo of the man driving the car down the california coastline",
    "image_urls": [
        "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input.png",
        "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input-2.png"
    ],
    "num_images": 1
}'
```
响应示例响应示例
```
{
    "status": "IN_QUEUE",
    "request_id": "f8837f29-26cb-4213-90f5-22b2911a0ea7",
    "response_url": "https://queue.fal.run/fal-ai/nano-banana/requests/f8837f29-26cb-4213-90f5-22b2911a0ea7",
    "status_url": "https://queue.fal.run/fal-ai/nano-banana/requests/f8837f29-26cb-4213-90f5-22b2911a0ea7/status",
    "cancel_url": "https://queue.fal.run/fal-ai/nano-banana/requests/f8837f29-26cb-4213-90f5-22b2911a0ea7/cancel",
    "logs": null,
    "metrics": {},
    "queue_position": 0
}
```