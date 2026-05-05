# 生成视频（Video）

执行video操作，提交绘图任务。提交任务后，获取到任务id，使用查询接口查询任务状态。（视频的按钮可以使用action进行点击）
请求体参数另外说明：
方式1：Base64 图片数组 + 描述
{
"prompt": "一只可爱的小猫在花园里缓慢走动",
"base64Array": [
"data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ...",
"data:image/jpeg;base64,iVBORw0KGgoAAAANSUhEUgAA..."
],
"notifyHook": "[https://your-domain.com/mj/notify](https://your-domain.com/mj/notify)"
}
方式2：Prompt 中包含图片地址
{
"prompt": "[https://example.com/image.jpg](https://example.com/image.jpg) 一只可爱的小猫在花园里缓慢走动",
"notifyHook": "[https://your-domain.com/mj/notify](https://your-domain.com/mj/notify)"
}
方式3：基于已有任务生成视频
{
"taskId": "existing-task-id-12345",
"prompt": "基于这张图片生成视频，小猫在花园里走动",
"notifyHook": "[https://your-domain.com/mj/notify](https://your-domain.com/mj/notify)"
}

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
curl --location --request POST &#x27;http://47.102.134.41:3000/mj/submit/video&#x27; \
--header &#x27;Accept: application/json&#x27; \
--header &#x27;Authorization: sk-&#x27; \
--header &#x27;Content-Type: application/json&#x27; \
--data-raw &#x27;{
    "prompt": "一只可爱的小猫在花园里缓慢走动",
    "base64Array": [
        "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ..."
    ]
}&#x27;
```
响应示例响应示例
```
{
    "code": 1,
    "description": "提交成功",
    "properties": null,
    "result": "task-id-12345"
}
```