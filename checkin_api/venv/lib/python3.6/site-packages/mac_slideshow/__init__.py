#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pgrep
import public
import mac_slideshow.preferences
import mac_slideshow.path
import mac_slideshow.style


SAVER = "/System/Library/Frameworks/ScreenSaver.framework/Resources/iLifeSlideshows.saver"
EXECUTABLE = "/System/Library/CoreServices/ScreenSaverEngine.app/Contents/MacOS/ScreenSaverEngine"  # High Sierra+
APP = "/System/Library/Frameworks/ScreenSaver.framework/Versions/A/Resources/ScreenSaverEngine.app"  # Sierra or lower


def _fullpath(path):
    return os.path.abspath(os.path.expanduser(path))


@public.add
class Process:
    """ScreenSaver process object"""
    __readme__ = ["stop", "pid", "running"]

    @property
    def pid(self):
        """return screensaver pid"""
        return pid()

    @property
    def running(self):
        """return True if screensaver is running, else False"""
        return bool(self.pid)

    def stop(self):
        """stop screensaver"""
        stop()

    def __bool__(self):
        return bool(self.pid)

    def __nonzero__(self):
        return bool(self.pid)

    def __str__(self):
        if self.pid:
            return "<Screensaver (pid=%s)>" % self.pid
        return "<Screensaver (stopped)>"


@public.add
def pid():
    """return ScreenSaverEngine.app pid"""
    pids = pgrep.pgrep("ScreenSaverEngine")
    if pids:
        return pids[0]


@public.add
def enabled():
    """return True if iLifeSlideshow screensaver enabled"""
    args = ["defaults", "-currentHost", "read", "com.apple.screensaver", "moduleDict"]
    return "iLifeSlideshow" in os.popen("%s 2> /dev/null" % " ".join(args)).read()


@public.add
def enable():
    """enable iLifeSlideshow screensaver"""
    if enabled():
        return
    args = ["defaults", "-currentHost", "write", "com.apple.screensaver", "moduleDict", "-dict", "moduleName", "iLifeSlideshow", "path", SAVER, "type", "0"]
    os.system(" ".join(args))
    os.system(" ".join(["killall", "cfprefsd", "System Preferences"]))


@public.add
def start(path=None):
    """start screensaver and return Process object"""
    if path:
        mac_slideshow.path.write(_fullpath(path))
    enable()
    if os.path.exists(EXECUTABLE):
        os.system("%s 2> /dev/null &" % EXECUTABLE)
    else:
        os.system("open -a %s" % APP)
    return Process()


@public.add
def stop():
    """stop screensaver"""
    _pid = pid()
    if _pid:
        os.popen("kill %s" % _pid)


@public.add
def restart(path=None):
    """restart screensaver and return Process object"""
    stop()
    start(path)
    return Process()
