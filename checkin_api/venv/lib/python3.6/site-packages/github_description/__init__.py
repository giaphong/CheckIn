#!/usr/bin/env python
import github
import os
import public


def _get_repo(fullname):
    g = github.Github(os.environ["GITHUB_TOKEN"])
    if "/" in fullname:
        return g.get_repo(fullname)
    return g.get_user().get_repo(fullname)


@public.add
def get(fullname):
    """return repo description"""
    return _get_repo(fullname).description


@public.add
def update(fullname, description):
    """update repo description"""
    _get_repo(fullname).edit(description=description)
