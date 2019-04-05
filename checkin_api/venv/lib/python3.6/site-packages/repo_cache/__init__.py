#!/usr/bin/env python
import hashlib
import os
import public
import shutil

XDG_CACHE_HOME = os.getenv("XDG_CACHE_HOME", os.path.expanduser("~/.cache"))
REPO_CACHE_HOME = os.getenv("REPO_CACHE_HOME", os.path.join(XDG_CACHE_HOME, "repo-cache"))


@public.add
def shasum():
    """return a string with sha1 checksum for a current repo (working dir)"""
    return hashlib.sha1("{}\n".format(os.getcwd()).encode()).hexdigest()


@public.add
def fullpath(key):
    """return a string with a cache file full path"""
    return os.path.join(REPO_CACHE_HOME, shasum(), key)


@public.add
def clear():
    """clear repo cache"""
    path = os.path.join(REPO_CACHE_HOME, shasum())
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    if os.path.isdir(fullpath):
        shutil.rmtree(fullpath)


@public.add
def read(key):
    """return a cached string"""
    path = fullpath(key)
    if os.path.exists(path):
        return open(path).read()


@public.add
def write(key, string):
    """write a string to a repo cache and return a cache file full path"""
    path = fullpath(key)
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    open(path, "w").write(string)
    return path
