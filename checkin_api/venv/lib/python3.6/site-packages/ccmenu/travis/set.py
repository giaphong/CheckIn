#!/usr/bin/env python
"""replace travis projects and restart CCMenu.app"""
import ccmenu
import click

MODULE_NAME = "ccmenu.travis.set"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s name ...' % MODULE_NAME


@click.command()
@click.argument('names', nargs=-1, required=True)
def _cli(names):
    ccmenu.travis.replace(names)
    ccmenu.restart()


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
