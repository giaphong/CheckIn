#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _
import public


"""
https://django-bakery.readthedocs.io/en/latest/commonchallenges.html
"""

APP_LABEL = 'django_github_pages'


@public.add
class Topic(models.Model):
    """Topic model. fields: `name`. attr: `repos`. properties: `count`"""

    class Meta:
        app_label = APP_LABEL
        ordering = ['name']

    name = models.CharField(_('Name'), max_length=100)

    @property
    def count(self):
        return self.repos.count()

    def get_absolute_url(self):
        return '/topics/%s/' % self.name

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


@public.add
class Repo(models.Model):
    """Repo model. fields: `owner`, `name`, `private`, `fork`, `description`, `homepage`, `language`, `topics`"""

    class Meta:
        app_label = APP_LABEL
        ordering = ['owner', 'name']

    name = models.CharField(_('Name'), max_length=255)
    owner = models.CharField(_('Owner'), max_length=255)

    private = models.BooleanField(_('Private'), default=True)
    fork = models.BooleanField(_('Private'), default=False)

    description = models.CharField(_('Description'), max_length=255, default='')
    homepage = models.CharField(_('Homepage'), max_length=255, default='')
    language = models.CharField(_('Language'), max_length=100, default='')

    forks_count = models.IntegerField(_('forks count'), null=True, blank=True, editable=False)
    stargazers_count = models.IntegerField(_('stargazers count'), null=True, blank=True, editable=False)
    watchers_count = models.IntegerField(_('watchers count'), null=True, blank=True, editable=False)
    open_issues_count = models.IntegerField(_('open_issues count'), null=True, blank=True, editable=False)
    subscribers_count = models.IntegerField(_('subscribers count'), null=True, blank=True, editable=False)

    pushed_at = models.DateTimeField(_('pushed_at'), null=True, blank=True, editable=False)
    created_at = models.DateTimeField(_('created_at'), null=True, blank=True, editable=False)
    updated_at = models.DateTimeField(_('updated_at'), null=True, blank=True, editable=False)

    topics = models.ManyToManyField(Topic, related_name='repos')

    @property
    def url(self):
        return "https://github.com/%s/%s" % (self.owner, self.name)

    def get_absolute_url(self):
        return '/repos/%s/' % self.name

    def __str__(self):
        return '<Repo id=%s "%s">' % (self.id, self.fullname,)

    def __repr__(self):
        return '<Repo id=%s "%s">' % (self.id, self.fullname,)
