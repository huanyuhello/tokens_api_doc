# 语音转文本 whisper-1


## 请求参数


### Header 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `Accept` | string | 必需 | 示例: application/json |
| `Authorization` | string | 必需 | 示例: |
| `sk-` |  |  |  |
| `Content-Type` | string | 必需 | 示例: multipart/form-data |


### Body 参数 (multipart/form-data)

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `file` | file | 可选 | 要转录的音频文件，采用以下格式之一：mp3、mp4、mpeg、mpga、m4a、wav 或 webm。 |
| `model` | string | 可选 | 要使用的模型的 ID。仅whisper-1当前可用。 |
| `prompt` | string | 可选 | 可选文本，用于指导模型的风格或继续之前的音频片段。提示应与音频语言相匹配。 |
| `response_format` | string | 可选 | 成绩单输出的格式，采用以下选项之一：json、text、srt、verbose_json 或 vtt。 |
| `temperature` | number | 可选 | 采样温度，介于 0 和 1 之间。较高的值（如 0.8）将使输出更加随机，而较低的值（如 0.2）将使输出更加集中和确定。如果设置为 0，模型将使用对数概率自动升高温度，直到达到特定阈值。 |
| `language` | string | 可选 | 输入音频的语言。以ISO-639-1格式提供输入语言将提高准确性和延迟。 |


## 返回响应
