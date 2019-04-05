#!/usr/bin/env python
import os
import sys
import public


@public.add
def read(path, size=-1, encoding="utf-8"):
    """return file content (if file exists)"""
    if not path:
        return
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        return
    if (sys.version_info[0] == 3):
        r = open(path, encoding=encoding).read(size)
    else:
        r = open(path).read(size)
    return r
