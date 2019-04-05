#!/usr/bin/env python
"""print repo topics"""
import click
import github_topics

MODULE_NAME = "github_topics.get"
USAGE = 'python -m %s fullname' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
@click.argument('fullname')
def _cli(fullname):
    topics = github_topics.get(fullname)
    if topics:
        print("\n".join(sorted(topics)))


if __name__ == "__main__":
    _cli()
