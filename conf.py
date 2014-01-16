# -*- coding: utf-8 -*-
'''
Sphinx documentation for NebriOS 
'''
import os
import sys

from sphinx.directives import TocTree

# -- General configuration -----------------------------------------------------

project = 'NebriOS'
copyright = '2014 NebriOS'

master_doc = 'index'
templates_path = ['_templates']
exclude_patterns = ['_build']

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

modindex_common_prefix = ['nebrios.']

autosummary_generate = True


### HTML options
html_theme = 'default'

html_title = None
html_short_title = 'nebrios'

html_static_path = ['_static']
html_use_smartypants = False

html_use_index = True
html_last_updated_fmt = '%b %d, %Y'
html_show_sourcelink = False
html_show_sphinx = True
html_show_copyright = True
#html_use_opensearch = ''


### Manpage options
# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
authors = [
    'Adam Temple <adam@nebrios.com> and others.',
]

man_pages = [
    ('index', authors, 1),
    ('index', authors, 1),
]


### epub options
epub_title = 'NebriOS Documentation'
epub_author = 'Adam Temple'
epub_publisher = epub_author
epub_copyright = '2014, NebriOS'

epub_scheme = 'URL'
epub_identifier = 'http://nebrios.com/'


###################################################
