#!/usr/bin/env python
import os
import public
import subprocess

APPLESCRIPT = """
on run argv
    tell application "Finder"
        set _alias to make new alias at (posix file (item 2 of argv)) to (posix file (item 1 of argv))
        set name of _alias to (item 3 of argv)
    end tell
end run
"""


@public.add
def mkalias(src, dst):
    """make MacOS Finder alias"""
    src = os.path.abspath(os.path.expanduser(src))
    dst = os.path.abspath(os.path.expanduser(dst))
    if os.path.exists(dst) and os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    folder = os.path.dirname(dst)
    name = os.path.basename(dst)
    if os.path.exists(dst) and os.path.isfile(dst):
        os.unlink(dst)
    if not os.path.exists(folder):
        os.makedirs(folder)
    subprocess.check_call(["osascript", "-e", APPLESCRIPT, src, folder, name], stdout=subprocess.PIPE)
    """refresh Finder/Dock icon"""
    os.utime(folder, None)
