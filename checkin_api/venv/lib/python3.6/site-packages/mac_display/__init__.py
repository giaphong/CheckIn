#!/usr/bin/env python
# -*- coding: utf-8 -*-
import public
import runcmd

"""
cli detect sleeping:
echo $(ioreg -n IODisplayWrangler | grep -i IOPowerManagement | perl -pe 's/^.*DevicePowerState\"=([0-9]+).*$/\1/')/4 | bc
"""


@public.add
def sleep():
    """put your display to sleep"""
    cmd = ["/usr/bin/pmset", "displaysleepnow"]
    runcmd.run(cmd)


@public.add
def sleeping():
    """return True if display is sleeping"""
    out = runcmd.run(["/usr/sbin/ioreg", "-n", "IODisplayWrangler"])._raise().out
    state = int(out.split('"DevicePowerState"=')[1][0])  # 0-4
    return state in [0, 1]


@public.add
def wake():
    """wake from sleep"""
    cmd = ["/usr/bin/caffeinate", "-u", "-t", "1"]
    runcmd.run(cmd)
