#!/usr/bin/env python
"""print Dock files paths"""
import click
import mac_dock

MODULE_NAME = "mac_dock.files.path"
PROG_NAME = 'python -m %s' % MODULE_NAME


@click.command()
def _cli():
    paths = list(map(lambda i: i.path, mac_dock.files.items()))
    if paths:
        print("\n".join(paths))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
