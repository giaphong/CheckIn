#!/usr/bin/env python
import os
import sys
import public


@public.add
def size():
    """return size in bytes of a stdin"""
    return os.fstat(sys.stdin.fileno()).st_size


@public.add
def isatty():
    """return True if stdin is open and connected to a tty(-like) device, else False"""
    return sys.stdin.isatty()


@public.add
def read():
    """return a string with stdin data"""
    if size() > 0:
        return sys.stdin.read()
    return ""
