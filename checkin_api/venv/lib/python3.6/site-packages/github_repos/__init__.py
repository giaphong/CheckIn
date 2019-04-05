#!/usr/bin/env python
import github
import os
import public


@public.add
def repos(login=None):
    """return a list of user repos"""
    fullnames = []
    TOKEN = os.environ["GITHUB_TOKEN"]
    g = github.Github(TOKEN)
    if login:
        user = g.get_user(login)
    else:
        user = g.get_user()
    for repo in user.get_repos():
        fullname = "%s/%s" % (repo.owner.login, repo.name)
        fullnames += [fullname]
    return fullnames
