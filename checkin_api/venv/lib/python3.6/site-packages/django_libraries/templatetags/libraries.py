#!/usr/bin/env python
from django import template
from django.conf import settings
from django.utils.html import mark_safe
import os
import sys

register = template.Library()
DIR = os.path.abspath(os.path.dirname(__file__))

def isfile(name):
    return "/" in name or "." in name

def static_html(name):
    uri = settings.STATIC_URL+name
    if ".js" in name:
        return '<script src="%s" type="text/javascript"></script>' % uri
    if ".css" in name:
        return '<link rel="stylesheet" type="text/css" href="%s" />' % uri
    raise ValueError("unknown library. allowed: .css, .js")

def library_html(name):
    path = os.path.join(DIR,"%s.py" % name)
    if not os.path.exists(path):
        KeyError("'%s' - unknown library")
    try:
        sys.path.append(DIR)
        module = __import__(name)
        tag = getattr(module,name.replace("-","_"))
        return tag()
    finally:
        sys.path.remove(DIR)

@register.simple_tag
def libraries(*names):
    lines = []
    for name in names:
        if not name:
            lines.append("")
            continue
        if isfile(name):
            lines.append(static_html(name))
            continue
        lines.append(library_html(name))
    html = "\n".join(lines)
    return mark_safe(html)
