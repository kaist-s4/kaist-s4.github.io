---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Fuzzing JavaScript Engines with Aspect-preserving Mutation
subtitle: ''
summary: ''
authors:
- Soyeon Park
- Wen Xu
- Insu Yun
- Daehee Jang
- Taesoo Kim
tags: []
categories: []
date: '2020-05-01'
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
publishDate: '2020-11-21T07:51:47.147149Z'
publication_types:
- '0'
abstract: "Fuzzing is a practical, widely-deployed technique to find bugs in complex,\
  \ real-world programs like JavaScript engines. We observed, however, that existing\
  \ fuzzing approaches, either generative or mutational, fall short in fully harvesting\
  \ high-quality input corpora such as known proof of concept (PoC) exploits or unit\
  \ tests. Existing fuzzers tend to destruct subtle semantics or conditions encoded\
  \ in the input corpus in order to generate new test cases because this approach\
  \ helps in discovering new code paths of the program. Nevertheless, for JavaScript-like\
  \ complex programs, such a conventional design leads to test cases that tackle only\
  \ shallow parts of the complex codebase and fails to reach deep bugs effectively\
  \ due to the huge input space.\n\nIn this paper, we advocate a new technique, called\
  \ an aspect-preserving mutation, that stochastically preserves the desirable properties,\
  \ called aspects, that we prefer to be maintained across mutation. We demonstrate\
  \ the aspect preservation with two mutation strategies, namely, structure and type\
  \ preservation, in our fully-fledged JavaScript fuzzer, called DIE. Our evaluation\
  \ shows that DIE's aspect-preserving mutation is more effective in discovering new\
  \ bugs (5.7 x more unique crashes) and producing valid test cases (2.4 x fewer runtime\
  \ errors) than the state-of-the-art JavaScript fuzzers. DIE newly discovered 48\
  \ high-impact bugs in ChakraCore, JavaScriptCore, and V8 (38 fixed with 12 CVEs\
  \ assigned as of today). The source code of DIE is publicly available as an open-source\
  \ project.\n"
publication: '*Proceedings of the 41st IEEE Symposium on Security and Privacy (Oakland)*'
url_slides: pubs/2020/park:die-slides.pdf
url_paper: pubs/2020/park:die.pdf
---
