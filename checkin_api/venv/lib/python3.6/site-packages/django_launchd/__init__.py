#!/usr/bin/env python
import os
import plistlib
import public


@public.add
def files(path="~/Library/LaunchAgents"):
    """return a list of plist files within folder and any subfolders"""
    if not path:
        path = "~/Library/LaunchAgents"
    path = os.path.abspath(os.path.expanduser(path))
    result = []
    for root, dirs, _files in os.walk(path):
        for f in filter(lambda f: os.path.splitext(f)[1] == ".plist", _files):
            result.append(os.path.join(root, f))
    return result


@public.add
def read(path):
    """return a dictionary with plist file data"""
    if hasattr(plistlib, "load"):
        return plistlib.load(open(path, 'rb'))
    return plistlib.readPlist(path)
