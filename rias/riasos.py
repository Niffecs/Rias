"""
User Settings
"""
import os
import sys


def get_hostname():
    if "nt" in os.name:
        return "Windows"
    elif "posix" in os.name:
        return "Linux"
    else:
        # No Mac OS
        sys.exit(0)
