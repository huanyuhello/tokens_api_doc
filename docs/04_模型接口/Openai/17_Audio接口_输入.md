# Audio接口 / 输入

本中转所有模型均已适配v1/chat/completions
只需要把模型名称完整复制到model参数即可使用

## 请求参数
Header 参数生成代码
### 

- 
- 
- 
Body 参数application/json生成代码
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
    "model": "gpt-4o-audio-preview",
    "modalities": [
        "text",
        "audio"
    ],
    "audio": {
        "voice": "alloy",
        "format": "wav"
    },
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is in this recording?"
                },
                {
                    "type": "input_audio",
                    "input_audio": {
                        "data": "",
                        "format": "wav"
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