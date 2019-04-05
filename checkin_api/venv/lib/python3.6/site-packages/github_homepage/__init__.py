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
    """return repo homepage"""
    return _get_repo(fullname).homepage


@public.add
def update(fullname, url):
    """update repo homepage"""
    _get_repo(fullname).edit(homepage=url)
