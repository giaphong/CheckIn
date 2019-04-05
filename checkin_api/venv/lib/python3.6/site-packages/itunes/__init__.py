#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import applescript
import public
import itunes.playlists
import itunes.tracks
import itunes.volume


@public.add
def tell(code):
    """execute applescript `tell application "iTunes" ...`"""
    return applescript.tell.app("iTunes", code)


@public.add
def pause():
    """pause iTunes"""
    tell("pause")


@public.add
def play():
    tell("play")


@public.add
def mute():
    """mute iTunes"""
    tell("set mute to true")


@public.add
def muted():
    """return True if iTunes muted, else False"""
    return "true" in tell("get mute").out


@public.add
def unmute():
    """unmute iTunes"""
    tell("set mute to false")


@public.add
def stop():
    """stop"""
    tell("stop")


@public.add
def next():
    """play next track"""
    tell("play next track")


@public.add
def prev():
    """play previous track"""
    tell("play previous track")


@public.add
def playing():
    """return True if iTunes is playing, else False"""
    return "playing" in state()


@public.add
def state():
    """return player state string"""
    return tell("(get player state as text)").out


"""process functions"""


@public.add
def activate():
    """open iTunes and make it frontmost"""
    tell('activate')


@public.add
def frontmost():
    """return True if `iTunes.app` is frontmost app, else False"""
    out = os.popen("lsappinfo info -only name `lsappinfo front`").read()
    return "iTunes" in out.split('"')


@public.add
def kill():
    os.popen("kill %s &> /dev/null" % pid())


@public.add
def pid():
    """return iTunes.app pid"""
    for l in os.popen("ps -ax").read().splitlines():
        if "/Applications/iTunes.app" in l and "iTunesHelper" not in l:
            return int(list(filter(None, l.split(" ")))[0])


@public.add
def quit():
    """Quit iTunes"""
    tell("quit")
