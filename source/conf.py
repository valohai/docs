#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath("./_ext"))

needs_sphinx = '1.8'

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinxcontrib.images',
    'sphinx_click.ext',
    'sphinx_sitemap',
    '_redirects',
    'card',
    'card_collection',
    'vh_header',
    'vh_row',
    'vh_demo',
]
templates_path = [
    '_templates',
]

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
    'exclude_feedback': ['index', 'tutorials/index', 'quickstarts/index'],
}
html_sidebars = {}
html_extra_path = ['robots.txt']
intersphinx_mapping = {'https://docs.python.org/3/': None}

# Replace the lexer with ours
from sphinx.highlighting import lexers
from extended_yaml_lexer import ExtendedYAMLLexer

lexers['yaml'] = ExtendedYAMLLexer()
