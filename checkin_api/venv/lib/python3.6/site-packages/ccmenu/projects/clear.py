#!/usr/bin/env python
"""clear all projects"""
import ccmenu
import click

MODULE_NAME = "ccmenu.projects.clear"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s' % MODULE_NAME


@click.command()
def _cli():
    ccmenu.projects.clear()


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
