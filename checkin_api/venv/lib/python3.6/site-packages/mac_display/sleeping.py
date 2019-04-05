#!/usr/bin/env python
"""print `true` if display is sleeping, else `false`"""
import mac_display

if __name__ == "__main__":
    print("true") if mac_display.sleeping() else print("false")
