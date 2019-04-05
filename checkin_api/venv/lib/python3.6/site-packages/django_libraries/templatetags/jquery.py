#!/usr/bin/env python
from django import template
from django.utils.html import mark_safe

register = template.Library()

"""
https://cdnjs.com/libraries/jquery/

http://code.jquery.com/jquery-latest.min.js # v1.11.1 always
http://blog.jquery.com/2014/07/03/dont-use-jquery-latest-js/
"""

HTML = """<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/{version}/jquery.min.js"type="text/javascript"></script>"""
VERSION = "3.3.1"

@register.simple_tag
def jquery(version=VERSION):
    html = HTML.format(version=version)
    return mark_safe(html)

