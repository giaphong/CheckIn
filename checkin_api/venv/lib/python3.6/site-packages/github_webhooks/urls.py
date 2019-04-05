#!/usr/bin/env python
"""print repo webhooks urls"""
import click
import github_repo
import github_webhooks

MODULE_NAME = "github_webhooks.urls"
PROG_NAME = 'python -m %s' % MODULE_NAME


@click.command()
def _cli():
    urls = []
    fullname = github_repo.fullname()
    data = github_webhooks.api.get(fullname)
    for hook in data:
        url = hook["config"]["url"]
        urls.append(url)
    if urls:
        print("\n".join(urls))


if __name__ == "__main__":
    _cli()
