# 场景一：stems声曲分离 Vocals Instrumental

分离后 Vocals 人声
分离后 Instrumental 纯音乐 伴奏
A.生成音乐
可以通过场景 1 2 3 生成音乐 获取其中的一首歌的 clip_id 值为 a624123d-22cc-4d4d-bf28-78d312f61597
B.声曲分离.新
post {{BASE_URL}}/suno/generate
请求体
注意 mv为 chirp-auk
task 为 gen_stem
stem_task 为 two
stem_type_group_name 为 Two
continue_clip_id 就是 A 步骤中的 clip_id
可跨账号
计费:一次生成费用
{
"task": "gen_stem",
"generation_type": "TEXT",
"title": "安全之弦",
"mv": "chirp-auk",
"prompt": "",
"make_instrumental": true,
"continue_clip_id": "4720ad51-6d31-417c-a3a7-346b0b99abbc",
"continued_aligned_prompt": null,
"continue_at": null,
"stem_type_id": 91,
"stem_type_group_name": "Two",
"stem_task": "two"
}
返回体
{
"clips": [
{
"id": "5f3587e2-75fb-4c36-84b3-3ec113897a4c",
"video_url": "",
"audio_url": "",
"major_model_version": "",
"model_name": "",
"metadata": {
"tags": "Chinese",
"prompt": "在那遥远的星空之下，如今谁还在彷徨？\n就像无法游泳的鱼儿，我却只能责怪自己没有坚强的鳍片。\n快将彷徨化成力量，快把挫折当做指南。\n直到梦想实现之前，我坚定地守候着。\n昨天流逝了岁月，明天我将追随风的脚步，攀上高峰。\n呼唤吧，让我们出发，骑在梦想龙的脊背，穿越命运的坎坷。\n摆脱困境的束缚，即使失去了一切，人仍然渴望温暖的拥抱。\n人之所以能体会到他人的快乐，是因为心灵的善良。\n快将彷徨化成力量，快把挫折当做指南。\n我还是那只无法游泳的鱼儿，责怪自己没有坚强的鳍片。",
"stem_from_id": "a624123d-22cc-4d4d-bf28-78d312f61597",
"type": "stem",
"duration": 217.24
},
"is_liked": false,
"user_id": "58387c47-dc80-466f-a7b1-a2eed61c24fb",
"display_name": "FluidXylophone2289",
"handle": "fluidxylophone2289",
"is_handle_updated": false,
"avatar_image_url": "[https://cdn1.suno.ai/defaultPink.webp](https://cdn1.suno.ai/defaultPink.webp)",
"is_trashed": false,
"created_at": "2024-12-25T16:51:36.619Z",
"status": "queued",
"title": "骑在梦想龙的脊背 - Vocals",
"play_count": 0,
"upvote_count": 0,
"is_public": false
},
{
"id": "9c85d619-4cac-4561-8fa3-604c116fa1c5",
"video_url": "",
"audio_url": "",
"major_model_version": "",
"model_name": "",
"metadata": {
"tags": "Chinese",
"prompt": "",
"stem_from_id": "a624123d-22cc-4d4d-bf28-78d312f61597",
"type": "stem",
"duration": 217.24
},
"is_liked": false,
"user_id": "58387c47-dc80-466f-a7b1-a2eed61c24fb",
"display_name": "FluidXylophone2289",
"handle": "fluidxylophone2289",
"is_handle_updated": false,
"avatar_image_url": "[https://cdn1.suno.ai/defaultPink.webp](https://cdn1.suno.ai/defaultPink.webp)",
"is_trashed": false,
"created_at": "2024-12-25T16:51:36.625Z",
"status": "queued",
"title": "骑在梦想龙的脊背 - Instrumental",
"play_count": 0,
"upvote_count": 0,
"is_public": false
}
]
}
C.获取结果
get {{BASE_URL}}/suno/feed/5f3587e2-75fb-4c36-84b3-3ec113897a4c,9c85d619-4cac-4561-8fa3-604c116fa1c5
返回体
[
{
"audio_url": "[https://cdn1.suno.ai/5f3587e2-75fb-4c36-84b3-3ec113897a4c.mp3](https://cdn1.suno.ai/5f3587e2-75fb-4c36-84b3-3ec113897a4c.mp3)",
"avatar_image_url": "[https://cdn1.suno.ai/defaultPink.webp](https://cdn1.suno.ai/defaultPink.webp)",
"created_at": "2024-12-25T16:51:36.619Z",
"display_name": "FluidXylophone2289",
"handle": "fluidxylophone2289",
"id": "5f3587e2-75fb-4c36-84b3-3ec113897a4c",
"image_large_url": "[https://cdn2.suno.ai/image_large_5f3587e2-75fb-4c36-84b3-3ec113897a4c.jpeg](https://cdn2.suno.ai/image_large_5f3587e2-75fb-4c36-84b3-3ec113897a4c.jpeg)",
"image_url": "[https://cdn2.suno.ai/image_5f3587e2-75fb-4c36-84b3-3ec113897a4c.jpeg](https://cdn2.suno.ai/image_5f3587e2-75fb-4c36-84b3-3ec113897a4c.jpeg)",
"is_handle_updated": false,
"is_liked": false,
"is_public": false,
"is_trashed": false,
"major_model_version": "",
"metadata": {
"duration": 217.24,
"prompt": "在那遥远的星空之下，如今谁还在彷徨？\n就像无法游泳的鱼儿，我却只能责怪自己没有坚强的鳍片。\n快将彷徨化成力量，快把挫折当做指南。\n直到梦想实现之前，我坚定地守候着。\n昨天流逝了岁月，明天我将追随风的脚步，攀上高峰。\n呼唤吧，让我们出发，骑在梦想龙的脊背，穿越命运的坎坷。\n摆脱困境的束缚，即使失去了一切，人仍然渴望温暖的拥抱。\n人之所以能体会到他人的快乐，是因为心灵的善良。\n快将彷徨化成力量，快把挫折当做指南。\n我还是那只无法游泳的鱼儿，责怪自己没有坚强的鳍片。",
"stem_from_id": "a624123d-22cc-4d4d-bf28-78d312f61597",
"tags": "Chinese",
"type": "stem"
},
"model_name": "",
"play_count": 0,
"status": "complete",
"title": "骑在梦想龙的脊背 - Vocals",
"upvote_count": 0,
"video_url": "[https://cdn1.suno.ai/5f3587e2-75fb-4c36-84b3-3ec113897a4c.mp4](https://cdn1.suno.ai/5f3587e2-75fb-4c36-84b3-3ec113897a4c.mp4)"
},
{
"audio_url": "[https://cdn1.suno.ai/9c85d619-4cac-4561-8fa3-604c116fa1c5.mp3](https://cdn1.suno.ai/9c85d619-4cac-4561-8fa3-604c116fa1c5.mp3)",
"avatar_image_url": "[https://cdn1.suno.ai/defaultPink.webp](https://cdn1.suno.ai/defaultPink.webp)",
"created_at": "2024-12-25T16:51:36.625Z",
"display_name": "FluidXylophone2289",
"handle": "fluidxylophone2289",
"id": "9c85d619-4cac-4561-8fa3-604c116fa1c5",
"image_large_url": "[https://cdn2.suno.ai/image_large_9c85d619-4cac-4561-8fa3-604c116fa1c5.jpeg](https://cdn2.suno.ai/image_large_9c85d619-4cac-4561-8fa3-604c116fa1c5.jpeg)",
"image_url": "[https://cdn2.suno.ai/image_9c85d619-4cac-4561-8fa3-604c116fa1c5.jpeg](https://cdn2.suno.ai/image_9c85d619-4cac-4561-8fa3-604c116fa1c5.jpeg)",
"is_handle_updated": false,
"is_liked": false,
"is_public": false,
"is_trashed": false,
"major_model_version": "",
"metadata": {
"duration": 217.24,
"prompt": "",
"stem_from_id": "a624123d-22cc-4d4d-bf28-78d312f61597",
"tags": "Chinese",
"type": "stem"
},
"model_name": "",
"play_count": 0,
"status": "complete",
"title": "骑在梦想龙的脊背 - Instrumental",
"upvote_count": 0,
"video_url": "[https://cdn1.suno.ai/9c85d619-4cac-4561-8fa3-604c116fa1c5.mp4](https://cdn1.suno.ai/9c85d619-4cac-4561-8fa3-604c116fa1c5.mp4)"
}
]