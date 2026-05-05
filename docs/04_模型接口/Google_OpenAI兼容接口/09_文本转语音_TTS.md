# 文本转语音 / TTS

可用的 TTS 模型之一:tts-1 或 tts-1-hd

inputstring 必需要生成音频的文本。最大长度为4096个字符。

voicestring 必需生成音频时使用的语音。支持的语音有:alloy、echo、fable、onyx、nova 和 shimmer。

response_formatstring 必需默认为 mp3 音频的格式。支持的格式有:mp3、opus、aac 和 flac。

encoding_formatstring 必需默认为 1 生成的音频速度。选择0.25到4.0之间的值。1.0是默认值。

示例
## 返回响应
🟢200成功application/json生成代码Body生成代码object 请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/v1/audio/speech' \
--header 'Authorization: sk-' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model": "gemini-2.5-pro-preview-tts",
    "input": "The quick brown fox jumped over the lazy dog.",
    "voice": "alloy",
    "response_format": "wav"
}'
```
响应示例响应示例
```
{}
```