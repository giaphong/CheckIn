#!/usr/bin/env python
import os
import public


def _iter_dirs(path):
    for root, dirs, files in os.walk(path):
        for d in dirs:
            yield os.path.join(root, d)


@public.add
def getdirs(path):
    """return a list of all dirs in the directory and subdirectories"""
    return list(_iter_dirs(path))
