#!/usr/bin/env python
from string import Formatter
import public


@public.add
def keys(string):
    """return a list of format keys"""
    return [fname for _, fname, _, _ in Formatter().parse(string) if fname]
