# !/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _
import os
import public


@public.add
class Category(models.Model):
    """Category model. fields: `name`, `parent`, `description`"""

    class Meta:
        app_label = 'django_path'
        ordering = ['name']

    name = models.CharField(_('Name'), max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    description = models.CharField(_('Description'), max_length=255, blank=True)

    @property
    def paths(self):
        return self.path_set.all()

    @property
    def categories(self):
        return self.category_set.all()

    def __str__(self):
        return '<Category id=%s "%s">' % (self.id, self.name,)

    def __repr__(self):
        return '<Category id=%s "%s">' % (self.id, self.name,)


@public.add
class Path(models.Model):
    """Path model. fields: `path`"""
    class Meta:
        app_label = 'django_path'
        ordering = ['path']

    path = models.TextField(_('Path'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Category'))

    @property
    def exists(self):
        return os.path.exists(self.path)

    def read(self):
        if os.path.exists(self.path):
            return open(self.path).read()

    def __str__(self):
        return '<Path id=%s path="%s">' % (self.id, self.path,)

    def __repr__(self):
        return '<Path id=%s path="%s">' % (self.id, self.path,)
