#!/usr/bin/env python
import mac_dock
import values


class App(mac_dock.Item):
    @property
    def extra(self):
        return self.data["tile-data"]["dock-extra"]

    @property
    def bundle(self):
        return self.data["tile-data"].get("bundle-identifier", "")  # empty if just added


def add(path):
    """add app to Dock"""
    data = mac_dock.preferences.read()
    for _path in values.get(path):
        d = {'tile-data': {'file-data': {'_CFURLString': _path, '_CFURLStringType': 0}}}
        if _path not in str(data["persistent-apps"]):
            data["persistent-apps"].append(d)
    mac_dock.preferences.write(data)


def rm(app):
    """rm app from Dock"""
    mac_dock.items.rm("persistent-apps", app)


def items():
    """return a list of Dock apps"""
    return list(map(App, mac_dock.preferences.read()["persistent-apps"]))
