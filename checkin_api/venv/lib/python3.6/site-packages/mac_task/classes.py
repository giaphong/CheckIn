# !/usr/bin/env python
import inspect
import mac_app_generator
import os
import public
import sys
from task.classes import Task
import task


@public.add
class AppTask(mac_app_generator.App, Task):
    """MacOS app task class. inherited from `task.classes.Task` and `mac_app_generator.App`"""

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)

    @property
    def path(self):
        return self.app_path

    @property
    def app_path(self):
        return os.path.expanduser("~/Applications/.tasks/%s.app" % self.app_name)

    @property
    def app_code(self):
        path = sys.modules[self.__class__.__module__].__file__
        module_name = os.path.splitext(os.path.basename(path))[0]
        return """#!/usr/bin/env python
# -*- coding: utf-8 -*-
import {module_name}

{module_name}.{class_name}().run()
""".format(class_name=self.__class__.__name__, module_name=module_name)

    def __str__(self):
        return "<AppTask %s>" % (type(self).__name__)

    def __repr__(self):
        return self.__str__()


@public.add
def getclasses():
    """return a list of AppTask subclasses"""
    classes = []
    for module in task.getmodules():
        for k, v in module.__dict__.items():
            if inspect.isclass(v) and issubclass(v, AppTask):
                classes.append(v)
    return classes
