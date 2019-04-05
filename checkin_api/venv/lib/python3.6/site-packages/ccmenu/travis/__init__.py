#!/usr/bin/env python
import ccmenu
import public


def url(name, branch=None, token=None):
    url = "https://api.travis-ci.org/repositories/%s/cc.xml" % name
    params = []
    if branch:
        params.append("branch=%s" % branch)
    if token:
        params.append("token=%s" % token)
    if params:
        url = "%s?%s" % (url, "&".join(params))
    return url


@public.add
def add(name):
    """add travis project by fullname (owner/repo)"""
    ccmenu.projects.add(name, url(name))


@public.add
def replace(names):
    """replace travis projects"""
    clear()
    for name in names:
        add(name)


@public.add
def clear():
    """clear travis projects"""
    data = ccmenu.preferences.read()
    Projects = data.get("Projects", {})
    Projects = list(filter(lambda p: "api.travis-ci." not in p["serverUrl"], Projects))
    data["Projects"] = Projects
    ccmenu.preferences.write(data)
