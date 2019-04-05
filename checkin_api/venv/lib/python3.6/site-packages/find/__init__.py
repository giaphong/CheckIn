#!/usr/bin/env python
import os
import public


def _fullpath(path):
    return os.path.abspath(os.path.expanduser(path))


def _iter_files(path, followlinks=False):
    for root, dirs, files in os.walk(path, followlinks=followlinks):
        for f in files:
            yield os.path.join(root, f)


def _iter_dirs(path, followlinks=False):
    for root, dirs, files in os.walk(path, followlinks=followlinks):
        for d in dirs:
            yield os.path.join(root, d)


@public.add
def dirs(path, followlinks=False):
    """return a list of dirs"""
    return list(_iter_dirs(path, followlinks))


@public.add
def files(path, followlinks=False):
    """return a list of files"""
    return list(_iter_files(path, followlinks))
