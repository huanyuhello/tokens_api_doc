# 图片生成 / Imagen 4

Gemini 绘图和视频生成指引
​
Imagen 绘图
Imagen 是 Google 推出的先进图像生成 AI 模型系列，能够根据文本提示创建高质量、逼真的图像。本指南将帮助您了解如何使用 Imagen 系列 API 生成图像，包括参数设置、模型选择和代码示例。
可用模型列表：
imagen-4.0-generate-preview-05-20：最新的正式预览版
imagen-4.0-ultra-generate-exp-05-20：更高级的 4.0 实验款
imagen-3.0-generate-002：3.0 正式版
目前 Imagen 仅支持英文提示词（prompt），集成时建议增加自动翻译，让用户能够无障碍使用
绘制大量文本的表现不稳定，建议只绘制重点关键词
抢先体验期间，Imagen 系列模型同价，后续可能会按官方正式价格调整。
模型参数
Imagen 目前仅支持英文提示词，并提供以下参数：
numberOfImages: 要生成的图像数量，范围从 1 到 4（含）。默认值为 4。另外注意 imagen-4.0-ultra-generate-exp-05-20 单次只能生成 1 张。
aspectRatio: 更改生成图像的宽高比。支持的值有 “1:1”、“3:4”、“4:3”、“9:16” 和 “16:9”。默认值为 “1:1”。
personGeneration: 允许模型生成人物图像。支持以下值：
“DONT_ALLOW”: 阻止生成人物图像。
“ALLOW_ADULT”: 生成成人图像，但不生成儿童图像。这是默认值。

## 请求参数
Header 参数生成代码Acceptstring 必需示例:application/jsonAuthorizationstring 必需示例:sk-Content-Typestring 必需示例:application/jsonBody 参数application/json生成代码modelstring 必需要使用的模型的 ID。有关哪些模型适用于聊天 API 的详细信息

messagesarray [object] 必需以聊天格式生成聊天完成的消息。

rolestring 必需contentstring 必需temperaturestring 可选使用什么采样温度，介于 0 和 2 之间。较高的值（如 0.8）将使输出更加随机，而较低的值（如 0.2）将使输出更加集中和确定。 我们通常建议改变这个或top_p但不是两者。

top_pstring 可选一种替代温度采样的方法，称为核采样，其中模型考虑具有 top_p 概率质量的标记的结果。所以 0.1 意味着只考虑构成前 10% 概率质量的标记。 我们通常建议改变这个或temperature但不是两者。

nstring 可选为每个输入消息生成多少个聊天完成选项。

streamstring 可选如果设置，将发送部分消息增量，就像在 ChatGPT 中一样。当令牌可用时，令牌将作为纯数据服务器发送事件data: [DONE]发送，流由消息终止。

stopstring 可选API 将停止生成更多令牌的最多 4 个序列。

max_tokensstring 可选聊天完成时生成的最大令牌数。 输入标记和生成标记的总长度受模型上下文长度的限制。

presence_penaltystring 可选-2.0 和 2.0 之间的数字。正值会根据到目前为止是否出现在文本中来惩罚新标记，从而增加模型谈论新主题的可能性

frequency_penaltystring 可选-2.0 和 2.0 之间的数字。正值会根据新标记在文本中的现有频率对其进行惩罚，从而降低模型逐字重复同一行的可能性。

logit_biasstring 可选修改指定标记出现在完成中的可能性。 接受一个 json 对象，该对象将标记（由标记器中的标记 ID 指定）映射到从 -100 到 100 的关联偏差值。从数学上讲，偏差会在采样之前添加到模型生成的 logits 中。确切的效果因模型而异，但 -1 和 1 之间的值应该会减少或增加选择的可能性；像 -100 或 100 这样的值应该导致相关令牌的禁止或独占选择。

userstring 可选代表您的最终用户的唯一标识符，可以帮助 OpenAI 监控和检测滥用行为。

示例
## 返回响应
🟢200成功application/json生成代码Body生成代码idstring 必需objectstring 必需createdstring 必需choicesarray [object] 必需indexstring 必需messageobject 必需finish_reasonstring 必需usageobject 必需prompt_tokensstring 必需completion_tokensstring 必需total_tokensstring 必需请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/v1/images/generations' \
--header 'Accept: application/json' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model": "imagen-4.0-generate-preview-06-06",
    "prompt": "a portrait of a sheepadoodle wearing a cape",
    "response_format": "b64_json",
    "n": 1
}'
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