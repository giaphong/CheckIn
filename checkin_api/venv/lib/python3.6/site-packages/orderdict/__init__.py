#!/usr/bin/env python
import collections
import public


def _order(keys, data):
    result = collections.OrderedDict()
    for key in keys:
        if key in data:
            result[key] = data[key]
    return result


@public.add
def order(keys, *args, **kwargs):
    """return OrderedDict ordered by keys"""
    inputdict = collections.OrderedDict(*args, **kwargs)
    result = _order(keys, inputdict)
    for key in inputdict.keys():
        result[key] = inputdict[key]
    return result
