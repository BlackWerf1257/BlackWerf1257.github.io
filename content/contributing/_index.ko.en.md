+++
title = "Contribute"
description = "How to Contribute to Goyo"
weight = 7
sort_by = "weight"

[extra]
+++
Thank you for contributing to Goyo!

## How to Contribute

- Report bugs via [GitHub Issues](https://github.com/hahwul/goyo/issues/new) - Suggest new features - Improve documentation - Submit pull requests - Share the Goyo site

## Settings

Prerequisites: Zola v0.21.0+, Just, Git

```bash
# 포크 및 클론
git clone https://github.com/YOUR-USERNAME/goyo.git
cd goyo

# 의존성 설정
cd /tmp
curl -sLo tailwindcss https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64
chmod +x tailwindcss && mv tailwindcss ../goyo/src/
cd ../goyo
curl -sLo src/daisyui.js https://github.com/saadeghi/daisyui/releases/latest/download/daisyui.js
curl -sLo src/daisyui-theme.js https://github.com/saadeghi/daisyui/releases/latest/download/daisyui-theme.js

# 빌드 및 실행
just build
just dev  # http://127.0.0.1:1111
```

## Guidelines

**Code:** - Follow existing patterns - Keep it simple - Test locally - Clear commit messages

**Documentation:** - Clear language - Examples provided - Multilingual support

**Theme:** - Responsiveness testing - Dark/Light mode verification - Accessibility maintenance

## Submit a Pull Request

```bash
git checkout -b feature/your-feature
# 변경 작업
just build && zola check --skip-external-links
git commit -m "Add feature: description"
git push origin feature/your-feature
```

Open a PR on [github.com/hahwul/goyo](https://github.com/hahwul/goyo)

**PR Guidelines:** - One feature per PR - Clear description - Issue reference (e.g., "Fixes #123") - Open to feedback

## General Tasks

```bash
just build                          # 사이트 빌드
just dev                            # 개발 서버
zola check --skip-external-links    # 링크 확인
rm -rf public                       # 빌드 정리
```

## Test

- Build without errors - Verify internal links - Test in browsers - Check dark/light mode - Multilingual testing (if applicable)

## Get Help

- [GitHub issue](https://github.com/hahwul/goyo/issues) - [Documentation](https://goyo.hahwul.com)

Thank you for contributing to Goyo! ❤️ 