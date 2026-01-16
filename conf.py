# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add paths if needed
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'JCPenney Credit Card Activation'
copyright = '2026, JCPenney'
author = 'JCPenney Support Team'

# Full version
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Extensions (add later if required)
extensions = []

# Allow raw HTML inside .rst files
raw_enabled = True

# Templates path
templates_path = ['_templates']

# Files/folders to ignore
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Default theme (you may switch later)
# html_theme = 'sphinx_rtd_theme'

# SEO-friendly titles
html_title = "How to Activate Your JCPenney Credit Card – Easy Guide"
html_short_title = "JCPenney Card Activation"

# Favicon (place favicon.ico in _static or root folder)
html_favicon = 'favicon.ico'

# Hide "View page source"
html_show_sourcelink = False

# Allow unsafe raw HTML (required for buttons & overlays)
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static files (CSS, images, JS)
# html_static_path = ['_static']
