# This file is kept for compatibility.
# All configuration is now in settings.py to avoid naming conflicts
# with installed packages that also use the name 'config'.
from settings import config_data, working_dir

__all__ = ["config_data", "working_dir"]
