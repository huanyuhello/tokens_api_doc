# deep-research / 深度研究

要进行深度研究，请使用Responses API，并将模型设置为o3-deep-research或o4-mini-deep-research。

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
curl --location --request POST &#x27;http://47.102.134.41:3000/v1/responses&#x27; \
--header &#x27;Accept: application/json&#x27; \
--header &#x27;Authorization: sk-&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data-raw &#x27;{
    "model": "o3-deep-research",
    "tools": [
        {
            "type": "web_search_preview"
        }
    ],
    "input": [
        {
            "role": "user",
            "content": "讲一个三句话的关于独角兽的睡前故事。"
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