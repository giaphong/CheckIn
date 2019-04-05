#!/usr/bin/env python
import plistlib
import public


def _read(path):
    if hasattr(plistlib, "load"):
        return plistlib.load(open(path, 'rb'))
    return plistlib.readPlist(path)


@public.add
def read(path):
    """return a dictionary with plist file environment variables"""
    return _read(path).get("EnvironmentVariables", {})


@public.add
def write(path, **vars):
    """write environment variables to a plist file"""
    data = _read(path)
    data["EnvironmentVariables"] = vars
    if data != read(path):
        if hasattr(plistlib, "dump"):
            plistlib.dump(data, open(path, 'wb'))
        else:
            plistlib.writePlist(data, path)
