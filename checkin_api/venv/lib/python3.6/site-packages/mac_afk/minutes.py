#!/usr/bin/env python
"""macOS afk time in minutes"""
import mac_afk


def cli():
    print(mac_afk.minutes())


if __name__ == "__main__":
    cli()
