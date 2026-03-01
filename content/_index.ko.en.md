+++
template = "landing.html"
title = "Back"

[extra]
version = "v0.1.0"

# Section order configuration - customize the order of landing page sections
# Available sections: "hero", "features", "trust", "easy_command", "showcase", "social_proof", "final_cta"
# If not specified, default order is used: hero -> features -> trust -> easy_command -> showcase -> social_proof -> final_cta
section_order = ["hero", "features", "trust", "showcase", "social_proof", "final_cta"]

[extra.hero]
title = "Welcome to Goyo!"
badge = "Clean Theme, Tranquil Feel"
description = "Inspired by the Korean word '고요' (Goyo), Goyo is a Zola theme that prioritizes simplicity and clean documentation. With Goyo, you can easily create beautiful and practical documentation pages."
image = "/images/landing.jpg"
image_mobile = "/images/landing-mobile.webp"
gradient_opacity = 30
image_opacity = 25
cta_buttons = [
    { text = "시작하기", url = "/introduction", style = "primary" },
    { text = "GitHub에서 보기", url = "https://github.com/hahwul/goyo", style = "secondary" },
]

[extra.features_section]
title = "Key Features"
description = "Clean and minimal, focused on content"

[[extra.features_section.features]]
title = "Document-friendly"
desc = "깔끔한 문서 작성 경험을 제공합니다."
icon = "book"

[[extra.features_section.features]]
title = "Simple design"
desc = "미니멀리즘을 추구하는 테마입니다."
icon = "minimize"

[[extra.features_section.features]]
title = "Customization and elegant landing pages"
desc = "높은 커스터마이징성과 아름다운 랜딩 페이지를 제공합니다."
icon = "palette"

[[extra.features_section.features]]
title = "SEO Optimization"
desc = "검색 엔진에 최적화된 구조를 제공합니다."
icon = "magnifying-glass-chart"

[[extra.features_section.features]]
title = "Various shortcodes"
desc = "다양하고 유용한 숏코드를 제공합니다."
icon = "code"

[[extra.features_section.features]]
title = "Dark & Light Mode"
desc = "다크 모드와 라이트 모드를 모두 지원합니다."
icon = "circle-half-stroke"

[extra.trust_section]
title = "Technology Stack"
logos = [
    { src = "/resources/zola.svg", alt = "Zola" },
    { src = "/resources/tailwindcss.svg", alt = "Tailwindcss" },
    { src = "/resources/daisyui.svg", alt = "DaisyUI"},
]

[extra.showcase_section]
title = "Theme Showcase"
subtitle = "Goyo 테마의 다양한 측면을 살펴보세요"

[[extra.showcase_section.tabs]]
name = "문서화"
title = "Clean documentation"
description = "Experience beautiful, easy-to-read document pages with Goyo's minimalist design approach."
image = "/writing/shortcodes/gallery/images/image5.jpeg"

[[extra.showcase_section.tabs]]
name = "커스터마이징"
title = "Easy customization"
description = "Customize your site with simple settings options. Easily change colors, fonts, and layouts."
image = "/writing/shortcodes/gallery/images/image1.jpeg"

[[extra.showcase_section.tabs]]
name = "다국어"
title = "Multilingual Support"
description = "Built-in multilingual support. Create content in multiple languages and enable users to switch seamlessly."
image = "/writing/shortcodes/gallery/images/image6.jpeg"

[extra.social_proof_section]
title = "User reviews"
testimonials = [
    { author = "KSG", role = "보안 개발자 / OWASP Noir", quote = "복잡한 기술 없이도 검색, 다국어, 댓글 등 실용 기능이 포함된 점이 매우 실용적입니다.", avatar = "/resources/ksg.jpg" },
    { author = "Lina", role = "보안 엔지니어", quote = "넘나 간단하고 빠르지만 어마무시하게 이쁜 테마를 적용할 수 있어 너무 좋습니다! 이 테마로 내 마음속 고요를 찾아 떠나보겠습니다~", avatar = "/resources/lina.jpg" },
    { author = "Bori Bae", role = "보안 엔지니어", quote = "테마가 깔끔하고 설정이 직관적이여서 처음쓰는 사람도 쉽게 사용할수있어요!", avatar = "/resources/bori.png" },
]

[extra.final_cta_section]
title = "Contribute"
description = "Goyo is an open-source project made with ❤️. If you'd like to contribute to this project, please check CONTRIBUTING.md and submit a pull request with great content!"
button = { text = "기여 가이드 보기", url = "/ko/contributing" }
+++
