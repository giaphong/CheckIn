#!/usr/bin/env python
"""create github repo(s)"""
import click
import github_create

MODULE_NAME = "github_create"
USAGE = 'python -m %s name ...' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
@click.argument('names', nargs=-1, required=True)
def _cli(names):
    for name in names:
        github_create.create(name)


if __name__ == "__main__":
    _cli()
