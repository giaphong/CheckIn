#!/usr/bin/env python
import os
try:
    from urllib import unquote  # python2
except ImportError:
    from urllib.parse import unquote  # python3
import mac_dock
import values


class Item:
    def __init__(self, data):
        self.data = data

    @property
    def guid(self):
        return self.data["GUID"]

    @property
    def label(self):
        return self.data["tile-data"].get("file-label", "")  # empty if just added

    @property
    def url(self):
        # _CFURLStringType (0: path, 15: url), _CFURLString
        return self.data["tile-data"]["file-data"]["_CFURLString"]

    @property
    def path(self):
        path = unquote(self.url).replace("file://", "")
        return path[:-1] if path and path[-1] == "/" else path

    def __getitem__(self, key):
        return self.data[key]

    def __str__(self):
        return '<Dock label="%s" path="%s">' % (self.label, self.path)

    def __repr__(self):
        return self.__str__()


def _eq(item_data, value):
    item = Item(item_data)
    for item_value in [item.label, item.path, os.path.basename(item.path)]:
        if item_value and item_value.lower() == value.lower():
            return True


def rm(section, value):
    data = mac_dock.preferences.read()
    for value in list(set(values.get(value))):
        i = 0
        for item_data in data[section]:
            if _eq(item_data, value):
                data[section].pop(i)
                continue
            i += 1
    mac_dock.preferences.write(data)
