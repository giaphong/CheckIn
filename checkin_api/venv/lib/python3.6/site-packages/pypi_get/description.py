#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""print project description"""
import click
import pypi_get

MODULE_NAME = "pypi_get.%s" % __file__.split("/")[-1].split(".")[0]
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s name [version]' % MODULE_NAME


@click.command()
@click.argument('name', required=True)
@click.argument('version', required=False)
def _cli(name, version=None):
    data = pypi_get.get(name, version)
    if "info" in data and "description" in data["info"]:
        description = data["info"]["description"]
        if description:
            print(description)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
