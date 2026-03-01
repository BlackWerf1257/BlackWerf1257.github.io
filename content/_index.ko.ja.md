+++
template = "landing.html"
title = "戻る"

[extra]
version = "v0.1.0"

# Section order configuration - customize the order of landing page sections
# Available sections: "hero", "features", "trust", "easy_command", "showcase", "social_proof", "final_cta"
# If not specified, default order is used: hero -> features -> trust -> easy_command -> showcase -> social_proof -> final_cta
section_order = ["hero", "features", "trust", "showcase", "social_proof", "final_cta"]

[extra.hero]
title = "Goyoへようこそ！"
badge = "Clean Theme, Tranquil Feel"
description = "韓国語の「静けさ」からインスピレーションを得たGoyoは、シンプルさと洗練された文書を志向するZolaテーマです。Goyoを使えば、美しく実用的な文書ページを簡単に作成できます。"
image = "/images/landing.jpg"
image_mobile = "/images/landing-mobile.webp"
gradient_opacity = 30
image_opacity = 25
cta_buttons = [
    { text = "시작하기", url = "/introduction", style = "primary" },
    { text = "GitHub에서 보기", url = "https://github.com/hahwul/goyo", style = "secondary" },
]

[extra.features_section]
title = "主な機能"
description = "すっきりとしてミニマルで、コンテンツに集中できる"

[[extra.features_section.features]]
title = "文書に優しい"
desc = "깔끔한 문서 작성 경험을 제공합니다."
icon = "book"

[[extra.features_section.features]]
title = "シンプルなデザイン"
desc = "미니멀리즘을 추구하는 테마입니다."
icon = "minimize"

[[extra.features_section.features]]
title = "カスタマイズと洗練されたランディングページ"
desc = "높은 커스터마이징성과 아름다운 랜딩 페이지를 제공합니다."
icon = "palette"

[[extra.features_section.features]]
title = "SEO最適化"
desc = "검색 엔진에 최적화된 구조를 제공합니다."
icon = "magnifying-glass-chart"

[[extra.features_section.features]]
title = "様々なショートコード"
desc = "다양하고 유용한 숏코드를 제공합니다."
icon = "code"

[[extra.features_section.features]]
title = "ダーク＆ライトモード"
desc = "다크 모드와 라이트 모드를 모두 지원합니다."
icon = "circle-half-stroke"

[extra.trust_section]
title = "技術スタック"
logos = [
    { src = "/resources/zola.svg", alt = "Zola" },
    { src = "/resources/tailwindcss.svg", alt = "Tailwindcss" },
    { src = "/resources/daisyui.svg", alt = "DaisyUI"},
]

[extra.showcase_section]
title = "テーマショーケース"
subtitle = "Goyo 테마의 다양한 측면을 살펴보세요"

[[extra.showcase_section.tabs]]
name = "문서화"
title = "簡潔な文書化"
description = "Goyoのミニマルなデザインアプローチで、美しく読みやすい文書ページを体験してください。"
image = "/writing/shortcodes/gallery/images/image5.jpeg"

[[extra.showcase_section.tabs]]
name = "커스터마이징"
title = "簡単なカスタマイズ"
description = "簡単な設定オプションでサイトをカスタマイズしましょう。色、フォント、レイアウトを簡単に変更できます。"
image = "/writing/shortcodes/gallery/images/image1.jpeg"

[[extra.showcase_section.tabs]]
name = "다국어"
title = "多言語サポート"
description = "多言語に対する組み込みサポート。複数の言語でコンテンツを作成し、ユーザーがシームレスに切り替えることを可能にします。"
image = "/writing/shortcodes/gallery/images/image6.jpeg"

[extra.social_proof_section]
title = "ユーザーの評価"
testimonials = [
    { author = "KSG", role = "보안 개발자 / OWASP Noir", quote = "복잡한 기술 없이도 검색, 다국어, 댓글 등 실용 기능이 포함된 점이 매우 실용적입니다.", avatar = "/resources/ksg.jpg" },
    { author = "Lina", role = "보안 엔지니어", quote = "넘나 간단하고 빠르지만 어마무시하게 이쁜 테마를 적용할 수 있어 너무 좋습니다! 이 테마로 내 마음속 고요를 찾아 떠나보겠습니다~", avatar = "/resources/lina.jpg" },
    { author = "Bori Bae", role = "보안 엔지니어", quote = "테마가 깔끔하고 설정이 직관적이여서 처음쓰는 사람도 쉽게 사용할수있어요!", avatar = "/resources/bori.png" },
]

[extra.final_cta_section]
title = "貢献する"
description = "Goyoは❤️で作られたオープンソースプロジェクトです。このプロジェクトに貢献したい場合は、CONTRIBUTING.mdを確認し、素晴らしいコンテンツと共にプルリクエストを提出してください！"
button = { text = "기여 가이드 보기", url = "/ko/contributing" }
+++
