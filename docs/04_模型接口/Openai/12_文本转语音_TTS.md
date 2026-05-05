# 文本转语音 / TTS

文本转语音（TTS）API 基于先进的生成 AI 模型，可以将输入的文本转换为逼真的语音音频。支持多种用途：
为书面博客文章配音
生成多种语言的语音音频
提供实时音频输出流
可用模型列表：
gpt-4o-audio-preview —— OpenAI 最新的音频生成模型，支持对话式音频生成
gpt-4o-mini-tts —— 智能实时应用的首选模型，支持高级语音控制，可以通过提示词控制多种语音特性：
口音 (Accent)
情感范围 (Emotional range)
语调 (Intonation)
印象/风格 (Impressions)
语速 (Speed of speech)
语调 (Tone)
轻声说话 (Whispering)
tts-1-hd —— 高清音质的上一代 TTS 模型
tts-1 —— 标准 TTS 模型，平衡质量和速度
性能建议： 为获得最快的响应时间，建议使用 wav 或 pcm 作为响应格式。对于高质量音频，建议使用 tts-1-hd；对于更快的生成速度，使用 tts-1；对于智能语音应用，推荐使用 gpt-4o-mini-tts。
音色预览： 你可以在 OpenAI.fm 试听不同音色效果。
模型调用方式
标准 TTS 模型（tts-1, tts-1-hd）
使用 /v1/audio/speech 端点，通过 client.audio.speech.create() 方法调用。
​gpt-4o-mini-tts 模型
使用 /v1/audio/speech 端点，支持 instructions 参数进行高级语音控制。
gpt-4o-audio-preview 模型
使用 /v1/chat/completions 端点，需要设置 modalities: ["text", "audio"] 和 audio 配置。

## 请求参数
Header 参数生成代码Authorizationstring 必需示例:sk-Body 参数application/json生成代码modelstring 必需可用的 TTS 模型之一:tts-1 或 tts-1-hd

inputstring 必需要生成音频的文本。最大长度为4096个字符。

voicestring 必需生成音频时使用的语音。支持的语音有:alloy、echo、fable、onyx、nova 和 shimmer。

response_formatstring 可选默认为 mp3 音频的格式。支持的格式有:mp3、opus、aac 和 flac。

encoding_formatstring 可选默认为 1 生成的音频速度。选择0.25到4.0之间的值。1.0是默认值。

示例
## 返回响应
🟢200成功application/json生成代码Body生成代码object 请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/v1/audio/speech' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model": "tts-1",
    "input": "The quick brown fox jumped over the lazy dog.",
    "voice": "alloy",
    "response_format": "wav"
}'
```
响应示例响应示例
```
{
    "model": "tts-1",
    "input": "The quick brown fox jumped over the lazy dog.",
    "voice": "alloy"
}
```