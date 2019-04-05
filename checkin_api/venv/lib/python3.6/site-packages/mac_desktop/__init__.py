#!/usr/bin/env python
# -*- coding: utf-8 -*-
import applescript
import os
from PIL import Image
from PIL import ImageChops
from PIL import ImageStat
import public
import tempfile


def wallpaper():
    """return wallpaper path"""
    return applescript.tell.app("System Events", "tell every desktop to picture").out


@public.add
def visibility():
    """return Desktop visibility percentage (0..1)"""
    screen_file = os.path.join(tempfile.gettempdir(), "screencapture.png")
    diff_file = os.path.join(tempfile.gettempdir(), "diff.png")
    os.system("/usr/sbin/screencapture -x %s" % screen_file)
    im1 = Image.open(screen_file)
    im2 = Image.open(wallpaper())
    im2 = im2.resize((im1.size[0], im1.size[1]), Image.ANTIALIAS)

    diff_img = ImageChops.difference(im1, im2)
    diff_img.convert('RGB').save(diff_file)
    stat = ImageStat.Stat(diff_img)
    """can be [r,g,b] or [r,g,b,a]"""
    diff_ratio = sum(stat.mean) / (len(stat.mean) * 100)
    map(os.unlink, [screen_file, diff_file])
    return 1 - diff_ratio


@public.add
def toggle():
    """toggle Desktop (show/hide)"""
    applescript.tell.app("System Events", "key code 103")
