#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import public
import runcmd


@public.add
def get(path=None):
    """return `git status` string"""
    if not path:
        path = os.getcwd()
    cmd = ["git", "status", "-s"]
    r = runcmd.run(cmd, cwd=path)._raise()
    return r.out


@public.add
class Status:
    """`git status` parser"""
    __readme__ = ["startswith", "A", "D", "M", "R", "untracked"]
    path = None
    out = None

    def __init__(self, path=None):
        if not path:
            path = os.getcwd()
        self.path = path
        self.out = get(path)

    def _startswith(self, string):
        """return a list of files startswith string"""
        lines = []
        for line in self.out.splitlines():
            if line.find(string) == 0:
                lines.append(" ".join(line.split(" ")[2:]))
        return lines

    @property
    def A(self):
        """return a list of added files"""
        return self._startswith(" A")

    @property
    def D(self):
        """return a list of deleted files"""
        return self._startswith(" D")

    @property
    def M(self):
        """return a list of modified files"""
        return self._startswith(" M")

    @property
    def R(self):
        """return a list of renamed files"""
        return self._startswith(" R")

    @property
    def untracked(self):
        """return a list of untracked files"""
        return self._startswith(" ??")
