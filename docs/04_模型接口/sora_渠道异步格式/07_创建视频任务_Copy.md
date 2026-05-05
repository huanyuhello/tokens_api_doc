# 创建视频任务 Copy


## 请求参数


### Header 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `Authorization` | string | 必需 | 示例: |
| `sk-` |  |  |  |
| `Content-Type` | string | 必需 | 示例: application/json |


### Body 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `必填` |  |  |  |
| `model` | string | 可选 | 枚举值: |
| `sora-2` |  |  |  |
| `sora-2-hd` |  |  | 示例值: |
| `sora_video2` | prompt |  |  |
| `string` | 可选 |  | 示例值: 画面动起来 |
| `seconds` | string | 可选 |  |
| `string` | 可选 |  | 只允许设置这三个值：10、15、25，其他值无效。并且25s需要sora-2-pro才有效 示例值: 10 |
| `input_reference` | integer | 必需 | 图片 可选 示例值: file:///Users/xiangsx/Downloads/RHTtTcBrlY5wGxop9ux8DqRckyIKxd.png |
| `size` | string | 可选 |  |
| `enum` | 可选 |  | 宽x高，会忽略具体数据 宽>高 为横屏，宽<高为竖屏 720x1280 1280x720 1024x1792 1792x1024 |
| `watermark` | boolean | 可选 |  |
| `boolean` | 可选 |  | 是否需要水印，不传默认无水印（测试中） 示例值: |
| `false` | 示例 |  |  |


## 返回响应
