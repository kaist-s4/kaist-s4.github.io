---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'AVPASS: Leaking and Bypassing Antivirus Detection Model Automatically'
subtitle: ''
summary: ''
authors:
- Jinho Jung
- Chanil Jeon
- Max Wolotsky
- Insu Yun
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
publishDate: '2020-11-21T07:51:48.100293Z'
publication_types:
- '0'
abstract: "AVPASS is a tool for leaking the detection model \nof Android antivirus\
  \ (AV) programs, and bypassing \nthe AV detection by using the leaked information\
  \ \ncoupled with APK perturbation techniques. AVPASS \nis able to infer not only\
  \ the detection features, \nbut also hierarchy of detection rule chains. \nWith\
  \ help from the leaked model and the built-in \nAPK perturbation functions, AVPASS\
  \ is able to \ndisguise any android malware as a benign application. \nFurthermore,\
  \ using our novel additive mode, AVPASS \nsupports safe querying and guarantees\
  \ that one can \ntest if the application will be detected by the AV \nwithout sending\
  \ the whole or core parts of application. \nAs a result, AVPASS leaked significant\
  \ detection \nfeatures of commercial AVs and achieved almost \nzero detection from\
  \ VirusTotal when tested with \nmore than 5,000 malware. \n\nIn this talk, we present\
  \ the entire pipeline of \nthe APK perturbation process, leaking model process,\
  \ \nand auto-bypassing process. In addition, we show \nfindings about commercial\
  \ AVs, including their \ndetection features and hierarchy, and inform the \nattendees\
  \ about the potential weaknesses of modern AVs. \n\nAVPASS will be demonstrated,\
  \ showing that it modifies \nreal world malware precisely, and allows them to \n\
  bypass all AVs following the leaked model. AVPASS \nwill be released with every\
  \ tool that we have built, \nincluding the original source code and the related\
  \ \ntest data, to enable researchers to replicate the \nresearch on their own.\n\
  \n"
publication: '*Black Hat USA Briefings (Black Hat USA)*'
url_code: https://github.com/sslab-gatech/avpass
url_slides: pubs/2017/jung:avpass-slides.pdf
---
