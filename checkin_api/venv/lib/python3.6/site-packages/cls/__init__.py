#!/usr/bin/env python
import inspect
import public


def _validate(cls):
    if not inspect.isclass(cls):
        raise ValueError("%s not a class" % cls)


def _is_attr(value):
    return not inspect.ismethod(value) and not isinstance(value, property)


@public.add
def attrs(cls):
    """return a list with class attrs names"""
    _validate(cls)
    result = []
    for key, value in cls.__dict__.items():
        if key[:2] != '__' and _is_attr(value):
            result.append(key)
    return list(sorted(result))


@public.add
def properties(cls):
    """return a list with class properties names"""
    _validate(cls)
    result = []
    for key, value in cls.__dict__.items():
        if isinstance(value, property):
            result.append(key)
    return list(sorted(result))
