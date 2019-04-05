#!/usr/bin/env python
"""print Dock files labels"""
import click
import mac_dock

MODULE_NAME = "mac_dock.files.label"
PROG_NAME = 'python -m %s' % MODULE_NAME


@click.command()
def _cli():
    labels = list(map(lambda i: i.label, mac_dock.files.items()))
    if labels:
        print("\n".join(labels))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
