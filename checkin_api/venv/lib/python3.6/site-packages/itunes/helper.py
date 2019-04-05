#!/usr/bin/env python
# -*- coding: utf-8 -*-
import public
import applescript


@public.add
def tell(code):
    return applescript.tell.app("iTunes", code)
