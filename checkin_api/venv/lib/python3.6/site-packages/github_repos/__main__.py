#!/usr/bin/env python
"""print user repos"""
import click
import github_repos

MODULE_NAME = "github_repos"
USAGE = 'python -m %s [login]' % MODULE_NAME
PROG_NAME = 'python -m %s ' % USAGE


@click.command()
@click.argument('login',required=False)
def _cli(login=None):
    repos = github_repos.repos(login)
    if repos:
        print("\n".join(repos))


if __name__ == "__main__":
    _cli()
