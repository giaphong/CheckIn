#!/usr/bin/env python
"""set/get volume"""
import click
import mac_volume


MODULE_NAME = "mac_volume"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [volume]' % MODULE_NAME


@click.command()
@click.argument('volume', nargs=-1, required=True)
def _cli(volume=None):
    if volume is not None:
        mac_volume.change(int(volume))
    else:
        print(mac_volume.get())


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
