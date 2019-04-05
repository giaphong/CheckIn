#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from django.db import models
import elapsed
import public


class datetime(datetime.datetime):
    @property
    def elapsed(self):
        return elapsed.get(self)


@public.add
class DateTimeElapsedField(models.DateTimeField):
    """models.DateTimeField subclass with `elapsed` attr"""

    def from_db_value(self, value, expression, connection):
        if value:
            return datetime.combine(value.date(), value.time())

    def to_python(self, value):
        if value:
            dt = models.DateTimeField().to_python(value)
            return datetime.combine(dt.date(), dt.time())


"""usage:
from django_datetime_elapsed_field import DateTimeElapsedField

class Example(models.Model):
    created_at = DateTimeElapsedField(...)
"""
