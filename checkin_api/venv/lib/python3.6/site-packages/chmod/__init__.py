#!/usr/bin/env python
import chmod.check
import chmod.make
import public
import runcmd


@public.add
def chmod(args):
    """run chmod with arguments"""
    cmd = ["chmod"] + list(args)
    return runcmd.run(cmd)._raise().out
