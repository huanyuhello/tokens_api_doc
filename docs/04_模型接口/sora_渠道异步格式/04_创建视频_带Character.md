# 创建视频 带Character


## 请求参数


### Header 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `Authorization` | string | 必需 | 默认值: {{Authorization}} |


### Body 参数

| 参数名 | 类型 | 必需 | 描述 |
|--------|------|------|------|
| `model` | file | 必需 |  |
| `enum` | 必需 |  | 枚举值: |
| `sora-2` |  |  |  |
| `sora-2-hd` |  |  | 示例: |
| `sora-2` | prompt |  |  |
| `string` | 画面动起来 | 必需 |  |
| `seconds` | string |  | 10 可选 |
| `input_reference` | string | 可选 | 示例: file:///Users/xiangsx/Downloads/RHTtTcBrlY5wGxop9ux8DqRckyIKxd.png |
| `size` | string | 可选 | 宽x高，会忽略具体数据 宽>高 为横屏，宽<高为竖屏 枚举值: 1024x1792 |
| `enum` |  |  | 高清竖屏仅 sora-2-pro 可用 1792x1024 高清横屏仅 sora-2-pro 可用 720x1280 标清竖屏 1280x720 标清横屏 示例: 16x9 |
| `watermark` | string | 可选 | 是否需要水印，不传默认无水印 示例: |
| `true` | private |  |  |
| `string` | 可选 |  | 是否隐藏视频，true-视频不会发布，同时视频无法进行 remix(二次编辑)， 默认为 false 示例: |
| `false` | character_url |  |  |
| `string` | 可选 |  | 创建角色需要的视频链接，注意视频中一定不能出现真人，否则会失败 示例: https://filesystem.site/cdn/20251030/javYrU4etHVFDqg8by7mViTWHlMOZy.mp4 |
| `character_timestamps` | string | 可选 | 视频角色出现的秒数范围，格式 {start},{end}, 注意 end-start 的范围 1～3秒 示例: 1,3 |
| `character_from_task` | string | 可选 | 已完成的任务 id,可以根据已经生成的任务 id，来创建角色 |


## 返回响应
