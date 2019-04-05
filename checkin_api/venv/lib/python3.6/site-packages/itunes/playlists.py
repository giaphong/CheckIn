#!/usr/bin/env python
import public
import itunes


@public.add
def names():
    return itunes.tell('get name of playlists').split(", ")


@public.add
def play(playlist_name):
    return itunes.tell('play playlist named "%s"' % playlist_name)
