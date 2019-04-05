#!/usr/bin/env python
"""`git remote rm name`"""
import click
import github_remote

MODULE_NAME = "github_remote.rm"
PROG_NAME = 'python -m %s' % MODULE_NAME


def _help(ctx, param, value):
    if value:
        print("usage: %s" % PROG_NAME)
        ctx.exit()


@click.command()
@click.option('--help', is_flag=True, is_eager=False, expose_value=False, callback=_help)
def _cli():
    github_remote.rm()


if __name__ == "__main__":
    _cli()
