#!/usr/bin/env python
"""generate `classes` table"""
import click
import readme_docstring

MODULE_NAME = "readme_docstring.classes"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s' % MODULE_NAME


@click.command()
def _cli():
    table = readme_docstring.Classes()
    if table:
        print(str(table))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
