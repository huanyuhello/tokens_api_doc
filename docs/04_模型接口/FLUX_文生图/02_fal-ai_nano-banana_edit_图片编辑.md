# /fal-ai/nano-banana/edit 图片编辑

官方文档: [https://fal.ai/models/fal-ai/nano-banana/edit](https://fal.ai/models/fal-ai/nano-banana/edit)

## 请求参数
Header 参数生成代码
### 

- 
- 
- 
Body 参数application/json必填生成代码
### 

- 
- 
- 
示例
## 返回响应
🟢200成功application/json生成代码Body生成代码
### 

- 
- 
- 
请求示例请求示例ShellJavaScriptJavaSwiftcURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST &#x27;http://47.102.134.41:3000/fal-ai/nano-banana/edit&#x27; \
--header &#x27;Authorization: sk-&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data-raw &#x27;{
    "prompt": "make a photo of the man driving the car down the california coastline",
    "image_urls": [
        "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input.png",
        "https://storage.googleapis.com/falserverless/example_inputs/nano-banana-edit-input-2.png"
    ],
    "num_images": 1
}&#x27;
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