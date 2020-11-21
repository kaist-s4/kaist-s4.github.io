---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'CAB-Fuzz: Practical Concolic Testing Techniques for COTS Operating Systems'
subtitle: ''
summary: ''
authors:
- Su Yong Kim
- Sangho Lee
- Insu Yun
- Wen Xu
- Byoungyoung Lee
- Youngtae Yun
- Taesoo Kim
tags: []
categories: []
date: '2017-07-01'
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
publishDate: '2020-11-21T07:51:48.437036Z'
publication_types:
- '0'
abstract: "Discovering the security vulnerabilities of commercial off-the-shelf\n\
  (COTS) operating systems (OSes) is challenging because they not only\nare huge and\
  \ complex, but also lack detailed debug\ninformation. Concolic testing, which generates\
  \ all feasible inputs of\na program by using symbolic execution and tests the program\
  \ with the\ngenerated inputs, is one of the most promising approaches to solve\n\
  this problem. Unfortunately, the state-of-the-art concolic testing\ntools do not\
  \ scale well for testing COTS OSes because of state\nexplosion. Indeed, they often\
  \ fail to find a single bug (or crash) in\nCOTS OSes despite their long execution\
  \ time.\n\nIn this paper, we propose CAB-Fuzz (Context-Aware and\nBoundary-focused),\
  \ a practical concolic testing tool to quickly\nexplore interesting paths that are\
  \ highly likely triggering real bugs\nwithout debug information. First, CAB-Fuzz\
  \ prioritizes the boundary\nstates of arrays and loops, inspired by the fact that\
  \ many\nvulnerabilities originate from a lack of proper boundary\nchecks. Second,\
  \ CAB-Fuzz exploits real programs interacting with COTS\nOSes to construct proper\
  \ contexts to explore deep and complex kernel\nstates without debug information.\
  \ We applied CAB-Fuzz to Windows 7 and\nWindows Server 2008 and found 21 undisclosed\
  \ unique crashes, including\ntwo local privilege escalation vulnerabilities (CVE2015-6098\
  \ and\nCVE-2016-0040) and one information disclosure vulnerability in a\ncryptography\
  \ driver (CVE2016-7219). CAB-Fuzz found vulnerabilities\nthat are non-trivial to\
  \ discover; five vulnerabilities have existed\nfor 14 years, and we could trigger\
  \ them even in the initial version of\nWindows XP (August 2001)."
publication: '*Proceedings of the 2017 USENIX Annual Technical Conference (ATC)*'
url_slides: pubs/2017/kim:cab-fuzz-slides.pdf
url_paper: pubs/2017/kim:cab-fuzz.pdf
---
