#!/usr/bin/env python
"""remove file from Dock"""
import click
import mac_dock

MODULE_NAME = "mac_dock.files.rm"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = "python -m %s path ..." % MODULE_NAME


@click.command()
@click.argument('path', nargs=-1)
def _cli(path):
    if not path:
        path = list(map(lambda i: i.path, mac_dock.files.items()))
    mac_dock.files.rm(path)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
