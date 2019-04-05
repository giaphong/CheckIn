# !/usr/bin/env python
# -*- coding: utf-8 -*-
import django
from django.conf import settings

if not settings.configured:
    django.setup()
