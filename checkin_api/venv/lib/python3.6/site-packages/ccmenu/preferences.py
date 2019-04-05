#!/usr/bin/env python
import os
import plistlib
import public


PLIST = os.path.expanduser("~/Library/Containers/net.sourceforge.cruisecontrol.CCMenu/Data/Library/Preferences/net.sourceforge.cruisecontrol.CCMenu.plist")


@public.add
def read():
    """return a dictionary with plist file data"""
    if not os.path.exists(PLIST):
        return {}
    if hasattr(plistlib, "load"):
        return plistlib.load(open(PLIST, 'rb'))
    return plistlib.readPlist(PLIST)


@public.add
def write(data):
    """write dictionary data to a plist file"""
    if os.path.exists(PLIST) and data == read():
        return
    if not os.path.exists(os.path.dirname(PLIST)):
        os.makedirs(os.path.dirname(PLIST))
    if hasattr(plistlib, "dump"):
        plistlib.dump(data, open(PLIST, 'wb'))
    else:
        plistlib.writePlist(data, PLIST)
    return True
