#!/usr/bin/env python
import subprocess

PLIST = '/System/Library/LaunchAgents/com.apple.Dock.plist'
LABEL = 'com.apple.Dock.agent'


def load():
    subprocess.call(['/bin/launchctl', 'load', PLIST])


def unload():
    subprocess.call(['/bin/launchctl', 'unload', PLIST])


def start():
    subprocess.call(['/bin/launchctl', 'start', LABEL])
