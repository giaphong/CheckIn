#!/usr/bin/env python
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser
import public


def _sectiondict(config, section):
    result = dict()
    for k, v in config.items(section):
        result[k] = v
    return result


@public.add
def read(path):
    """return a dictionary with ini file data"""
    result = dict()
    config = ConfigParser()
    with open(path, "r") as f:
        config.read_file(f) if hasattr(config, "read_file") else config.readfp(f)
    for section in config.sections():
        result[section] = _sectiondict(config, section)
    return result

