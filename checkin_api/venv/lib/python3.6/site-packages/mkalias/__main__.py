#!/usr/bin/env python
"""make MacOS Finder alias"""
import click
import mkalias

MODULE_NAME = "mkalias"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s src dst' % MODULE_NAME


@click.command()
@click.argument('src', required=True)
@click.argument('dst', required=True)
def _cli(src, dst):
    mkalias.mkalias(src, dst)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
