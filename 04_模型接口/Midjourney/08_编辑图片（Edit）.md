# 编辑图片（Edit）

执行edit接口，可以编辑外部传入的图片，可以进行局部重绘，也可以直接改图

## 请求参数
Header 参数生成代码
### 

- 
- 
- 
Body 参数application/json必填生成代码
### 

- 
- 
- 
示例
## 返回响应
🟢200成功application/json生成代码Body生成代码
### 

- 
- 
- 
请求示例请求示例ShellJavaScriptJavaSwiftcURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST &#x27;http://47.102.134.41:3000/mj/submit/edits&#x27; \
--header &#x27;Accept: application/json&#x27; \
--header &#x27;Authorization: sk-&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data-raw &#x27;{
    "action": "EDITS",
    "prompt": "将图片转为吉卜力风格",
    "maskBase64": "data:image/png;base64,iVBORw0KGgoAAAAlFTkSuQmCC",
    "base64Array": [
        "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSQ=="
    ]
}&#x27;
```
响应示例响应示例
```
{}
```