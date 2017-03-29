#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

needs_sphinx = '1.5'

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
]
templates_path = [
    '_templates',
]

source_suffix = ['.rst', '.md']
master_doc = 'index'
project = 'Valohai'
copyright = '2017, Valohai'
author = 'Valohai'
version = ''
release = ''
language = None
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = True
html_theme = 'alabaster'
html_theme_options = {}
html_static_path = ['_static']
intersphinx_mapping = {'https://docs.python.org/': None}
