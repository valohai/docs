#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('.'))

needs_sphinx = '1.8'

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinxcontrib.images',
    'sphinx_click.ext',
    'sphinx_sitemap',
    '_redirects',
]
templates_path = [
    '_templates',
]

# <FILTHY-HACK>
import sphinx_click.ext


def i_feel_so_filthy(opt):
    # This fixes a bug in sphinx-click/docutils combo that cause improper escaping of
    # backticks (`) in click documentation that trigger the following warning from docutils RST parser.
    # "WARNING: Inline interpreted text or phrase reference start-string without end-string."
    # TODO: clean and make a proper PR sometime
    opt = sphinx_click.ext._get_help_record(opt)

    yield '.. option:: {}'.format(opt[0])
    if opt[1]:
        yield ''
        from docutils import statemachine
        for line in statemachine.string2lines(opt[1], tab_width=4, convert_whitespace=True):
            line = line.replace('`', '\\`')  # THE ONLY CHANGE <=
            yield sphinx_click.ext._indent(line)


sphinx_click.ext._format_option = i_feel_so_filthy
# </FILTHY-HACK>

site_url = 'https://docs.valohai.com/'
source_suffix = ['.rst', '.md']
master_doc = 'index'
project = 'Valohai'
copyright = '2016 - 2019, Valohai'
author = 'Valohai'
version = ''
release = ''
language = None
exclude_patterns = [
    '_**',
    '**/_**',
]
pygments_style = 'valodoc_pygments_style.Valodoc'
todo_include_todos = True
html_favicon = 'favicon.ico'
html_theme = 'valodoc'
html_theme_path = ['_themes']
html_static_path = ['_static']
html_theme_options = {
    'analytics_id': 'UA-87958940-1',
    'canonical_url': 'https://docs.valohai.com/',
}
html_sidebars = {}
html_extra_path = ['robots.txt']
intersphinx_mapping = {'https://docs.python.org/3/': None}

# Replace the lexer with ours
from sphinx.highlighting import lexers
from extended_yaml_lexer import ExtendedYAMLLexer

lexers['yaml'] = ExtendedYAMLLexer()
