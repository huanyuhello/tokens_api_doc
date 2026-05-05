# 语音转文本 / gpt-4o-transcribe

要转录的音频文件，采用以下格式之一：mp3、mp4、mpeg、mpga、m4a、wav 或 webm。

modelstring 可选要使用的模型的 ID。仅whisper-1当前可用。

promptstring 可选可选文本，用于指导模型的风格或继续之前的音频片段。提示应与音频语言相匹配。

response_formatstring 可选成绩单输出的格式，采用以下选项之一：json、text、srt、verbose_json 或 vtt。

temperaturenumber 可选采样温度，介于 0 和 1 之间。较高的值（如 0.8）将使输出更加随机，而较低的值（如 0.2）将使输出更加集中和确定。如果设置为 0，模型将使用对数概率自动升高温度，直到达到特定阈值。

languagestring 可选输入音频的语言。以ISO-639-1格式提供输入语言将提高准确性和延迟。

## 返回响应
🟢200成功application/json生成代码Body生成代码object 请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/v1/audio/transcriptions' \
--header 'Accept: application/json' \
--header 'Authorization: sk-' \
--form 'file=@""' \
--form 'model=""' \
--form 'prompt=""' \
--form 'response_format=""' \
--form 'temperature=""' \
--form 'language=""'
```
响应示例响应示例
```
{
    "text": "Imagine the wildest idea that you've ever had, and you're curious about how it might scale to something that's a 100, a 1,000 times bigger. This is a place where you can get to do that."
}
```