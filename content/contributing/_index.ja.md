+++
title = "寄稿"
description = "Goyoへの貢献ガイド"
weight = 7
sort_by = "weight"

[extra]
+++
ご寄稿いただきありがとうございます！

## 貢献する方法

- バグは[GitHub issues](https://github.com/hahwul/goyo/issues/new)で報告してください- 機能の提案- ドキュメントの改善- プルリクエストの送信- あなたのGoyoサイトを共有してください

## セットアップ

前提条件: Zola v0.21.0以上、Just、Git

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

## ガイドライン

**コード:** - 既存のパターンに従う - シンプルに保つ - ローカルでテストする - コミットメッセージを明確にする

**ドキュメント:**- 明確な表現- 具体例を提示- 複数言語に対応

**テーマ:**- レスポンシブ対応のテスト- ダーク/ライトモードの確認- アクセシビリティの維持

## プルリクエストを送信する

```bash
git checkout -b feature/your-feature
# Make changes
just build && zola check --skip-external-links
git commit -m "Add feature: description"
git push origin feature/your-feature
```

[github.com/hahwul/goyo](https://github.com/hahwul/goyo) でオープンPRを作成してください。

**プルリクエストのガイドライン:**- 1回のプルリクエストにつき1つの機能- 明確な説明- 関連する課題への参照（例: 「#123 を修正」）- フィードバックを受け入れる姿勢

## 一般的なタスク

```bash
just build                          # Build site
just dev                            # Development server
zola check --skip-external-links    # Check links
rm -rf public                       # Clean build
```

テスト

- エラーなしでビルドする- 内部リンクを確認する- ブラウザでテストする- ダークモード/ライトモードを検証する- 多言語対応をテストする（該当する場合）

## サポートを受ける

- [GitHub Issues](https://github.com/hahwul/goyo/issues)- [ドキュメント](https://goyo.hahwul.com)

ご協力ありがとうございます！❤️