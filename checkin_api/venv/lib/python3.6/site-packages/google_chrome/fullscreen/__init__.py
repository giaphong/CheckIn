#!/usr/bin/env python
import google_chrome
import public


@public.add
def detect():
    """return True if fullscreen mode detected, else False"""
    out = google_chrome.tell("""
    set fullscreen to false
        if count of windows is not 0 then
            set {x,y,width, height} to bounds of front window
            set fullscreen to x is 0 and y is 0
        end if
        return fullscreen
    """).out
    return "true" in out


@public.add
def toggle():
    """toggle fullscreen mode"""
    google_chrome.tell("""activate
delay 0.5 -- delay REQUIRED
tell application "System Events"
        keystroke "f" using {command down, control down}
end tell""")


@public.add
def enter():
    """enter fullscreen mode"""
    if not detect():
        toggle()

@public.add
def exit():
    """exit fullscreen mode"""
    if detect():
        toggle()
