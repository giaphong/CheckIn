#!/usr/bin/env python
"""add repo webhook(s)"""
import click
import github_repo
import github_webhooks

MODULE_NAME = "github_webhooks.add"
USAGE = 'python -m %s events url' % MODULE_NAME
PROG_NAME = 'python -m %s' % MODULE_NAME


@click.command()
@click.argument('events', required=True)
@click.argument('url', required=True)
def _cli(events, url):
    fullname = github_repo.fullname()
    events = events.replace(" ", "").split(",")
    data = github_webhooks.add(fullname, events, url)
    print(data)


if __name__ == "__main__":
    _cli()
