# Coze 配置使用 Tokens 教程

---

## 配置步骤

### 第一步：创建新项目

登录 [Coze](https://www.coze.cn/) 后，点击**创建新项目**。

### 第二步：创建工作流

在项目中点击**创建新的工作流**。

### 第三步：添加 HTTP 请求节点

在工作流编辑器中，添加 **HTTP 请求**节点。

### 第四步：填写请求配置

按如下信息填写 HTTP 请求节点：

**请求地址：**
```
http://47.102.134.41:3000/v1/chat/completions
```

**请求方式：** `POST`

**Header：**
```json
{
  "Authorization": "Bearer sk-...",
  "Content-Type": "application/json"
}
```

**Body：**
```json
{
  "model": "claude-opus-4-6",
  "messages": [
    { "role": "user", "content": "你好" }
  ]
}
```

### 第五步：运行测试

点击**运行节点**，右侧输出正常响应即配置成功。
