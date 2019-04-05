#!/usr/bin/env python
from django import template
from django_github_pages.models import Repo

register = template.Library()

"""
settings.py:
INSTALLED_APPS = [
    'django_github_pages',
]

template.html:
{% load topics %}

{% for topic in repo.name|topics %}
    {{ topic.name }}
{% endfor %}
"""


@register.filter
def topics(name):
    repo = Repo.objects.get(name=name.split("/")[0])
    return repo.topics.all()
