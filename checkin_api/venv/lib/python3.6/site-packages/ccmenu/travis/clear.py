#!/usr/bin/env python
"""clear travis projects"""
import ccmenu
import click

MODULE_NAME = "ccmenu.travis.clear"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s' % MODULE_NAME


@click.command()
def _cli():
    ccmenu.travis.clear()


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
