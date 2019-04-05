#!/usr/bin/env python
from django import template
from django.utils.html import mark_safe

register = template.Library()

"""
https://getbootstrap.com/docs/
"""

HTML = """<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css">
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap-theme.min.css">"""
VERSION = "4.2.1"

@register.simple_tag
def bootstrap(version=VERSION):
    html = HTML.format(version=version)
    return mark_safe(html)

