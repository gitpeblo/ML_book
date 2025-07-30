"""
conf.py — Main configuration file for Sphinx / Jupyter Book builds.

This file controls:
- Project metadata (title, author, release, etc.)
- Extensions that Sphinx uses
- Paths to static files (CSS, JS, images)
- Theme and HTML customizations

⚡ Role in our case:
We will add entries that tell Sphinx to include our custom CSS and JavaScript
files during the HTML build process.
This allows us to change or replace styles (CSS) and perform DOM manipulations (JS)
across the entire built site.
"""

# -----------------------------------------------------------
# Custom static files (CSS + JS) for alerts replacement
# -----------------------------------------------------------

# Paths to static files relative to `conf.py`.
# `_static` is a default folder where we place our custom CSS and JS.
html_static_path = ['_static']

# Add our custom CSS file.
# This file will be copied into the build output and linked in every page.
html_css_files = [
    'custom.css',   # Our stylesheet to override default alert style
]

# Add our custom JS file.
# This file will be copied into the build output and executed on every page load.
html_js_files = [
    'custom.js',    # Our script to replace <div class="alert alert-warning"> with <div class="exercise-block">
]

# -----------------------------------------------------------
# 🔍 Notes
# -----------------------------------------------------------
# - `custom.css` and `custom.js` must exist in the `_static` folder.
# - During build, Sphinx will automatically insert:
#       <link rel="stylesheet" href="_static/custom.css">
#       <script src="_static/custom.js"></script>
#   into the HTML `<head>` or `<body>`.
# - Any changes in these files require rebuilding (`make html` or `jb build .`).
