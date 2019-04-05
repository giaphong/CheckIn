#!/usr/bin/env python
"""print user packages"""
import click
import pypi_xmlrpc

MODULE_NAME = "pypi_xmlrpc.user_packages"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s user' % MODULE_NAME


@click.command()
@click.argument('user', required=True)
def _cli(user):
    packages = pypi_xmlrpc.user_packages(user)
    for role, name in packages:
        if "Maintainer".lower() in role.lower():
            print("%s (Maintainer)" % name)
        else:
            print(name)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
