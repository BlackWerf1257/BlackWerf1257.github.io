+++
template = "landing.html"
title = "戻る"

[extra]
version = "v0.1.0"

# Section order configuration - customize the order of landing page sections
# Available sections: "hero", "features", "trust", "easy_command", "showcase", "social_proof", "final_cta"
# If not specified, default order is used: hero -> features -> trust -> easy_command -> showcase -> social_proof -> final_cta
section_order = ["hero", "features", "trust", "easy_command", "showcase", "social_proof", "final_cta"]

[extra.hero]
title = "ようこそGoyoへ！"
badge = "Clean Theme, Tranquil Feel"
description = "韓国の言葉「ゴヨ」（고요）——静けさや穏やかさを意味する——に着想を得たGoyoは、シンプルさと洗練されたドキュメント作成を目指すZolaテーマです。Goyoを使えば、美しく実用的なドキュメントページを簡単に作成できます。"
image = "/images/landing.webp"
image_mobile = "/images/landing-mobile.webp"
gradient_opacity = 30
image_opacity = 25
cta_buttons = [
    { text = "Get Started", url = "/introduction", style = "primary" },
    { text = "View on GitHub", url = "https://github.com/hahwul/goyo", style = "secondary" },
]

[extra.features_section]
title = "主要機能"
description = "清潔で、ミニマルで、コンテンツに焦点を当てた"

[[extra.features_section.features]]
title = "ドキュメント対応"
desc = "Provides a clean writing experience for documentation."
icon = "book"

[[extra.features_section.features]]
title = "シンプルなデザイン"
desc = "A theme that pursues minimalism."
icon = "minimize"

[[extra.features_section.features]]
title = "カスタマイズと洗練されたランディングページ"
desc = "Highly customizable with a beautiful landing page."
icon = "palette"

[[extra.features_section.features]]
title = "SEO最適化済み"
desc = "Provides a structure optimized for search engines."
icon = "magnifying-glass-chart"

[[extra.features_section.features]]
title = "各種ショートコード"
desc = "Offers a variety of useful shortcodes."
icon = "code"

[[extra.features_section.features]]
title = "ダークモードとライトモード"
desc = "Supports both dark and light modes."
icon = "circle-half-stroke"

[extra.trust_section]
title = "技術スタック"
logos = [
    { src = "/resources/zola.svg", alt = "Zola" },
    { src = "/resources/tailwindcss.svg", alt = "Tailwindcss" },
    { src = "/resources/daisyui.svg", alt = "DaisyUI"},
]

[extra.easy_command_section]
title = "簡単な設置"
description = "お好みの方法で、わずか数秒でGoyoを始めましょう"

[[extra.easy_command_section.tabs]]
name = "Git Clone"
command = "git clone https://github.com/hahwul/goyo.git themes/goyo"

[[extra.easy_command_section.tabs]]
name = "Git Submodule"
command = "git submodule add https://github.com/hahwul/goyo.git themes/goyo"

[[extra.easy_command_section.tabs]]
name = "Download"
command = "curl -sL https://github.com/hahwul/goyo/archive/refs/heads/main.zip -o goyo.zip"

[[extra.easy_command_section.tabs]]
name = "More"
link = "/get_started/installation"

[extra.showcase_section]
title = "テーマショーケース"
subtitle = "Explore different aspects of Goyo theme"

[[extra.showcase_section.tabs]]
name = "Documentation"
title = "クリーンなドキュメント"
description = "Goyoのミニマリストデザインアプローチで、美しく読みやすいドキュメントページを体験してください。"
image = "/writing/shortcodes/gallery/images/image5.jpeg"

[[extra.showcase_section.tabs]]
name = "Customization"
title = "簡単なカスタマイズ"
description = "シンプルな設定オプションでサイトをカスタマイズしましょう。色、フォント、レイアウトを簡単に変更できます。"
image = "/writing/shortcodes/gallery/images/image1.jpeg"

[[extra.showcase_section.tabs]]
name = "Multilingual"
title = "多言語サポート"
description = "複数言語の組み込みサポート。異なる言語でコンテンツを作成し、ユーザーがシームレスに切り替えて利用できるようにします。"
image = "/writing/shortcodes/gallery/images/image6.jpeg"

[extra.social_proof_section]
title = "ユーザーの声"
testimonials = [
    { author = "KSG", role = "Security Developer / OWASP Noir", quote = "Without extra tools, it includes practical features like search, multilingual support, and comments out of the box", avatar = "/resources/ksg.jpg" },
    { author = "Lina", role = "Security Engineer", quote = "It's so simple and fast, yet I can apply an incredibly beautiful theme, which I absolutely love! I'm ready to embark on a journey to find the calm in my heart with this theme!", avatar = "/resources/lina.jpg" },
    { author = "Bori Bae", role = "Security Engineer", quote = "The theme is clean and the settings are intuitive, so even first-time users can easily use it!", avatar = "/resources/bori.png" },
]

[extra.final_cta_section]
title = "寄稿"
description = "Goyoは❤️を込めて作られたオープンソースプロジェクトです。このプロジェクトに貢献したい場合は、CONTRIBUTING.mdを参照し、あなたの素晴らしいコンテンツをプルリクエストで提出してください！"
button = { text = "View Contributing Guide", url = "/contributing" }
+++
