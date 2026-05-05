# 文本转语音 TTS


## 请求参数


### Header 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `Authorization` | string | 必需 | 示例: |
| `sk-` |  |  |  |


### Body 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `model` | string | 必需 | 可用的 TTS 模型之一:tts-1 或 tts-1-hd |
| `input` | string | 必需 | 要生成音频的文本。最大长度为4096个字符。 |
| `voice` | string | 必需 | 生成音频时使用的语音。支持的语音有:alloy、echo、fable、onyx、nova 和 shimmer。 |
| `response_format` | string | 可选 | 默认为 mp3 音频的格式。支持的格式有:mp3、opus、aac 和 flac。 |
| `encoding_format` | string | 可选 | 默认为 1 生成的音频速度。选择0.25到4.0之间的值。1.0是默认值。 示例 |


## 返回响应
