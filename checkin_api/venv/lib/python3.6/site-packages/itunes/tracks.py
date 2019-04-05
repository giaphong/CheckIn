#!/usr/bin/env python
import public
import itunes


@public.add
def play(track, playlist):
    itunes.tell('play track "%s" of playlist "%s"' % (track, playlist))
