#!/usr/bin/env python
"""generate `functions` table"""
import click
import readme_docstring

MODULE_NAME = "readme_docstring.functions"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s' % MODULE_NAME


@click.command()
def _cli():
    table = readme_docstring.Functions()
    if table:
        print(str(table))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
