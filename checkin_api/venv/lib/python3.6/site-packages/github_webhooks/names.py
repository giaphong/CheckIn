#!/usr/bin/env python
"""print repo webhooks names"""
import click
import github_repo
import github_webhooks

MODULE_NAME = "github_webhooks.names"
PROG_NAME = 'python -m %s' % MODULE_NAME


@click.command()
def _cli():
    names = []
    fullname = github_repo.fullname()
    data = github_webhooks.api.get(fullname)
    for hook in data:
        url = hook["config"]["name"]
        names.append(url)
    if names:
        print("\n".join(names))


if __name__ == "__main__":
    _cli()
