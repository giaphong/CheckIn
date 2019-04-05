#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import public
import subprocess
import time


@public.add
def args(**kwargs):
    """return a list with `growlnotify` cli arguments"""
    args = []
    for k, v in kwargs.items():
        short = len(k) == 1
        string = "-%s" % k if short else "--%s" % k
        if isinstance(v, bool):
            """flag, e.g.: -s, --sticky"""
            if v:
                args += [string]
        else:
            """ -t "title text", --title "title text """
            args += [string, str(v)]
    return args


@public.add
def notify(**kwargs):
    """run growlnotify"""
    if "m" not in kwargs and "message" not in kwargs:
        kwargs["m"] = ""
    cmd = ["growlnotify"] + args(**kwargs)
    out = os.popen("osascript -e 'tell application \"System Events\" to (name of processes) contains \"Growl\"'").read()
    if "false" in out:
        subprocess.check_call(["open", "-a", "Growl"])
    subprocess.check_call(cmd)
