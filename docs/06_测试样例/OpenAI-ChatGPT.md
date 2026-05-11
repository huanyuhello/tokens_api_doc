# OpenAI ChatGPT 测试样例

> 覆盖 ChatGPT 接口文档中的所有示例，包括文本生成、图片理解、函数调用、联网搜索、多轮对话。

## 安装依赖

```bash
pip install openai
```

## 用法

```bash
# 运行全部用例
python test_chatgpt.py --api-key sk-xxxx

# 运行指定用例
python test_chatgpt.py --api-key sk-xxxx --test 1.1
```

## 完整代码

```python
"""
ChatGPT 接口测试文件
覆盖 chatgpt接口文档.md 中的所有示例接口

用法：
    python test_chatgpt.py --api-key sk-xxxx
    python test_chatgpt.py --api-key sk-xxxx --test 1.1
"""

import argparse
import json
import sys
from openai import OpenAI

BASE_URL = "https://tokens.smartfashionai.cn/v1"


def make_client(api_key: str) -> OpenAI:
    return OpenAI(api_key=api_key, base_url=BASE_URL)


# ── 一、文本生成 ──────────────────────────────────────────────

def test_1_1_basic(client: OpenAI):
    """1.1 基础文本生成"""
    print("\n[1.1] 基础文本生成")
    response = client.chat.completions.create(
        model="gpt-5.4",
        messages=[{"role": "user", "content": "请用一句话介绍量子计算"}],
        max_tokens=1024,
    )
    print("  ✓", response.choices[0].message.content)


def test_1_2_system_prompt(client: OpenAI):
    """1.2 带系统提示词"""
    print("\n[1.2] 带系统提示词")
    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {"role": "system", "content": "你是一位专业的代码审查工程师，请用简洁专业的语言回答问题。"},
            {"role": "user", "content": "如何避免 SQL 注入攻击？"},
        ],
        max_tokens=2048,
        temperature=0.7,
    )
    print("  ✓", response.choices[0].message.content[:100], "...")


def test_1_3_stream(client: OpenAI):
    """1.3 流式输出"""
    print("\n[1.3] 流式输出")
    stream = client.chat.completions.create(
        model="gpt-5.4",
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


def test_1_4_multi_turn(client: OpenAI):
    """1.4 多轮对话"""
    print("\n[1.4] 多轮对话")
    response = client.chat.completions.create(
        model="gpt-5.4",
        messages=[
            {"role": "user", "content": "Python 中列表和元组有什么区别？"},
            {"role": "assistant", "content": "列表是可变的，元组是不可变的。列表用方括号 [] 定义，元组用圆括号 () 定义。"},
            {"role": "user", "content": "那什么时候应该用元组？"},
        ],
        max_tokens=1024,
    )
    print("  ✓", response.choices[0].message.content[:100], "...")


# ── 二、图片理解 ──────────────────────────────────────────────

def test_2_image_url(client: OpenAI):
    """二、图片理解（URL）"""
    print("\n[2] 图片理解（URL）")
    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": "https://www.gstatic.com/webp/gallery/1.jpg"}},
                    {"type": "text", "text": "请描述这张图片的内容"},
                ],
            }
        ],
        max_tokens=1024,
    )
    print("  ✓", response.choices[0].message.content[:100], "...")


# ── 三、函数调用 ──────────────────────────────────────────────

def test_3_tool_use(client: OpenAI):
    """三、函数调用（Tool Use）"""
    print("\n[3] 函数调用")
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "获取指定城市的当前天气",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "城市名称，如北京、上海"},
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"], "description": "温度单位"},
                    },
                    "required": ["city"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="gpt-5.4",
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


# ── 四、联网搜索 ──────────────────────────────────────────────

def test_4_web_search(client: OpenAI):
    """四、联网搜索（Web Search）"""
    print("\n[4] 联网搜索")
    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[{"role": "user", "content": "2025年最新的AI大模型有哪些？"}],
        max_tokens=2048,
    )
    print("  ✓", response.choices[0].message.content[:150], "...")


# ── 五、多轮对话含函数回传 ────────────────────────────────────

def test_5_multi_turn_tool(client: OpenAI):
    """五、多轮对话（含函数结果回传）"""
    print("\n[5] 多轮对话（含函数结果回传）")

    def get_weather(city: str) -> str:
        return f"{city}今天晴，气温 22°C，微风"

    messages = [{"role": "user", "content": "北京今天天气怎么样？"}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "获取指定城市的当前天气",
                "parameters": {
                    "type": "object",
                    "properties": {"city": {"type": "string"}},
                    "required": ["city"],
                },
            },
        }
    ]

    response = client.chat.completions.create(
        model="gpt-5.4", messages=messages, tools=tools, tool_choice="auto", max_tokens=1024
    )
    assistant_message = response.choices[0].message
    assistant_dict = {"role": "assistant", "content": assistant_message.content}
    if assistant_message.tool_calls:
        assistant_dict["tool_calls"] = [
            {
                "id": tc.id,
                "type": "function",
                "function": {"name": tc.function.name, "arguments": tc.function.arguments},
            }
            for tc in assistant_message.tool_calls
        ]
    messages.append(assistant_dict)

    if assistant_message.tool_calls:
        for tc in assistant_message.tool_calls:
            args = json.loads(tc.function.arguments)
            result = get_weather(**args)
            messages.append({"role": "tool", "tool_call_id": tc.id, "content": result})

    final = client.chat.completions.create(model="gpt-5.4", messages=messages, max_tokens=1024)
    print("  ✓", final.choices[0].message.content)


# ── 主入口 ────────────────────────────────────────────────────

ALL_TESTS = {
    "1.1": test_1_1_basic,
    "1.2": test_1_2_system_prompt,
    "1.3": test_1_3_stream,
    "1.4": test_1_4_multi_turn,
    "2":   test_2_image_url,
    "3":   test_3_tool_use,
    "4":   test_4_web_search,
    "5":   test_5_multi_turn_tool,
}


def main():
    parser = argparse.ArgumentParser(description="ChatGPT 接口测试")
    parser.add_argument("--api-key", required=True, help="API Key（sk-xxxx）")
    parser.add_argument("--test", default="all", help="指定用例编号，如 1.1 / 3，默认 all")
    args = parser.parse_args()

    client = make_client(args.api_key)

    if args.test == "all":
        targets = list(ALL_TESTS.values())
    else:
        if args.test not in ALL_TESTS:
            print(f"未知用例: {args.test}，可选: {list(ALL_TESTS.keys())}")
            sys.exit(1)
        targets = [ALL_TESTS[args.test]]

    passed = failed = 0
    for fn in targets:
        try:
            fn(client)
            passed += 1
        except Exception as e:
            print(f"  ✗ {fn.__doc__} 失败: {e}")
            failed += 1

    print(f"\n{'='*40}")
    print(f"结果: {passed} 通过 / {failed} 失败")


if __name__ == "__main__":
    main()
```
