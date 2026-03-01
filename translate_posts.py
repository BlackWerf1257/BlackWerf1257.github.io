"""
Zola 다국어 자동 번역 스크립트
사용법: python translate_posts.py --api-key YOUR_DEEPL_API_KEY [옵션]

필요 패키지 설치:
    pip install deepl

DeepL 무료 API 키 발급:
    https://www.deepl.com/ko/pro-api (신용카드 없이 가입 가능)
"""

import os
import re
import argparse
import deepl

# ─────────────────────────────────────────────
# 설정
# ─────────────────────────────────────────────

# 번역할 대상 언어 목록 (DeepL 언어 코드 : Zola 파일 확장자)
TARGET_LANGUAGES = {
    "EN-US": "en",
    "JA":    "ja",
}

# 번역하지 않을 frontmatter 필드 (원본 값 유지)
SKIP_FRONTMATTER_FIELDS = {"date", "slug", "taxonomies", "extra", "template", "weight"}

# 번역할 frontmatter 필드
TRANSLATE_FRONTMATTER_FIELDS = {"title", "description"}


# ─────────────────────────────────────────────
# 마크다운 파싱
# ─────────────────────────────────────────────

def parse_frontmatter(content: str):
    """
    TOML frontmatter(+++ ... +++)와 본문을 분리합니다.
    반환: (frontmatter_text, body_text) 또는 (None, content)
    """
    match = re.match(r"^\+\+\+\s*\n(.*?)\n\+\+\+\s*\n(.*)", content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return None, content


def rebuild_content(frontmatter: str, body: str) -> str:
    return f"+++\n{frontmatter}\n+++\n{body}"


# ─────────────────────────────────────────────
# frontmatter 번역
# ─────────────────────────────────────────────

def translate_frontmatter(frontmatter: str, translator: deepl.Translator, target_lang: str) -> str:
    """
    frontmatter에서 번역 대상 필드만 번역합니다.
    나머지 필드는 그대로 유지합니다.
    """
    lines = frontmatter.split("\n")
    result = []
    for line in lines:
        # key = value 형태 파싱
        m = re.match(r'^(\w+)\s*=\s*"(.+)"$', line.strip())
        if m:
            key, value = m.group(1), m.group(2)
            if key in TRANSLATE_FRONTMATTER_FIELDS:
                translated = translator.translate_text(value, target_lang=target_lang).text
                # 원본 들여쓰기 유지
                indent = len(line) - len(line.lstrip())
                result.append(f'{" " * indent}{key} = "{translated}"')
                continue
        result.append(line)
    return "\n".join(result)


# ─────────────────────────────────────────────
# 본문 번역 (코드 블록 보호)
# ─────────────────────────────────────────────

PLACEHOLDER_PATTERN = "CODEBLOCK_{index}_PLACEHOLDER"

def protect_code_blocks(body: str):
    """
    코드 블록(```...```)을 플레이스홀더로 교체하여 번역 대상에서 제외합니다.
    반환: (보호된 본문, {플레이스홀더: 원본코드} 딕셔너리)
    """
    code_blocks = {}
    counter = [0]

    def replacer(m):
        placeholder = PLACEHOLDER_PATTERN.format(index=counter[0])
        code_blocks[placeholder] = m.group(0)
        counter[0] += 1
        return placeholder

    protected = re.sub(r"```[\s\S]*?```", replacer, body)
    # 인라인 코드도 보호
    protected = re.sub(r"`[^`\n]+`", replacer, protected)
    return protected, code_blocks


def restore_code_blocks(body: str, code_blocks: dict) -> str:
    for placeholder, original in code_blocks.items():
        body = body.replace(placeholder, original)
    return body


def translate_body(body: str, translator: deepl.Translator, target_lang: str) -> str:
    """
    본문을 번역합니다. 코드 블록은 번역하지 않습니다.
    """
    protected, code_blocks = protect_code_blocks(body)

    # 단락 단위로 나눠서 번역 (빈 줄은 유지)
    paragraphs = re.split(r"(\n{2,})", protected)
    translated_parts = []

    for part in paragraphs:
        # 빈 줄 구분자는 그대로 유지
        if re.match(r"^\n+$", part):
            translated_parts.append(part)
            continue

        # 플레이스홀더만 있는 줄은 번역 불필요
        if all(
            token.strip() == "" or re.match(r"CODEBLOCK_\d+_PLACEHOLDER", token.strip())
            for token in part.split("\n")
        ):
            translated_parts.append(part)
            continue

        # 마크다운 링크/이미지 URL은 번역 제외를 위해 텍스트만 번역
        try:
            result = translator.translate_text(part, target_lang=target_lang)
            translated_parts.append(result.text)
        except Exception as e:
            print(f"  ⚠ 번역 실패 (원본 유지): {e}")
            translated_parts.append(part)

    restored = restore_code_blocks("".join(translated_parts), code_blocks)
    return restored


# ─────────────────────────────────────────────
# 파일 처리
# ─────────────────────────────────────────────

def get_output_path(source_path: str, lang_suffix: str) -> str:
    """
    hello.md  →  hello.en.md
    hello.ko.md 는 건너뜁니다.
    """
    base, ext = os.path.splitext(source_path)
    # 이미 언어 접미사가 있는 파일은 건너뜀
    for suffix in TARGET_LANGUAGES.values():
        if base.endswith(f".{suffix}"):
            return None
    return f"{base}.{lang_suffix}{ext}"


def translate_file(source_path: str, translator: deepl.Translator, force: bool = False):
    """
    단일 마크다운 파일을 모든 대상 언어로 번역합니다.
    """
    with open(source_path, "r", encoding="utf-8") as f:
        content = f.read()

    frontmatter, body = parse_frontmatter(content)

    for deepl_lang, zola_suffix in TARGET_LANGUAGES.items():
        output_path = get_output_path(source_path, zola_suffix)
        if output_path is None:
            continue  # 이미 번역된 파일

        if os.path.exists(output_path) and not force:
            print(f"  ⏭ 스킵 (이미 존재): {output_path}")
            continue

        print(f"  🌐 번역 중 [{deepl_lang}]: {output_path}")

        try:
            if frontmatter:
                translated_fm = translate_frontmatter(frontmatter, translator, deepl_lang)
                translated_body = translate_body(body, translator, deepl_lang)
                translated_content = rebuild_content(translated_fm, translated_body)
            else:
                translated_content = translate_body(content, translator, deepl_lang)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(translated_content)

            print(f"  ✅ 완료: {output_path}")

        except Exception as e:
            print(f"  ❌ 오류: {e}")


# ─────────────────────────────────────────────
# 메인
# ─────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Zola 블로그 마크다운 파일을 DeepL로 자동 번역합니다."
    )
    parser.add_argument(
        "--api-key", required=True,
        help="DeepL API 키 (https://www.deepl.com/ko/pro-api 에서 무료 발급)"
    )
    parser.add_argument(
        "--content-dir", default="content",
        help="Zola content 폴더 경로 (기본값: ./content)"
    )
    parser.add_argument(
        "--file", default=None,
        help="특정 파일만 번역 (예: content/posts/hello.md)"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="이미 존재하는 번역 파일도 덮어씁니다"
    )
    args = parser.parse_args()

    # DeepL 클라이언트 초기화 (무료 키는 자동 감지됨)
    translator = deepl.Translator(args.api_key)

    # 남은 사용량 확인
    usage = translator.get_usage()
    print(f"📊 DeepL 사용량: {usage.character.count:,} / {usage.character.limit:,} 자")

    if args.file:
        # 단일 파일 번역
        if not os.path.exists(args.file):
            print(f"❌ 파일을 찾을 수 없습니다: {args.file}")
            return
        print(f"\n📄 {args.file}")
        translate_file(args.file, translator, force=args.force)
    else:
        # content 폴더 전체 순회
        md_files = []
        for root, _, files in os.walk(args.content_dir):
            for fname in files:
                if fname.endswith(".md"):
                    md_files.append(os.path.join(root, fname))

        # 이미 번역된 파일(예: .en.md, .ja.md) 제외
        source_files = []
        for path in md_files:
            base = os.path.splitext(path)[0]
            is_translated = any(base.endswith(f".{s}") for s in TARGET_LANGUAGES.values())
            if not is_translated:
                source_files.append(path)

        print(f"\n📂 번역 대상 파일: {len(source_files)}개\n")
        for path in source_files:
            print(f"📄 {path}")
            translate_file(path, translator, force=args.force)

    print("\n🎉 번역 완료!")


if __name__ == "__main__":
    main()
