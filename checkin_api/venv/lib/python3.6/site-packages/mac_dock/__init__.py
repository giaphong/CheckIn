#!/usr/bin/env python
import mac_dock.launchctl as launchctl
import mac_dock.preferences as preferences
import mac_dock.items as items
from mac_dock.items import Item
import mac_dock.apps as apps
import mac_dock.files as files
import mac_dock.folders as folders
import public

autohide = preferences.read().get("autohide", None)
tilesize = preferences.read().get("tilesize", None)


@public.add
def save():
    """save Dock preferences"""
    data = preferences.read()
    if isinstance(autohide, bool):
        data["autohide"] = autohide
    if isinstance(tilesize, (int, float)):
        data["tilesize"] = tilesize
    preferences.write(data)
