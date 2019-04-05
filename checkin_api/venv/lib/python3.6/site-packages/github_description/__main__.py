#!/usr/bin/env python
"""get/set repo description"""
import click
import github_description

MODULE_NAME = "github_description"
USAGE = 'python -m %s fullname [description]' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
@click.argument('fullname')
@click.argument('words', nargs=-1, required=False)
def _cli(fullname, words=None):
    description = " ".join(words)
    if words:
        github_description.update(fullname, description)
    else:
        description = github_description.get(fullname)
        if description:
            print(description)


if __name__ == "__main__":
    _cli()
