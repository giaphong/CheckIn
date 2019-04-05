#!/usr/bin/env python
"""add environment variables from env file(s)"""
import click
import launchd_env
import env_file

MODULE_NAME = "launchd_env.add"
USAGE = 'python -m %s plist_file env_file ...' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
@click.argument('plist_file', required=True)
@click.argument('env_files', nargs=-1, required=True)
def _cli(plist_file, env_files):
    vars = dict(launchd_env.read(plist_file))
    for f in env_files:
        vars.update(env_file.get(f))
    launchd_env.write(plist_file, **vars)


if __name__ == "__main__":
    _cli()
