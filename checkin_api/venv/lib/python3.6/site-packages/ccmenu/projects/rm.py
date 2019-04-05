#!/usr/bin/env python
"""remove from CCMenu"""
import ccmenu
import click

MODULE_NAME = "ccmenu.projects.rm"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s project ...' % MODULE_NAME


@click.command()
@click.argument('project', nargs=-1, required=True)
def _cli(projects):
    for project in projects:
        ccmenu.projects.rm(project)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
