#!/usr/bin/env python
import inspect
import public


@public.add
def depth():
    """return recursion depth. 0 if no recursion"""
    counter = 0
    frames = inspect.getouterframes(inspect.currentframe())[1:]
    top_frame = inspect.getframeinfo(frames[0][0])
    for frame, _, _, _, _, _ in frames[1:]:
        (path, line_number, func_name, lines, index) = inspect.getframeinfo(frame)
        if path == top_frame[0] and func_name == top_frame[2]:
            counter += 1
    return counter
