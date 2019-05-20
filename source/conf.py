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
    'sphinx_sitemap',
]
templates_path = [
    '_templates',
]

site_url = 'https://docs.valohai.com/'
source_suffix = ['.rst', '.md']
master_doc = 'index'
project = 'Valohai'
copyright = '2018, Valohai'
author = 'Valohai'
version = ''
release = ''
language = None
exclude_patterns = [
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
intersphinx_mapping = {'https://docs.python.org/3/': None}

# Replace the lexer with ours
from sphinx.highlighting import lexers
from extended_yaml_lexer import ExtendedYAMLLexer
lexers['yaml'] = ExtendedYAMLLexer()
