#!/usr/bin/env python
import os
import public


@public.add
def readable(path):
    """return True if path is readable"""
    if os.path.exists(path):
        return os.access(path, os.R_OK)


@public.add
def executable(path):
    """return True if path is executable"""
    if os.path.exists(path):
        return os.access(path, os.X_OK)


@public.add
def writable(path):
    """return True if path is writable"""
    if os.path.exists(path):
        return os.access(path, os.W_OK)
