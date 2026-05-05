# fal-ai nano-banana edit 图片编辑


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
| `prompt` | string |  | 图像编辑的提示词。 必需 |
| `image_urls` | string | 必需 | 需要编辑的图片url。 |
| `num_images` | string | 必需 | 生成图片数量。范围值1-4。默认值：1 示例 |


## 返回响应
