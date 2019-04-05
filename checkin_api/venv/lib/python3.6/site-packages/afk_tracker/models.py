#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
import public

@public.add
class Afk(models.Model):
    """Afk model. fields: `created_at`, `afk`"""

    class Meta:
        app_label = 'afk_tracker'
        ordering = ['-created_at']

    created_at = models.DateTimeField(auto_now_add=True)
    afk = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '<Afk id="{id}" created_at="{created_at}" afk="{afk}">'.format(
            id=self.id,
            created_at=self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            afk=self.afk
        )

    def __repr__(self):
        return self.__str__()
