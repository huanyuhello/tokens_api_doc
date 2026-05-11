# OpenClaw 配置教程

> 在 OpenClaw 中配置多个模型供应商（Claude / GPT / Gemini）。

---

## 前置条件

- 已注册并获取 API 密钥：[https://tokens.smartfashionai.cn/](https://tokens.smartfashionai.cn/)

---

## 配置说明

OpenClaw 通过 `models.providers` 字段配置自定义供应商。每个供应商使用一个唯一的 `custom-N` 标识，调用模型时需加上对应前缀，例如 `custom-1/claude-sonnet-4-6`。

---

## 供应商一：Claude 模型

使用 `anthropic-messages` API 接口：

```json
"models": {
  "providers": {
    "custom-1": {
      "baseUrl": "https://tokens.smartfashionai.cn/",
      "apiKey": "你的 API Key",
      "api": "anthropic-messages",
      "models": [
        {
          "id": "claude-sonnet-4-6",
          "name": "claude-sonnet-4-6",
          "api": "anthropic-messages",
          "reasoning": true,
          "input": ["text", "image"],
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
}
```

---

## 供应商二：GPT 模型

使用 `openai-completions` API 接口：

```json
"models": {
  "providers": {
    "custom-2": {
      "baseUrl": "https://tokens.smartfashionai.cn/",
      "apiKey": "你的 API Key",
      "api": "openai-completions",
      "models": [
        {
          "id": "gpt-5.2",
          "name": "gpt-5.2",
          "api": "openai-completions",
          "reasoning": true,
          "input": ["text", "image"],
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
}
```

---

## 供应商三：Gemini 模型

使用 `openai-completions` API 接口：

```json
"models": {
  "providers": {
    "custom-3": {
      "baseUrl": "https://tokens.smartfashionai.cn/",
      "apiKey": "你的 API Key",
      "api": "openai-completions",
      "models": [
        {
          "id": "gemini-3-pro-preview",
          "name": "gemini-3-pro-preview",
          "api": "openai-completions",
          "reasoning": true,
          "input": ["text", "image"],
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
        "fallbacks": []
      }
    }
  }
}
```

---

## 模型调用格式

选择模型时，需在模型名称前加上对应供应商前缀：

| 供应商 | 模型调用格式 |
|--------|-------------|
| custom-1（Claude） | `custom-1/claude-sonnet-4-6` |
| custom-2（GPT） | `custom-2/gpt-5.2` |
| custom-3（Gemini） | `custom-3/gemini-3-pro-preview` |
