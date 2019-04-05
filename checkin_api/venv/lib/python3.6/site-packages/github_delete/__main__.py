#!/usr/bin/env python
"""delete github repo(s)"""
import click
import github_delete

MODULE_NAME = "github_delete"
USAGE = 'python -m %s name ...' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
@click.argument('names', nargs=-1, required=True)
def _cli(names):
    for name in names:
        github_delete.delete(name)


if __name__ == "__main__":
    _cli()
