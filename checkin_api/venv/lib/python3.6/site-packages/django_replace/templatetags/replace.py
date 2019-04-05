#!/usr/bin/env python
import re
from django import template

register = template.Library()

"""
multiple arguments not suported
{{ value|replace:",old,new" }}
"""


@register.filter
def replace(string, argument):
    ignore, search, replace = argument.split(argument[0])
    return re.sub(search, replace, string)
