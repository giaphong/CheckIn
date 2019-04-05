#!/usr/bin/env python
import public
import runcmd

BIN = "/Applications/HardwareMonitor.app/Contents/MacOS/hwmonitor"


@public.add
def read():
    """return string with `hwmonitor` output"""
    return runcmd.run([BIN])._raise().out


@public.add
def sensors():
    """return dict with sensor names as keys and temperature as values"""
    result = dict()
    for l in read().splitlines():
        if ":" in l:
            k, v = l.split(":")
            result[k] = int(v.split(' ')[1])
    return result


@public.add
def sensor(name):
    """return sensor value by sensor name"""
    for k, v in sensors().items():
        if name.lower() in k.lower():
            return v
