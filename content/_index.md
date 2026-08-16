+++
template = "landing.html"
title = "Goyo"

[extra]
version = "v0.1.0"

section_order = ["hero", "features", "trust", "easy_command", "showcase", "social_proof", "final_cta"]

[extra.hero]
title = "Welcome to BlackWerf1257"
badge = "따근따근한 신입 개발자"
description = "꿈을 향해달려가는 개발자"
image = "/images/landing.webp"
image_mobile = "/images/landing-mobile.webp"
gradient_opacity = 30
image_opacity = 25
cta_buttons = [
    { text = "블로그 탐색하기", url = "/Introduction", style = "primary" },
    { text = "깃허브로 이동하기", url = "https://github.com/BlackWerf1257", style = "secondary" },
]

[extra.features_section]
title = "간단하게 알아보기"
description = "더 자세하게 알아보기"

[[extra.features_section.features]]
title = "자기소개"
desc = ""
icon = "circle-half-stroke"

[[extra.features_section.features]]
title = "학력"
desc = """ 

- 2021:3 - 2025:2 백석대학교 첨단 IT학부 졸업			

- 2026:3 - :열린사이버대 자연숲치유학과 재학중 """

icon = "book"

[[extra.features_section.features]]
title = "경력"
desc = "- 2026.3 ~ : (株)テクエイヴ (일본)"
icon = "minimize"

[[extra.features_section.features]]
title = "수상"
desc = ""
icon = "palette"

[[extra.features_section.features]]
title = "프로젝트 경험"
desc = "여기를 눌러 이동하기"
url = "/Project"
icon = "magnifying-glass-chart"

[[extra.features_section.features]]
title = "기술 스택"
desc = "여기를 눌러 이동하기"
url = "/Skill"
icon = "code"

+++
