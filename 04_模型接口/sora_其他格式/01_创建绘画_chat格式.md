# 创建绘画

给定一个提示，该模型将返回一个或多个预测的完成，并且还可以返回每个位置的替代标记的概率。
为提供的提示和参数创建完成
官方文档：[https://platform.openai.com/docs/api-reference/chat/create](https://platform.openai.com/docs/api-reference/chat/create)
请求参数

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
curl --location --request POST &#x27;http://47.102.134.41:3000/v1/chat/completions&#x27; \
--header &#x27;X-Forwarded-Host: 示例值:localhost:5173&#x27; \
--header &#x27;Accept: application/json&#x27; \
--header &#x27;Authorization: sk-&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data-raw &#x27;{
    "model": "sora-2",
    "max_tokens": 1000,
    "messages": [
        {
            "role": "user",
            "content": "an astronaut golden retriever named Sora levitates around an intergalactic pup-themed space station with a tiny jet back that propels him. gorgeous specular lighting and comets fly through the sky, retro-future astro-themed music plays in the background. light glimmers off the dog&#x27;\&#x27;&#x27;s eyes. the dog initially propels towards the space station with the doors opening to let him in. the shot then changes. now inside the space station, many tennis balls are flying around in zero gravity. the dog&#x27;\&#x27;&#x27;s astronaut helmet opens up so he can grab one. 35mm film, the intricate details and texturing of the dog&#x27;\&#x27;&#x27;s hair are clearly visible and the light of the comets shimmers off the fur."
        }
    ],
    "stream": true
}&#x27;
```
响应示例响应示例
```
{
    "id": "chatcmpl-123",
    "object": "chat.completion",
    "created": 1677652288,
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "\n\nHello there, how may I assist you today?"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 9,
        "completion_tokens": 12,
        "total_tokens": 21
    }
}
```