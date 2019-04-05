#!/usr/bin/env python
"""remove app from Dock"""
import click
import mac_dock

MODULE_NAME = "mac_dock.apps.rm"
PROG_NAME = 'python -m %s' % "mac_dock.apps.rm"
USAGE = "python -m %s path ..." % MODULE_NAME


@click.command()
@click.argument('path', nargs=-1)
def _cli(path):
    mac_dock.apps.rm(path)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
