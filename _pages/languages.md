---
title: titles.languages
author: Jesper Dramsch
layout: post
namespace: languages
permalink: /languages/
pemalink_de: /sprachen/
permalink_es: /idiomas/
permalink_fr: /langues/
permalink_pt-br: /idiomas/
permalink_zh-cn: /语言/
permalink_hi: /भाषाएँ/
permalink_id: /bahasa/
---

{% for lang in site.languages %}

-   [{{ site.languages_available[lang] }} ({{lang}})]({% tl about {{lang}} %})

{% endfor %}
