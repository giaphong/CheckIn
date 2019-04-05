#!/usr/bin/env python
"""add travis repos"""
import ccmenu
import click

MODULE_NAME = "ccmenu.travis.add"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s name ...' % MODULE_NAME


@click.command()
@click.argument('names', nargs=-1, required=True)
def _cli(names):
    for name in names:
        ccmenu.travis.add(name)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
