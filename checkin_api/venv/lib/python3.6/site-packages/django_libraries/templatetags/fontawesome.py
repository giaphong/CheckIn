#!/usr/bin/env python
from django import template
from django.utils.html import mark_safe

register = template.Library()

"""
https://fontawesome.com/start
"""

HTML = """<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">"""
VERSION = "5.6.3"

@register.simple_tag
def fontawesome():
    html = HTML
    return mark_safe(html)
