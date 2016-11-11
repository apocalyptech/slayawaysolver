#!/bin/bash
# vim: set expandtab tabstop=4 shiftwidth=4:

# If you want to use Cython to compile app.py into something a bit faster,
# use this.  Results in something like a 45% speed increase, which is nice.

cp slaysolver/app.py slaysolver/app.pyx
python cythonize.py build_ext --inplace
rm slaysolver/app.pyx
