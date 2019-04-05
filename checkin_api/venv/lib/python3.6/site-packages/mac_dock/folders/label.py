#!/usr/bin/env python
"""print Dock folders labels"""
import click
import mac_dock

MODULE_NAME = "mac_dock.folders.label"
PROG_NAME = 'python -m %s' % MODULE_NAME


@click.command()
def _cli():
    labels = list(map(lambda i: i.label, mac_dock.folders.items()))
    if labels:
        print("\n".join(labels))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
