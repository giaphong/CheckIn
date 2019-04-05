#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
import django_launchd
import os
import public
import subprocess


@public.add
class Plist(models.Model):
    """launchd.plist model. fields: `path`"""
    __readme__ = ["lock", "unlock", "load", "unload", "read" "get"]

    class Meta:
        app_label = 'django_launchd'

    path = models.CharField(max_length=1024, unique=True)

    @property
    def exists(self):
        """return True if plist exists"""
        if self.path:
            return os.path.exists(self.path)

    def lock(self, key):
        """add Lock object for this agent"""
        Lock.objects.get_or_create(plist=self, key=key)

    def unlock(self, key):
        """remove Lock object for this agent"""
        Lock.objects.filter(plist=self, key=key).delete()

    def load(self):
        """launchctl load plist"""
        args = ["launchctl", "load", self.path]
        subprocess.check_call(args, stderr=subprocess.PIPE)

    def unload(self):
        """launchctl unload plist"""
        args = ["launchctl", "unload", self.path]
        subprocess.check_call(args, stderr=subprocess.PIPE)

    def read(self):
        """return a dictionary with plist file data"""
        return django_launchd.read(self.path)

    def get(self, key, default=None):
        """return the value for key if key is in the plist dictionary, else default"""
        return self.read().get(key, default)


@public.add
class Lock(models.Model):
    """launchd.plist Lock class. fields: `plist` (ForeignKey), `key`"""
    class Meta:
        app_label = 'django_launchd'

    plist = models.ForeignKey(Plist, on_delete=models.CASCADE, related_name="locks")
    key = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
