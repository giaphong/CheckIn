#!/usr/bin/env python
import public
import itunes


@public.add
def get():
    if itunes.pid():
        return int(itunes.tell('sound volume').out)


@public.add
def change(value):
    itunes.tell('set sound volume to %s' % value)
