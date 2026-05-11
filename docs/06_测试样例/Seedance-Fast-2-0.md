# Seedance Fast 2.0 测试样例

> 覆盖 Seedance Fast 2.0 接口文档中的所有示例，包括文生视频、图生视频、视频生视频、多模态。

## 安装依赖

```bash
pip install requests
```

## 用法

```bash
# 运行全部用例
python test_seedance_fast2.py --api-key sk-xxxx

# 运行指定用例
python test_seedance_fast2.py --api-key sk-xxxx --test 文生视频

# 查询已有任务状态
python test_seedance_fast2.py --api-key sk-xxxx --task-id task_xxxx
```

## 完整代码

```python
"""
Seedance Fast 2.0 接口测试文件
覆盖 02_Seedance-Fast-2-0-视频生成.md 中的所有示例接口

用法：
    python test_seedance_fast2.py --api-key sk-xxxx
    python test_seedance_fast2.py --api-key sk-xxxx --test 文生视频
    python test_seedance_fast2.py --api-key sk-xxxx --task-id task_xxxx
"""

import argparse
import sys
import time
import requests

BASE_URL = "https://tokens.smartfashionai.cn"


def make_headers(api_key: str) -> dict:
    return {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}


# ── 轮询工具 ──────────────────────────────────────────────────

def poll_task(api_key: str, task_id: str, interval: int = 5, timeout: int = 300) -> dict:
    headers = make_headers(api_key)
    deadline = time.time() + timeout
    while time.time() < deadline:
        resp = requests.get(f"{BASE_URL}/v1/video/generations/{task_id}", headers=headers)
        resp.raise_for_status()
        result = resp.json()
        status = result["data"]["status"]
        print(f"    状态: {status}  进度: {result['data'].get('progress', '-')}")
        if status in ("SUCCESS", "SUCCEEDED", "COMPLETED"):
            return result
        if status in ("FAILURE", "FAILED", "CANCELLED", "EXPIRED"):
            raise RuntimeError(f"任务失败: {result['data'].get('fail_reason')}")
        time.sleep(interval)
    raise TimeoutError(f"任务 {task_id} 超时（{timeout}s）")


def submit(api_key: str, payload: dict) -> str:
    headers = make_headers(api_key)
    resp = requests.post(f"{BASE_URL}/v1/video/generations", json=payload, headers=headers)
    resp.raise_for_status()
    task_id = resp.json()["task_id"]
    print(f"  已提交，task_id = {task_id}")
    return task_id


# ── 测试用例 ──────────────────────────────────────────────────

def test_text_to_video(api_key: str):
    """文生视频"""
    print("\n[文生视频] seedance-2.0-fast 720p 16:9")
    task_id = submit(api_key, {
        "model": "seedance-2.0-fast",
        "prompt": "一只猫在草地上奔跑，阳光明媚，镜头缓慢推进",
        "duration": 5,
        "metadata": {"resolution": "720p", "ratio": "16:9"},
    })
    result = poll_task(api_key, task_id)
    print(f"  ✓ 视频地址: {result['data']['result_url']}")


def test_image_to_video(api_key: str):
    """图生视频（首帧）"""
    print("\n[图生视频（首帧）] seedance-2.0-fast 720p 9:16")
    task_id = submit(api_key, {
        "model": "seedance-2.0-fast",
        "prompt": "人物优雅地转身，微风吹起裙摆",
        "duration": 5,
        "metadata": {
            "resolution": "720p",
            "ratio": "9:16",
            "content": [
                {
                    "type": "image_url",
                    "role": "first_frame",
                    "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png"},
                }
            ],
        },
    })
    result = poll_task(api_key, task_id)
    print(f"  ✓ 视频地址: {result['data']['result_url']}")


def test_video_to_video(api_key: str):
    """视频生视频（参考视频）"""
    print("\n[视频生视频] seedance-2.0-fast 720p 16:9")
    task_id = submit(api_key, {
        "model": "seedance-2.0-fast",
        "prompt": "将原视频场景转换为赛博朋克风格，霓虹灯光，雨夜氛围",
        "duration": 5,
        "metadata": {
            "resolution": "720p",
            "ratio": "16:9",
            "content": [
                {
                    "type": "video_url",
                    "role": "reference_video",
                    "video_url": {"url": "https://www.w3schools.com/html/mov_bbb.mp4"},
                }
            ],
        },
    })
    result = poll_task(api_key, task_id)
    print(f"  ✓ 视频地址: {result['data']['result_url']}")


def test_multimodal(api_key: str):
    """多模态（视频 + 参考图 + 音频）"""
    print("\n[多模态] seedance-2.0-fast 视频+图+音频")
    task_id = submit(api_key, {
        "model": "seedance-2.0-fast",
        "prompt": "根据参考视频的场景和参考图的风格，生成一段新的视频",
        "duration": 5,
        "metadata": {
            "resolution": "720p",
            "ratio": "16:9",
            "content": [
                {
                    "type": "video_url",
                    "role": "reference_video",
                    "video_url": {"url": "https://www.w3schools.com/html/mov_bbb.mp4"},
                },
                {
                    "type": "image_url",
                    "role": "reference_image",
                    "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png"},
                },
                {
                    "type": "audio_url",
                    "role": "reference_audio",
                    "audio_url": {"url": "https://www.w3schools.com/html/horse.mp3"},
                },
            ],
        },
    })
    result = poll_task(api_key, task_id)
    print(f"  ✓ 视频地址: {result['data']['result_url']}")


def test_query_status(api_key: str, task_id: str):
    """查询任务状态"""
    print(f"\n[查询任务状态] task_id={task_id}")
    headers = make_headers(api_key)
    resp = requests.get(f"{BASE_URL}/v1/video/generations/{task_id}", headers=headers)
    resp.raise_for_status()
    data = resp.json()
    print(f"  ✓ status={data['data']['status']}  progress={data['data'].get('progress', '-')}")
    if data["data"].get("result_url"):
        print(f"  ✓ 视频地址: {data['data']['result_url']}")


# ── 主入口 ────────────────────────────────────────────────────

ALL_TESTS = {
    "文生视频":   test_text_to_video,
    "图生视频":   test_image_to_video,
    "视频生视频": test_video_to_video,
    "多模态":     test_multimodal,
}


def main():
    parser = argparse.ArgumentParser(description="Seedance Fast 2.0 接口测试")
    parser.add_argument("--api-key", required=True, help="API Key（sk-xxxx）")
    parser.add_argument("--test", default="all",
                        help="指定用例名称：文生视频 / 图生视频 / 视频生视频 / 多模态，默认 all")
    parser.add_argument("--task-id", default="", help="直接查询已有任务状态")
    args = parser.parse_args()

    if args.task_id:
        test_query_status(args.api_key, args.task_id)
        return

    if args.test == "all":
        targets = list(ALL_TESTS.items())
    else:
        if args.test not in ALL_TESTS:
            print(f"未知用例: {args.test}，可选: {list(ALL_TESTS.keys())}")
            sys.exit(1)
        targets = [(args.test, ALL_TESTS[args.test])]

    passed = failed = 0
    for name, fn in targets:
        try:
            fn(args.api_key)
            passed += 1
        except Exception as e:
            print(f"  ✗ [{name}] 失败: {e}")
            failed += 1

    print(f"\n{'='*40}")
    print(f"结果: {passed} 通过 / {failed} 失败")


if __name__ == "__main__":
    main()
```
