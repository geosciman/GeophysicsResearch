# -*- coding: utf-8 -*-
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))

project = u'Geophysics'
copyright = u'2018, GeosciMan'
author = u'GeosciMan'

version = u'1.0'
release = u'1.0'
needs_sphinx = '1.5'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
nitpicky = True
numfig = True
master_doc = 'index'
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = True
intersphinx_mapping = {'https://docs.python.org/': None}

# HTML output
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    html_theme = 'default'
else:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    'analytics_id': 'UA-107774305-2',    # Google Analytics
    'collapse_navigation': False,
    'sticky_navigation': False,
    'display_version': False,
}

html_context = {
    'display_github': True,
    'github_user': 'GeosciMan',
    'github_repo': 'GeophysicsResearch',
    'github_version': 'master',
    'conf_py_path': '/source/',
}
html_last_updated_fmt = '%x'
html_use_smartypants = True
html_domain_indices = True
html_use_index = True
html_split_index = False
html_show_sourcelink = True
html_use_opensearch = ''
htmlhelp_basename = 'Geophysics'

# LaTeX
latex_engine="xelatex"
latex_elements = {
        'papersize' : 'a4paper',
    'utf8extra' : '',
    'inputenc'  : '',
    'cmappkg'   : '',
    'fontenc'   : '',
    'releasename' : 'By GeosciMan@GitHub',
    'release' : '1.0',
    'babel'     : r'''\usepackage[english]{babel}''',
    'preamble' : r'''
        \usepackage{ctex}
        \parindent 2em
        \setcounter{tocdepth}{3}
        \renewcommand\familydefault{\ttdefault}
        \renewcommand\CJKfamilydefault{\CJKrmdefault}
    ''',
}
latex_documents = [
    (master_doc, 'Geophysics.tex', u'Geophysics',
     u'GeosciMan', 'manual', True),
]
