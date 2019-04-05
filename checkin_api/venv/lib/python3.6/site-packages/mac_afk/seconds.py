#!/usr/bin/env python
"""macOS afk time in seconds"""
import mac_afk


def cli():
    print(mac_afk.seconds())


if __name__ == "__main__":
    cli()
