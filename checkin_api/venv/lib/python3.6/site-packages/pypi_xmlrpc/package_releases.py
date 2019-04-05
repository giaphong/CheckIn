#!/usr/bin/env python
"""print package releases"""
import click
import pypi_xmlrpc

MODULE_NAME = "pypi_xmlrpc.package_releases"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s name' % MODULE_NAME


@click.command()
@click.argument('name', required=True)
def _cli(name):
    releases = pypi_xmlrpc.package_releases(name)
    if releases:
        print("\n".join(releases))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
