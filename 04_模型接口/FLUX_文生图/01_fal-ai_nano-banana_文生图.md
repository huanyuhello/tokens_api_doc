# /fal-ai/nano-banana 文生图

官方文档: [https://fal.ai/models/fal-ai/nano-banana](https://fal.ai/models/fal-ai/nano-banana)

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
curl --location --request POST &#x27;http://47.102.134.41:3000/fal-ai/nano-banana&#x27; \
--header &#x27;Authorization: sk-&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data-raw &#x27;{
    "prompt": "An action shot of a black lab swimming in an inground suburban swimming pool. The camera is placed meticulously on the water line, dividing the image in half, revealing both the dogs head above water holding a tennis ball in it&#x27;\&#x27;&#x27;s mouth, and it&#x27;\&#x27;&#x27;s paws paddling underwater.",
    "num_images": 1
}&#x27;
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