---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
slug: {{ substr (md5 (printf "%s%s" .Date (replace .TranslationBaseName "-" " " | title))) 0 16 }}
draft: false
---

