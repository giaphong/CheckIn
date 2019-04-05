#!/usr/bin/env python
import inspect
import json
import os
import public
import values


XDG_CONFIG_HOME = os.getenv("XDG_CONFIG_HOME", os.path.expanduser("~/.config"))
README_GENERATOR_HOME = os.getenv("README_GENERATOR_HOME", os.path.join(XDG_CONFIG_HOME, "readme-generator"))

HEADERS_FILE = os.path.join(README_GENERATOR_HOME, "headers.json")
HEADERS = {}
if os.path.exists(HEADERS_FILE):
    HEADERS = json.loads(open(HEADERS_FILE).read())

ORDER_FILE = os.path.join(README_GENERATOR_HOME, "order.txt")
ORDER = []
if os.path.exists(ORDER_FILE):
    ORDER = list(filter(None, open(ORDER_FILE).read().splitlines()))

DISABLED_FILE = os.path.join(README_GENERATOR_HOME, "disabled.txt")
DISABLED = []
if os.path.exists(DISABLED_FILE):
    DISABLED = list(filter(None, open(DISABLED_FILE).read().splitlines()))


@public.add
class Readme:
    """README.md generator"""

    __readme__ = dict(
        # order="list of sections order",
        # header_lvl="header default lvl (4)",
        # headers="dict with sections headers (optional)",
        # sections="dict with sections (loaded from .md files)",

        # get_section=None,
        # get_sections=None,
        # get_header=None,

        load=None,

        render=None,
        save=None
    )
    order = ORDER
    disabled = []
    sections = {}
    headers = HEADERS
    header_lvl = 4

    def __init__(self, path=None, **kwargs):
        for k, v in kwargs.items():
            self.set_section(k, v)
        if os.path.exists(README_GENERATOR_HOME):
            self.load(README_GENERATOR_HOME)
        self.load(path)

    def get_header(self, name):
        """return a string with section header"""
        header = self.headers.get(name, name.title())
        if not header:
            return ""
        if "#" in header:
            return header
        return "%s %s" % ("#" * self.header_lvl, header)

    def get_section(self, name):
        """return a string with README section"""
        if name in self.sections:
            return self.sections[name]
        if hasattr(self.__class__, name):
            value = getattr(self, name)
            value = value() if inspect.isroutine(value) else value
            if value:
                return str(value)

    def get_sections(self):
        """return all sections in a list of (name, string) pairs sorted by `order`"""
        result = []
        for name in self.order:
            if name not in getattr(self, "disabled", []):
                value = self.get_section(name)
                if value:
                    result.append((name, value))
        return result

    def set_section(self, name, string):
        self.sections[name] = string

    def render(self):
        """render to a string"""
        # todo: clean
        sections = []
        for name, string in filter(lambda pair: pair[1], self.get_sections()):
            if string.splitlines()[0].strip() and string.find("#") != 0:
                header = self.get_header(name)
                string = "%s\n%s" % (header, str(string).lstrip())
            sections.append(string.strip())
        return "\n\n".join(filter(None, sections))

    def save(self, path='README.md'):
        """save to file"""
        if os.path.dirname(path) and not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        open(path, "w").write(self.render())
        return self

    def load_sections(self, path="."):
        """load sections from `.md` markdown files"""
        """
    path/<section_name>.md
    path/<section_name2>.md
        """
        if not path:
            path = os.getcwd()
        for f in map(lambda l: os.path.join(path, l), os.listdir(path)):
            if os.path.isfile(f) and os.path.splitext(f)[1] == ".md":
                key = os.path.splitext(os.path.basename(f))[0]
                value = open(f).read()
                self.set_section(key, value)
        return self

    def load_headers(self, path):
        """load `disabled.txt`"""
        headers = json.loads(open(path).read())
        self.headers.update(headers)

    def load_disabled(self, path):
        """load `disabled.txt`"""
        self.disabled = list(filter(None, open(path).read().splitlines()))

    def load_order(self, path):
        """load `order.txt`"""
        self.order = list(filter(None, open(path).read().splitlines()))

    def load(self, path):
        """load sections and order"""
        for path in values.get(path):
            if not os.path.exists(path):
                raise OSError("%s NOT EXISTS" % path)
            if os.path.exists(path) and os.path.isdir(path):
                self.load_sections(path)
                f = os.path.join(path, "disabled.txt")
                if os.path.exists(f):
                    self.load_disabled(f)
                f = os.path.join(path, "headers.json")
                if os.path.exists(f):
                    self.load_headers(f)
                f = os.path.join(path, "order.txt")
                if os.path.exists(f):
                    self.load_order(f)

    def __str__(self):
        return self.render()
