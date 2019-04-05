#!/usr/bin/env python
# -*- coding: utf-8 -*-
import applescript
import google_chrome.fullscreen
import os
import public
import runcmd
import values


@public.add
def tell(code):
    """execute applescript `tell application "Google Chrome" ...`"""
    return applescript.tell.app("Google Chrome", code).exc()


@public.add
def close(urls):
    """close tabs with url(s)"""
    for url in values.get(urls):
        code = """
repeat with w in every window
    repeat with t in every tab in w
        if (URL of t) is ("%s" as text) then
            tell t to close
        end if
    end repeat
end repeat""" % str(url)
        tell(code)


@public.add
def open(url):
    """open url(s)"""
    tell('open location "%s"' % url)


@public.add
def refresh(url, activate=True):
    """refresh url. return True if url is opened, else False"""
    code = """repeat with w in every window
    set tab_i to 0
    repeat with t in every tab in w
        set tab_i to (tab_i+1)
        if "{url}" is ((URL of t) as text) or "{url}/" is ((URL of t) as text) then
            tell t to reload
            if %s is true then
                set index of w to 1 --activate window
                tell w to set active tab index to tab_i --activate tab
            end if
            return true
        end if
    end repeat
end repeat""".format(url=url) % "true" if activate else "false"
    return bool(tell(code).out)


@public.add
def url():
    """return current tab url"""
    return tell("if count of windows is not 0 then return URL of active tab of first window").out


@public.add
def urls():
    """return a list of tabs urls"""
    code = """repeat with w in  every window
    repeat with t in every tab in w
      log (URL of t as text)
    end repeat
end repeat"""
    return tell(code).err.splitlines()


"""Google Chrome.app process functions"""


@public.add
def activate():
    """activate Google Chrome and bring it to front"""
    tell('activate')


@public.add
def frontmost():
    """return True if `Google Chrome.app` is frontmost app, else False"""
    out = os.popen("lsappinfo info -only name `lsappinfo front`").read()
    return "Google Chrome" in out.split('"')


@public.add
def kill():
    """kill Google Chrome.app process"""
    _pid = pid()
    if _pid:
        os.popen("kill %s &> /dev/null" % _pid)


@public.add
def pid():
    """return Google Chrome.app pid"""
    for l in os.popen("ps -ax").read().splitlines():
        if "Google Chrome.app" in l:
            return int(list(filter(None, l.split(" ")))[0])


@public.add
def quit():
    """quit Google Chrome.app"""
    tell("quit")
