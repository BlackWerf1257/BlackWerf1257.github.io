+++
title = "貢献する"
description = "Goyoへの貢献方法"
weight = 7
sort_by = "weight"

[extra]
+++
Goyoへの貢献に感謝します！

## 貢献方法

- [GitHubイシュー](https://github.com/hahwul/goyo/issues/new)でバグ報告 - 機能提案 - ドキュメント改善 - プルリクエスト提出 - Goyoサイト共有

## 設定

事前要件: Zola v0.21.0以上、Just、Git

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

##ガイドライン

**コード:** - 既存のパターンに従う - シンプルに保つ - ローカルテスト - 明確なコミットメッセージ

**文書:** - 明確な言語 - 例を提供 - 多言語対応

**テーマ:** - レスポンシブテスト - ダーク/ライトモードの確認 - アクセシビリティの維持

プルリクエストの提出

```bash
git checkout -b feature/your-feature
# 변경 작업
just build && zola check --skip-external-links
git commit -m "Add feature: description"
git push origin feature/your-feature
```

[github.com/hahwul/goyo](https://github.com/hahwul/goyo)でプルリクエストを開く

**PRガイドライン:**- PRごとに1つの機能- 明確な説明- イシュー参照 (例: "Fixes #123")- フィードバックを受け入れる姿勢

## 一般作業

```bash
just build                          # 사이트 빌드
just dev                            # 개발 서버
zola check --skip-external-links    # 링크 확인
rm -rf public                       # 빌드 정리
```

## テスト

- エラーなしでビルド - 内部リンクの確認 - ブラウザでのテスト - ダーク/ライトモードの確認 - 多言語テスト（該当する場合）

## サポートを受ける

- [GitHub イシュー](https://github.com/hahwul/goyo/issues)- [ドキュメント](https://goyo.hahwul.com)

Goyoへの貢献に感謝します！❤️