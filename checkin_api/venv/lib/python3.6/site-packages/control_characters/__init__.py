#!/usr/bin/env python
import public
import unicodedata


@public.add
def remove(string):
    """return a string without control characters"""
    return "".join(ch for ch in string if unicodedata.category(ch)[0] != "C")
