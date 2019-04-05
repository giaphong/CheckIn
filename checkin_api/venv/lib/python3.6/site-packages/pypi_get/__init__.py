#!/usr/bin/env python
import public
import requests


@public.add
def get(name, version=None):
    """return a dictionary with pypi project data"""
    url = "https://pypi.org/pypi/%s/json" % name
    if version:
        url = "https://pypi.org/pypi/%s/%s/json" % (name, version)
    r = requests.get(url)
    if r.status_code < 400:
        return r.json()
    return {}
