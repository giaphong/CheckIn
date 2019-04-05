#!/usr/bin/env python
"""remove all repo topics"""
import click
import github_topics

MODULE_NAME = "github_topics.clear"
USAGE = 'python -m %s fullname' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
@click.argument('fullname')
def _cli(fullname):
    github_topics.clear(fullname)


if __name__ == "__main__":
    _cli()
