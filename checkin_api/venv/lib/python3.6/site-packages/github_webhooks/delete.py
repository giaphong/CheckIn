#!/usr/bin/env python
"""delete all repo webhooks"""
import click
import github_repo
import github_webhooks

MODULE_NAME = "github_webhooks.delete"
USAGE = 'python -m %s webhook ...' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
@click.argument('webhooks', nargs=-1, required=True)
def _cli(webhooks):
    fullname = github_repo.fullname()
    for webhook in webhooks:
        github_webhooks.delete(fullname, webhook)


if __name__ == "__main__":
    _cli()
