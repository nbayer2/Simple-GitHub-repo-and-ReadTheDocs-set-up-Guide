# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Documentation Guide'
copyright = '2020, Nicolas Bayer'
author = 'Nicolas Bayer'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = 'v0.1'


# -- General configuration---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = [
#]
# extensions from fabian
extensions = [
#     'recommonmark',
     'm2rr',
#     'sphinx.ext.autodoc',
#     'sphinx.ext.autosummary',
#     'sphinx.ext.napoleon'
]
#################

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Set master (rst file)
# The master toctree document.
master_doc = 'index'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
#source_suffix = '.rst'

# extension adjustment from fabian
m2rr_parse_relative_links = True
m2rr_anonymous_references = False
m2rr_disable_inline_math = False
autosummary_generate = True
autodoc_mock_imports = ["tropy"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
#inzubinden? So ist es etwas pixelig...
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'nature'
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     '**': [
#         'about.html',
#         'navigation.html',
#         'relations.html',  # needs 'show_related': True theme option to display
#         'searchbox.html',
#         'donate.html',
#     ]
# }

# Add TROPOS Logo for the HTML page. 
html_logo = './images/TROPOS-Logo_ENG.png'

# -- Options for LaTeX output ------------------------------------------------

latex_engine = 'pdflatex'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').

    #
    'papersize': 'a4paper',

    'fncychap': '\\usepackage{fncychap}',
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',

    'figure_align':'htbp',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    #
     'preamble': r'''
        %%%add number to subsubsection 2=subsection, 3=subsubsection
        %%% below subsubsection is not good idea.
        %\setcounter{secnumdepth}{3}
        %
        %%%% Table of content upto 2=subsection, 3=subsubsection
        \setcounter{tocdepth}{2}
        \usepackage{amsmath,amsfonts,amssymb,amsthm}
        \usepackage{graphicx}
        
        %%% reduce spaces for Table of contents, figures and tables
        %%% it is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document
        \usepackage[notlot,nottoc,notlof]{}
        
        \usepackage{color}
        \usepackage{transparent}
        \usepackage{eso-pic}
        \usepackage{lipsum}
        
        %\usepackage{footnotebackref} %%link at the footnote to go to the place of footnote in the text
       
        %% spacing between line
        \usepackage{setspace}
        %%%%\onehalfspacing
        %%%%\doublespacing
        \singlespacing
        
        %%%%%%%%%%% datetime
        \usepackage{datetime}
        
        \newdateformat{MonthYearFormat}{%
            \monthname[\THEMONTH], \THEYEAR} 
      ''',

     'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1
        
        \makeatletter
        \begin{titlepage}
            \centering
            
            \vspace*{40mm} %%% * is used to give space from top
            \textbf{\Huge \@title }\\[20pt]
            
            \vspace{20mm}
            \begin{figure}[!h]
                \centering
                \sphinxlogo
            \end{figure}
            \vspace{20mm}
            
            {\Large \@author \par }
            
            \vspace*{0mm}
            {\small  Generated : \today}
        \end{titlepage}
        \makeatother
        
        %\clearpage
        \pagenumbering{roman}
        %\tableofcontents
        \pagenumbering{arabic}
        ''',

}
latex_logo = './images/TROPOS-Logo_ENG.png'
latex_toplevel_sectioning='chapter'
