"""
conf.py — Main configuration file for Sphinx build

This file controls:
  - Project metadata (title, author, release info)
  - Extensions to be loaded
  - HTML theme and customization
  - Paths to static assets (CSS, JS)
  - Any custom transforms or replacements (like replacing <div alert>)

In this setup:
  - We use a custom transform (replace_alert_div.py) to rewrite Jupyter-generated
    alert blocks (<div class="alert alert-block alert-warning">) into cleaner
    <div class="alert alert-warning"> format so they display consistently in HTML.
  - The transform is explicitly imported and registered to guarantee execution.
"""

import os
import sys

# Add custom extension folder to Python path
sys.path.insert(0, os.path.abspath('./_ext'))

# ✅ Explicitly import the replace_alert_div module
import replace_alert_div #type: ignore

# -- Project information -----------------------------------------------------
project = 'ML Book'
author = 'Paolo Bonfini'
release = '2025'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_nb',              # For Jupyter notebooks
    'sphinx_book_theme',    # Theme
    'replace_alert_div'     # Custom extension for replacing alert divs
]

# -- Paths for templates -----------------------------------------------------
templates_path = ['_templates']

# -- HTML output configuration -----------------------------------------------
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

# -- Custom CSS ---------------------------------------------------------------
html_css_files = [
    'custom.css'
]

# -- Setup hook to register transforms ----------------------------------------
def setup(app):
    """
    Sphinx entry point for additional setup.
    We call the setup() function from replace_alert_div so the transform is applied.
    """
    replace_alert_div.setup(app)
