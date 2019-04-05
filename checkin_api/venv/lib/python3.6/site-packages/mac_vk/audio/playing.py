#!/usr/bin/env python
"""print vk.com page url if audios is playing"""
import mac_vk


def _cli():
    url = mac_vk.audio.playing()
    if url:
        print(url)


if __name__ == "__main__":
    _cli()
