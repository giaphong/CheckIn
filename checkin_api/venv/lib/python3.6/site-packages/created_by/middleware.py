#!/usr/bin/env python
from django.db.models import signals
from django.utils.functional import curry


class CreatedByMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.process_request(request)
        if response is None:
            response = self.get_response(request)
        response = self.process_response(request, response)
        return response

    def process_request(self, request):
        if request.method in ('GET', 'HEAD', 'OPTIONS', 'TRACE'):
            user = None
            if hasattr(request, 'user') and request.user.is_authenticated:
                user = request.user

            mark_created_by = curry(self.mark_created_by, user)
            signals.pre_save.connect(mark_created_by, dispatch_uid=(self.__class__, request,), weak=False)

    def process_response(self, request, response):
        return response

    def mark_created_by(self, user, sender, instance, **kwargs):
        for field in instance._meta.fields:
            """hasattr(instance, 'created_by') to avoid RelatedObjectDoesNotExist"""
            if 'created_by' == field.name:
                if not hasattr(instance, 'created_by'):
                    instance.created_by = user
