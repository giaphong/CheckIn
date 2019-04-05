#!/usr/bin/env python
"""todo"""
import ccmenu
import click

MODULE_NAME = "ccmenu.projects.add"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s name url' % MODULE_NAME


@click.command()
@click.argument('name', required=True)
@click.argument('url', required=True)
def _cli(name,url):
    ccmenu.projects.add(name,url)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
