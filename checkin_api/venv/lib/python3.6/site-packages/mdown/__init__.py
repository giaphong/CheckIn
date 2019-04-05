#!/usr/bin/env python
# -*- coding: utf-8 -*-
import public

EXTENSIONS = [".markdown", ".mdown", ".mkdn", ".md", ".mkd", ".mdwn", ".mdtxt", ".mdtext"]


def _format(formula, **kwargs):
    data = dict()
    for k, v in kwargs.items():
        data[k] = v.lstrip().rstrip() if v else ''
    return formula.format(**data)


@public.add
def header(title, lvl):
    """return string with markdown header"""
    return "%s %s" % ("#" * int(lvl), title.rstrip())


@public.add
def image(url, link='', title='', alt=''):
    """return string with markdown image"""
    formula = '![{alt}]({url} "{title}")' if title else '![{alt}]({url})'
    formula = "%s({url})" % formula if link else formula
    return _format(formula, url=url, link=link, title=title, alt=alt)


@public.add
def code(code, language=None):
    """return string with markdown code block"""
    return _format("""```{language}
{code}
```""", code=code, language=language)


@public.add
def table(headers, matrix):
    """return string with markdown table (one-line cells only)"""
    def line1(string):
        return string.splitlines()[0] if string.splitlines() else ''

    def one_line_cells(cells, headers):
        cells = list(map(lambda s: line1(s).lstrip().rstrip(), cells))
        if len(cells) != len(headers):
            err_msg = """different length of headers (%s) and row cells (%s):
%s
%s""" % (len(headers), len(cells), "|".join(headers), "|".join(cells))
            raise ValueError(err_msg)
        return cells

    headers = list(map(lambda s: line1(s).lstrip().rstrip(), headers))
    matrix = list(map(lambda cols: one_line_cells(cols, headers), matrix))
    if matrix:
        return """%s
-|-
%s""" % ("|".join(headers), "\n".join(map(lambda r: "|".join(r), matrix)))


def link():
    raise NotImplementedError


def lists(items, ordered=False):
    raise NotImplementedError


def blockquote(text):
    raise NotImplementedError
