#!/usr/bin/env python
import os
import public
import shields
import setupcfg


def name():
    if os.path.exists("setup.cfg"):
        return setupcfg.get("metadata", "name")
    return os.popen("python setup.py --name").popen().strip()


@public.add
def pyversions():
    """python versions badge"""
    if os.path.exists("setup.py"):
        return shields.pypi.Pyversions(name(), longCache=True)
    return ""


@public.add
def v():
    """pypi project version badge"""
    if os.path.exists("setup.py"):
        return shields.pypi.V(name(), maxAge=3600)
    return ""
