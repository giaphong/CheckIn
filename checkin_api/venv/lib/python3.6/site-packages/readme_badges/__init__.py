#!/usr/bin/env python
import badge
import os
import public
import readme_badges.github
import readme_badges.npm
import readme_badges.pypi
import shields
import github_repo


class Language(shields.Badge):
    subject = "language"
    color = "blue"
    longCache = True


@public.add
def language(text):
    """language badge"""
    if text:
        return str(Language(status=text))
    return ""


class Travis(badge.Badge):
    def __init__(self, fullname=None):
        if not fullname:
            fullname = github_repo.fullname()
            if not fullname:
                owner = os.popen("git config user.name").read().strip()
                repo = os.path.basename(os.getcwd())
                fullname = "%s/%s" % (owner, repo)
        self.fullname = fullname

    title = "Travis"
    image = "https://api.travis-ci.org/{fullname}.svg?branch={branch}"
    link = "https://travis-ci.org/{fullname}/"


@public.add
def travis(fullname=None):
    """travis status badge"""
    return str(Travis(fullname))
