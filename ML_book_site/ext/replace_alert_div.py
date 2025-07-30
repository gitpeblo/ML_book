"""
conf.py
Minimal Sphinx configuration.
Loads custom extension to replace alert divs during build.
"""

import os
import sys

# Add _ext folder to Python path
sys.path.append(os.path.abspath("./_ext"))

# Load our custom extension
extensions = [
    "replace_alerts",  # Name matches _ext/replace_alerts.py
]
