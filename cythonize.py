#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

from distutils.core import setup
from Cython.Build import cythonize

# If you want to use Cython to compile app.py into something a bit faster,
# use this.  (Added a cythonize.sh script to automate it.)  Results in
# something like a 45% speed increase, which is nice.

setup(
    name = 'Slayaway Camp Solver',
    ext_modules = cythonize('slaysolver/app.pyx'),  # accepts a glob pattern
)
