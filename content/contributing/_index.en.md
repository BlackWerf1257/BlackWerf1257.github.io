+++
title = "Contributing"
description = "Guide to contributing to Goyo"
weight = 7
sort_by = "weight"

[extra]
+++
Thank you for contributing to Goyo!

## Ways to Contribute

- Report bugs via [GitHub issues](https://github.com/hahwul/goyo/issues/new) - Suggest features - Improve documentation - Submit pull requests - Share your Goyo sites

## Setup

Prerequisites: Zola v0.21.0+, Just, Git

```bash
# Fork and clone
git clone https://github.com/YOUR-USERNAME/goyo.git
cd goyo

# Setup dependencies
cd /tmp
curl -sLo tailwindcss https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64
chmod +x tailwindcss && mv tailwindcss ../goyo/src/
cd ../goyo
curl -sLo src/daisyui.js https://github.com/saadeghi/daisyui/releases/latest/download/daisyui.js
curl -sLo src/daisyui-theme.js https://github.com/saadeghi/daisyui/releases/latest/download/daisyui-theme.js

# Build and run
just build
just dev  # http://127.0.0.1:1111
```

## Guidelines

**Code:** - Follow existing patterns - Keep it simple - Test locally - Clear commit messages

**Documentation:** - Clear language - Provide examples - Support multiple languages

**Theme:** - Test responsiveness - Check dark/light mode - Maintain accessibility

## Submit Pull Request

```bash
git checkout -b feature/your-feature
# Make changes
just build && zola check --skip-external-links
git commit -m "Add feature: description"
git push origin feature/your-feature
```

Open PR at [github.com/hahwul/goyo](https://github.com/hahwul/goyo)

**PR Guidelines:** - One feature per PR - Clear description - Reference issues (e.g., "Fixes #123") - Be open to feedback

## Common Tasks

```bash
just build                          # Build site
just dev                            # Development server
zola check --skip-external-links    # Check links
rm -rf public                       # Clean build
```

## Testing

- Build without errors - Check internal links - Test in browser - Verify dark/light modes - Test multilingual (if applicable)

## Getting Help

- [GitHub Issues](https://github.com/hahwul/goyo/issues) - [Documentation](https://goyo.hahwul.com)

Thank you for contributing! ❤️ 