# PDF文件分析

PDF转成base64替换到${base64String}

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
    "model": "gpt-4.1",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "file",
                    "file": {
                        "filename": "draconomicon.pdf",
                        "file_data": "data:application/pdf;base64,${base64String}"
                    }
                },
                {
                    "type": "text",
                    "text": "What is the first dragon in the book?"
                }
            ]
        }
    ]
}&#x27;
```
响应示例响应示例
```
{
    "id": "string",
    "object": "string",
    "created": 0,
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "string",
                "content": "string"
            },
            "finish_reason": "string"
        }
    ],
    "usage": {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0
    }
}
```