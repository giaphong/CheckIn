#!/usr/bin/env python
import os
import public
import runcmd

"""
https://github.com/owner/repo

git@github.com:owner/repo.git           ssh
https://github.com/owner/repo.git       https

multiple ssh key:
git@owner.github.com:owner/repo.git
git@owner-github.com:owner/repo.git
git@github-owner:owner/repo.git
"""

def _remotes():
    result = []
    for l in os.popen("git remote -v").read().splitlines():
        name, url, role = l.split()
        if "fetch" in role:
            result.append([name, url])
    return result

@public.add
def add(name, url):
    """`git remote add name url`"""
    runcmd.run(["git", "remote", "add", name, url])._raise()


@public.add
def get():
    """return git remote tuple (name, url)"""
    for name, url in _remotes():
        if "git@" in url and "github" in url.split("@")[1]:
            return name, url
        if "https://" in url and "github" in url.split("/")[2]:
            return name, url

@public.add
def name():
    """return git remote name"""
    name, url = get() or (None, None)
    return name


@public.add
def url():
    """return git remote url"""
    name, url = get() or (None, None)
    return url


@public.add
def rm():
    """`git remote rm name`"""
    _name = name()
    if _name:
        runcmd.run(["git", "remote", "rm", _name])

