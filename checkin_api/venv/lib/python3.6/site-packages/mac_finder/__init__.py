#!/usr/bin/env python
# -*- coding: utf-8 -*-
import applescript
import mac_finder.icon
import os
import public
import runcmd


@public.add
def tell(code):
    """execute applescript `tell application "Finder" ...`"""
    return applescript.tell.app("Finder", code)


@public.add
def selection():
    """return a list with Finder selection paths"""
    paths = applescript.run("""
try
    tell application "Finder"
        get selection
        set l to {}
        repeat with s in (get selection)
            set fullpath to POSIX path of (s as alias)
            log fullpath --2 stderr
        end repeat
    end tell
on error errorMessage number errorNumber
    log errorMessage
    return errorNumber
end try
""").exc().err.splitlines()
    return list(map(lambda path: path if path[-1] != "/" else path[0:-1], paths))


@public.add
def frontmost():
    """return True if Finder is frontmost app, else False"""
    out = os.popen("lsappinfo info -only name `lsappinfo front`").read()
    return "Finder" in out.split('"')


@public.add
def reveal(path):
    """reveal path in Finder"""
    runcmd.run(["/usr/bin/open", "-R", path])
