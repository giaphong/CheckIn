#!/usr/bin/env python
import inspect
import os
import public

"""
https://pypi.org/pypi?%3Aaction=list_classifiers
"""


def _string(value):
    try:
        return isinstance(value, basestring)
    except NameError:
        return isinstance(value, str)


def _valid(value):
    return _string(value) and " :: " in value


def _iterable_values(value):
    try:
        value = list(value)
        for v in value:
            if not _valid(v):
                return []
        return list(value)
    except TypeError:
        return []


def _values(value):
    if _string(value):
        if _valid(value):
            return [value]
    if hasattr(value, "__iter__"):
        return _iterable_values(value)
    return []


@public.add
class Classifiers(list):
    """classifiers.txt generator"""
    __readme__ = ["load", "save", "update"]

    def __init__(self, *args):
        super(Classifiers, self).__init__(*args)
        self.update()

    def update(self):
        """update classifiers from attrs/properties with with `::` """
        for name, member in inspect.getmembers(self):
            self += _values(member)

    def load(self, path):
        """load classifiers from file"""
        for line in open(path).read().splitlines():
            if _valid(line):
                self.append(line)
        return self

    def save(self, path):
        """save classifiers to file"""
        path = os.path.abspath(os.path.expanduser(path))
        if not os.path.exists(path):
            os.makedirs(path)
        open(path, "w").write("\n".join(self))
        return self

    def append(self, x):
        if x not in self:
            list.append(self, x)
            self.sort()
        return self

    def __add__(self, other):
        for value in other:
            if value not in self:
                self.append(value)
        self.sort()
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return "\n".join(self)

    def __repr__(self):
        return self.__str__()
