#!/usr/bin/env python
"""print Dock apps labels"""
import click
import mac_dock

MODULE_NAME = "mac_dock.apps.label"
PROG_NAME = 'python -m %s' % MODULE_NAME


def _help(ctx, param, value):
    if value:
        print("usage: %s" % PROG_NAME)
        ctx.exit()


@click.command()
@click.option('--help', is_flag=True, is_eager=False, expose_value=False, callback=_help)
def _cli():
    labels = list(map(lambda i: i.label, mac_dock.apps.items()))
    if labels:
        print("\n".join(labels))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
