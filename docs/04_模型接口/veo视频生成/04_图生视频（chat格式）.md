# 图生视频（chat格式）

veo3-fast 文字快速生成视频
veo3-pro 不垫图
veo3-pro-frames 垫图

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
--header &#x27;Accept: application/json&#x27; \
--header &#x27;Authorization: sk-&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data-raw &#x27;{
    "model": "veo_3_1",
    "stream": true,
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What&#x27;\&#x27;&#x27;s in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                    }
                }
            ]
        }
    ]
}&#x27;
```
响应示例响应示例
```
{
    "id": "chatcmpl-89DheNHkXJZegjted4eBXeqGUGEpM",
    "object": "chat.completion",
    "created": 1755853547,
    "model": "veo3-pro",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "\n\n> 视频生成任务已创建\n> 任务ID: `veo3-pro:03bd6356-8ec6-4e06-be7f-c06febc5eb47`\n> 为了防止任务中断，可以从以下链接持续获取任务进度:\n> [数据预览](https://asyncdata.net/web/veo3-pro:03bd6356-8ec6-4e06-be7f-c06febc5eb47) | [原始数据](https://asyncdata.net/source/veo3-pro:03bd6356-8ec6-4e06-be7f-c06febc5eb47)\n> 等待处理中.\n\n> 类型: 文字生成\n> 🎬 开始生成视频...........................\n\n> 🎉 高质量视频已生成\n\n[▶️ 在线观看](https://filesystem.site/cdn/20250822/2hO6Q2oDZtT5I2sZd1lmyGUjmXntfT.mp4) | [⏬ 下载视频](https://filesystem.site/cdn/download/20250822/2hO6Q2oDZtT5I2sZd1lmyGUjmXntfT.mp4)"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 21,
        "completion_tokens": 289,
        "total_tokens": 310,
        "prompt_tokens_details": {
            "text_tokens": 14
        },
        "completion_tokens_details": {
            "content_tokens": 289
        }
    }
}
```