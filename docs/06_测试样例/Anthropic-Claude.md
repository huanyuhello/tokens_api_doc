# Anthropic Claude 测试样例

> 覆盖 Claude 接口文档中的所有示例，支持 OpenAI 协议与 Anthropic 协议。

## 安装依赖

```bash
pip install openai anthropic
```

## 用法

```bash
# 运行全部用例
python test_claude.py --api-key sk-xxxx

# 运行指定用例
python test_claude.py --api-key sk-xxxx --test 1.1
```

## 完整代码

```python
"""
Claude 接口测试文件
覆盖 claudecode接口文档.md 中的所有示例接口（OpenAI 协议 + Anthropic 协议）

用法：
    python test_claude.py --api-key sk-xxxx
    python test_claude.py --api-key sk-xxxx --test 1.1
"""

import argparse
import base64
import json
import sys
from pathlib import Path
from openai import OpenAI
import anthropic

BASE_URL = "https://tokens.smartfashionai.cn"


def make_openai_client(api_key: str) -> OpenAI:
    return OpenAI(api_key=api_key, base_url=f"{BASE_URL}/v1")


def make_anthropic_client(api_key: str) -> anthropic.Anthropic:
    return anthropic.Anthropic(api_key=api_key, base_url=BASE_URL)


# ── 一、OpenAI 协议 ───────────────────────────────────────────

def test_1_1_basic(client: OpenAI):
    """1.1 文本生成（OpenAI 协议）"""
    print("\n[1.1] 文本生成（OpenAI 协议）")
    response = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": "请用一句话介绍量子计算"}],
        max_tokens=1024,
    )
    print("  ✓", response.choices[0].message.content)


def test_1_2_stream(client: OpenAI):
    """1.2 流式输出（OpenAI 协议）"""
    print("\n[1.2] 流式输出（OpenAI 协议）")
    stream = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": "写一首关于秋天的短诗"}],
        max_tokens=512,
        stream=True,
    )
    print("  ✓ ", end="")
    for chunk in stream:
        if not chunk.choices:
            continue
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
    print()


def test_1_3_image(client: OpenAI):
    """1.3 图片理解（OpenAI 协议）"""
    print("\n[1.3] 图片理解（OpenAI 协议）")
    response = client.chat.completions.create(
        model="claude-opus-4-6",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png"}},
                    {"type": "text", "text": "请描述这张图片的内容"},
                ],
            }
        ],
        max_tokens=1024,
    )
    print("  ✓", response.choices[0].message.content[:100], "...")


def test_1_4_tool_use(client: OpenAI):
    """1.4 函数调用（OpenAI 协议）"""
    print("\n[1.4] 函数调用（OpenAI 协议）")
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "获取指定城市的当前天气",
                "parameters": {
                    "type": "object",
                    "properties": {"city": {"type": "string", "description": "城市名称，如北京、上海"}},
                    "required": ["city"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": "北京今天天气怎么样？"}],
        tools=tools,
        tool_choice="auto",
        max_tokens=1024,
    )
    message = response.choices[0].message
    if message.tool_calls:
        for tc in message.tool_calls:
            args = json.loads(tc.function.arguments)
            print(f"  ✓ 调用函数: {tc.function.name}，参数: {args}")
    else:
        print("  ✓ 直接回答:", message.content)


def test_1_5_thinking(client: OpenAI):
    """1.5 扩展思考（OpenAI 协议）"""
    print("\n[1.5] 扩展思考（OpenAI 协议）")
    response = client.chat.completions.create(
        model="claude-opus-4-6",
        messages=[{"role": "user", "content": "请分析：一家初创公司是否应该在早期就引入微服务架构？"}],
        extra_body={"thinking": {"type": "adaptive", "budget_tokens": 2000}},
        max_tokens=4000,
    )
    content = response.choices[0].message.content
    print("  ✓", (content or "")[:100], "...")


# ── 二、Anthropic 协议 ────────────────────────────────────────

def test_2_1_basic(ac: anthropic.Anthropic):
    """2.1 文本生成（Anthropic 协议）"""
    print("\n[2.1] 文本生成（Anthropic 协议）")
    message = ac.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": "请用一句话介绍量子计算"}],
    )
    print("  ✓", message.content[0].text)


def test_2_2_image(ac: anthropic.Anthropic):
    """2.2 图片理解（Anthropic 协议）"""
    print("\n[2.2] 图片理解（Anthropic 协议）")
    message = ac.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "image", "source": {"type": "url", "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/280px-PNG_transparency_demonstration_1.png"}},
                    {"type": "text", "text": "请描述这张图片的内容"},
                ],
            }
        ],
    )
    print("  ✓", message.content[0].text[:100], "...")


def test_2_3_thinking(ac: anthropic.Anthropic):
    """2.3 扩展思考（Anthropic 协议）"""
    print("\n[2.3] 扩展思考（Anthropic 协议）")
    response = ac.messages.create(
        model="claude-opus-4-6",
        max_tokens=4000,
        thinking={"type": "adaptive", "budget_tokens": 2000},
        messages=[{"role": "user", "content": "请分析：一家初创公司是否应该在早期就引入微服务架构？"}],
    )
    for block in response.content:
        if block.type == "thinking":
            print(f"  [思考] {block.thinking[:60]}...")
        elif block.type == "text":
            print(f"  ✓ {block.text[:100]}...")


def test_2_4_tool_use(ac: anthropic.Anthropic):
    """2.4 函数调用（Anthropic 协议）"""
    print("\n[2.4] 函数调用（Anthropic 协议）")
    response = ac.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        tools=[
            {
                "name": "get_weather",
                "description": "获取指定城市的当前天气",
                "input_schema": {
                    "type": "object",
                    "properties": {"city": {"type": "string", "description": "城市名称，如北京、上海"}},
                    "required": ["city"],
                },
            }
        ],
        messages=[{"role": "user", "content": "北京今天天气怎么样？"}],
    )
    for block in response.content:
        if block.type == "tool_use":
            print(f"  ✓ 调用函数: {block.name}，参数: {block.input}")
        elif block.type == "text":
            print(f"  ✓ 直接回答: {block.text}")


# ── 主入口 ────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Claude 接口测试")
    parser.add_argument("--api-key", required=True, help="API Key（sk-xxxx）")
    parser.add_argument("--test", default="all", help="指定用例编号，如 1.1 / 2.3，默认 all")
    args = parser.parse_args()

    oc = make_openai_client(args.api_key)
    ac = make_anthropic_client(args.api_key)

    ALL_TESTS = {
        "1.1": lambda: test_1_1_basic(oc),
        "1.2": lambda: test_1_2_stream(oc),
        "1.3": lambda: test_1_3_image(oc),
        "1.4": lambda: test_1_4_tool_use(oc),
        "1.5": lambda: test_1_5_thinking(oc),
        "2.1": lambda: test_2_1_basic(ac),
        "2.2": lambda: test_2_2_image(ac),
        "2.3": lambda: test_2_3_thinking(ac),
        "2.4": lambda: test_2_4_tool_use(ac),
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
