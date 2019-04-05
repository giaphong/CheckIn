#!/usr/bin/env python
"""print Dock apps bundles"""
import click
import mac_dock

MODULE_NAME = "mac_dock.apps.bundle"
PROG_NAME = 'python -m %s' % MODULE_NAME


@click.command()
def _cli():
    bundles = list(map(lambda i: i.bundle, mac_dock.apps.items()))
    if bundles:
        print("\n".join(bundles))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
