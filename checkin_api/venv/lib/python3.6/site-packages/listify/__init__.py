#!/usr/bin/env python
import functools
import types
import public

"""
decorator for making generator functions return a list instead
"""


@public.add
def listify(func):
    """`@listify` decorator"""
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        r = func(*args, **kwargs)
        if r is None:
            return []
        if isinstance(r, types.GeneratorType):
            return list(r)
        return r
    return new_func
