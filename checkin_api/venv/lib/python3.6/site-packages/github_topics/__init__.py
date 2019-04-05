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
    """return a list of repo topics"""
    return _get_repo(fullname).get_topics()


@public.add
def replace(fullname, topics):
    """replace repo topics"""
    return _get_repo(fullname).replace_topics(list(topics))


@public.add
def add(fullname, topics):
    """add repo topics"""
    old_topics = get(fullname)
    new_topics = list(set(list(old_topics) + list(topics)))
    replace(fullname, new_topics)


@public.add
def rm(fullname, topics):
    """remove repo topics"""
    old_topics = get(fullname)
    new_topics = list(set(old_topics) - set(topics))
    replace(fullname, new_topics)


@public.add
def clear(fullname):
    """remove all repo topics"""
    replace(fullname, [])
