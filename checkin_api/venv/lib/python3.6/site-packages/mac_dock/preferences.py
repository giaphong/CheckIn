#!/usr/bin/env python
import os
import plistlib
import subprocess
import mac_dock

PLIST = os.path.expanduser("~/Library/Preferences/com.apple.dock.plist")


def read():
    if os.path.exists(PLIST):
        return plistlib.readPlist(PLIST)
    return {}


def write(data):
    old = read()
    if old == data:
        return
    mac_dock.launchctl.unload()
    subprocess.call(["defaults", "delete", "com.apple.dock"])  # reset cfprefsd cache
    plistlib.writePlist(data, PLIST)
    subprocess.call(["killall", "cfprefsd"])
    mac_dock.launchctl.load()
    mac_dock.launchctl.start()
