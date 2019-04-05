#!/usr/bin/env python
try:
    from xmlrpclib import ServerProxy
except ImportError:
    from xmlrpc.client import ServerProxy
import public

pypi = ServerProxy('https://pypi.org/pypi', allow_none=True)


@public.add
def list_packages():
    """return a list of all server packages"""
    return pypi.list_packages()


@public.add
def user_packages(user):
    """return a list of user packages"""
    return pypi.user_packages(user)


@public.add
def release_urls(name, version):
    """return a list of release urls"""
    return pypi.release_urls(name, version)


@public.add
def package_roles(name):
    """return a list of package roles"""
    return pypi.package_roles(name)


@public.add
def package_releases(name, show_hidden=True):
    """return a list of package releases"""
    return pypi.package_releases(name, show_hidden)


@public.add
def release_data(name, version):
    """return dictionary with release data"""
    return pypi.release_data(name, version)
