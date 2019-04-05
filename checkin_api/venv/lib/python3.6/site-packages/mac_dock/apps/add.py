#!/usr/bin/env python
"""add app to Dock"""
import click
import mac_dock

MODULE_NAME = "mac_dock.apps.add"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = "python -m %s path ..." % MODULE_NAME


@click.command()
@click.argument('path', nargs=-1)
def _cli(path):
    mac_dock.apps.add(path)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
