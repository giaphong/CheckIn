#!/usr/bin/env python
import subprocess
import public
import values


def _kill_args(pid):
    return ["kill"] + list(map(str, values.get(pid)))


@public.add
def kill(pid):
    """kill process by pid and return stderr"""
    if not pid:
        return
    args = _kill_args(pid)
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    return err.decode().rstrip()
