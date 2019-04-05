#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import public
import pgrep
import applescript
import mac_screensaver.preferences

"""
High Sierra:
/System/Library/CoreServices/ScreenSaverEngine.app/Contents/MacOS/ScreenSaverEngine

Sierra or lower:
/System/Library/Frameworks/ScreenSaver.framework/Versions/A/Resources/ScreenSaverEngine.app
"""


@public.add
def stop():
    """kill screensaver process"""
    os.system("kill -9 %s" % pid())


@public.add
def name():
    """return active screensaver name"""
    code = "get name of current screen saver"
    return applescript.tell.app("System Events", code).out


@public.add
def names():
    """return a list of screensavers names"""
    code = """repeat with ss in screen savers
    log (name of ss as text)
end repeat"""
    return applescript.tell.app("System Events", code).err.splitlines()


@public.add
def pid():
    """return screensaver pid"""
    pids = pgrep.pgrep("ScreenSaverEngine")
    if pids:
        return pids[0]


@public.add
def start():
    """start screensaver"""
    path = "/System/Library/CoreServices/ScreenSaverEngine.app/Contents/MacOS/ScreenSaverEngine"
    if os.path.exists(path):
        os.system("%s &" % path)
    else:
        app = "/System/Library/Frameworks/ScreenSaver.framework/Versions/A/Resources/ScreenSaverEngine.app"
        os.system("open -a %s" % app)
