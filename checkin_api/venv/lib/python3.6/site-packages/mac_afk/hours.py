#!/usr/bin/env python
"""macOS afk time in hours"""
import mac_afk


def cli():
    print(mac_afk.hours())


if __name__ == "__main__":
    cli()
