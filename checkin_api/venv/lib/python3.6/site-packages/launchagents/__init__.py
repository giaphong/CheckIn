#!/usr/bin/env python
import launchctl
import os
import plistlib
import public
import subprocess
import sys

MAC = "darwin" in sys.platform.lower()


@public.add
def read(path):
    """return a dictionary with a plist file data"""
    if hasattr(plistlib, "load"):
        return plistlib.load(open(path, 'rb'))
    return plistlib.readPlist(path)


@public.add
def write(path, data):
    """write a dictionary to a plist file"""
    path = os.path.abspath(os.path.expanduser(path))
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    data = {k: v for k, v in data.items() if v is not None}
    if hasattr(plistlib, "dump"):
        plistlib.dump(data, open(path, 'wb'))
    else:
        plistlib.writePlist(data, path)


@public.add
def update(path, **kwargs):
    """update a plist file"""
    new = {}
    if os.path.exists(path):
        old = dict(read(path))
        new = dict(old)
    new.update(kwargs)
    write(path, new)


@public.add
def jobs():
    """return a list of launchctl jobs for `~/Library/LaunchAgents/*.plist` only"""
    labels = list(map(lambda f: read(f).get("Label", None), files()))
    return list(filter(lambda j: j.label in labels, launchctl.jobs()))


@public.add
def files():
    """return a list of `~/Library/LaunchAgents/*.plist` files"""
    path = os.path.expanduser("~/Library/LaunchAgents")
    if not os.path.exists(path):
        return []
    result = []
    for root, dirs, files in os.walk(path):
        plistfiles = list(filter(lambda f: os.path.splitext(f)[1] == ".plist", files))
        result += list(map(lambda f: os.path.join(root, f), plistfiles))
    return result


@public.add
def load():
    """load `~/Library/LaunchAgents/*.plist`"""
    args = ["launchctl", "load"] + files()
    subprocess.check_call(args)


@public.add
def unload():
    """unload `~/Library/LaunchAgents/*.plist`"""
    args = ["launchctl", "unload"] + files()
    subprocess.check_call(args)
