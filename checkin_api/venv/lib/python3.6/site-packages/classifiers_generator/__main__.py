#!/usr/bin/env python
"""generate `classifiers.txt`"""
import click
import classifiers_generator
import os
import sys

MODULE_NAME = "classifiers-generator"
USAGE = 'python -m %s [requirements_path]' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
@click.argument('path', default='requirements.txt', required=False)
def _cli(path='requirements.txt'):
    if not path:
        path = 'requirements.txt'
    if not os.path.exists(path):
        sys.exit("ERROR: requirements.txt NOT EXISTS")
    classifiers = classifiers_generator.Requirements(path).classifiers()
    if classifiers:
        print("\n".join(classifiers))


if __name__ == "__main__":
    _cli()
