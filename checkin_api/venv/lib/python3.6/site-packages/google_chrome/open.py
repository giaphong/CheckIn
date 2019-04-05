#!/usr/bin/env python
"""open url(s)"""
import click
import google_chrome

MODULE_NAME = "google_chrome.open"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s url ...' % MODULE_NAME

@click.command()
@click.argument("url")
def _cli(url):
    google_chrome.refresh(url) or google_chrome.open(url)
    google_chrome.activate()

if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
