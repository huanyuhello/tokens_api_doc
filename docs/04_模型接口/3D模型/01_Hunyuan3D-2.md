# Hunyuan3D-2


## 请求参数


### Header 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `Authorization` | string | 必需 | 示例: |
| `sk-` |  |  |  |


### Body 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `必填` |  |  |  |
| `model` | string | 必需 | 指定使用的模型。目前仅支持 Hunyuan3D-2。 |
| `image` | string | 必需 | 待转换的图片文件。格式支持 jpg, jpeg, png, bmp。推荐分辨率为 1024x1024，文件大小不能超过 10MB。 |
| `prompt` | string | 必需 |  |
| `seed` | integer | 可选 | 随机种子。整数，用于复现生成结果。如果设置为-1，则为随机种子。 |
| `extra_fields` | object | 可选 |  |
| `type` | string |  | 枚举值: glb 可选 |
| `texture` | string | 可选 | 是否为生成的3D模型生成纹理。 默认值: |
| `true` | num_inference_steps |  |  |
| `string` | 可选 |  | 推理步数。取值范围 [1, 10]。数值越大，模型细节可能越丰富，但生成时间也越长。 默认值: 5 |
| `octree_resolution` | string | 可选 | 八叉树分辨率。可选值为 [64, 128, 256]。数值越大，模型面数越多，细节越丰富，生成时间也越长。 默认值: 128 |
| `guidance_scale` | string | 可选 | 引导系数。取值范围 [1.0, 10.0]。数值越大，生成结果与输入图片的关联性越强。 默认值: 5 示例 |


## 返回响应
