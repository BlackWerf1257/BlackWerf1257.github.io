+++
template = "landing.html"
title = "Goyo"

[extra]
version = "v0.1.0"

section_order = ["hero", "features", "trust", "easy_command", "showcase", "social_proof", "final_cta"]

[extra.hero]
title = "Welcome to BlackWerf1257"
badge = "3か月キャリアの新人プログラマ"
description = "夢を向けて行くプログラマ"
image = "/images/landing.webp"
image_mobile = "/images/landing-mobile.webp"
gradient_opacity = 30
image_opacity = 25
cta_buttons = [
    { text = "ブログへ移動", url = "/Introduction", style = "primary" },
    { text = "GitHubへ移動", url = "https://github.com/BlackWerf1257", style = "secondary" },
]

[extra.features_section]
title = "自分紹介一覧"
description = "一緒に進みませんか？"

[[extra.features_section.features]]
title = "自分紹介"
desc = "続けて自身を加工しながるジュニアプログラマー."
icon = "circle-half-stroke"

[[extra.features_section.features]]
title = "学歴"
desc = """ 

* 2021:3 - 2025:2 白石大学 先端IT学部 卒業（韓国）\n                 

- 2026:3 - :開きサイバー大学 自然森林療法学科 在学中（韓国）

 """

icon = "book"

[[extra.features_section.features]]
title = "キャリア"
desc = "- 2026.3 ~ : (株)テクエイヴ (日本)"
icon = "minimize"

[[extra.features_section.features]]
title = "受賞"
desc = ""
icon = "palette"

[[extra.features_section.features]]
title = "プロジェクト経験"
desc = "ここをクリックして移動する"
url = "/Project"
icon = "magnifying-glass-chart"

[[extra.features_section.features]]
title = "技術一覧"
desc = "ここをクリックして移動する"
url = "/Skill"
icon = "code"

+++
