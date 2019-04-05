#!/usr/bin/env python
from distutils import dir_util
import os
import shutil
import public


def _cp_file(source, target):
    if (os.path.exists(target) or os.path.lexists(target)):
        if os.path.isfile(source) != os.path.isfile(target):
            os.unlink(target)
    dirname = os.path.dirname(target)
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname)
    shutil.copy(source, target)


def _cp_dir(source, target):
    if not os.path.exists(target):
        os.makedirs(target)
    dir_util.copy_tree(source, target)


def _get_target(source, target):
    if os.path.isfile(source) and os.path.isdir(target):
        return os.path.join(target, os.path.basename(source))
    return target


def _copy(source, target):
    target = _get_target(source, target)
    if os.path.isfile(source) or os.path.islink(source):
        _cp_file(source, target)
    if os.path.isdir(source):
        _cp_dir(source, target)


@public.add
def cp(source, target, force=True):
    """Copy the directory/file src to the directory/file target"""
    if (os.path.exists(target) and not force) or source == target:
        return
    _copy(source, target)
