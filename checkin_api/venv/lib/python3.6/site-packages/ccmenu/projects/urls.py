#!/usr/bin/env python
"""print project urls"""
import ccmenu
import click

MODULE_NAME = "ccmenu.projects.urls"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s' % MODULE_NAME


@click.command()
def _cli():
    urls = ccmenu.projects.urls()
    if urls:
        print("\n".join(urls))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
