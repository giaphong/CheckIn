#!/usr/bin/env python
import os
import plistlib
import public
import ccmenu.preferences
import ccmenu.projects
import ccmenu.travis

@public.add
def restart():
    """restart CCMenu.app"""
    os.system("killall cfprefsd CCMenu 2> /dev/null")
    os.system("open -a CCMenu 2> /dev/null")
