#!/usr/bin/env python
"""get/set repo homepage"""
import click
import github_homepage

MODULE_NAME = "github_homepage"
USAGE = 'python -m %s fullname [url]' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
@click.argument('fullname')
@click.argument('url', required=False)
def _cli(fullname, url=None):
    if url is not None:
        github_homepage.update(fullname, url)
    else:
        url = github_homepage.get(fullname)
        if url:
            print(url)


if __name__ == "__main__":
    _cli()
