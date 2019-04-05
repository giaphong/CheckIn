#!/usr/bin/env python
import os
import plistlib
import public


LOGS = os.path.expanduser("~/Library/Logs/LaunchAgents")


def read(path):
    if hasattr(plistlib, "load"):
        return plistlib.load(open(path, 'rb'))
    return plistlib.readPlist(path)


def write(path, data):
    """write dictionary to a plist file"""
    if hasattr(plistlib, "dump"):
        plistlib.dump(data, open(path, 'wb'))
    else:
        plistlib.writePlist(data, path)


@public.add
def mkdir(plist_path):
    """make plist file log folders"""
    data = read(plist_path)
    for key in ["StandardOutPath", "StandardErrorPath"]:
        path = data.get(key, "")
        dirname = os.path.dirname(path)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)


@public.add
def add(plist_path):
    """add logs to plist file"""
    data = read(plist_path)
    log_keys = {"StandardOutPath": "out.log", "StandardErrorPath": "err.log"}
    Label = data.get("Label", "")
    if not Label:
        raise ValueError("%s Label unknown" % plist_path)
    for key, filename in log_keys.items():
        if key not in data:
            path = os.path.join(LOGS, Label, filename)
            data[key] = path
    if data != read(plist_path):
        write(plist_path, data)
