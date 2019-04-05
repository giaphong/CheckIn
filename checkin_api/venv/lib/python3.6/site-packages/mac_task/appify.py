#!/usr/bin/env python
"""create applications from `AppTask` subclasses"""
import task.setup
from mac_task.classes import getclasses


def appify():
    classes = getclasses()
    print("%s AppTask subclasses" % len(classes))
    for cls in classes:
        cls().create_app()
        print(cls().app_path)


def _cli():
    appify()


if __name__ == "__main__":
    _cli()
