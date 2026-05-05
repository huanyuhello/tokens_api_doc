# Hunyuan3D-2

指定使用的模型。目前仅支持 Hunyuan3D-2。

imagestring 必需待转换的图片文件。格式支持 jpg, jpeg, png, bmp。推荐分辨率为 1024x1024，文件大小不能超过 10MB。

promptstring 必需seedinteger 可选随机种子。整数，用于复现生成结果。如果设置为-1，则为随机种子。

extra_fieldsobject 可选typestring 枚举值: glb可选texturestring 可选是否为生成的3D模型生成纹理。
默认值:
true

num_inference_stepsstring 可选推理步数。取值范围 [1, 10]。数值越大，模型细节可能越丰富，但生成时间也越长。
默认值:
5

octree_resolutionstring 可选八叉树分辨率。可选值为 [64, 128, 256]。数值越大，模型面数越多，细节越丰富，生成时间也越长。
默认值:
128

guidance_scalestring 可选引导系数。取值范围 [1.0, 10.0]。数值越大，生成结果与输入图片的关联性越强。
默认值:
5

示例
## 返回响应
🟢200成功application/json生成代码Body生成代码dataarray[string]必需urlstring 可选createdinteger 必需请求示例请求示例ShellJavaScriptJavacURLcURL-WindowsHttpiewgetPowerShell
```
curl --location --request POST 'https://4sapi.com/v1/images/generations' \
--header 'Authorization: sk-' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model": "Hunyuan3D-2",
    "prompt": " ",
    "image": "https://s3.ffire.cc/files/christmas-tree.png"
}'
```
响应示例响应示例
```
{
    "data": [
        {
            "url": "https://xxxxxxxxxxxxxx"
        }
    ],
    "created": 1753872474
}
```