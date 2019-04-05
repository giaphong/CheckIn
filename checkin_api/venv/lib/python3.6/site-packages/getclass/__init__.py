#!/usr/bin/env python
import copy
import inspect
import sys
import public


def _is_src_staticmethod(obj):
    try:
        lines, _ = inspect.getsourcelines(obj)
        if lines and lines[0].strip() == "@staticmethod":
            return True
    except TypeError:
        pass


"""
python 2: <function staticmethod at ...>
python 3: <function CLS.staticmethod at ...>
"""


def _is_py2_staticmethod(obj):
    return "<function staticmethod at" in str(obj)


def _is_py3_staticmethod(obj):
    return "<function " in str(obj) and "." in str(obj)


def isstaticmethod(obj):
    if _is_src_staticmethod(obj):
        return True
    if _is_py2_staticmethod(obj) or _is_py3_staticmethod(obj):
        return True
    return False


def isclassmethod(obj):
    if not obj:
        return False
    im_self = hasattr(obj, "im_self")  # python2
    __self__ = hasattr(obj, "__self__")  # python3
    return inspect.ismethod(obj) and (im_self or __self__)


def isproperty(obj):
    return isinstance(obj, property)


"""
python2.6 inspect.getmembers raise error
abc.ABCMeta
AttributeError: __abstractmethods__
"""


def _getmembers(obj, predicate):
    try:
        return inspect.getmembers(obj, predicate)
    except Exception:
        return []


def _get_modules():
    return copy.copy(list(sys.modules.values()))


def _get_module_properties(module):
    for _, cls in _getmembers(module, inspect.isclass):
        for _, prop in _getmembers(cls, isproperty):
            yield cls, prop


def _get_all_properties():
    for module in _get_modules():
        for cls, prop in _get_module_properties(module):
            yield cls, prop


def _get_property_class(obj):
    for cls, prop in _get_all_properties():
        if id(prop) == id(obj):
            return cls


def _get_instance_method_class(obj):
    try:
        return obj.im_class  # python2
    except AttributeError:
        return obj.__self__  # python3


def _get_module_classes(module):
    for name, member in _getmembers(module, inspect.isclass):
        yield member


def _get_obj_class(obj):
    module = inspect.getmodule(obj)
    for cls in _get_module_classes(module):
        if id(obj) == id(getattr(cls, obj.__name__, None)):
            return cls


def _get__class__(obj):
    if hasattr(obj, "__class__") and not inspect.isroutine(obj):
        return obj.__class__  # instance class


def _get_class(obj):
    if inspect.ismethod(obj):  # method
        return _get_instance_method_class(obj)
    if isinstance(obj, property):  # property
        return _get_property_class(obj)
    if isclassmethod(obj) or isstaticmethod(obj):
        return _get_obj_class(obj)
    return _get__class__(obj)


@public.add
def getclass(obj):
    """return instance/method/property/classmethod/staticmethod class"""
    if not obj or inspect.ismodule(obj) or inspect.isclass(obj):
        return None
    return _get_class(obj)
