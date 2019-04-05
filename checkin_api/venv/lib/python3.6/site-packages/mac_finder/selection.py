#!/usr/bin/env python
"""print Finder selection paths"""
import mac_finder


def _cli():
    _selection = mac_finder.selection()
    if _selection:
        print("\n".join(_selection))


if __name__ == '__main__':
    _cli()
