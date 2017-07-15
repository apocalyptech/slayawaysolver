#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4 fileencoding=utf-8:

import unittest

if __name__ == '__main__':

    testsuite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(testsuite)
