---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Compromising the macOS kernel through Safari by chaining six vulnerabilities
subtitle: ''
summary: ''
authors:
- Yonghwi Jin
- Jungwon Lim
- Insu Yun
- Taesoo Kim
tags: []
categories: []
date: '2020-08-01'
lastmod: 2020-11-21T12:00:34+09:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2020-11-21T07:51:46.973052Z'
publication_types:
- '0'
abstract: "Compromising a kernel through a browser is the ultimate goal for offensive\
  \ security researchers. Because of continuous efforts to eliminate vulnerabilities\
  \ and introduce various mitigations, a remote kernel exploit from a browser becomes\
  \ extremely difficult, seemingly impossible.\n\nIn this talk, we will share our\
  \ Safari exploit submitted to Pwn2Own 2020. Combining *SIX* different vulnerabilities,\
  \ our exploit successfully compromises the macOS kernel starting from the Safari\
  \ browser. It breaks every mitigation in macOS including ASLR, DEP, sandbox, and\
  \ even System Integrity Protection (SIP). Inspecting every vulnerability used in\
  \ this exploit, we will show not only state-of-the-art hacking techniques but also\
  \ challenges in protecting complicated systems (i.e., browsers and operating systems)\
  \ and in introducing their mitigations. Moreover, we will introduce a new technique\
  \ that reliably exploits a TOCTOU vulnerability in macOS.\n\n"
publication: '*Black Hat USA Briefings (Black Hat USA)*'
url_code: https://github.com/sslab-gatech/pwn2own2020
url_slides: pubs/2020/jin:pwn2own2020-safari-slides.pdf
---
