# 获取个人 Token

个人 Token（系统访问令牌）用于调用本文档中所有个人接口的身份认证。

## 获取方式

调用以下接口生成系统访问令牌：

**GET** `https://tokens.smartfashionai.cn/api/user/token`

详细说明参见 [生成系统访问令牌](./一_个人信息/07_生成系统访问令牌.md)。

## 使用方式

将生成的 Token 放入请求 Header：

| Header 名 | 值 |
|-----------|-----|
| `Authorization` | `你的系统访问令牌` |
| `New-Api-User` | `你的用户 ID（数字）` |
