#!/usr/bin/env python
import github
import os
import public


@public.add
def create(fullname):
    """create github repo"""
    g = github.Github(os.environ["GITHUB_TOKEN"])
    owner = g.get_user()
    repo_name = fullname.split("/")[-1]
    if "/" in fullname:
        owner_name = fullname.split("/")[0]
        if owner.login != owner_name:
            owner = g.get_organization(owner_name)
    try:
        owner.get_repo(repo_name)
        print("SKIP: %s/%s already exists" % (owner.login, repo_name))
    except github.GithubException:
        owner.create_repo(repo_name)
