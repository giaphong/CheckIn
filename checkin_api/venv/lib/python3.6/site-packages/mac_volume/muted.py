#!/usr/bin/env python
"""print `muted` if muted"""
import mac_volume


if __name__ == "__main__":
    if mac_volume.muted():
        print("muted")
