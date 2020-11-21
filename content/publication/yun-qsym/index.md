---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'QSYM: A Practical Concolic Execution Engine Tailored for Hybrid Fuzzing'
subtitle: ''
summary: ''
authors:
- Insu Yun
- Sangho Lee
- Meng Xu
- Yeongjin Jang
- Taesoo Kim
tags: []
categories: []
date: '2018-08-01'
lastmod: 2020-11-21T12:00:35+09:00
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
publishDate: '2020-11-21T07:51:47.756236Z'
publication_types:
- '0'
abstract: "Recently, hybrid fuzzing has been proposed to address the limitations of\n\
  fuzzing and concolic execution by combining both approaches. The hybrid\napproach\
  \ has shown its effectiveness in various synthetic benchmarks such as\nDARPA Cyber\
  \ Grand Challenge (CGC) binaries, but it still suffers from scaling\nto find bugs\
  \ in complex, real-world software. We observed that the performance\nbottleneck\
  \ of the existing concolic executor is the main limiting factor for\nits adoption\
  \ beyond a small-scale study.\n\nTo overcome this problem, we design a fast concolic\
  \ execution engine, called\nQSYM, to support hybrid fuzzing. The key idea is to\
  \ tightly integrate the\nsymbolic emulation with the native execution using dynamic\
  \ binary translation,\nmaking it possible to implement more fine-grained, so faster,\
  \ instruction-level\nsymbolic emulation. Additionally, QSYM loosens the strict soundness\n\
  requirements of conventional concolic executors for better performance, yet\ntakes\
  \ advantage of a faster fuzzer for validation, providing unprecedented\nopportunities\
  \ for performance optimizations, e.g., optimistically solving\nconstraints and pruning\
  \ uninteresting basic blocks.\n\nOur evaluation shows that QSYM does not just outperform\
  \ state-of-the-art\nfuzzers (i.e., found 14× more bugs than VUzzer in the LAVA-M\
  \ dataset, and\noutperformed Driller in 104 binaries out of 126), but also found\
  \ 13 previously\nunknown security bugs in eight real-world programs like Dropbox\
  \ Lepton, ffmpeg,\nand OpenJPEG, which have already been intensively tested by the\n\
  state-of-the-art fuzzers, AFL and OSS-Fuzz.\n"
publication: '*Proceedings of the 27th USENIX Security Symposium (Security)*'
url_code: https://github.com/sslab-gatech/qsym
url_slides: pubs/2018/yun:qsym-slides.pdf
url_paper: pubs/2018/yun:qsym.pdf
---
