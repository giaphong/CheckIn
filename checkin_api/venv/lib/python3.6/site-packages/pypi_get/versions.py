#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""print project versions"""
import click
import pypi_get

MODULE_NAME = "pypi_get.%s" % __file__.split("/")[-1].split(".")[0]
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s name' % MODULE_NAME


@click.command()
@click.argument('name', required=True)
def _cli(name):
    data = pypi_get.get(name)
    if "releases" in data:
        releases = data["releases"]
        if releases:
            print("\n".join(list(releases.keys())))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
