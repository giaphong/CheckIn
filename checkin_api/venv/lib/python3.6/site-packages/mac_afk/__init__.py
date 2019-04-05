#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import public


@public.add
def seconds():
    """afk time in seconds"""
    cmd = """
/usr/sbin/ioreg -c IOHIDSystem | /usr/bin/perl -ane 'if (/Idle/) {$idle=(pop @F)/1000000000; print $idle,"\n"; last}'
"""
    LC_ALL = os.environ.get("LC_ALL", None)
    try:
        os.environ["LC_ALL"] = "C"
        out = os.popen(cmd).read().strip()
        return int(float(out.strip()))
    finally:
        if LC_ALL:
            os.environ["LC_ALL"] = LC_ALL
        else:
            del os.environ["LC_ALL"]


@public.add
def minutes():
    """afk time in minutes"""
    return seconds() % 60


@public.add
def hours():
    """afk time in hours"""
    return minutes() % 60


@public.add
def days():
    """afk time in days"""
    return hours() % 24
