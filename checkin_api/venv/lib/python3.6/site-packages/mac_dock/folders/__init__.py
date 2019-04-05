#!/usr/bin/env python
try:
    from urllib import quote  # python2
except ImportError:
    from urllib.parse import quote  # python3
import os
import mac_dock


class Folder(mac_dock.Item):
    @property
    def preferreditemsize(self):
        return self.data["tile-data"]["preferreditemsize"]

    @property
    def arrangement(self):
        return self.data["tile-data"].get("arrangement", "")  # empty if just added

    @property
    def displayas(self):
        return self.data["tile-data"].get("displayas", "")  # empty if just added

    @property
    def showas(self):
        return self.data["tile-data"].get("showas", "")  # empty if just added

    def __str__(self):
        return '<Dock folder label="%s" path="%s" arrangement="%s" displayas="%s" showas="%s">' % (self.label, self.path, self.arrangement, self.displayas, self.showas)


def items():
    """return a list of Dock folders"""
    d = mac_dock.preferences.read()["persistent-others"]
    return list(map(Folder, filter(lambda i: "dir" in i["tile-type"], d)))


def add(path, arrangement=0, displayas=1, showas=0):
    """add folder to Dock"""
    if not arrangement:
        arrangement = 1
    if not displayas:
        displayas = 2
    if not showas:
        showas = 4
    path = os.path.realpath(os.path.abspath(os.path.expanduser(path)))
    data = mac_dock.preferences.read()
    ns_url = "file://%s/" % quote(path)
    label_name = os.path.basename(path)
    d = {'tile-data': {'arrangement': arrangement,
                       'displayas': displayas,
                       'file-data': {'_CFURLString': ns_url,
                                     '_CFURLStringType': 15},
                       'file-label': label_name,
                       'showas': showas
                       },
         'tile-type': 'directory-tile'}
    if not bool(list(filter(lambda i: i.path == path, items()))):
        data["persistent-others"].append(d)
    mac_dock.preferences.write(data)


def rm(path):
    """remove folder from Dock"""
    if not path:
        path = list(map(lambda i: i.path, items()))
    mac_dock.items.rm("persistent-others", path)


"""
persistent-others
tile-data file-type
2   for non-volume
18  for volume
32  if not a folder
"""
