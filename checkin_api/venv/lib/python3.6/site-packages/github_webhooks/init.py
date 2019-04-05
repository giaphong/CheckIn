#!/usr/bin/env python
"""init webhook from init file sections"""
import click
import github_repo
import github_webhooks

MODULE_NAME = "github_webhooks.init"
USAGE = 'python -m %s section ...' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
@click.argument('sections', nargs=-1, required=True)
def _cli(sections):
    fullname = github_repo.fullname()
    github_webhooks.init(fullname, sections)


if __name__ == "__main__":
    _cli()
