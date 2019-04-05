#!/usr/bin/env python
"""set Finder tags. `red` - status, `orange` - stderr, `gray` - unloaded"""
import click
import mac_agents
import os

LaunchAgents = os.path.join(os.environ["HOME"], "Library/LaunchAgents")


MODULE_NAME = "mac_agents.tag"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s [path]' % MODULE_NAME


@click.command()
@click.argument('path', default=LaunchAgents, required=True)
def _cli(path):
    mac_agents.tag(path)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
