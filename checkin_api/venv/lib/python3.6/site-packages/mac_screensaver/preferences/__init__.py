#!/usr/bin/env python
import os
import public

DOMAIN = "com.apple.screensaver"


def _read(key):
    cmd = "/usr/bin/defaults -currentHost read %s %s" % (DOMAIN, key)
    return os.popen(cmd).read().strip()


@public.add
def clock():
    """return True if "Show with clock" enabled, else False"""
    key = "showClock"
    return bool(_read(key))


@public.add
def idle():
    """return screensaver idle time in seconds. 0 if disabled"""
    key = "idleTime"
    return int(_read(key))
