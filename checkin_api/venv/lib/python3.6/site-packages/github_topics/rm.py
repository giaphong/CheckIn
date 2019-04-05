#!/usr/bin/env python
"""remove repo topics"""
import click
import github_topics

MODULE_NAME = "github_topics.remove"
USAGE = 'python -m %s fullname topic ...' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
@click.argument('fullname')
@click.argument('topics', nargs=-1, required=True)
def _cli(fullname, topics):
    github_topics.rm(fullname, topics)


if __name__ == "__main__":
    _cli()
