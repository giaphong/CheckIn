#!/usr/bin/env python
"""print Dock apps paths"""
import click
import mac_dock

MODULE_NAME = "mac_dock.apps.path"
PROG_NAME = 'python -m %s' % MODULE_NAME


@click.command()
def _cli():
    paths = list(map(lambda i: i.path, mac_dock.apps.items()))
    if paths:
        print("\n".join(paths))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
