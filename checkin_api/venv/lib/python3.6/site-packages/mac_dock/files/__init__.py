#!/usr/bin/env python
try:
    from urllib import quote  # python2
except ImportError:
    from urllib.parse import quote  # python3
import os
import mac_dock


def items():
    """return a list of Dock files"""
    d = mac_dock.preferences.read()["persistent-others"]
    return list(map(mac_dock.Item, filter(lambda i: "file" in i["tile-type"], d)))


def add(path):
    """add file to Dock"""
    path = os.path.realpath(os.path.abspath(os.path.expanduser(path)))
    data = mac_dock.preferences.read()
    ns_url = "file://%s/" % quote(path)
    label_name = os.path.basename(path)
    d = {'tile-data': {'file-data': {'_CFURLString': ns_url, '_CFURLStringType': 15},
                       'file-label': label_name},
         'tile-type': 'file-tile'}
    if not bool(list(filter(lambda i: i.path == path, items()))):
        data["persistent-others"].append(d)
    mac_dock.preferences.write(data)


def rm(path):
    """remove file from Dock"""
    mac_dock.items.rm("persistent-others", path)


"""
persistent-others
tile-data file-type
2   for non-volume
18  for volume
32  if not a folder
"""
