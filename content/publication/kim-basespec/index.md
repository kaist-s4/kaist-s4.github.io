---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'BaseSpec: Comparative Analysis of Baseband Software and Cellular Specifications
  for L3 Protocols'
subtitle: ''
summary: ''
authors:
- Eunsoo Kim*
- Dongkwan Kim*
- Cheoljun Park
- Insu Yun
- Yongdae Kim
tags: []
categories: []
date: '2021-02-01'
lastmod: 2021-07-08T13:28:33+09:00
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
publishDate: '2021-07-08T04:28:33.530797Z'
publication_types:
- '0'
abstract: "Cellular basebands play a crucial role in mobile communication. However,\
  \ it is significantly challenging to assess their security for several reasons.\
  \ Manual analysis is inevitable because of the obscurity and complexity of baseband\
  \ firmware; however, such analysis requires repetitive efforts to cover diverse\
  \ models or versions. Automating the analysis is also non-trivial because the firmware\
  \ is significantly large and contains numerous functions associated with complex\
  \ cellular protocols. Therefore, existing approaches on baseband analysis are limited\
  \ to only a couple of models or versions within a single vendor. In this paper,\
  \ we propose a novel approach named BaseSpec, which performs a comparative analysis\
  \ of baseband software and cellular specifications. By leveraging the standardized\
  \ message structures in the specification, BaseSpec inspects the message structures\
  \ implemented in the baseband software systematically. It requires a manual yet\
  \ one-time analysis effort to determine how the message structures are embedded\
  \ in target firmware. Then, BaseSpec compares the extracted message structures with\
  \ those in the specification syntactically and semantically, and finally, it reports\
  \ mismatches. These mismatches indicate the developer mistakes, which break the\
  \ compliance of the baseband with the specification, or they imply potential vulnerabilities.\
  \ We evaluated BaseSpec with 18 baseband firmware images of 9 models from one of\
  \ the top three vendors and found hundreds of mismatches. By analyzing these mismatches,\
  \ we discovered 9 erroneous cases: 5 functional errors and 4 memory-related vulnerabilities.\
  \ Notably, two of these are critical remote code execution 0-days. Moreover, we\
  \ applied BaseSpec to 3 models from another vendor, and BaseSpec found multiple\
  \ mismatches, two of which led us to discover a buffer overflow bug.\n"
publication: '*Proceedings of the 2021  Annual Network and Distributed System Security
  Symposium (NDSS)*'
url_slides: pubs/2021/kim:basespec-slides.pdf
url_paper: pubs/2021/kim:basespec.pdf
---
