# GPT-Image-2 测试样例

> 覆盖 GPT-Image-2 接口文档中的所有示例，包括文生图、高清生成、流式生成、批量生成、图像编辑、局部重绘、多参考图融合。

## 安装依赖

```bash
pip install openai
```

## 用法

```bash
# 运行全部用例（图像编辑类需提供图片）
python test_gptimage.py --api-key sk-xxxx

# 运行指定用例
python test_gptimage.py --api-key sk-xxxx --test 1.1

# 图像编辑（需指定图片路径）
python test_gptimage.py --api-key sk-xxxx --test 2.1 --image /path/to/image.png

# 局部重绘（需指定图片和 mask）
python test_gptimage.py --api-key sk-xxxx --test 2.2 --image /path/to/image.png --mask /path/to/mask.png
```

## 完整代码

```python
"""
GPT Image 接口测试文件
覆盖 gptimage接口文档.md 中的所有示例接口

用法：
    python test_gptimage.py --api-key sk-xxxx
    python test_gptimage.py --api-key sk-xxxx --test 1.1
    python test_gptimage.py --api-key sk-xxxx --test 2.1 --image /path/to/image.png
    python test_gptimage.py --api-key sk-xxxx --test 2.2 --image /path/to/image.png --mask /path/to/mask.png
"""

import argparse
import base64
import sys
from pathlib import Path
from openai import OpenAI

BASE_URL = "https://tokens.smartfashionai.cn/v1"


def make_client(api_key: str) -> OpenAI:
    return OpenAI(api_key=api_key, base_url=BASE_URL)


def save_b64(b64: str, path: str):
    with open(path, "wb") as f:
        f.write(base64.b64decode(b64))
    print(f"  ✓ 已保存: {path}")


# ── 一、文生图 ────────────────────────────────────────────────

def test_1_1_basic(client: OpenAI):
    """1.1 基础文生图"""
    print("\n[1.1] 基础文生图")
    response = client.images.generate(
        model="gpt-image-2",
        prompt="一只在樱花树下打盹的橘猫，水彩画风格",
        n=1,
        size="1024x1024",
    )
    b64 = response.data[0].b64_json
    if b64:
        save_b64(b64, "output_1_1.png")
    else:
        print("  ✓ url:", response.data[0].url)


def test_1_2_hd(client: OpenAI):
    """1.2 高清生成"""
    print("\n[1.2] 高清生成")
    response = client.images.generate(
        model="gpt-image-2",
        prompt="未来城市夜景，赛博朋克风格，霓虹灯倒映在雨后街道",
        size="2048x1152",
        quality="high",
        extra_body={"output_format": "webp", "output_compression": 85},
    )
    b64 = response.data[0].b64_json
    if b64:
        save_b64(b64, "output_1_2.webp")
    else:
        print("  ✓ url:", response.data[0].url)


def test_1_3_stream(client: OpenAI):
    """1.3 流式生成（SSE）"""
    print("\n[1.3] 流式生成（SSE）")
    response = client.images.generate(
        model="gpt-image-2",
        prompt="山间云雾缭绕的古寺，中国水墨画风格",
        extra_body={"stream": True, "partial_images": 2},
    )
    b64 = response.data[0].b64_json
    if b64:
        save_b64(b64, "output_1_3.png")
    else:
        print("  ✓ url:", response.data[0].url)


def test_1_4_batch(client: OpenAI):
    """1.4 批量生成多张图片"""
    print("\n[1.4] 批量生成（n=2）")
    response = client.images.generate(
        model="gpt-image-2",
        prompt="极简风格的产品展示图，白色背景，专业摄影",
        n=2,
        size="1024x1024",
        quality="medium",
    )
    for i, img in enumerate(response.data):
        b64 = img.b64_json
        if b64:
            save_b64(b64, f"output_1_4_{i+1}.png")
        else:
            print(f"  ✓ [{i+1}] url:", img.url)


# ── 二、图像编辑 ──────────────────────────────────────────────

def test_2_1_edit(client: OpenAI, image_path: str):
    """2.1 基础图像编辑"""
    print("\n[2.1] 基础图像编辑")
    if not Path(image_path).exists():
        print(f"  ⚠ 跳过：图片文件不存在 {image_path}（用 --image 指定）")
        return
    with open(image_path, "rb") as f:
        response = client.images.edit(
            model="gpt-image-2",
            image=f,
            prompt="将背景替换为日落时分的海滩",
            size="1024x1024",
        )
    b64 = response.data[0].b64_json
    if b64:
        save_b64(b64, "output_2_1_edited.png")
    else:
        print("  ✓ url:", response.data[0].url)


def test_2_2_inpaint(client: OpenAI, image_path: str, mask_path: str):
    """2.2 局部重绘（带 mask）"""
    print("\n[2.2] 局部重绘（带 mask）")
    if not Path(image_path).exists():
        print(f"  ⚠ 跳过：图片文件不存在 {image_path}（用 --image 指定）")
        return
    if not Path(mask_path).exists():
        print(f"  ⚠ 跳过：mask 文件不存在 {mask_path}（用 --mask 指定）")
        return
    with open(image_path, "rb") as img_f, open(mask_path, "rb") as mask_f:
        response = client.images.edit(
            model="gpt-image-2",
            image=img_f,
            mask=mask_f,
            prompt="在透明区域添加一只白色的猫",
            size="1024x1024",
        )
    b64 = response.data[0].b64_json
    if b64:
        save_b64(b64, "output_2_2_inpainted.png")
    else:
        print("  ✓ url:", response.data[0].url)


def test_2_3_multi_ref(client: OpenAI, image_path: str):
    """2.3 多参考图融合"""
    print("\n[2.3] 多参考图融合")
    if not Path(image_path).exists():
        print(f"  ⚠ 跳过：图片文件不存在 {image_path}（用 --image 指定）")
        return
    with open(image_path, "rb") as f1, open(image_path, "rb") as f2:
        response = client.images.edit(
            model="gpt-image-2",
            image=[f1, f2],
            prompt="将两张图片的风格融合，生成统一风格的新图",
            size="1024x1024",
        )
    b64 = response.data[0].b64_json
    if b64:
        save_b64(b64, "output_2_3_merged.png")
    else:
        print("  ✓ url:", response.data[0].url)


# ── 主入口 ────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="GPT Image 接口测试")
    parser.add_argument("--api-key", required=True, help="API Key（sk-xxxx）")
    parser.add_argument("--test", default="all", help="指定用例编号，如 1.1 / 2.1，默认 all")
    parser.add_argument("--image", default="test_image.png", help="图像编辑用的原图路径")
    parser.add_argument("--mask", default="test_mask.png", help="局部重绘用的 mask 路径")
    args = parser.parse_args()

    client = make_client(args.api_key)

    ALL_TESTS = {
        "1.1": lambda: test_1_1_basic(client),
        "1.2": lambda: test_1_2_hd(client),
        "1.3": lambda: test_1_3_stream(client),
        "1.4": lambda: test_1_4_batch(client),
        "2.1": lambda: test_2_1_edit(client, args.image),
        "2.2": lambda: test_2_2_inpaint(client, args.image, args.mask),
        "2.3": lambda: test_2_3_multi_ref(client, args.image),
    }

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
            fn()
            passed += 1
        except Exception as e:
            print(f"  ✗ [{name}] 失败: {e}")
            failed += 1

    print(f"\n{'='*40}")
    print(f"结果: {passed} 通过 / {failed} 失败")


if __name__ == "__main__":
    main()
```
