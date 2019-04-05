#!/usr/bin/env python
import os
import shutil
import public
import mac_localized.strings
import values

"""
Folder.localized/.localized/de.strings:
"Folder" = "Translation";
"""


@public.add
def name(path):
    """return folder name without `.localized` prefix"""
    return os.path.basename(path).replace(".localized", "")


@public.add
def fullpath(path):
    """return path with `.localized` postfix"""
    if os.path.splitext(path)[1] != ".localized":
        path = "%s.localized" % path
    return os.path.expanduser(path)


@public.add
def load(path):
    """return dictionary with keys as languages and translations with values"""
    result = dict()
    _localized = os.path.join(fullpath(path), ".localized")
    if os.path.exists(_localized):
        for f in mac_localized.strings.find(_localized):
            lang = os.path.splitext(os.path.basename(f))[0]
            key, value = mac_localized.strings.load(f) or (None, None)
            if key:
                result[lang] = value
    return result


@public.add
def rm(path, languages=None):
    """rm .localized/ lang files or .localized/ folder"""
    _localized = os.path.join(fullpath(path), ".localized")
    for lang in values.get(languages):
        f = os.path.join(_localized, "%s.strings" % lang)
        if os.path.exists(f):
            os.unlink(f)
    if not languages and os.path.exists(_localized):
        shutil.rmtree(_localized)


@public.add
def mkdir(path, **strings):
    """mkdir (if not exists), write translations and return folder fullpath"""
    path = fullpath(path)
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    update(path, **strings)
    return path


@public.add
def update(path, **strings):
    """update folder translations"""
    for lang, value in strings.items():
        f = os.path.join(fullpath(path), ".localized", "%s.strings" % lang)
        mac_localized.strings.update(f, name(path), value)


@public.add
def get(path, lang):
    """return translation"""
    return load(path).get(lang, None)
