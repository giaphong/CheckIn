#!/usr/bin/env python
import ini2dict
import os
import public
import values
import github_webhooks.api


GITHUB_WEBHOOKS_INI = os.path.expanduser("~/.github-webhooks.ini")
GITHUB_WEBHOOKS_INI = os.getenv("GITHUB_WEBOOKS_INI", GITHUB_WEBHOOKS_INI)


@public.add
def exists(fullname, webhook):
    """return True if webhook exists"""
    for hook in github_webhooks.api.get(fullname):
        name = hook["name"]
        url = hook["config"]["url"]
        if hook == name or hook == url:
            return True
    return False


@public.add
def add(fullname, url, events=["push"]):
    """add repo webhook"""
    if not events:
        events = ["push"]
    for hook in github_webhooks.api.get(fullname):
        if hook["config"]["url"] == url:
            return hook
    events = values.get(events)
    api_url = "https://api.github.com/repos/%s/hooks" % fullname
    config = dict(url=url, content_type="json")
    data = dict(name="web", active=True, events=events, config=config)
    return github_webhooks.api.request("POST", api_url, data).json()


@public.add
def delete(fullname, webhooks):
    """delete repo webhooks by id or name or url"""
    data = github_webhooks.api.get(fullname)
    for webhook in values.get(webhooks):
        for hook in data:
            hook_id = hook["id"]
            name = hook["name"]
            url = hook["config"]["url"]
            if webhook == hook_id or webhook == name or webhook == url:
                github_webhooks.api.delete(fullname, hook_id)


@public.add
def init(fullname, sections):
    """init webhook from init file sections"""
    webhooks = ini2dict.read(GITHUB_WEBHOOKS_INI)
    for section in values.get(sections):
        url = webhooks[section]["url"]
        events = webhooks[section].get("events", "push").replace(" ", "").split(",")
        add(fullname, url, events=events)

"""
path = "/Users/russianidiot/git/looking-for-a-job/private-dotfiles/dotfiles"
fullname = "looking-for-a-job/private-dotfiles"
init(fullname, "push")
# print(github_webhooks.api.get(fullname))
#delete(fullname, "web")
# os.chdir(path)
# print(github_webhooks.api.get(fullname))
"""
