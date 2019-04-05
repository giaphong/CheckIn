#!/usr/bin/env python
import os
import public


def _iter_files(path):
    for root, dirs, files in os.walk(path):
        for f in files:
            yield os.path.join(root, f)


@public.add
def getfiles(path):
    """return a list of all files in the directory and subdirectories"""
    return list(_iter_files(path))
