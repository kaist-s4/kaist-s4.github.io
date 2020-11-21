---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Automatic Techniques to Systematically Discover New Heap Exploitation Primitives
subtitle: ''
summary: ''
authors:
- Insu Yun
- Dhaval Kapil
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
publishDate: '2020-11-21T07:51:46.805847Z'
publication_types:
- '0'
abstract: "Exploitation techniques to abuse metadata of heap allocators have been\
  \ widely studied because of their generality (i.e., application independence) and\
  \ powerfulness (i.e., bypassing modern mitigation). However, such techniques are\
  \ commonly considered arts, and thus the ways to discover them remain ad-hoc, manual,\
  \ and allocator-specific.\n\nIn this paper, we present an automatic tool, ArcHeap,\
  \ to systematically discover the unexplored heap exploitation primitives, regardless\
  \ of their underlying implementations. The key idea of ArcHeap is to let the computer\
  \ autonomously explore the spaces, similar in concept to fuzzing, by specifying\
  \ a set of common designs of modern heap allocators and root causes of vulnerabilities\
  \ as models, and by providing heap operations and attack capabilities as actions.\
  \ During the exploration, ArcHeap checks whether the combinations of these actions\
  \ can be potentially used to construct exploitation primitives, such as arbitrary\
  \ write or overlapped chunks. As a proof, ArcHeap generates working PoC that demonstrates\
  \ the discovered exploitation technique.\n\nWe evaluated ArcHeap with ptmalloc2\
  \ and 10 other allocators, and discovered five previously unknown exploitation techniques\
  \ in ptmalloc2 as well as several techniques against seven out of 10 allocators\
  \ including the security-focused allocator, DieHarder. To show the effectiveness\
  \ of ArcHeap's approach in other domains, we also studied how security features\
  \ and exploit primitives evolve across different versions of ptmalloc2.\n"
publication: '*Proceedings of the 29th USENIX Security Symposium (Security)*'
url_slides: pubs/2020/yun:archeap-slides.pdf
url_paper: pubs/2020/yun:archeap.pdf
url_code: https://github.com/sslab-gatech/archeap
---
