"""
  Liste der globalen Variabeln
"""
import sys
import platform
from rias.riasos import get_hostname as hostname

# Path to Libary
libpath = sys.argv[0]

# User Settings
user = {
    "language": "Python",
    "node": platform.node(),
    "OS": hostname(),
    "PYVersion": sys.version,
}

# Loadable Module
list_function = ["git", "folder", "crypt"]
