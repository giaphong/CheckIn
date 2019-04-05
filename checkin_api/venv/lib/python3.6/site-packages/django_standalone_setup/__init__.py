# !/usr/bin/env python
# -*- coding: utf-8 -*-
import django
from django.conf import settings
import os

if not settings.configured:
    if "DJANGO_SETTINGS_MODULE" not in os.environ:
        raise OSError("DJANGO_SETTINGS_MODULE environment variable not defined")
    django.setup()
