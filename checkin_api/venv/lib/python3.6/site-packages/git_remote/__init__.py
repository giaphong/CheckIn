#!/usr/bin/env python
import runcmd
import public

"""
https://git-scm.com/docs/git-remote
"""


@public.add
def run(args):
    """run `git remote` with args and return output"""
    return runcmd.run(["git", "remote"] + list(args))._raise().out


@public.add
def add(name, url):
    """`git remote add name url`"""
    run(["add", name, url])


@public.add
def remove(name):
    """`git remote rm name`"""
    run(["remove", name])


@public.add
def rm(name):
    """`git remote rm name`"""
    run(["rm", name])


@public.add
def rename(old, new):
    """`git remote rename old new`"""
    run(["rename", old, new])


@public.add
def set_url(name, url):
    """`git remote set-url old new`"""
    return run(["set-url", name, url])


@public.add
def remotes():
    """return a list of git remote tuples (name, url)"""
    result = []
    for l in run(["-v"]).splitlines():
        name, url, role = l.split()
        if "fetch" in role:
            result.append([name, url])
    return result


@public.add
def names():
    """return git remote names"""
    return list(lambda name, url: name, remotes())


@public.add
def urls():
    """return git remote urls"""
    return list(lambda name, url: url, remotes())
