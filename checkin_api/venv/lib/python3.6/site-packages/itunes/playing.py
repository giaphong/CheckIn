#!/usr/bin/env python
"""print true if iTunes playing"""
import itunes

if __name__ == "__main__":
    if itunes.playing():
        print("true")
