#!/usr/bin/env python3
"""Gemini 接口测试脚本"""
import argparse
import base64
import urllib.request

import google.genai as genai
import google.genai.types as types


API_BASE    = "https://tokens.smartfashionai.cn"
TEXT_MODEL  = "gemini-3.1-pro-preview"
IMAGE_MODEL = "gemini-3.1-flash-image-preview"


def make_client(api_key: str) -> genai.Client:
    return genai.Client(
        api_key=api_key,
        http_options={"base_url": API_BASE},
    )


def _fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read()


# ── 1. 文本生成 ────────────────────────────────────────────────

def test_basic_text(client):
    """1.1 基础文本生成"""
    resp = client.models.generate_content(
        model=TEXT_MODEL,
        contents="你是谁？",
    )
    return resp.text[:40]


def test_system_prompt(client):
    """1.2 系统提示词"""
    resp = client.models.generate_content(
        model=TEXT_MODEL,
        contents="你好",
        config=types.GenerateContentConfig(
            system_instruction="你是一个专业的Python助手，只回答Python相关的问题",
            max_output_tokens=512,
        ),
    )
    return resp.text[:40]


def test_streaming(client):
    """1.3 流式输出"""
    chunks = []
    for chunk in client.models.generate_content_stream(
        model=TEXT_MODEL,
        contents="写一首关于人工智能的五言绝句",
    ):
        if chunk.text:
            chunks.append(chunk.text)
    text = "".join(chunks)
    return f"共 {len(chunks)} 个 chunk，总长 {len(text)} 字"


def test_thinking(client):
    """1.4 思考模式"""
    resp = client.models.generate_content(
        model=TEXT_MODEL,
        contents="天空为什么是蓝色的？",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=2000),
        ),
    )
    return resp.text[:50]


# ── 2. 图片理解 ────────────────────────────────────────────────
# 使用 picsum.photos 提供稳定可访问的测试图片（JPEG 格式）
_IMG_URL_1 = "https://picsum.photos/seed/cat/300/200"
_IMG_URL_2 = "https://picsum.photos/seed/dog/300/200"


def test_image_url(client):
    """2.1 图片理解（下载后以 inline_data 传入）"""
    data = _fetch_bytes(_IMG_URL_1)
    part = types.Part(inline_data=types.Blob(mime_type="image/jpeg", data=data))
    resp = client.models.generate_content(
        model=TEXT_MODEL,
        contents=[part, "这张图片展示了什么？"],
    )
    return resp.text[:40]


def test_image_base64(client):
    """2.2 Base64图片理解"""
    data = _fetch_bytes(_IMG_URL_1)
    b64 = base64.b64encode(data).decode()
    part = types.Part(
        inline_data=types.Blob(mime_type="image/jpeg", data=base64.b64decode(b64))
    )
    resp = client.models.generate_content(
        model=TEXT_MODEL,
        contents=[part, "描述一下这张图片"],
    )
    return resp.text[:40]


def test_multi_image(client):
    """2.3 多图片理解"""
    data1 = _fetch_bytes(_IMG_URL_1)
    data2 = _fetch_bytes(_IMG_URL_2)
    parts = [
        "图片一：",
        types.Part(inline_data=types.Blob(mime_type="image/jpeg", data=data1)),
        "图片二：",
        types.Part(inline_data=types.Blob(mime_type="image/jpeg", data=data2)),
        "分别描述这两张图片",
    ]
    resp = client.models.generate_content(
        model=TEXT_MODEL,
        contents=parts,
    )
    return resp.text[:40]


# ── 3. 图片生成 ────────────────────────────────────────────────

def test_image_generation(client):
    """3.1 图片生成"""
    resp = client.models.generate_content(
        model=IMAGE_MODEL,
        contents="画一只可爱的卡通猫咪",
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
        ),
    )
    for part in resp.candidates[0].content.parts:
        if part.inline_data:
            return f"生成图片: {part.inline_data.mime_type}, {len(part.inline_data.data)} bytes"
    return "未生成图片"


def test_image_generation_b64(client):
    """3.2 图片生成（返回 Base64）"""
    resp = client.models.generate_content(
        model=IMAGE_MODEL,
        contents="画一只可爱的卡通狗狗",
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
        ),
    )
    for part in resp.candidates[0].content.parts:
        if part.inline_data:
            b64 = base64.b64encode(part.inline_data.data).decode()
            return f"Base64 图片: {part.inline_data.mime_type}, {len(b64)} chars"
    return "未生成图片"


# ── 4. 视频理解 ────────────────────────────────────────────────

def test_video(client):
    """4. 视频理解（下载后以 inline_data 传入，代理不支持 file_data.file_uri）"""
    data = _fetch_bytes("https://www.w3schools.com/html/mov_bbb.mp4")
    resp = client.models.generate_content(
        model=VIDEO_MODEL,
        contents=[
            types.Part(inline_data=types.Blob(mime_type="video/mp4", data=data)),
            "这段视频展示了什么内容？请简单描述。",
        ],
    )
    return resp.text[:40]


# ── 5. 工具调用 ────────────────────────────────────────────────

def test_tool_calling(client):
    """5. 工具调用"""
    weather_tool = types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name="get_weather",
                description="获取指定城市的天气信息",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "city": types.Schema(type=types.Type.STRING, description="城市名称"),
                        "unit": types.Schema(type=types.Type.STRING, description="温度单位"),
                    },
                    required=["city"],
                ),
            )
        ]
    )
    resp = client.models.generate_content(
        model=TEXT_MODEL,
        contents="北京今天天气怎么样？用摄氏度",
        config=types.GenerateContentConfig(tools=[weather_tool]),
    )
    for part in resp.candidates[0].content.parts:
        if part.function_call:
            fc = part.function_call
            return f"调用工具: {fc.name}({dict(fc.args)})"
    return "未触发工具调用"


# ── 主测试运行器 ───────────────────────────────────────────────

def run_tests(api_key: str):
    client = make_client(api_key)
    tests = [
        ("1.1 基础文本生成",    test_basic_text),
        ("1.2 系统提示词",      test_system_prompt),
        ("1.3 流式输出",        test_streaming),
        ("1.4 思考模式",        test_thinking),
        ("2.1 图片URL理解",    test_image_url),
        ("2.2 Base64图片理解",  test_image_base64),
        ("2.3 多图片理解",      test_multi_image),
        ("3.1 图片生成",        test_image_generation),
        ("3.2 图片生成(B64)",   test_image_generation_b64),
        ("4. 视频理解",         test_video),
        ("5. 工具调用",         test_tool_calling),
    ]
    passed = failed = 0
    for name, fn in tests:
        print(f"[测试] {name} ... ", end="", flush=True)
        try:
            result = fn(client)
            print(f"✓  {result}")
            passed += 1
        except Exception as e:
            print(f"✗  {e}")
            failed += 1
    print("\n" + "=" * 50)
    print(f"结果: {passed} 通过 / {failed} 失败 / {passed + failed} 总计")
    if failed > 0:
        import sys
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", required=True)
    args = parser.parse_args()
    run_tests(args.api_key)
