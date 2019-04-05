#!/usr/bin/env python
"""print project names"""
import ccmenu
import click

MODULE_NAME = "ccmenu.projects.names"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s' % MODULE_NAME


@click.command()
def _cli():
    names = ccmenu.projects.names()
    if names:
        print("\n".join(names))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
