# openclaw配置使用教程


## cpenclaw的API配置（claude）#


```js
"models": {
    "providers": {
      "custom-1": {
        "baseUrl": "https://tokens.smartfashionai.cn/",
        "apiKey": "你自己的KEY",
        "api": "anthropic-messages",
        "models": [
          {
            "id":claude-sonnet-4-6 ",
            "name": claude-sonnet-4-6",
            "api": anthropic-messages",
            "reasoning": true,(自选推理与否)
            "input": [
              "text",
              "image"
            ],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 200000,
            "maxTokens": 8192
          }
        ]
      }
    },
    
```js
```


## cpenclaw的API配置（GPT/gemini）#


```js
`"models": {
    "providers": {
      "custom-2": {
        "baseUrl": "https://tokens.smartfashionai.cn/",
        "apiKey": "你自己的KEY",
        "api": "anthropic-messages",
        "models": [
          {
            "id":gpt-5.2 ",
            "name": gpt-5.2",
            "api": openai-completions",
            "reasoning":true,(自选推理与否)
            "input": [
              "text",
              "image"
            ],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 200000,
            "maxTokens": 8192
           }
        ]
      }
    }
    

```js
"models": {
    "providers": {
      "custom-3": {
        "baseUrl": "https://tokens.smartfashionai.cn/",
        "apiKey": "你自己的KEY",
        "api": "anthropic-messages",
        "models": [
          {
            "id":gemini-3-pro-preview",
            "name": gemini-3-pro-preview",
            "api": openai-completions",
            "reasoning":true,(自选推理与否)
            "input": [
              "text",
              "image"
            ],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
            "contextWindow": 200000,
            "maxTokens": 8192
           }
        ]
      }
    },

  "agents": {
    "defaults": {
      "model": {
        "primary": "custom-1/claude-sonnet-4-6",
        "fallbacks": []`
        
        
```js
```

选择模型的时候，前缀要和这个渠道一致比如custom-1和custom-2然后后面就是/claude-sonnet-4-6和gpt-5.2等模型custom-1/claude-sonnet-4-6custom-2/gpt-5.2custom-3/gemini-3-pro-preview