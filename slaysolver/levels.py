#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4 fileencoding=utf-8:

import re
from slaysolver.app import Level, DIR_N, DIR_S, DIR_E, DIR_W
from . import movies

levelre = re.compile('^(nc17_)?s(\d+)_([sd])(\d+)$')
def level_sort_key(levelname):
    match = levelre.match(levelname)
    if not match:
        return 'ZZZ'
    if match.group(1):
        nc17 = True
    else:
        nc17 = False
    movie = int(match.group(2))
    leveltype = match.group(3)
    levelnum = int(match.group(4))

    # This here to handle 2.5
    if movie != 25:
        movie *= 10

    # Sort regular levels before deleted scenes
    if leveltype == 's':
        typekey = 1
    else:
        typekey = 2

    # Though sort NC-17 levels after both of those
    if nc17:
        typekey = 3

    return '{:03d}_{}_{:02d}'.format(movie, typekey, levelnum)

class Levels(object):

    def __init__(self):
        self.levels = {}
        self.level_names = []
        for level_set in movies.get_movies():
            for (name, func) in level_set.__dict__.items():
                match = levelre.match(name)
                if match:
                    self.level_names.append(name)
                    self.levels[name] = func
        self.level_names.sort(key=lambda name: level_sort_key(name))

    def get_level(self, name):
        return self.levels[name]()

    def report_levels(self):
        print('Available level names:')
        print('')
        for name in self.level_names:
            level = self.get_level(name)
            print('   {}: {}'.format(name, level.desc))
        print('')
