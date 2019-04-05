#!/usr/bin/env python
import github
import os
import public


@public.add
def delete(fullname):
    """delete github repo"""
    g = github.Github(os.environ["GITHUB_TOKEN"])
    owner = g.get_user()
    repo_name = fullname.split("/")[-1]
    if "/" in fullname:
        owner_name = fullname.split("/")[0]
        if owner.login != owner_name:
            owner = g.get_organization(owner_name)
    try:
        owner.get_repo(repo_name).delete()
    except github.GithubException:
        print("SKIP: %s/%s not exists" % (owner.login, repo_name))
