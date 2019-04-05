#!/usr/bin/env python
# -*- coding: utf-8 -*-
import public
import runcmd
import values


@public.add
def run(args):
    """run `open` with arguments"""
    runcmd.run(["open"] + args)._raise()


@public.add
def app(names):
    """open app(s)"""
    run(["-a"] + values.get(names))


@public.add
def path(paths):
    """reveal path(s) in Finder"""
    run(["-R"] + values.get(paths))


@public.add
def url(urls):
    """open url(s) in default web browser"""
    run(values.get(urls))
