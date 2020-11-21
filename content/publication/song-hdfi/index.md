---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'HDFI: Hardware-Assisted Data-Fow Isolation'
subtitle: ''
summary: ''
authors:
- Chengyu Song
- Hyungon Moon
- Monjur Alam
- Insu Yun
- Byoungyoung Lee
- Taesoo Kim
- Wenke Lee
- Yunheung Paek
tags: []
categories: []
date: '2016-05-01'
lastmod: 2020-11-21T12:00:36+09:00
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
publishDate: '2020-11-21T07:51:49.155583Z'
publication_types:
- '0'
abstract: "Memory corruption vulnerabilities are the root cause of many\nmodern attacks.\
  \ Existing defense mechanisms are inadequate; in\ngeneral, the software-based approaches\
  \ are not efficient and the\nhardware-based approaches are not flexible. In this\
  \ paper, we present\nhardware-assisted data-flow isolation, or, Hdfi, a new fine-grained\n\
  data isolation mechanism that is broadly applicable and very efficient.\nHdfi enforces\
  \ isolation at the machine word granularity by virtually\nextending each memory\
  \ unit with an additional tag that is defined\nby data-flow.  This capability allows\
  \ Hdfi to enforce a variety of\nsecurity models such as the Biba Integrity Model\
  \ and the Bell--LaPadula\nModel. We implemented Hdfi by extending the RISC-V instruction\
  \ set\narchitecture (ISA) and instantiating it on the Xilinx Zynq ZC706\nevaluation\
  \ board. We ran several benchmarks including the SPEC CINT\n2000 benchmark suite.\
  \  Evaluation results show that the performance\noverhead caused by our modification\
  \ to the hardware is low (<2%). We\nalso developed or ported several security mechanisms\
  \ to leverage\nHdfi, including stack protection, standard library enhancement,\n\
  virtual function table protection, code pointer protection, kernel\ndata protection,\
  \ and information leak prevention.  Our results show\nthat Hdfi is easy to use,\
  \ imposes low performance overhead, and allows\nus to create more elegant and more\
  \ secure solutions.\n"
publication: '*Proceedings of the 37th IEEE Symposium on Security and Privacy (Oakland)*'
url_code: https://github.com/sslab-gatech/hdfi
url_slides: pubs/2016/song:hdfi-slides.pdf
url_paper: pubs/2016/song:hdfi.pdf
---
