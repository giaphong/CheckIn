#!/usr/bin/env python
import os
import public


@public.add
def executable(path):
    """make path executable"""
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)
