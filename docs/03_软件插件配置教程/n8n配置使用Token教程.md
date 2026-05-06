# n8n 配置使用 Tokens 教程

---

## 方式一：通过 OpenAI 凭证接入

### 第一步：添加账户凭证

1. 在 n8n 中点击 **Overview** → **Credentials**
2. 在弹出窗口中选择 **OpenAI**
3. 填写以下信息：
    - **API Key**：你在 Tokens 平台创建的令牌 Key
    - **Base URL**：`http://47.102.134.41:3000/v1`
4. 点击保存，出现绿色成功提示即配置完成

---

## 方式二：通过 HTTP Request 节点接入

### 文本对话工作流

1. 创建工作流，添加**手动触发**节点
2. 添加 **HTTP Request** 节点，按如下配置：

**请求地址：**
```
http://47.102.134.41:3000/v1/chat/completions
```

**请求方式：** `POST`

**Header（JSON 格式）：**
```json
{
  "Authorization": "Bearer sk-...",
  "Content-Type": "application/json"
}
```

**Body（JSON 格式）：**
```json
{
  "model": "gemini-2.5-pro-all",
  "messages": [
    { "role": "system", "content": "你是一个AI助理" },
    { "role": "user", "content": "你好" }
  ]
}
```

3. 点击顶部 **Execute step** 测试，右侧 OUTPUT 正常输出即成功

---

### 图片生成工作流

1. 添加 **HTTP Request** 节点，按如下配置：

**请求地址：**
```
http://47.102.134.41:3000/v1/images/generations
```

**Header（JSON 格式）：**
```json
{
  "Authorization": "Bearer sk-...",
  "Content-Type": "application/json"
}
```

**Body（JSON 格式）：**
```json
{
  "model": "gpt-image-1",
  "prompt": "a white siamese cat",
  "n": 1,
  "size": "1024x1024"
}
```

2. 点击右上角测试，输出图片 URL 即成功
3. 可通过在线 Base64 转码工具将结果转为图片预览
