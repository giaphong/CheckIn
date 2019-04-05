#!/usr/bin/env python
"""print git remote url"""
import click
import github_remote

MODULE_NAME = "github_remote.url"
PROG_NAME = 'python -m %s' % MODULE_NAME


def _help(ctx, param, value):
    if value:
        print("usage: %s" % PROG_NAME)
        ctx.exit()


@click.command()
@click.option('--help', is_flag=True, is_eager=False, expose_value=False, callback=_help)
def _cli():
    url = github_remote.url()
    if url:
        print(url)


if __name__ == "__main__":
    _cli()
