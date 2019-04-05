#!/usr/bin/env python
import ccmenu.preferences
import os
import plistlib
import public

"""
free:
https://api.travis-ci.org/repositories/{user}/{repo}/cc.xml
https://api.travis-ci.org/repositories/{user}/{repo}/cc.xml?branch=<branch>

private:
https://api.travis-ci.org/repositories/{user}/{repo}/cc.xml?token=<token>
https://api.travis-ci.org/repositories/{user}/{repo}/cc.xml?token=<token>&branch=<branch>
"""

@public.add
def names():
    """return a list of projects names"""
    projects = ccmenu.preferences.read().get("Projects",[])
    return list(sorted(map(lambda p:p["projectName"],projects)))

@public.add
def urls():
    """return a list of projects urls"""
    projects = ccmenu.preferences.read().get("Projects",[])
    return list(sorted(map(lambda p:p["serverUrl"],projects)))

@public.add
def add(name,url):
    """add project"""
    data = ccmenu.preferences.read()
    Projects = data.get("Projects",{})
    Project = dict(projectName=name,serverUrl=url)
    Projects.append(Project)
    data["Projects"] = Projects
    ccmenu.preferences.write(data)

@public.add
def clear():
    """clear all projects"""
    data = ccmenu.preferences.read()
    data["Projects"] = []
    ccmenu.preferences.write(data)

@public.add
def rm(project):
    """remove project"""
    data = ccmenu.preferences.read()
    Projects = data.get("Projects",{})
    for Project in Projects:
        name = Project["projectName"]
        url = Project["serverUrl"]
        if name == project or os.path.basename(name) == project or url == project:
            Projects.remove(Project)
    data["Projects"] = Projects
    ccmenu.preferences.write(data)
