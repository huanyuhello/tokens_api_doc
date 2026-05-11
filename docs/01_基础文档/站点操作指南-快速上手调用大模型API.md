# 快速上手：调用大模型 API

!!! tip "新用户必看"
    API 站点地址：**[https://tokens.smartfashionai.cn/](https://tokens.smartfashionai.cn/)**
    
    如有疑问或企业级需求，请联系微信：**xiaochaozhz**

---

## 调用流程概览

```
注册用户 → 充值余额 → 创建令牌 → 选择分组 → 设置额度/期限 → 完成创建
```

!!! info "核心公式"
    **API = URL + 令牌（Key）**
    
    | 配置项 | 值 |
    |--------|-----|
    | URL | `https://tokens.smartfashionai.cn/` |
    | 密钥 | `SK-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` |

---

## 步骤一：充值余额

进入「控制台」页面，选择左侧栏的 **「钱包管理」**，根据实际需求充值，确保账户余额大于 0。

---

## 步骤二：创建 API Key

1. 选择左侧栏的 **「密钥管理」**，点击 **「添加令牌」**
2. 填入令牌名称，根据实际需求选择 **分组** 并设置 **额度**
3. 点击提交按钮，生成 Key
4. 生成后可查看该 Key 的状态、余额、分组等信息
5. 不同分组可用的模型及对应价格，可在 **「模型广场」** 中查看

!!! warning "关于分组选择"
    不同分组的资源渠道、稳定性、质量各不相同，请结合自身需求选择性价比最高的方案。如有疑问可联系客服协助选择。

---

## 步骤三：获取中转站点信息

在控制台页面右侧可查看不同站点信息，可根据自己的网络情况选择合适的站点。

---

## 步骤四：发起 API 调用

将生成的 Key 放在 HTTP 请求头（Header）中进行鉴权，并向指定接口地址发送请求：

```http
Authorization: Bearer SK-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

配置模型时，请在 **「模型广场」** 复制模型名称，名称必须完全一致，例如：

```
claude-sonnet-4-5-20250929
```

---

## 步骤五：替换 API 地址（开发者）

如果你是开发者，将 OpenAI 官方文档中的基础地址替换为我们的中转地址即可：

| 原始地址 | 替换为 |
|----------|--------|
| `https://api.openai.com/` | `https://tokens.smartfashionai.cn/` |

!!! note "常用 URL 格式"
    不同软件或平台可能需要追加路径，具体以模型广场中该模型的 API 端点为准：
    
    ```
    https://tokens.smartfashionai.cn/
    https://tokens.smartfashionai.cn/v1          ← 最常见
    https://tokens.smartfashionai.cn/v1/chat/completions
    ```
    
    Claude 模型同时支持原生 `v1/messages` 接口，详情参考 Claude 原生接口调用文档。

---

## 联系方式

| 用途 | 联系方式 |
|------|----------|
| 普通咨询 / 技术支持 | 微信：**xiaochaozhz** |
| 企业开票 / 对公付款 / 商务合作 | 微信：**xiaochaozhz** |
