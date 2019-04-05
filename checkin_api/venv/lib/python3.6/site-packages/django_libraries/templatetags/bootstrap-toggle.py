#!/usr/bin/env python
from django import template
from django.utils.html import mark_safe

register = template.Library()

"""
http://www.bootstraptoggle.com/
"""

HTML = """<link href="https://gitcdn.github.io/bootstrap-toggle/{version}/css/bootstrap-toggle.min.css" rel="stylesheet">
<script src="https://gitcdn.github.io/bootstrap-toggle/{version}/js/bootstrap-toggle.min.js"></script>"""
VERSION = "2.2.2"

@register.simple_tag
def bootstrap_toggle(version=VERSION):
    html = HTML.format(version=version)
    return mark_safe(html)

