#!/usr/bin/env python
"""generate README"""
import click
import readme_generator


MODULE_NAME = "readme_generator"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s source_folder ...' % MODULE_NAME


@click.command()
@click.argument('folders', nargs=-1, required=True)
def _cli(folders):
    readme = readme_generator.Readme(folders)
    string = readme.render()
    if string:
        print(string)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
