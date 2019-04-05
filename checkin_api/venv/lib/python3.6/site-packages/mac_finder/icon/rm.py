#!/usr/bin/env python
"""remove icon"""
import os
import click
import mac_finder

MODULE_NAME = "mac_finder.icon.rm"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = "python -m %s path ..." % MODULE_NAME


@click.command()
@click.argument('path', nargs=-1, required=True)
def _cli(path):
    for _path in path:
        fullpath = os.path.abspath(os.path.expanduser(_path))
        if os.path.exists(fullpath):
            mac_finder.icon(fullpath)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
