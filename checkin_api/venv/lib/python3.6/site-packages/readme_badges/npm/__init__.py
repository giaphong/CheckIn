#!/usr/bin/env python
import json
import os
import public
import shields


def name():
    if os.path.exists("package.json"):
        return json.loads(open("package.json").read())["name"]


@public.add
def v():
    """npm package version badge"""
    if os.path.exists("package.json"):
        return shields.npm.V(name(), maxAge=3600)
    return ""
