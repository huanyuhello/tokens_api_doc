# response_format

官方结构化输出

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
    "model": "gpt-4o-2024-08-06",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful math tutor."
        },
        {
            "role": "user",
            "content": "solve 8x + 31 = 2"
        }
    ],
    "response_format": {
        "type": "json_schema",
        "json_schema": {
            "name": "math_response",
            "strict": true,
            "schema": {
                "type": "object",
                "properties": {
                    "steps": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "explanation": {
                                    "type": "string"
                                },
                                "output": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "explanation",
                                "output"
                            ],
                            "additionalProperties": false
                        }
                    },
                    "final_answer": {
                        "type": "string"
                    }
                },
                "required": [
                    "steps",
                    "final_answer"
                ],
                "additionalProperties": false
            }
        }
    }
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