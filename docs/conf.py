# -*- coding: utf-8 -*-
#
# Configuration file for Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config.html

# -- Path setup --------------------------------------------------------------

import os
import sys

# Add your project's root directory to the sys.path.
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Read The Docs test for straightCrimpin'
copyright = 'Copyright © 2023, StraightCrimpin'
author = 'StraightCrimpin'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',  # Include docstrings from your code
    'sphinx.ext.napoleon',  # Support Google-style docstrings
    'sphinx.ext.viewcode',  # Add links to source code
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'Readme'

# -- Options for HTML output -------------------------------------------------

# HTML theme options. You can customize these settings as needed.
html_theme = 'alabaster'
html_theme_options = {
    'logo': './images/logo/generic_logo.png',  # Path to your project's logo
    'github_user': 'straightCrimpin',  # GitHub username
    'github_repo': 'readthedocs_test',  # GitHub repository name
    'github_banner': True,
    'github_button': True,
    'show_powered_by': False,
    'show_related': False,
}

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {}

# -- Options for manual page output ------------------------------------------

man_pages = [
    (master_doc, 'mydocumentation', 'My Documentation', [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

texinfo_documents = [
    (master_doc, 'MyDocumentation', 'My Documentation',
     author, 'MyDocumentation', 'One line description of project.',
     'Miscellaneous'),
]

# -- Extension configuration -------------------------------------------------

# If you have autodoc-based documentation, you can configure options here.

# If you use napoleon for Google-style docstrings, configure its options here.
napoleon_google_docstring = False
napoleon_numpy_docstring = True

# -- Additional custom configuration ----------------------------------------

# Add custom CSS or JavaScript files to your documentation.
# html_static_path = ['_static']

# Specify additional files and directories to copy to the output build directory.
# html_extra_path = ['extrafiles']

# Define a list of directories to be searched for Sphinx extensions.
# sys.path.append(os.path.abspath('_ext'))

# -- Options for linkcheck builder ------------------------------------------

# Use linkcheck to verify that external links in your documentation are valid.
# linkcheck_ignore = [r'http://localhost:\d+']
