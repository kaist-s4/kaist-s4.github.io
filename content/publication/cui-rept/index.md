---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'REPT: Reverse Debugging of Failures in Deployed Software'
subtitle: ''
summary: ''
authors:
- Weidong Cui
- Xinyang Ge
- Baris Kasikci
- Ben Niu
- Upamanyu Sharma
- Ruoyu Wang
- Insu Yun
tags: []
categories: []
date: '2018-10-01'
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
publishDate: '2020-11-21T07:51:47.388526Z'
publication_types:
- '0'
abstract: "Debugging software failures in deployed systems is important because they\n\
  impact real users and customers. However, debugging such failures is\nnotoriously\
  \ hard in practice because developers have to rely on limited\ninformation such\
  \ as memory dumps. The execution history is usually unavailable\nbecause high-fidelity\
  \ program tracing is not affordable in deployed systems.\n\nIn this paper, we present\
  \ REPT, a practical system that enables reverse\ndebugging of software failures\
  \ in deployed systems. REPT reconstructs the\nexecution history with high fidelity\
  \ by combining online lightweight hardware\ntracing of a program's control flow\
  \ with offline binary analysis that recovers\nits data flow. It is seemingly impossible\
  \ to recover data values thousands of\ninstructions before the failure due to information\
  \ loss and concurrent\nexecution. REPT tackles these challenges by constructing\
  \ a partial execution\norder based on timestamps logged by hardware and iteratively\
  \ performing forward\nand backward execution with error correction.\n\nWe design\
  \ and implement REPT, deploy it on Microsoft Windows, and integrate it\ninto Windows\
  \ Debugger. We evaluate REPT on 16 real-world bugs and show that it\ncan recover\
  \ data values accurately (92% on average) and efficiently (less than\n20 seconds)\
  \ for these bugs. We also show that it enables effective reverse\ndebugging for\
  \ 14 bugs.\n"
publication: '*Proceedings of the 13th USENIX Symposium on Operating Systems Design
  and Implementation (OSDI)*'
url_slides: pubs/2018/cui:rept-slides.pdf
url_paper: pubs/2018/cui:rept.pdf
---
