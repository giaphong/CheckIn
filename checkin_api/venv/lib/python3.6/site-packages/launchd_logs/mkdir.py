#!/usr/bin/env python
"""make plist file log folders"""
import click
import launchd_logs

MODULE_NAME = "launchd_logs.mkdir"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s plist_path ...' % MODULE_NAME


@click.command()
@click.argument('plist_paths', nargs=-1, required=True)
def _cli(plist_paths):
    for plist_path in plist_paths:
        launchd_logs.mkdir(plist_path)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
