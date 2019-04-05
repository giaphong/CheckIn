#!/usr/bin/env python
import os
import find
import public
import mac_colors

"""
~/Library/Logs
"""

PATH = os.path.join(os.environ["HOME"], "Library/Logs")


def _size(path):
    return os.stat(path).st_size


def files(filenames=None, minsize=0):
    """return a list of files"""
    if not minsize:
        minsize = 0
    if not os.path.exists(PATH):
        return
    for f in find.files(PATH):
        if _size(f) >= minsize and (not filenames or os.path.basename(f) in filenames):
            yield f


@public.add
def logs(filenames=None, minsize=0):
    """return a list of `.log` files"""
    return list(filter(lambda f: f[-4:] == ".log", files(filenames, minsize)))


@public.add
def rm(filenames=None, minsize=0):
    """remove `.log` files"""
    for f in logs(filenames, minsize):
        if os.path.exists(f):
            os.unlink(f)


@public.add
def errors():
    """return a list of `*err*.log` files (`stderr.log`, `err.log`, `error.log`, ...)"""
    result = []
    for f in logs(minsize=1):
        if "err" in os.path.splitext(os.path.basename(f))[0]:
            result.append(f)
    return result


def _trees(paths):
    for path in paths:
        while path != os.path.dirname(PATH):
            yield path
            path = os.path.dirname(path)


@public.add
def tag():
    """set Finder tag. `red` - not empty error logs, `none` - other logs"""
    red = list(_trees(errors()))
    none = list(set(_trees(logs())) - set(red))
    mac_colors.red(red)
    mac_colors.none(none)
