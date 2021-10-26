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
    'sphinx_inline_tabs',
    'sphinx_copybutton',
    'sphinxcontrib.video',
    'sphinxcontrib.details.directive'
]

templates_path = ["_templates"]
html_additional_pages = {
    #"index": "landing_page.html"
}

site_url = 'https://docs.valohai.com/'
source_suffix = ['.rst', '.md']
master_doc = 'index'
project = 'Valohai'
copyright = '2016 - 2021, Valohai'
author = 'Valohai'
docstitle = 'Valohai docs'
version = ''
release = ''
language = None
exclude_patterns = [
    '_**',
    '**/_**',
]
todo_include_todos = True
html_favicon = 'favicon.ico'
html_logo = 'favicon.ico'
html_theme = 'furo'
html_theme_path = ['_themes']
html_static_path = ['_static']
html_theme_options = {

    "light_css_variables": {
        "color-brand-primary": "#003B49",
        "color-brand-content": "#003B49",
    },
    "dark_css_variables": {
        "color-brand-primary": "#2DCCD3",
        "color-brand-content": "#2DCCD3",
    }
}
html_sidebars = {}
html_extra_path = ['robots.txt']
intersphinx_mapping = {'https://docs.python.org/3/': None}

# Replace the lexer with ours
from sphinx.highlighting import lexers
from extended_yaml_lexer import ExtendedYAMLLexer

lexers['yaml'] = ExtendedYAMLLexer()
