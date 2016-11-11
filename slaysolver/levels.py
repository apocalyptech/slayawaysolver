#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import re
from slaysolver.app import Level, DIR_N, DIR_S, DIR_E, DIR_W

levelre = re.compile('^(nc17_)?s(\d+)_([sd])(\d+)$')
def level_sort_key(levelname):
    match = levelre.match(levelname)
    if not match:
        return 'ZZZ'
    if match.group(1):
        nc17 = 1
    else:
        nc17 = 0
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

    return '%d_%03d_%d_%02d' % (nc17, movie, typekey, levelnum)

class Levels(object):

    def __init__(self):
        self.levels = {}
        self.level_names = []
        for (name, method) in Levels.__dict__.items():
            match = levelre.match(name)
            if match:
                self.level_names.append(name)
                self.levels[name] = method.__func__
        self.level_names.sort(key=lambda name: level_sort_key(name))

    def get_level(self, name):
        return self.levels[name]()

    def report_levels(self):
        print('Available level names:')
        print('')
        for name in self.level_names:
            level = self.get_level(name)
            print('   %s: %s' % (name, level.desc))
        print('')

    @staticmethod
    def s1_s01():

        level = Level('Slayaway Camp 1, Scene 1', 7, 2,
            0, 1,
            0, 1)

        # Victim
        level.add_victim(4, 0)

        # Return
        return level

    @staticmethod
    def s1_s02():

        level = Level('Slayaway Camp 1, Scene 2', 6, 6,
            0, 1,
            0, 1)

        # Walls
        level.wall_east(3, 0)
        level.wall_south(3, 0)
        level.wall_east(3, 1)
        level.wall_east(3, 2)
        level.wall_south(4, 2)
        level.wall_south(5, 2)
        level.wall_south(4, 3)
        level.wall_south(5, 3)
        level.wall_east(3, 4)
        level.wall_east(3, 5)

        level.wall_box(0, 2)
        level.wall_box(1, 2)

        # Victim
        level.add_victim(5, 3)

        # Return
        return level

    @staticmethod
    def s1_s03():

        level = Level('Slayaway Camp 1, Scene 3', 6, 7,
            1, 5,
            0, 0)

        # Walls
        level.wall_east(0, 0)

        level.wall_south(0, 3)
        level.wall_south(1, 3)
        level.wall_south(2, 3)
        level.wall_south(5, 3)

        level.wall_east(0, 4)
        level.wall_south(0, 4)

        level.wall_box(3, 5)
        level.wall_box(3, 6)

        level.wall_west(1, 1)
        level.wall_south(1, 1)
        level.wall_south(2, 1)
        level.wall_east(2, 1)
        level.wall_east(2, 0)

        level.add_victim(4, 0)
        level.add_victim(1, 3)

        return level

    @staticmethod
    def s1_s04():

        level = Level('Slayaway Camp 1, Scene 4', 6, 6,
            0, 4,
            2, 4)

        level.wall_north(0, 4)
        level.wall_east(0, 3)
        level.wall_east(0, 2)
        level.wall_east(0, 1)
        level.wall_north(0, 1)

        level.wall_box(5, 4)
        level.wall_box(3, 2)

        level.add_victim(1, 2)
        level.add_victim(4, 3)

        return level

    @staticmethod
    def s1_s05():

        level = Level('Slayaway Camp 1, Scene 5', 7, 6,
            0, 0,
            3, 0)

        level.wall_east(0, 0)
        level.wall_east(0, 1)
        level.wall_east(0, 2)
        level.wall_east(1, 4)
        level.wall_north(3, 4)
        level.wall_west(6, 3)
        level.wall_west(6, 2)

        level.wall_west(4, 5)
        level.wall_north(4, 5)
        level.wall_north(5, 5)
        level.wall_north(6, 5)

        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_east(2, 0)

        level.add_victim(0, 3)
        level.add_victim(1, 3)
        level.add_victim(5, 2)

        return level

    @staticmethod
    def s1_s07():

        level = Level('Slayaway Camp 1, Scene 7', 6, 6,
            5, 5,
            0, 3)

        level.wall_box(0, 5)
        level.wall_box(3, 4)
        level.wall_box(4, 3)
        level.wall_box(1, 1)

        level.wall_east(2, 0)
        level.wall_south(3, 0)
        level.wall_west(4, 1)
        level.wall_south(4, 1)
        level.wall_south(5, 1)

        level.set_hazard(2, 2)

        level.add_victim(2, 1)
        level.add_victim(2, 4)
        level.add_victim(2, 5)
        level.add_victim(4, 2)

        return level

    @staticmethod
    def s1_s08():

        level = Level('Slayaway Camp 1, Scene 8', 8, 6,
            3, 5,
            6, 0)

        level.wall_west(6, 5)
        level.wall_north(6, 5)
        level.wall_north(7, 5)

        level.wall_east(1, 5)
        level.wall_north(1, 5)
        level.wall_north(0, 5)
        level.wall_north(0, 3)
        level.wall_box(1, 0)
        level.wall_box(5, 0)
        level.wall_box(7, 0)
        level.wall_box(7, 1)

        level.wall_south(3, 2)
        level.wall_box(4, 2)

        level.wall_south(2, 3)
        level.wall_south(3, 3)
        level.wall_south(4, 3)
        level.wall_south(5, 3)

        level.set_hazard(1, 3)
        level.set_hazard(6, 3)

        level.add_victim(3, 3)

        return level

    @staticmethod
    def s1_s09():

        level = Level('Slayaway Camp 1, Scene 9', 5, 6,
            2, 5,
            4, 5,
            6)

        level.wall_box(3, 5)
        level.wall_box(4, 3)
        level.wall_box(4, 0)

        level.wall_east(0, 5)
        level.wall_east(0, 4)
        level.wall_north(0, 4)

        level.add_victim(2, 1)
        
        return level

    @staticmethod
    def s1_s10():

        # Fudging the exit a bit, here.  The actual level
        # is special-cased so that you win when you scare
        # the victim into the hole.
        level = Level('Slayaway Camp 1, Scene 10', 6, 6,
            5, 4,
            4, 5)

        level.set_hazard(5, 5)
        level.set_hazard(1, 5)

        level.add_victim(3, 5)

        level.short_wall_west(1, 0)
        level.short_wall_south(1, 0)
        level.short_wall_east(1, 1)

        level.short_wall_south(3, 0)

        level.short_wall_east(4, 0)

        level.short_wall_south(5, 1)

        level.short_wall_south(0, 2)

        level.short_wall_east(3, 2)
        level.short_wall_south(3, 2)

        level.short_wall_east(1, 3)

        level.short_wall_south(3, 3)

        level.wall_south(5, 3)

        level.wall_south(2, 4)
        level.wall_south(3, 4)

        return level

    @staticmethod
    def s1_d1():

        level = Level('Slayaway Camp 1, Deleted Scene 1', 7, 7,
            5, 6,
            3, 4)

        level.wall_south(0, 2)
        level.wall_east(0, 2)
        level.wall_south(1, 1)
        level.wall_east(1, 1)
        level.wall_east(1, 0)
        level.wall_west(5, 0)
        level.wall_south(5, 0)
        level.wall_west(6, 1)
        level.wall_west(6, 2)
        level.wall_south(6, 2)

        level.wall_box(3, 6)
        level.wall_box(6, 5)
        level.wall_box(6, 6)

        level.wall_west(2, 3)
        level.wall_east(2, 3)
        level.wall_west(2, 4)

        level.wall_south(4, 1)
        level.wall_south(4, 3)
        level.wall_south(3, 4)
        level.wall_south(5, 4)

        level.set_hazard(2, 0)
        level.set_hazard(2, 6)
        level.set_hazard(4, 2)

        level.add_victim(2, 2)

        return level

    @staticmethod
    def s1_d2():

        level = Level('Slayaway Camp 1, Deleted Scene 2', 6, 6,
            3, 3,
            3, 2,
            10)

        level.wall_box(1, 1)
        level.wall_box(1, 2)
        level.wall_box(4, 1)
        level.wall_box(3, 4)
        level.wall_box(4, 4)
        level.wall_box(2, 5)

        level.add_victim(1, 0)
        level.add_victim(0, 5)
        level.add_victim(5, 3)

        return level

    @staticmethod
    def s1_d3():

        level = Level('Slayaway Camp 1, Deleted Scene 3', 7, 8,
            0, 2,
            0, 1)

        level.wall_east(2, 7)
        level.wall_north(2, 7)
        level.wall_east(1, 6)
        level.wall_north(1, 6)
        level.wall_north(0, 6)
        level.wall_south(0, 3)
        level.wall_east(0, 3)
        level.wall_north(0, 3)
        level.wall_south(0, 0)
        level.wall_east(0, 0)
        level.wall_west(2, 0)
        level.wall_south(2, 0)
        level.wall_east(2, 0)
        level.wall_west(4, 0)
        level.wall_south(4, 0)
        level.wall_west(5, 1)
        level.wall_south(5, 1)
        level.wall_east(5, 1)
        level.wall_south(6, 0)

        level.wall_north(6, 5)
        level.wall_north(5, 5)
        level.wall_west(5, 5)
        level.wall_west(5, 6)
        level.wall_south(5, 6)
        level.wall_south(6, 6)
        
        level.wall_box(3, 2)

        level.add_victim(5, 4)
        level.add_victim(2, 5)
        level.add_victim(1, 0)
        level.add_victim(3, 0)

        return level

    @staticmethod
    def s1_d4():

        level = Level('Slayaway Camp 1, Deleted Scene 4', 8, 8,
            2, 7,
            1, 7)

        level.short_wall_west(3, 0)
        level.short_wall_south(3, 0)
        level.short_wall_south(5, 0)
        level.short_wall_west(6, 1)
        level.short_wall_west(6, 2)
        level.short_wall_south(6, 2)
        level.short_wall_south(7, 2)

        level.short_wall_south(2, 3)

        level.short_wall_south(0, 4)

        level.short_wall_south(6, 4)
        level.short_wall_south(7, 4)

        level.short_wall_south(5, 5)

        level.short_wall_west(4, 7)
        level.short_wall_east(5, 7)

        level.wall_box(0, 7)

        level.set_hazard(4, 0)
        level.set_hazard(1, 2)

        level.set_hazard(0, 5)
        level.set_hazard(1, 5)
        level.set_hazard(2, 5)
        level.set_hazard(0, 6)

        level.set_hazard(5, 5)
        level.set_hazard(6, 5)
        level.set_hazard(7, 5)
        level.set_hazard(6, 6)
        level.set_hazard(7, 6)
        level.set_hazard(6, 7)
        level.set_hazard(7, 7)

        level.add_victim(5, 2)
        level.add_victim(5, 3)
        level.add_victim(1, 3)
        level.add_victim(1, 6)

        return level

    @staticmethod
    def s1_d5():

        level = Level('Slayaway Camp 1, Deleted Scene 5', 7, 8,
            0, 2,
            4, 2)

        level.wall_box(1, 0)
        level.wall_box(6, 4)

        level.wall_east(1, 2)
        level.wall_east(1, 4)
        level.wall_south(0, 6)
        level.wall_south(3, 3)
        level.wall_east(4, 4)
        level.wall_south(4, 4)
        level.wall_east(4, 5)
        level.wall_west(4, 6)
        level.wall_south(4, 6)
        level.wall_south(5, 6)

        level.set_hazard(0, 0)
        level.set_hazard(6, 2)
        level.set_hazard(6, 3)
        level.set_hazard(2, 4)
        level.set_hazard(3, 4)
        level.set_hazard(4, 4)

        level.add_victim(3, 3)
        level.add_victim(5, 4)
        level.add_victim(3, 5)

        return level

    @staticmethod
    def s2_s01():

        level = Level('Slayaway Camp 2, Scene 1 - A Really Dumb Cop...', 5, 6,
            2, 5,
            3, 0)

        level.wall_box(0, 5)

        level.wall_south(0, 0)
        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_east(2, 0)

        level.wall_south(3, 3)
        level.wall_west(3, 3)
        level.wall_north(3, 3)
        level.wall_north(4, 3)
        level.wall_west(4, 4)
        level.wall_west(4, 5)

        level.wall_south(1, 2)

        level.add_victim(4, 2)
        level.add_cop(2, 1, DIR_S)

        return level

    @staticmethod
    def s2_s02():

        level = Level('Slayaway Camp 2, Scene 2 - Danger Lake', 8, 8,
            5, 7,
            0, 1)

        level.wall_box(0, 3)
        level.wall_box(1, 6)
        level.wall_box(2, 6)
        level.wall_box(2, 4)
        level.wall_box(3, 4)
        level.wall_box(2, 2)
        level.wall_box(3, 0)
        level.wall_box(4, 0)
        level.wall_box(4, 2)
        level.wall_box(5, 2)
        level.wall_box(6, 4)
        level.wall_box(5, 5)

        level.set_hazard(0, 7)

        level.set_hazard(5, 0)
        level.set_hazard(5, 1)
        for y in [0, 1, 2, 3, 6, 7]:
            level.set_hazard(6, y)
            level.set_hazard(7, y)

        level.add_victim(3, 1)
        level.add_victim(5, 3)

        return level

    @staticmethod
    def s2_s03():

        level = Level('Slayaway Camp 2, Scene 3 - Right to Remain Deadly', 7, 7,
            5, 2,
            6, 0)

        level.wall_box(0, 0)
        level.wall_box(0, 3)
        level.wall_box(2, 3)
        level.wall_box(6, 6)

        level.wall_north(0, 6)
        level.wall_north(1, 6)
        level.wall_north(2, 6)
        level.wall_north(3, 6)
        level.wall_east(3, 6)

        level.wall_west(6, 2)
        level.wall_south(6, 2)
        level.wall_north(6, 1)
        level.wall_north(5, 1)
        level.wall_south(5, 1)
        level.wall_north(4, 1)
        level.wall_west(4, 1)
        level.wall_west(4, 2)
        level.wall_east(4, 2)
        level.wall_south(4, 2)
        level.wall_west(4, 3)
        level.wall_south(4, 3)

        level.add_cop(4, 3, DIR_E)
        level.add_cop(3, 0, DIR_S)

        level.add_victim(2, 4)

        return level

    @staticmethod
    def s2_s04():

        level = Level('Slayaway Camp 2, Scene 4 - Triple Truncheon', 7, 7,
            1, 4,
            4, 0)

        level.wall_box(6, 0)
        level.wall_box(5, 2)
        level.wall_box(6, 6)

        level.wall_east(3, 0)
        level.wall_south(3, 0)
        level.wall_east(2, 1)
        level.wall_south(2, 1)
        level.wall_south(1, 1)
        level.wall_south(0, 1)

        level.wall_north(0, 3)
        level.wall_east(0, 3)
        level.wall_east(0, 4)
        level.wall_east(0, 5)
        level.wall_north(1, 6)
        level.wall_east(1, 6)

        level.wall_east(3, 2)
        level.wall_east(3, 3)
        level.wall_east(3, 4)

        level.add_cop(0, 2, DIR_E)
        level.add_cop(5, 0, DIR_S)
        level.add_cop(3, 3, DIR_S)

        level.add_victim(4, 4)
        
        return level

    @staticmethod
    def s2_s05():

        level = Level('Slayaway Camp 2, Scene 5 - Trypophobia', 6, 6,
            3, 4,
            5, 5)

        level.wall_south(2, 1)

        level.wall_north(1, 3)
        level.wall_east(1, 3)

        level.wall_west(5, 2)
        level.wall_south(5, 2)

        level.wall_west(5, 4)

        level.set_hazard(0, 0)
        level.set_hazard(4, 0)
        level.set_hazard(5, 2)
        level.set_hazard(1, 3)
        level.set_hazard(0, 5)
        level.set_hazard(2, 5)
        level.set_hazard(3, 5)

        level.add_victim(2, 0)
        level.add_victim(0, 2)
        level.add_victim(0, 3)

        return level

    @staticmethod
    def s2_s06():

        level = Level('Slayaway Camp 2, Scene 6 - Crime Scene Scream', 6, 6,
            5, 5,
            5, 0)

        level.wall_south(5, 1)

        level.wall_west(4, 3)
        level.wall_west(4, 4)
        level.wall_west(4, 5)

        level.wall_east(2, 0)
        level.wall_south(2, 0)
        level.wall_south(1, 0)
        level.wall_west(1, 1)
        level.wall_east(1, 1)
        level.wall_south(0, 1)

        level.wall_north(0, 5)
        level.wall_north(1, 5)
        level.wall_north(2, 5)
        level.wall_east(2, 5)

        level.add_cop(1, 1, DIR_S)
        level.add_cop(2, 4, DIR_E)

        level.add_victim(0, 2)
        level.add_victim(3, 5)
        level.add_victim(5, 2)

        return level

    @staticmethod
    def s2_s07():

        level = Level('Slayaway Camp 2, Scene 7 - Kabin Krush', 6, 6,
            0, 0,
            1, 5)

        level.wall_east(3, 1)
        level.wall_north(3, 1)
        level.wall_south(3, 1)
        level.wall_north(2, 1)
        level.wall_south(2, 1)
        level.wall_north(1, 1)
        level.wall_south(1, 1)
        level.wall_north(0, 1)
        level.wall_east(0, 2)
        level.wall_east(0, 3)
        level.wall_east(0, 4)
        level.wall_east(0, 5)

        level.wall_west(3, 5)
        level.wall_west(3, 4)
        level.wall_north(3, 4)
        level.wall_east(3, 4)
        level.wall_north(4, 5)
        level.wall_north(5, 5)

        level.add_cabinet_we(3, 2)
        level.add_cabinet_ns(5, 3)

        level.add_victim(2, 2)
        level.add_victim(5, 4)

        return level

    @staticmethod
    def s2_s08():

        level = Level('Slayaway Camp 2, Scene 8 - Forest Frenzy', 8, 7,
            1, 2,
            4, 4,
            7)

        # Adding hazards here is a bit silly, since they're all behind
        # walls, but we'll put 'em in anyway.

        level.set_hazard(0, 0)
        level.wall_south(0, 0)
        level.set_hazard(1, 0)
        level.wall_south(1, 0)
        level.set_hazard(2, 0)
        level.wall_south(2, 0)
        level.set_hazard(3, 0)
        level.wall_south(3, 0)
        level.wall_east(3, 0)

        level.set_hazard(5, 0)
        level.wall_west(5, 0)
        level.wall_south(5, 0)
        level.set_hazard(6, 0)
        level.set_hazard(7, 0)
        level.set_hazard(6, 1)
        level.wall_west(6, 1)
        level.wall_south(6, 1)
        level.set_hazard(7, 1)
        level.wall_south(7, 1)

        level.set_hazard(0, 5)
        level.wall_north(0, 5)
        level.set_hazard(1, 5)
        level.wall_north(1, 5)
        level.set_hazard(2, 5)
        level.wall_north(2, 5)
        level.set_hazard(3, 5)
        level.wall_north(3, 5)
        level.wall_east(3, 5)
        level.set_hazard(0, 6)
        level.set_hazard(1, 6)
        level.set_hazard(2, 6)
        level.set_hazard(3, 6)
        level.wall_east(3, 6)

        level.set_hazard(5, 6)
        level.wall_west(5, 6)
        level.wall_north(5, 6)
        level.set_hazard(6, 6)
        level.wall_north(6, 6)
        level.set_hazard(7, 6)
        level.set_hazard(7, 5)
        level.wall_west(7, 5)
        level.wall_north(7, 5)

        level.wall_south(3, 1)

        level.wall_south(1, 3)
        level.wall_south(2, 3)
        level.wall_south(3, 3)

        level.add_victim(4, 2)
        level.add_victim(4, 3)

        return level

    @staticmethod
    def s2_s09():

        level = Level('Slayaway Camp 2, Scene 9 - Bookcase Blues', 7, 6,
            2, 5,
            3, 0)

        level.wall_box(0, 0)
        level.wall_box(4, 0)
        level.wall_box(6, 2)

        level.wall_box(3, 2)
        level.wall_box(4, 2)

        level.wall_box(5, 5)
        level.wall_box(6, 5)

        level.wall_north(0, 3)
        level.wall_south(0, 3)

        level.wall_south(6, 3)

        level.add_cabinet_we(1, 2)
        level.add_cabinet_we(1, 3)
        level.add_cabinet_we(5, 3)

        level.add_cop(2, 2, DIR_S)

        level.add_victim(0, 3)
        level.add_victim(6, 3)

        return level

    @staticmethod
    def s2_s10():

        level = Level('Slayaway Camp 2, Scene 10 - Hotsprings Havoc', 6, 7,
            1, 2,
            3, 3)

        level.wall_west(3, 0)
        level.wall_west(3, 1)
        level.set_hazard(3, 0)
        level.set_hazard(4, 0)
        level.set_hazard(5, 0)
        level.set_hazard(3, 1)
        level.set_hazard(4, 1)
        level.set_hazard(5, 1)

        level.wall_north(0, 3)
        level.set_hazard(0, 3)
        level.set_hazard(0, 4)
        level.wall_south(0, 4)
        level.wall_east(0, 4)
        level.wall_north(1, 4)

        level.wall_north(2, 6)
        level.wall_west(2, 6)
        level.set_hazard(2, 6)
        level.set_hazard(3, 6)
        level.wall_east(3, 6)
        level.wall_east(3, 5)

        level.add_victim(4, 3)
        level.add_victim(5, 3)
        level.add_victim(5, 4)

        return level

    @staticmethod
    def s2_s11():

        level = Level('Slayaway Camp 2, Scene 11 - Swimming Hole Horrors', 8, 8,
            1, 2,
            7, 0)

        for x in range(7):
            level.set_hazard(x, 0)
            level.set_hazard(x, 7)
        level.set_hazard(7, 7)
        for y in range(2, 8):
            level.set_hazard(0, y)
            level.set_hazard(7, y)
        level.set_hazard(0, 1)

        for x in range(1, 7):
            level.wall_north(x, 1)
        level.wall_west(7, 0)
        level.wall_south(7, 1)

        for y in range(3, 7):
            level.wall_west(1, y)
            level.wall_east(6, y)

        for x in [1, 2, 4, 5, 6]:
            level.wall_south(x, 6)

        level.wall_west(2, 3)
        level.wall_south(2, 3)

        level.wall_east(4, 4)
        level.wall_east(4, 5)
        level.wall_south(4, 5)

        level.wall_box(1, 5)
        level.wall_box(1, 6)

        level.wall_box(5, 4)
        level.wall_box(5, 5)

        level.add_cabinet_we(5, 1)

        level.add_victim(2, 1)
        level.add_victim(6, 1)

        return level

    @staticmethod
    def s2_s12():

        level = Level('Slayaway Camp 2, Scene 12 - Swat Team', 6, 6,
            1, 2,
            2, 1,
            6)

        level.wall_box(0, 1)
        level.wall_box(5, 0)

        level.wall_west(3, 5)
        level.wall_north(3, 5)
        level.wall_north(4, 5)
        level.wall_west(5, 4)
        level.wall_north(5, 4)

        level.wall_east(3, 2)
        level.wall_south(1, 3)
        level.wall_south(2, 3)

        level.set_hazard(0, 0)
        level.set_hazard(4, 0)
        level.set_hazard(4, 4)

        level.add_victim(3, 0)
        level.add_victim(4, 3)
        level.add_victim(3, 4)

        return level

    @staticmethod
    def s2_s13():

        level = Level('Slayaway Camp 2, Scene 13 - Please... Make it stop...', 9, 9,
            8, 0,
            4, 2)

        level.wall_box(5, 0)
        level.wall_box(6, 0)
        level.wall_box(1, 1)
        level.wall_box(5, 3)

        level.wall_south(2, 0)
        level.wall_south(8, 0)
        level.wall_south(3, 1)
        level.wall_south(7, 1)
        level.wall_south(0, 2)
        level.wall_west(6, 2)
        level.wall_east(6, 2)
        level.wall_south(8, 2)
        level.wall_south(7, 3)
        level.wall_south(0, 4)
        level.wall_west(2, 4)
        level.wall_south(2, 4)
        level.wall_west(6, 4)
        level.wall_east(6, 4)
        level.wall_south(8, 4)
        level.wall_south(1, 5)
        level.wall_south(0, 6)
        level.wall_east(1, 6)
        level.wall_east(3, 6)
        level.wall_south(4, 6)
        level.wall_south(6, 6)
        level.wall_east(6, 6)
        level.wall_south(7, 6)
        level.wall_east(4, 7)
        level.wall_east(2, 8)
        level.wall_east(4, 8)

        level.set_hazard(4, 4)

        level.add_victim(4, 3)

        return level

    @staticmethod
    def s2_d1():

        level = Level('Slayaway Camp 2, Deleted Scene 1 - Back Yard of Death', 6, 6,
            0, 4,
            0, 0)

        level.wall_box(1, 1)
        level.wall_box(4, 1)
        level.wall_box(5, 1)
        level.wall_west(1, 0)

        level.wall_north(0, 4)
        level.wall_north(1, 4)
        level.wall_east(2, 5)

        level.add_cop(1, 0, DIR_E)
        level.add_victim(5, 0)
        level.add_victim(2, 4)

        return level

    @staticmethod
    def s2_d2():

        level = Level('Slayaway Camp 2, Deleted Scene 2 - Ritual Gone Wrong', 7, 7,
            4, 4,
            3, 3)

        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_south(4, 0)
        level.wall_south(5, 0)

        level.wall_box(1, 2)
        level.wall_box(1, 4)
        level.wall_box(4, 3)
        level.wall_box(6, 1)
        level.wall_box(6, 5)

        level.set_hazard(0, 0)
        level.set_hazard(6, 0)
        level.set_hazard(0, 6)
        level.set_hazard(6, 6)

        level.add_victim(2, 0)
        level.add_victim(4, 0)
        level.add_victim(0, 2)
        level.add_victim(5, 6)
        
        return level

    @staticmethod
    def s2_d3():

        level = Level('Slayaway Camp 2, Deleted Scene 3 - Swat Team', 7, 7,
            0, 1,
            1, 0,
            11)

        level.wall_box(4, 0)
        level.wall_box(5, 0)
        level.wall_box(1, 1)
        level.wall_box(0, 6)
        level.wall_box(1, 6)
        level.wall_box(6, 5)
        level.wall_box(6, 6)

        level.wall_west(1, 4)
        level.wall_south(1, 4)

        level.wall_east(5, 2)
        level.wall_south(5, 2)

        level.add_victim(2, 1)
        level.add_victim(1, 4)
        level.add_victim(5, 2)
        level.add_victim(4, 5)

        return level

    @staticmethod
    def s2_d4():

        level = Level('Slayaway Camp 2, Deleted Scene 4 - Countin\' Cops', 7, 7,
            3, 2,
            2, 1,
            7)

        level.wall_box(0, 5)
        level.wall_box(0, 6)
        level.wall_box(1, 6)
        level.wall_box(5, 2)

        level.wall_south(3, 3)

        level.add_cop(1, 3, DIR_W)
        level.add_cop(5, 3, DIR_E)
        level.add_victim(0, 3)
        level.add_victim(6, 3)

        return level

    @staticmethod
    def s2_d5():

        level = Level('Slayaway Camp 2, Deleted Scene 5 - Inside Out', 7, 7,
            1, 3,
            5, 5,
            10)

        level.wall_south(0, 0)
        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_south(3, 0)
        level.wall_east(3, 0)

        level.wall_box(0, 5)
        level.wall_box(2, 5)
        level.wall_box(4, 5)

        level.wall_south(6, 1)
        level.wall_south(4, 2)
        level.wall_east(5, 4)

        level.add_victim(3, 2)
        level.add_victim(3, 3)
        level.add_victim(3, 4)

        return level

    @staticmethod
    def s25_s01():

        level = Level('Slayaway Camp 2.5, Scene 1 - Phone Call of Duty', 7, 7,
            0, 6,
            2, 1)

        level.wall_east(0, 6)
        level.wall_east(0, 5)
        level.wall_east(0, 4)
        level.wall_east(0, 3)
        level.wall_east(0, 2)
        level.wall_east(0, 1)

        level.wall_east(1, 4)
        level.wall_east(1, 3)
        level.wall_east(1, 2)
        level.wall_east(1, 1)

        level.wall_east(2, 1)

        level.wall_north(4, 4)
        level.wall_north(5, 4)
        level.wall_east(5, 4)
        level.wall_east(5, 5)

        level.wall_west(4, 0)
        level.wall_south(4, 0)
        level.wall_west(5, 1)
        level.wall_south(5, 1)
        level.wall_south(6, 1)

        level.add_phone_pair(2, 0, 6, 6)

        level.add_cop(2, 3, DIR_S)
        level.add_victim(3, 6)

        return level

    @staticmethod
    def s25_s02():

        level = Level('Slayaway Camp 2.5, Scene 2 - Playmaker', 6, 5,
            4, 4,
            0, 2)

        level.wall_south(0, 0)
        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_east(2, 0)

        level.wall_west(4, 0)
        level.wall_south(4, 0)
        level.wall_west(5, 1)
        level.wall_west(5, 2)
        level.wall_south(5, 2)

        level.wall_box(1, 2)

        level.wall_north(0, 4)
        level.wall_north(1, 4)
        level.wall_east(1, 4)

        level.add_victim(3, 0)
        level.add_victim(4, 2)

        return level

    @staticmethod
    def s25_s03():

        level = Level('Slayaway Camp 2.5, Scene 3 - Ringing Phones Attract Curiosity', 7, 7,
            0, 5,
            6, 0)

        level.wall_west(6, 0)
        level.wall_west(6, 1)
        level.wall_west(6, 2)

        level.wall_north(0, 4)
        level.wall_north(1, 4)
        level.wall_east(1, 4)
        level.wall_south(1, 4)
        level.wall_west(1, 5)
        level.wall_south(1, 5)
        level.wall_south(2, 5)
        level.wall_south(3, 5)
        level.wall_south(4, 5)
        level.wall_east(4, 5)
        level.wall_east(4, 4)
        level.wall_north(4, 4)
        level.wall_north(3, 4)
        level.wall_north(2, 4)

        level.add_phone_pair(5, 0, 6, 6)

        level.add_cop(6, 2, DIR_S)

        level.add_victim(0, 0)
        level.add_victim(1, 6)

        return level

    @staticmethod
    def s25_s04():

        level = Level('Slayaway Camp 2.5, Scene 4 - Bookcase Blockade', 7, 6,
            0, 3,
            3, 4)

        level.wall_box(0, 0)
        level.wall_box(0, 1)
        level.wall_box(1, 4)
        level.wall_box(3, 0)

        level.wall_east(3, 4)

        level.wall_west(6, 0)
        level.wall_west(6, 1)
        level.wall_west(6, 2)
        level.wall_west(6, 3)
        level.wall_south(6, 3)

        level.add_cabinet_ns(5, 1)

        level.add_victim(1, 2)

        return level

    @staticmethod
    def s25_s05():

        level = Level('Slayaway Camp 2.5, Scene 5 - Feelin\' Outdoorsy', 6, 6,
            2, 5,
            2, 2)

        level.wall_box(0, 0)
        level.wall_box(0, 5)
        level.wall_box(2, 3)
        level.wall_box(3, 2)

        level.wall_west(4, 0)
        level.wall_south(4, 0)
        level.wall_south(5, 0)

        level.add_cop(1, 0, DIR_S)
        level.add_cop(4, 4, DIR_S)
        level.add_victim(4, 1)
        level.add_victim(5, 5)

        return level

    @staticmethod
    def s25_s06():

        level = Level('Slayaway Camp 2.5, Scene 6 - Dialing Dispatch Distractions', 6, 6,
            3, 1,
            3, 0)

        level.wall_south(0, 1)
        level.wall_south(1, 1)
        level.wall_east(0, 2)
        level.wall_east(0, 3)
        level.wall_east(0, 4)
        level.wall_south(0, 4)

        level.wall_east(1, 3)
        level.wall_east(2, 2)

        level.wall_west(4, 1)
        level.wall_south(4, 1)
        level.wall_east(4, 1)
        level.wall_north(5, 1)
        level.wall_west(4, 2)
        level.wall_south(4, 2)
        level.wall_south(5, 2)

        level.wall_north(3, 5)
        level.wall_north(4, 5)
        level.wall_north(5, 5)
        level.wall_west(5, 5)

        level.add_phone_pair(0, 0, 3, 5)

        level.add_cop(0, 5, DIR_E)
        level.add_cop(4, 1, DIR_N)

        level.add_victim(5, 0)
        level.add_victim(4, 3)
        level.add_victim(1, 5)

        return level

    @staticmethod
    def s25_s07():

        level = Level('Slayaway Camp 2.5, Scene 7 - Scarin\' and Slayin\'', 6, 6,
            0, 1,
            2, 3)

        level.wall_box(0, 3)
        level.wall_box(1, 5)
        level.wall_box(3, 5)
        level.wall_box(5, 0)

        level.wall_west(4, 1)
        level.wall_west(4, 2)
        level.wall_south(5, 1)

        level.add_victim(1, 2)
        level.add_victim(2, 5)
        level.add_victim(5, 4)

        return level

    @staticmethod
    def s25_s08():

        level = Level('Slayaway Camp 2.5, Scene 8 - Pantry Panic', 7, 7,
            0, 6,
            2, 0)

        level.wall_east(1, 0)
        level.wall_south(1, 0)
        level.wall_east(0, 1)
        level.wall_east(0, 2)
        level.wall_east(0, 3)
        level.wall_south(0, 3)
        level.wall_south(1, 3)
        level.wall_east(1, 3)
        level.wall_east(1, 2)

        level.wall_west(4, 0)
        level.wall_south(4, 0)
        level.wall_south(5, 0)
        level.wall_south(6, 0)

        level.wall_west(3, 6)
        level.wall_north(3, 6)
        level.wall_west(4, 5)
        level.wall_north(4, 5)
        level.wall_east(4, 5)
        level.wall_north(5, 6)
        level.wall_north(6, 6)

        level.add_cabinet_ns(2, 3)
        level.add_cabinet_ns(5, 3)
        level.add_cabinet_we(4, 1)

        level.add_cop(3, 1, DIR_S)
        level.add_cop(5, 2, DIR_N)
        level.add_victim(2, 2)
        level.add_victim(2, 5)

        return level

    @staticmethod
    def s25_s09():

        level = Level('Slayaway Camp 2.5, Scene 9 - Prank Calls', 7, 7,
            2, 2,
            3, 2)

        level.wall_box(0, 0)

        level.wall_north(0, 6)
        level.wall_north(1, 6)
        level.wall_north(2, 6)
        level.wall_north(3, 6)
        level.wall_east(3, 6)

        level.wall_west(5, 0)
        level.wall_south(5, 0)
        level.wall_south(6, 0)

        level.add_phone_pair(0, 4, 4, 0)

        level.add_victim(4, 2)
        level.add_victim(6, 3)
        
        return level

    @staticmethod
    def s25_s10():

        level = Level('Slayaway Camp 2.5, Scene 10 - Water, Water Everywhere', 8, 8,
            3, 4,
            3, 1)

        for x in range(8):
            level.set_hazard(x, 0)
            level.set_hazard(x, 7)
        for y in range(8):
            level.set_hazard(0, y)
            level.set_hazard(7, y)

        level.wall_box(1, 1)
        level.wall_box(1, 2)
        level.wall_box(2, 1)

        level.wall_box(5, 1)
        level.wall_box(6, 1)

        level.wall_box(3, 6)
        level.wall_box(6, 5)

        level.wall_west(1, 5)
        level.wall_west(1, 6)
        level.wall_south(1, 6)
        level.wall_south(2, 6)

        level.wall_east(6, 6)
        level.wall_east(6, 4)
        level.wall_east(6, 3)

        level.add_victim(3, 2)
        level.add_victim(5, 4)

        return level

    @staticmethod
    def s25_s11():

        level = Level('Slayaway Camp 2.5, Scene 11 - Split Personality', 8, 8,
            1, 1,
            7, 5)

        level.wall_box(0, 0)
        level.wall_box(0, 2)
        level.wall_box(3, 0)
        level.wall_box(1, 5)

        level.wall_east(3, 4)
        level.wall_north(3, 4)
        level.wall_west(3, 4)
        level.wall_west(3, 5)
        level.wall_south(3, 5)
        level.wall_south(4, 5)
        level.wall_north(4, 5)
        level.wall_south(5, 5)
        level.wall_east(5, 5)
        level.wall_east(5, 4)
        level.wall_west(5, 4)
        level.wall_north(5, 4)

        level.wall_north(7, 6)
        level.wall_west(7, 6)
        level.wall_west(7, 7)

        # Water
        level.set_hazard(7, 0)
        level.set_hazard(7, 1)

        level.set_hazard(4, 7)
        level.set_hazard(5, 7)
        level.set_hazard(6, 7)

        # Fire
        level.set_hazard(0, 1)
        level.set_hazard(5, 3)
        level.set_hazard(4, 4)

        level.add_cabinet_we(5, 1)
        level.add_cabinet_we(3, 3)
        level.add_cabinet_ns(2, 6)

        level.add_victim(5, 0)

        return level

    @staticmethod
    def s25_s12():

        level = Level('Slayaway Camp 2.5, Scene 12 - Careful Calling', 6, 7,
            4, 6,
            3, 6)

        level.wall_north(0, 4)
        level.wall_east(0, 4)
        level.wall_south(0, 5)
        level.wall_north(1, 5)
        level.wall_south(1, 5)
        level.wall_north(2, 5)
        level.wall_south(2, 5)
        level.wall_north(3, 5)
        level.wall_south(3, 5)
        level.wall_east(3, 5)

        level.wall_box(5, 5)

        level.wall_west(4, 0)
        level.wall_south(4, 0)
        level.wall_south(5, 0)

        level.add_phone_pair(0, 0, 0, 3)

        level.add_victim(0, 6)
        level.add_victim(5, 1)
        level.add_victim(5, 3)

        return level

    @staticmethod
    def s25_s13():

        level = Level('Slayaway Camp 2.5, Scene 13 - A Flaming Felony', 6, 7,
            0, 3,
            5, 6)

        level.wall_east(0, 0)
        level.wall_east(0, 1)
        level.wall_south(0, 1)

        level.wall_north(0, 4)
        level.wall_east(0, 4)
        level.wall_east(0, 5)
        level.wall_east(0, 6)

        level.wall_east(2, 3)
        level.wall_south(2, 3)

        level.wall_box(4, 6)

        level.set_hazard(5, 3)

        level.add_cop(4, 0, DIR_E)
        level.add_cop(4, 2, DIR_W)

        level.add_victim(5, 1)
        level.add_victim(3, 5)

        return level

    @staticmethod
    def s25_s14():

        level = Level('Slayaway Camp 2.5, Scene 14 - Living Room Lacerations', 8, 8,
            4, 4,
            1, 4)

        level.wall_box(0, 0)
        level.wall_box(1, 0)
        level.wall_box(3, 0)
        level.wall_box(0, 2)
        level.wall_box(2, 2)
        level.wall_box(3, 3)
        level.wall_box(2, 6)
        level.wall_box(4, 7)
        level.wall_box(7, 7)

        level.wall_south(3, 5)
        level.wall_east(6, 5)

        level.add_victim(0, 1)
        level.add_victim(7, 1)
        level.add_victim(3, 5)

        return level

    @staticmethod
    def s25_s15():

        level = Level('Slayaway Camp 2.5, Scene 15 - Kill the Camp Counsellor, Dale', 7, 8,
            1, 3,
            3, 0)

        level.wall_south(0, 1)
        level.wall_south(1, 1)
        level.wall_south(2, 1)
        level.wall_east(2, 1)
        level.wall_north(2, 1)
        level.wall_east(1, 0)

        level.wall_east(4, 0)
        level.wall_south(2, 2)
        level.wall_east(5, 2)
        level.wall_south(3, 4)
        level.wall_south(4, 4)

        level.wall_box(4, 3)

        level.add_cabinet_ns(3, 1)
        level.add_cabinet_ns(1, 6)
        level.add_cabinet_ns(6, 6)

        level.add_victim(2, 0)
        level.add_victim(4, 4)
        level.add_victim(1, 7)

        return level

    @staticmethod
    def s25_d1():

        level = Level('Slayaway Camp 2.5, Deleted Scene 1 - Squish and Scorch', 7, 7,
            3, 2,
            2, 3)

        level.wall_east(0, 1)
        level.wall_east(0, 2)
        level.wall_south(1, 5)

        level.wall_north(4, 1)
        level.wall_east(4, 1)
        level.wall_north(5, 2)
        level.wall_east(5, 2)

        level.wall_box(2, 1)
        level.wall_box(2, 2)

        level.set_hazard(0, 6)
        level.set_hazard(6, 6)

        level.add_cabinet_we(1, 0)
        level.add_cabinet_we(5, 0)
        level.add_cabinet_we(5, 5)

        level.add_victim(0, 0)
        level.add_victim(4, 0)
        level.add_victim(6, 0)
        level.add_victim(6, 1)

        return level

    @staticmethod
    def s25_d2():

        level = Level('Slayaway Camp 2.5, Deleted Scene 2 - Entrapment', 6, 6,
            2, 5,
            2, 1)

        level.wall_box(5, 0)
        level.wall_box(3, 1)
        level.wall_box(5, 5)

        level.wall_south(1, 0)
        level.wall_east(3, 4)

        level.add_cabinet_ns(2, 2)
        level.add_cabinet_we(4, 3)

        level.add_victim(1, 3)
        level.add_victim(3, 3)

        return level

    @staticmethod
    def s25_d3():

        level = Level('Slayaway Camp 2.5, Deleted Scene 3 - Ringing Rampage', 8, 7,
            3, 5,
            1, 2)

        level.wall_box(0, 0)
        level.wall_box(2, 0)
        level.wall_box(3, 6)
        level.wall_box(5, 2)
        level.wall_box(5, 3)

        level.wall_east(2, 2)
        level.wall_east(2, 3)
        level.wall_south(2, 3)
        level.wall_south(2, 4)

        level.wall_north(0, 5)
        level.wall_east(0, 5)
        level.wall_east(0, 6)

        level.wall_west(5, 0)
        level.wall_south(5, 0)
        level.wall_south(6, 0)
        level.wall_south(7, 0)

        level.wall_north(7, 4)
        level.wall_west(7, 4)
        level.wall_west(7, 5)
        level.wall_west(7, 6)

        level.add_phone_pair(2, 1, 1, 5)

        level.add_cop(1, 0, DIR_S)
        level.add_cop(5, 1, DIR_E)
        level.add_victim(7, 1)

        return level

    @staticmethod
    def s25_d4():

        level = Level('Slayaway Camp 2.5, Deleted Scene 4 - Domino Effect', 6, 6,
            2, 3,
            1, 5)

        level.wall_west(1, 0)
        level.wall_east(3, 0)
        
        level.wall_west(1, 2)
        level.wall_north(1, 2)

        level.wall_east(3, 2)
        level.wall_north(3, 2)

        level.wall_box(5, 4)
        level.wall_box(3, 5)

        level.add_cabinet_ns(2, 2)
        level.add_cabinet_ns(1, 3)
        level.add_cabinet_ns(3, 3)
        level.add_cabinet_ns(2, 4)
        level.add_cabinet_ns(4, 4)

        level.add_victim(1, 0)
        level.add_victim(2, 1)
        level.add_victim(4, 1)

        return level

    @staticmethod
    def s25_d5():

        level = Level('Slayaway Camp 2.5, Deleted Scene 5 - Faulty Floorboards', 8, 8,
            4, 7,
            4, 0)

        level.wall_east(0, 0)
        level.wall_east(0, 1)
        level.wall_south(0, 1)

        level.wall_box(0, 7)
        level.wall_box(5, 0)
        level.wall_box(3, 3)
        level.wall_box(5, 3)

        level.wall_west(2, 1)
        level.wall_north(2, 1)
        level.wall_south(6, 1)
        level.wall_south(0, 4)
        level.wall_south(6, 4)
        level.wall_east(6, 4)
        level.wall_east(3, 5)
        level.wall_south(2, 6)
        level.wall_east(5, 6)
        level.wall_east(6, 7)

        level.set_hazard(4, 4)

        level.add_cop(3, 2, DIR_E)
        level.add_cop(5, 2, DIR_W)
        level.add_victim(4, 3)

        return level

    @staticmethod
    def s3_s01():

        level = Level('Slayaway Camp 3, Scene 1 - The Abusement Park', 6, 6,
            1, 2,
            3, 0)

        level.wall_north(0, 1)
        level.wall_north(1, 1)
        level.wall_east(1, 1)
        level.wall_south(1, 1)
        level.wall_east(0, 2)
        level.wall_north(1, 3)
        level.wall_east(1, 3)
        level.wall_east(1, 4)
        level.wall_east(1, 5)

        level.wall_box(4, 1)
        level.wall_box(4, 4)

        level.set_mine(2, 0)
        level.set_mine(5, 5)

        level.add_cop(5, 2, DIR_S)
        level.add_victim(1, 0)
        level.add_victim(5, 3)
        level.add_victim(2, 4)

        return level

    @staticmethod
    def s3_s02():

        level = Level('Slayaway Camp 3, Scene 2 - Landmine Maneuvering', 7, 6,
            3, 3,
            3, 2)

        level.wall_south(0, 1)
        level.wall_south(1, 1)
        level.wall_east(1, 1)
        level.wall_north(2, 1)
        level.wall_west(2, 2)
        level.wall_west(2, 3)
        level.wall_south(2, 3)
        level.wall_south(3, 3)
        level.wall_south(1, 3)
        level.wall_south(0, 3)

        level.wall_north(4, 1)
        level.wall_east(4, 1)

        level.wall_south(1, 4)
        level.wall_south(2, 4)

        level.wall_north(6, 4)
        level.wall_west(6, 4)
        level.wall_west(6, 5)

        level.set_mine(0, 0)
        level.set_mine(5, 0)

        level.add_victim(2, 0)
        level.add_victim(5, 3)

        return level

    @staticmethod
    def s3_s03():

        level = Level('Slayaway Camp 3, Scene 3 - Mine Kampf', 8, 8,
            2, 6,
            4, 2)

        level.wall_box(0, 0)
        level.wall_box(7, 0)
        level.wall_box(5, 1)
        level.wall_box(3, 2)
        level.wall_box(5, 3)
        level.wall_box(1, 5)
        level.wall_box(0, 7)

        level.wall_north(0, 3)
        level.wall_south(1, 3)
        level.wall_north(1, 3)
        level.wall_east(1, 3)
        level.wall_south(0, 3)

        level.wall_east(1, 1)
        level.wall_east(2, 4)
        level.wall_east(3, 7)
        level.wall_north(2, 7)

        # Putting the hazards in here is silly, but whatever.
        level.wall_west(5, 5)
        level.wall_north(5, 5)
        level.wall_north(6, 5)
        level.wall_east(6, 5)
        level.wall_east(6, 6)
        level.wall_south(6, 6)
        level.wall_south(5, 6)
        level.wall_west(5, 6)
        level.set_hazard(5, 5)
        level.set_hazard(6, 5)
        level.set_hazard(5, 6)
        level.set_hazard(6, 6)

        level.set_mine(4, 1)
        level.set_mine(5, 2)
        level.set_mine(4, 3)

        level.add_victim(2, 3)

        return level

    @staticmethod
    def s3_s04():

        level = Level('Slayaway Camp 3, Scene 4 - Red Room of Death', 6, 7,
            3, 4,
            3, 2)

        level.wall_south(0, 0)
        level.wall_south(1, 0)
        level.wall_east(1, 0)

        level.wall_north(0, 6)
        level.wall_north(1, 6)
        level.wall_east(1, 6)

        level.wall_south(5, 1)
        level.wall_south(1, 3)
        level.wall_south(2, 3)

        level.wall_box(5, 0)
        level.wall_box(5, 6)

        level.add_phone_pair(0, 1, 5, 3)

        level.add_cop(0, 5, DIR_N)
        level.add_cop(3, 3, DIR_W)
        level.add_victim(5, 1)
        level.add_victim(2, 5)
        level.add_victim(4, 6)

        return level

    @staticmethod
    def s3_s05():

        level = Level('Slayaway Camp 3, Scene 5 - Mine His Own Business', 6, 6,
            3, 2,
            3, 1)

        level.wall_south(0, 0)
        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_south(3, 0)
        level.wall_south(4, 0)
        level.wall_east(4, 0)
        level.wall_east(1, 1)
        level.wall_south(0, 3)

        level.wall_box(3, 5)

        level.set_hazard(0, 1)
        level.set_hazard(0, 2)
        level.set_hazard(0, 3)

        level.set_mine(5, 3)
        level.set_mine(5, 5)

        level.add_phone_pair(1, 2, 5, 0)

        level.add_cop(5, 4, DIR_W)
        level.add_victim(5, 2)
        level.add_victim(1, 5)
        level.add_victim(4, 5)

        return level

    @staticmethod
    def s3_s06():

        level = Level('Slayaway Camp 3, Scene 6 - Laceration Labyrinth', 7, 7,
            3, 3,
            5, 2)

        level.wall_north(0, 3)
        level.wall_south(0, 3)
        level.wall_north(1, 3)
        level.wall_south(1, 3)
        level.wall_north(2, 3)
        level.wall_south(2, 3)
        level.wall_east(2, 3)

        level.wall_east(0, 0)
        level.wall_south(3, 0)
        level.wall_south(1, 1)
        level.wall_south(5, 1)
        level.wall_east(3, 2)
        level.wall_south(6, 3)
        level.wall_south(3, 4)
        level.wall_south(4, 5)
        level.wall_east(1, 6)

        level.add_victim(2, 1)
        level.add_victim(2, 4)

        return level

    @staticmethod
    def s3_s07():

        level = Level('Slayaway Camp 3, Scene 7 - Mine Their (Phone) Manners', 8, 7,
            3, 1,
            2, 1)

        level.wall_west(4, 0)
        level.wall_west(4, 1)
        level.wall_south(4, 1)
        level.wall_south(5, 1)
        level.wall_east(5, 1)
        level.wall_south(6, 0)
        level.wall_south(7, 0)

        level.wall_east(1, 2)
        level.wall_east(1, 3)

        level.wall_east(6, 2)
        level.wall_south(3, 3)

        level.wall_south(2, 5)
        level.wall_south(3, 5)

        level.wall_north(5, 5)
        level.wall_west(5, 5)
        level.wall_east(5, 5)
        level.wall_west(5, 6)
        level.wall_east(5, 6)

        level.wall_box(7, 4)

        level.set_mine(6, 4)

        level.add_phone_pair(1, 3, 6, 5)

        level.add_cop(0, 3, DIR_N)
        level.add_cop(1, 4, DIR_S)
        level.add_victim(1, 5)
        level.add_victim(5, 2)

        return level

    @staticmethod
    def s3_s08():

        level = Level('Slayaway Camp 3, Scene 8 - Mine Manipulation', 7, 7,
            1, 2,
            6, 6)

        level.wall_west(3, 0)
        level.wall_west(3, 1)
        level.wall_south(3, 1)
        level.wall_south(4, 1)
        level.wall_east(4, 1)
        level.wall_east(4, 2)
        level.wall_south(5, 0)
        level.wall_south(6, 0)

        level.wall_north(3, 3)
        level.wall_north(2, 3)
        level.wall_west(2, 3)
        level.wall_south(2, 3)
        level.wall_east(2, 4)
        level.wall_east(2, 5)
        level.wall_east(3, 5)

        level.wall_south(5, 5)
        level.wall_south(6, 5)

        level.set_mine(2, 2)
        level.set_mine(3, 6)

        level.add_phone_pair(0, 6, 2, 3)

        level.add_cop(5, 6, DIR_W)
        level.add_victim(2, 1)
        level.add_victim(2, 6)
        level.add_victim(4, 3)
        level.add_victim(6, 1)

        return level

    @staticmethod
    def s3_s09():

        level = Level('Slayaway Camp 3, Scene 9 - Don\'t Let the Cats Get Hurt', 6, 6,
            1, 5,
            4, 4)

        level.wall_east(0, 0)
        level.wall_south(4, 0)
        level.wall_south(3, 1)
        level.wall_south(2, 3)
        
        level.wall_south(0, 4)
        level.wall_south(1, 4)
        level.wall_south(2, 4)

        level.wall_east(4, 4)
        level.wall_box(4, 5)

        level.set_hazard(0, 0)
        level.set_hazard(5, 4)

        level.add_victim(1, 2)
        level.add_victim(5, 1)
        level.add_cat(0, 2)
        level.add_cat(5, 3)

        return level

    @staticmethod
    def s3_s10():

        # There's two little cat kennels/hutches which you scare
        # the cats into - I suspect that there's not actually a
        # "cat door" kind of restriction, and it's just a visual
        # representation, but there's no good way of knowing because
        # it's impossible to get a situation in the level where
        # it's possible to try and go into them, or scare a victim
        # into them.  So we'll just assume there's nothing actually
        # special about them.

        level = Level('Slayaway Camp 3, Scene 10 - Kitten Corral', 8, 6,
            4, 3,
            4, 0)

        level.wall_north(0, 3)
        level.wall_east(0, 3)
        level.wall_east(0, 4)
        level.wall_east(0, 5)

        level.wall_east(2, 1)
        level.wall_west(4, 2)
        level.wall_east(4, 2)
        level.wall_east(6, 3)
        level.wall_south(2, 4)

        level.wall_west(3, 0)
        level.wall_east(3, 0)
        level.wall_west(5, 0)
        level.wall_east(5, 0)

        level.wall_west(4, 5)
        level.wall_east(4, 5)
        level.wall_west(4, 4)
        level.wall_east(4, 4)
        level.wall_north(4, 4)

        level.add_cabinet_ns(1, 3)

        level.add_cop(0, 0, DIR_S)
        level.add_cop(7, 0, DIR_W)
        level.add_cop(4, 1, DIR_S)
        level.add_victim(2, 4)
        level.add_victim(5, 4)
        level.add_cat(3, 1)
        level.add_cat(5, 1)

        return level

    @staticmethod
    def s3_s11():

        level = Level('Slayaway Camp 3, Scene 11 - Mimin\' Murder', 8, 9,
            2, 3,
            2, 4)

        level.wall_box(0, 8)
        level.wall_box(7, 1)
        level.wall_box(7, 8)

        level.wall_south(1, 0)
        level.wall_south(5, 0)
        level.wall_east(2, 1)
        level.wall_east(0, 2)
        level.wall_south(2, 2)
        level.wall_south(4, 2)
        level.wall_east(4, 3)
        level.wall_south(6, 4)
        level.wall_east(0, 5)
        level.wall_south(1, 5)
        level.wall_south(4, 5)
        level.wall_east(4, 5)
        level.wall_south(1, 6)
        level.wall_south(3, 6)
        level.wall_east(3, 6)
        level.wall_south(7, 6)
        level.wall_south(2, 7)
        level.wall_south(5, 7)

        level.add_victim(3, 4)

        return level

    @staticmethod
    def s3_s12():

        level = Level('Slayaway Camp 3, Scene 12 - SWAT Team', 6, 7,
            2, 4,
            4, 4,
            8)

        level.wall_box(1, 0)

        level.wall_west(5, 0)
        level.wall_west(5, 1)
        level.wall_west(5, 2)
        level.wall_south(5, 2)

        level.wall_south(1, 2)
        level.wall_south(2, 2)
        level.wall_east(1, 5)

        level.add_victim(4, 1)
        level.add_victim(3, 3)
        level.add_victim(0, 5)
        level.add_victim(5, 6)

        return level

    @staticmethod
    def s3_s13():

        level = Level('Slayaway Camp 3, Scene 13 - Crispy Whiskers are Bad!', 6, 6,
            2, 0,
            4, 4)

        level.wall_box(3, 0)
        level.wall_box(5, 0)
        level.wall_box(2, 5)

        level.wall_east(0, 0)
        level.wall_east(0, 1)
        level.wall_south(0, 1)

        level.wall_north(0, 3)
        level.wall_east(0, 3)
        level.wall_south(0, 4)
        level.wall_south(1, 4)
        level.wall_north(1, 4)
        level.wall_east(1, 4)

        level.wall_west(4, 5)
        level.wall_north(4, 5)
        level.wall_north(5, 5)

        level.wall_east(1, 1)
        level.wall_south(4, 1)
        level.wall_south(2, 2)
        level.wall_east(4, 3)

        level.set_hazard(0, 2)
        level.set_hazard(3, 5)

        level.add_victim(4, 1)
        level.add_cat(3, 2)

        return level

    @staticmethod
    def s3_s14():

        level = Level('Slayaway Camp 3, Scene 14 - Bridge Over Troubled Water', 7, 7,
            0, 5,
            2, 6)

        level.wall_box(5, 2)
        level.wall_box(5, 4)

        level.wall_south(2, 0)
        level.wall_east(3, 0)
        level.wall_south(0, 2)
        level.wall_south(3, 2)
        level.wall_south(6, 2)
        level.wall_south(0, 3)
        level.wall_south(3, 3)

        level.wall_west(3, 6)
        level.wall_north(3, 6)
        level.wall_north(4, 6)
        level.wall_east(4, 6)

        level.set_hazard(0, 3)
        level.set_hazard(3, 3)
        level.set_hazard(4, 3)
        level.set_hazard(5, 3)
        level.set_hazard(6, 3)

        level.add_cabinet_we(1, 2)
        level.add_cabinet_we(3, 5)

        level.add_phone_pair(4, 2, 6, 2)

        level.add_cop(6, 0, DIR_S)
        level.add_cop(4, 5, DIR_N)
        level.add_victim(6, 5)

        return level

    @staticmethod
    def s3_s15():

        level = Level('Slayaway Camp 3, Scene 15 - Cats Can\'t Get Wet!', 8, 7,
            4, 6,
            1, 4)

        level.wall_west(1, 0)
        level.wall_east(1, 0)
        level.wall_west(1, 1)
        level.wall_east(1, 1)
        level.wall_south(1, 1)

        level.wall_south(4, 1)
        level.wall_east(6, 3)
        level.wall_east(4, 4)

        level.wall_box(4, 0)
        level.wall_box(6, 0)
        level.wall_box(2, 4)
        level.wall_box(0, 6)
        level.wall_box(7, 6)

        level.set_hazard(5, 0)
        for y in range(6):
            level.set_hazard(0, y)
            level.set_hazard(7, y)

        level.add_victim(3, 5)
        level.add_victim(4, 5)
        level.add_cat(1, 5)
        level.add_cat(5, 5)

        return level

    @staticmethod
    def s3_s16():

        # More exit-fudging here.

        level = Level('Slayaway Camp 3, Scene 16 - Crazy Coaster', 8, 8,
            6, 2,
            2, 6)

        level.wall_south(0, 0)
        level.wall_south(1, 0)
        level.wall_south(3, 0)
        level.wall_south(5, 0)
        level.wall_south(6, 0)
        level.wall_south(7, 0)
        level.wall_west(2, 0)
        level.wall_east(2, 0)

        level.wall_box(4, 1)
        level.wall_box(0, 2)
        level.wall_box(1, 2)
        level.wall_box(3, 2)
        level.wall_box(0, 7)

        level.wall_west(6, 7)
        level.wall_north(6, 7)
        level.wall_west(7, 6)
        level.wall_north(7, 6)

        level.wall_west(2, 3)
        level.wall_east(2, 3)
        level.wall_east(4, 3)
        level.wall_east(3, 4)
        level.wall_east(2, 6)
        level.wall_north(4, 6)
        level.wall_north(5, 6)

        level.set_hazard(2, 0)
        level.set_mine(0, 5)
        level.set_mine(2, 2)

        level.add_cabinet_ns(1, 4)
        level.add_cabinet_ns(6, 4)
        level.add_cabinet_ns(7, 4)

        level.add_victim(2, 1)
        level.add_victim(4, 5)
        level.add_victim(6, 5)

        return level

    @staticmethod
    def s3_d1():

        # Current highlighting can't actually show that the exit is below one
        # of the gravestones (cabinets).  Whatever.

        level = Level('Slayaway Camp 3, Deleted Scene 1 - Poe\'s Puzzle', 8, 8,
            0, 0,
            5, 3)

        level.wall_west(6, 0)
        level.wall_south(6, 0)
        level.wall_south(7, 0)

        level.wall_west(6, 7)
        level.wall_north(6, 7)
        level.wall_north(7, 7)

        level.add_cabinet_we(1, 1)
        level.add_cabinet_we(3, 1)
        level.add_cabinet_ns(5, 1)
        level.add_cabinet_we(7, 1)

        level.add_cabinet_ns(1, 3)
        level.add_cabinet_ns(3, 3)
        level.add_cabinet_ns(5, 3)
        level.add_cabinet_ns(7, 3)

        level.add_cabinet_we(1, 5)
        level.add_cabinet_ns(3, 5)
        level.add_cabinet_we(5, 5)
        level.add_cabinet_ns(7, 5)

        level.add_victim(2, 3)
        level.add_victim(6, 4)
        level.add_victim(2, 6)

        return level

    @staticmethod
    def s3_d2():

        level = Level('Slayaway Camp 3, Deleted Scene 2 - Meow Maze', 6, 6,
            0, 5,
            3, 5)

        level.wall_south(2, 0)
        level.wall_east(2, 0)
        level.wall_east(4, 0)
        level.wall_east(0, 1)
        level.wall_south(3, 1)
        level.wall_south(5, 1)
        level.wall_east(1, 2)
        level.wall_south(2, 3)
        level.wall_east(3, 3)
        level.wall_east(4, 3)
        level.wall_east(0, 4)
        level.wall_east(3, 4)
        level.wall_south(4, 4)
        level.wall_east(2, 5)

        level.set_mine(5, 1)

        level.add_victim(2, 0)
        level.add_victim(4, 2)
        level.add_cat(3, 1)
        level.add_cat(0, 3)
        level.add_cat(5, 5)

        return level

    @staticmethod
    def s3_d3():

        level = Level('Slayaway Camp 3, Deleted Scene 3 - Don\'t Squish the Kittens', 8, 8,
            3, 4,
            0, 0)

        level.wall_south(7, 1)
        level.wall_south(4, 5)
        level.wall_west(1, 7)
        level.wall_north(1, 7)
        level.wall_north(2, 7)
        level.wall_east(2, 7)

        level.wall_box(6, 5)
        level.wall_box(7, 7)

        level.set_hazard(3, 0)
        level.set_hazard(4, 0)
        level.set_hazard(5, 0)
        level.set_hazard(6, 0)
        level.set_hazard(7, 0)
        level.set_hazard(7, 1)

        level.add_cabinet_we(1, 0)
        level.add_cabinet_we(3, 2)
        level.add_cabinet_ns(5, 3)
        level.add_cabinet_ns(0, 4)
        level.add_cabinet_ns(1, 4)
        level.add_cabinet_we(1, 6)

        level.add_victim(3, 1)
        level.add_cat(2, 2)
        level.add_cat(0, 6)

        return level

    @staticmethod
    def s3_d4():

        level = Level('Slayaway Camp 3, Deleted Scene 4 - The Lone Flame', 8, 8,
            6, 3,
            1, 5)

        level.wall_east(0, 0)
        level.wall_east(0, 1)
        level.wall_east(0, 2)
        level.wall_south(0, 2)

        level.wall_west(7, 0)
        level.wall_west(7, 1)
        level.wall_west(7, 2)
        level.wall_west(7, 3)
        level.wall_west(7, 4)
        level.wall_south(7, 4)

        level.wall_west(2, 5)
        level.wall_north(2, 5)
        level.wall_north(3, 5)
        level.wall_south(3, 5)
        level.wall_east(3, 5)
        level.wall_west(2, 6)
        level.wall_south(2, 6)
        level.wall_east(2, 6)
        level.wall_south(3, 6)

        level.wall_west(5, 7)
        level.wall_north(5, 7)
        level.wall_north(6, 7)
        level.wall_east(6, 7)

        level.wall_box(2, 1)
        level.wall_south(3, 1)
        level.wall_east(3, 0)

        level.wall_west(3, 3)
        level.wall_north(4, 3)
        level.wall_east(4, 3)

        level.set_hazard(4, 3)

        level.add_cop(3, 6, DIR_E)
        level.add_cop(7, 6, DIR_W)

        level.add_victim(3, 3)
        level.add_victim(4, 4)
        level.add_victim(4, 7)
        level.add_victim(7, 7)

        return level

    @staticmethod
    def s3_d5():

        level = Level('Slayaway Camp 3, Deleted Scene 5 - Cornered', 8, 8,
            4, 1,
            0, 7)

        level.wall_east(4, 0)
        level.wall_south(6, 0)
        level.wall_south(0, 1)
        level.wall_east(2, 1)
        level.wall_south(5, 1)
        level.wall_east(6, 1)
        level.wall_south(7, 2)
        level.wall_south(2, 3)
        level.wall_south(4, 3)
        level.wall_east(5, 3)
        level.wall_south(6, 3)
        level.wall_south(1, 4)
        level.wall_east(4, 4)
        level.wall_east(6, 4)
        level.wall_east(0, 5)
        level.wall_east(2, 5)
        level.wall_south(4, 6)
        level.wall_south(6, 6)

        level.set_mine(3, 3)
        level.set_mine(1, 4)
        level.set_mine(5, 5)
        level.set_mine(7, 7)

        level.add_cabinet_ns(2, 6)
        level.add_cabinet_we(1, 7)

        level.add_victim(7, 4)
        level.add_victim(0, 7)
        level.add_victim(6, 7)

        return level

    @staticmethod
    def s4_s01():

        level = Level('Slayaway Camp 4, Scene 1 - Short Walls Don\'t Hide You!', 6, 6,
            0, 3,
            0, 0)

        level.wall_south(0, 1)
        level.wall_south(1, 1)
        level.wall_east(2, 0)

        level.wall_west(4, 3)
        level.wall_north(4, 3)
        level.wall_east(4, 3)
        level.wall_west(4, 4)
        level.wall_east(4, 4)
        level.wall_west(4, 5)
        level.wall_east(4, 5)

        level.wall_box(0, 2)
        level.wall_box(0, 4)

        level.short_wall_east(1, 2)
        level.short_wall_east(1, 3)
        level.short_wall_east(1, 4)

        level.short_wall_south(3, 3)

        level.add_victim(2, 3)

        return level

    @staticmethod
    def s4_s02():

        level = Level('Slayaway Camp 4, Scene 2 - Antagonizing the Enemy', 6, 7,
            0, 5,
            4, 2)

        level.wall_south(0, 0)
        level.wall_west(1, 1)
        level.wall_south(1, 1)
        level.wall_south(2, 1)
        level.wall_east(2, 1)
        level.wall_east(2, 0)

        level.wall_west(4, 0)
        level.wall_west(4, 1)
        level.wall_south(4, 1)
        level.wall_west(5, 2)
        level.wall_north(4, 3)
        level.wall_west(4, 3)
        level.wall_south(4, 3)
        level.wall_west(5, 4)
        level.wall_south(5, 4)

        level.wall_box(0, 6)
        level.wall_box(5, 6)

        level.wall_south(2, 3)
        level.short_wall_south(1, 3)
        level.short_wall_east(2, 5)

        level.add_phone_pair(1, 6, 3, 0)

        level.set_mine(5, 5)

        level.add_cabinet_we(3, 4)

        level.add_cop(1, 2, DIR_W)

        level.add_victim(0, 1)
        level.add_victim(3, 5)

        return level

    @staticmethod
    def s4_s03():

        level = Level('Slayaway Camp 4, Scene 3 - Locker Room Rampage', 6, 8,
            1, 6,
            4, 5)

        level.wall_north(5, 6)
        level.wall_west(5, 6)
        level.wall_west(5, 7)

        level.wall_west(4, 0)
        level.wall_west(4, 1)
        level.wall_west(4, 2)
        level.wall_south(4, 2)
        level.wall_south(5, 3)

        level.wall_box(3, 6)

        level.wall_east(0, 0)
        level.wall_south(2, 1)
        level.wall_east(1, 5)

        level.set_mine(0, 5)

        level.add_phone_pair(0, 0, 1, 3)

        level.add_cop(5, 3, DIR_W)
        level.add_victim(5, 0)
        level.add_victim(4, 4)
        level.add_cat(0, 3)

        return level

    @staticmethod
    def s4_s04():

        level = Level('Slayaway Camp 4, Scene 4 - Cafeteria Calamity', 8, 7,
            0, 3,
            0, 0)

        level.wall_box(7, 6)

        level.wall_north(0, 5)
        level.wall_east(1, 6)

        level.wall_north(1, 1)
        level.wall_east(1, 1)
        level.wall_east(1, 2)

        level.wall_north(3, 1)
        level.wall_west(3, 1)
        level.wall_east(3, 1)
        level.wall_west(3, 2)
        level.wall_east(3, 2)

        level.wall_west(5, 1)
        level.wall_east(5, 1)
        level.wall_west(5, 2)
        level.wall_east(5, 2)

        level.short_wall_south(0, 0)

        level.short_wall_west(2, 3)
        level.short_wall_south(2, 3)
        level.short_wall_south(3, 3)
        level.short_wall_south(4, 3)
        level.short_wall_south(5, 3)
        level.short_wall_east(5, 3)

        level.short_wall_east(6, 4)
        level.short_wall_south(6, 4)
        level.short_wall_west(6, 5)

        level.set_mine(2, 0)
        level.set_mine(4, 0)
        level.set_mine(5, 0)

        level.add_victim(2, 3)
        level.add_victim(3, 4)
        level.add_victim(5, 3)

        return level

    @staticmethod
    def s4_s05():

        level = Level('Slayaway Camp 4, Scene 5 - Principal\'s Office', 6, 6,
            4, 5,
            0, 3)

        level.wall_box(5, 0)
        level.wall_box(0, 5)

        level.wall_south(0, 2)
        level.wall_south(1, 2)
        level.wall_east(1, 4)
        level.wall_south(3, 4)
        level.wall_east(4, 3)
        level.wall_south(4, 3)

        level.escape_north(2)
        level.escape_north(3)
        level.escape_west(1)
        level.escape_west(2)

        level.add_victim(3, 0)
        level.add_victim(2, 1)
        level.add_victim(2, 2)

        return level

    @staticmethod
    def s4_s06():

        level = Level('Slayaway Camp 4, Scene 6 - Sneaky Science Lab Slasher', 6, 6,
            3, 5,
            0, 5)

        level.wall_south(0, 2)
        level.wall_east(0, 2)
        level.wall_east(0, 1)
        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_south(3, 0)
        level.wall_south(4, 0)
        level.wall_east(4, 0)

        level.wall_north(4, 3)
        level.wall_west(4, 3)
        level.wall_north(3, 3)
        level.wall_north(2, 3)
        level.wall_west(2, 3)
        level.wall_west(2, 4)
        level.wall_south(2, 4)
        level.wall_south(3, 4)
        level.wall_south(4, 4)
        level.wall_east(4, 4)
        level.wall_north(4, 4)

        level.escape_north(5)

        level.add_cop(4, 3, DIR_E)
        level.add_victim(1, 2)
        level.add_victim(2, 1)
        level.add_victim(5, 4)

        return level

    @staticmethod
    def s4_s07():

        level = Level('Slayaway Camp 4, Scene 7 - Changeroom Challenge', 7, 7,
            4, 5,
            5, 4)

        level.wall_south(0, 4)
        level.wall_south(1, 4)
        level.wall_east(1, 4)
        level.wall_north(1, 4)
        level.wall_east(0, 3)
        level.wall_east(0, 2)
        level.wall_east(0, 1)
        level.wall_east(0, 0)

        level.wall_north(0, 6)
        level.wall_north(1, 6)
        level.wall_east(1, 6)

        level.wall_west(3, 6)
        level.wall_north(3, 6)
        level.wall_north(4, 6)
        level.wall_north(5, 6)
        level.wall_north(6, 6)

        level.wall_east(4, 0)
        level.wall_south(1, 1)
        level.wall_east(2, 4)
        level.wall_north(4, 4)

        level.short_wall_west(3, 2)
        level.short_wall_south(3, 2)

        level.short_wall_north(5, 2)
        level.wall_east(5, 2)

        level.escape_north(3)
        level.escape_west(5)

        level.add_victim(3, 2)
        level.add_victim(2, 5)

        return level

    @staticmethod
    def s4_s08():

        level = Level('Slayaway Camp 4, Scene 8 - Gym Shorts', 8, 8,
            7, 1,
            0, 5)

        level.wall_box(1, 1)
        level.wall_box(5, 3)
        level.wall_box(0, 6)
        level.wall_box(5, 1)
        level.wall_box(6, 1)
        level.wall_box(2, 2)
        level.wall_box(3, 2)
        level.wall_box(0, 4)
        level.wall_box(1, 4)

        level.wall_north(3, 4)
        level.wall_west(3, 4)
        level.wall_east(3, 4)
        level.wall_west(3, 5)
        level.wall_east(3, 5)
        level.wall_west(3, 6)
        level.wall_east(3, 6)
        level.wall_south(3, 6)

        level.wall_west(5, 6)
        level.wall_north(5, 6)
        level.wall_south(5, 6)
        level.wall_south(6, 6)
        level.wall_east(6, 6)
        level.wall_east(6, 5)
        level.wall_north(6, 5)
        level.wall_west(6, 5)

        level.escape_west(7)

        level.add_cabinet_we(4, 0)
        level.add_cabinet_we(6, 2)
        level.add_cabinet_we(2, 3)
        level.add_cabinet_ns(4, 3)
        level.add_cabinet_ns(7, 3)
        level.add_cabinet_we(3, 7)
        level.add_cabinet_we(5, 7)

        level.add_victim(1, 7)
        level.add_victim(6, 7)

        return level

    @staticmethod
    def s4_s09():

        level = Level('Slayaway Camp 4, Scene 9 - Bomb Disposal Protocol', 8, 8,
            0, 7,
            1, 5)

        level.wall_west(7, 0)
        level.wall_west(7, 1)
        level.wall_west(7, 2)
        level.wall_west(7, 3)
        level.wall_west(7, 4)
        level.wall_south(7, 4)

        level.wall_south(0, 1)
        level.wall_east(1, 1)
        level.wall_east(2, 5)
        level.wall_east(2, 6)
        level.wall_south(4, 5)
        level.wall_south(5, 5)
        level.wall_south(6, 5)

        level.wall_box(5, 7)

        level.short_wall_west(3, 2)
        level.short_wall_north(3, 2)
        level.short_wall_north(4, 2)
        level.short_wall_east(4, 2)
        level.short_wall_east(4, 3)
        level.short_wall_south(4, 3)
        level.short_wall_south(3, 3)
        level.short_wall_west(3, 3)

        level.set_mine(4, 2)

        level.add_cop(2, 1, DIR_S)
        level.add_cop(5, 1, DIR_S)
        level.add_cop(2, 4, DIR_E)

        level.add_victim(1, 2)
        level.add_victim(6, 1)
        level.add_victim(3, 3)
        level.add_victim(2, 7)

        return level

    @staticmethod
    def s4_s10():

        level = Level('Slayaway Camp 4, Scene 10 - Bathroom Flood', 8, 8,
            3, 5,
            4, 5)

        level.wall_box(0, 0)
        level.wall_box(0, 7)

        level.set_hazard(7, 7)
        for x in range(1, 8):
            level.set_hazard(x, 0)

        level.short_wall_west(2, 2)
        level.short_wall_north(2, 2)
        level.short_wall_north(3, 2)
        level.short_wall_north(4, 2)
        level.short_wall_north(5, 2)
        level.short_wall_east(5, 2)
        level.short_wall_east(5, 3)
        level.short_wall_north(6, 4)
        level.short_wall_east(6, 4)
        level.short_wall_north(7, 5)
        level.short_wall_south(7, 5)
        level.short_wall_south(6, 5)
        level.short_wall_east(5, 6)
        level.short_wall_south(5, 6)
        level.short_wall_south(4, 6)
        level.short_wall_south(3, 6)
        level.short_wall_south(2, 6)
        level.short_wall_west(2, 6)
        level.short_wall_south(1, 5)
        level.short_wall_west(1, 5)
        level.short_wall_west(1, 4)
        level.short_wall_north(1, 4)
        level.short_wall_north(2, 4)
        level.short_wall_west(2, 3)

        level.short_wall_east(3, 5)

        level.add_victim(3, 1)
        level.add_victim(6, 3)
        level.add_victim(7, 4)
        level.add_victim(6, 6)
        level.add_cat(1, 3)

        return level

    @staticmethod
    def s4_s11():

        level = Level('Slayaway Camp 4, Scene 11 - Wood Shop Wipeout', 7, 7,
            3, 3,
            6, 2)

        level.wall_east(0, 0)
        level.wall_east(0, 1)
        level.wall_east(0, 2)
        level.wall_east(0, 3)
        level.wall_south(0, 3)

        level.wall_west(2, 0)
        level.wall_south(2, 0)
        level.wall_west(3, 1)
        level.wall_south(3, 1)
        level.wall_east(3, 1)
        level.wall_south(4, 0)
        level.wall_south(5, 0)
        level.wall_south(6, 0)

        level.wall_north(5, 3)
        level.wall_west(5, 3)
        level.wall_east(5, 3)
        level.wall_west(5, 4)
        level.wall_east(5, 4)
        level.wall_south(5, 4)

        level.wall_west(1, 6)
        level.wall_north(1, 6)
        level.wall_north(2, 6)
        level.wall_north(3, 6)
        level.wall_east(3, 6)

        level.short_wall_east(2, 3)
        level.short_wall_east(4, 6)

        level.escape_north(1)

        level.add_cop(2, 3, DIR_N)
        level.add_victim(1, 2)
        level.add_victim(4, 2)
        level.add_victim(4, 6)
        
        return level

    @staticmethod
    def s4_s12():

        # As with the other ending levels, we fudge the exit point here, which
        # isn't actually shown in the game.

        level = Level('Slayaway Camp 4, Scene 12 - Scare the Metalshop Guy', 8, 8,
            6, 4,
            6, 2)

        level.wall_box(1, 6)

        level.wall_south(0, 4)
        level.wall_east(2, 7)
        level.wall_south(5, 6)

        level.short_wall_north(6, 1)
        level.short_wall_east(6, 1)

        level.wall_south(1, 2)
        level.wall_west(1, 2)
        level.wall_north(1, 2)
        level.wall_north(2, 2)
        level.wall_north(3, 2)
        level.wall_north(4, 2)
        level.wall_east(4, 2)
        level.wall_south(4, 2)
        level.wall_south(3, 2)
        level.wall_east(2, 3)
        level.wall_south(2, 3)
        level.wall_west(2, 3)

        level.short_wall_north(5, 2)
        level.short_wall_west(2, 4)
        level.short_wall_south(2, 4)
        level.short_wall_south(3, 4)
        level.short_wall_south(4, 4)
        level.short_wall_south(5, 4)
        level.short_wall_east(5, 4)
        level.short_wall_east(5, 3)
        level.short_wall_east(5, 5)

        level.escape_west(1)
        level.escape_west(5)

        level.add_cabinet_we(4, 0)
        level.add_cabinet_ns(7, 6)

        level.add_victim(3, 1)
        level.add_victim(2, 4)
        level.add_victim(5, 5)
        level.add_victim(6, 6)

        return level

    @staticmethod
    def s4_d1():

        level = Level('Slayaway Camp 4, Deleted Scene 1 - Fine Art Fatalities', 6, 8,
            2, 4,
            3, 3,
            7)

        level.wall_west(1, 0)
        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_south(3, 0)
        level.wall_south(4, 0)
        level.wall_south(5, 0)

        level.wall_north(5, 2)
        level.wall_west(5, 2)
        level.wall_west(5, 3)
        level.wall_west(5, 4)
        level.wall_west(5, 5)
        level.wall_west(5, 6)
        level.wall_north(4, 7)
        level.wall_north(3, 7)
        level.wall_west(3, 7)

        level.wall_north(0, 7)
        level.wall_north(1, 7)
        level.wall_east(1, 7)

        level.short_wall_south(1, 1)
        level.short_wall_east(0, 4)
        level.short_wall_east(0, 5)

        level.set_hazard(0, 0)
        level.set_hazard(5, 1)

        level.add_cabinet_ns(2, 6)

        level.add_victim(3, 1)
        level.add_victim(0, 5)

        return level

    @staticmethod
    def s4_d2():

        level = Level('Slayaway Camp 4, Deleted Scene 2 - Pool Party', 8, 8,
            1, 6,
            5, 2)

        level.short_wall_east(0, 1)
        level.short_wall_east(6, 1)
        level.short_wall_south(6, 6)

        level.short_wall_west(2, 5)
        level.short_wall_west(2, 4)
        level.short_wall_west(2, 3)
        level.short_wall_west(2, 2)
        level.short_wall_north(2, 2)
        level.short_wall_north(3, 2)
        level.short_wall_north(4, 2)
        level.short_wall_north(5, 2)
        level.short_wall_east(5, 2)
        level.short_wall_east(5, 3)
        level.short_wall_east(5, 4)
        level.short_wall_east(5, 5)
        level.short_wall_south(5, 5)
        level.short_wall_south(4, 5)
        level.short_wall_south(3, 5)
        level.short_wall_west(3, 6)

        level.set_hazard(3, 3)
        level.set_hazard(3, 4)
        level.set_hazard(4, 3)
        level.set_hazard(4, 4)

        level.add_victim(2, 0)
        level.add_victim(3, 0)
        level.add_victim(1, 2)
        level.add_victim(0, 6)
        level.add_cat(2, 2)

        return level

    @staticmethod
    def s4_d3():

        level = Level('Slayaway Camp 4, Deleted Scene 3 - One Mine at a Time', 8, 8,
            4, 5,
            7, 3)

        level.wall_east(0, 0)
        level.wall_east(0, 1)
        level.wall_east(0, 2)
        level.wall_south(0, 2)

        level.wall_west(7, 0)
        level.wall_west(7, 1)
        level.wall_south(7, 1)

        level.wall_north(0, 7)
        level.wall_north(1, 7)
        level.wall_east(1, 7)

        level.wall_east(2, 0)
        level.wall_east(4, 1)
        level.wall_east(0, 4)
        level.wall_east(0, 5)
        level.wall_east(0, 6)
        level.wall_south(4, 4)
        level.wall_south(3, 5)

        level.wall_box(2, 4)
        level.wall_box(5, 2)
        level.wall_box(7, 7)

        level.set_mine(0, 6)
        level.set_mine(2, 0)
        level.set_mine(5, 4)

        level.add_victim(0, 4)
        level.add_victim(4, 2)
        level.add_victim(2, 6)

        return level

    @staticmethod
    def s4_d4():

        level = Level('Slayaway Camp 4, Deleted Scene 4 - Phone in Box', 7, 7,
            4, 3,
            3, 3)

        level.short_wall_west(2, 1)
        level.short_wall_south(2, 1)
        level.short_wall_south(3, 1)
        level.short_wall_south(4, 1)
        level.short_wall_east(4, 1)

        level.short_wall_west(2, 2)
        level.short_wall_west(2, 3)
        level.short_wall_west(2, 4)

        level.short_wall_east(4, 2)
        level.short_wall_east(4, 3)
        level.short_wall_east(4, 4)

        level.short_wall_west(2, 5)
        level.short_wall_north(2, 5)
        level.short_wall_north(3, 5)
        level.short_wall_north(4, 5)
        level.short_wall_east(4, 5)

        level.set_hazard(0, 3)
        level.set_hazard(1, 6)
        level.set_hazard(5, 3)

        level.add_phone_pair(0, 6, 2, 2)
        level.add_phone_pair(4, 2, 6, 0)
        level.add_phone_pair(3, 4, 5, 5)

        level.add_victim(0, 0)
        level.add_victim(5, 2)
        level.add_victim(2, 5)
        level.add_victim(6, 6)
        level.add_cat(0, 2)
        level.add_cat(1, 4)
        level.add_cat(4, 5)

        return level

    @staticmethod
    def s4_d5():

        level = Level('Slayaway Camp 4, Deleted Scene 5 - Library Lacerations', 9, 9,
            0, 8,
            4, 2)

        level.wall_box(0, 0)
        level.wall_box(8, 8)

        level.wall_west(4, 0)
        level.wall_east(4, 0)
        level.wall_south(6, 0)
        level.wall_south(7, 0)
        level.wall_east(4, 1)
        level.wall_east(7, 1)
        level.wall_south(1, 2)
        level.wall_east(2, 2)
        level.wall_south(4, 2)
        level.wall_south(7, 2)
        level.wall_south(0, 3)
        level.wall_east(4, 3)
        level.wall_east(7, 3)
        level.wall_east(6, 4)
        level.wall_east(2, 5)
        level.wall_south(4, 5)
        level.wall_south(6, 5)
        level.wall_east(7, 5)
        level.wall_east(0, 6)
        level.wall_south(2, 6)
        level.wall_south(0, 7)
        level.wall_south(1, 7)
        level.wall_east(5, 7)

        level.set_hazard(3, 1)
        level.set_hazard(5, 2)
        level.set_hazard(3, 8)

        level.add_cabinet_we(2, 1)
        level.add_cabinet_ns(5, 1)
        level.add_cabinet_we(2, 8)

        level.add_victim(4, 0)

        return level

    @staticmethod
    def s5_s01():

        level = Level('Slayaway Camp 5, Scene 1 - Introducing: SWAT Cops', 8, 6,
            0, 5,
            5, 0)

        level.wall_south(0, 2)
        level.wall_east(0, 2)
        level.wall_east(0, 1)
        level.wall_south(1, 0)
        level.wall_east(1, 0)

        level.wall_west(6, 0)
        level.wall_west(6, 1)
        level.wall_south(6, 1)
        level.wall_south(7, 1)

        level.wall_box(2, 2)
        level.wall_box(4, 2)
        level.wall_box(3, 5)
        level.wall_box(5, 5)

        level.wall_south(2, 3)

        level.add_swat(1, 2, DIR_S)
        level.add_swat(7, 4, DIR_W)
        level.add_victim(5, 4)

        return level

    @staticmethod
    def s5_s02():

        level = Level('Slayaway Camp 5, Scene 2 - Sandy SWAT Sneak', 6, 6,
            1, 2,
            0, 0)

        level.wall_west(4, 0)
        level.wall_south(4, 0)
        level.wall_south(5, 0)

        level.wall_box(5, 4)

        level.wall_south(0, 1)
        level.wall_south(1, 3)
        level.wall_east(0, 5)
        level.wall_east(3, 3)

        level.add_swat(1, 0, DIR_E)
        level.add_swat(5, 2, DIR_S)
        level.add_victim(4, 1)

        return level

    @staticmethod
    def s5_s03():

        level = Level('Slayaway Camp 5, Scene 3 - Bloodbath Beach', 6, 6,
            5, 2,
            0, 3)

        level.wall_south(0, 0)
        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_east(2, 0)

        level.wall_west(4, 0)
        level.wall_west(4, 1)
        level.wall_south(4, 1)
        level.wall_south(5, 1)

        level.wall_box(0, 4)
        level.wall_box(5, 4)

        level.wall_north(2, 3)
        level.wall_west(2, 3)
        level.wall_east(2, 3)
        level.wall_west(2, 4)
        level.wall_east(2, 4)
        level.wall_south(2, 4)

        level.set_hazard(3, 5)

        level.escape_north(3)
        level.escape_west(5)

        level.add_swat(4, 3, DIR_W)
        level.add_victim(1, 1)
        level.add_victim(3, 4)
        level.add_victim(2, 5)

        return level

    @staticmethod
    def s5_s04():

        level = Level('Slayaway Camp 5, Scene 4 - Sinkhole of Doom', 8, 8,
            4, 1,
            1, 4)

        level.wall_box(0, 1)
        level.wall_box(0, 7)
        level.wall_box(7, 0)

        level.wall_west(5, 7)
        level.wall_north(5, 7)
        level.wall_north(6, 7)
        level.wall_north(7, 7)

        level.wall_south(4, 2)
        level.wall_south(5, 2)
        level.wall_east(6, 3)
        level.wall_east(6, 4)
        level.wall_east(2, 6)

        level.set_hazard(2, 3)

        level.add_swat(6, 0, DIR_W)
        level.add_swat(6, 2, DIR_S)
        level.add_cop(1, 3, DIR_N)
        level.add_victim(0, 0)
        level.add_victim(3, 2)
        level.add_victim(5, 3)
        level.add_victim(3, 5)

        return level

    @staticmethod
    def s5_s05():

        level = Level('Slayaway Camp 5, Scene 5 - Boom Beach', 8, 7,
            7, 3,
            7, 0)

        level.wall_box(1, 4)
        level.wall_box(1, 5)
        level.wall_box(4, 6)
        level.wall_box(7, 6)

        level.short_wall_south(0, 2)
        level.short_wall_south(3, 0)
        level.short_wall_south(5, 0)
        level.short_wall_west(3, 2)
        level.short_wall_east(3, 2)
        level.short_wall_east(4, 2)

        level.short_wall_west(1, 1)
        level.short_wall_south(1, 1)
        level.short_wall_west(2, 2)
        level.short_wall_west(2, 3)
        level.short_wall_south(2, 3)
        level.short_wall_south(3, 3)
        level.short_wall_south(4, 3)
        level.short_wall_south(5, 3)
        level.short_wall_east(5, 3)
        level.short_wall_east(5, 2)
        level.short_wall_east(5, 1)
        level.short_wall_north(6, 1)
        level.short_wall_north(7, 1)

        level.set_mine(2, 0)
        level.set_mine(4, 0)
        level.set_mine(2, 2)

        level.add_victim(2, 3)
        level.add_victim(5, 3)
        level.add_victim(5, 5)

        return level


        return level

    @staticmethod
    def s5_s06():

        level = Level('Slayaway Camp 5, Scene 6 - Sand Castle Scarin\'', 6, 6,
            1, 5,
            4, 3)

        level.wall_box(1, 1)
        level.wall_box(5, 0)
        level.wall_box(0, 3)

        level.wall_west(3, 3)
        level.wall_west(3, 5)
        level.wall_north(4, 4)
        level.wall_east(4, 4)

        level.escape_north(3)
        level.escape_west(0)

        level.add_victim(1, 0)
        level.add_victim(3, 1)
        level.add_victim(3, 2)

        return level

    @staticmethod
    def s5_s07():

        level = Level('Slayaway Camp 5, Scene 7 - Deja Vu', 7, 7,
            5, 5,
            6, 0)

        level.short_wall_east(0, 5)
        level.short_wall_east(3, 6)

        level.short_wall_south(2, 3)
        level.short_wall_south(3, 3)
        level.short_wall_south(4, 3)
        level.short_wall_south(6, 3)

        level.short_wall_west(6, 0)
        level.short_wall_west(6, 1)
        level.short_wall_west(6, 2)

        level.short_wall_west(1, 3)
        level.short_wall_west(1, 2)
        level.short_wall_west(1, 1)
        level.short_wall_north(1, 1)
        level.short_wall_north(2, 1)
        level.short_wall_east(2, 1)
        level.short_wall_south(2, 1)
        level.short_wall_north(3, 1)
        level.short_wall_south(3, 1)
        level.short_wall_north(4, 1)
        level.short_wall_east(4, 1)
        level.short_wall_east(4, 2)

        level.set_mine(6, 1)

        level.add_cabinet_ns(1, 4)
        level.add_cabinet_ns(5, 3)

        level.add_victim(1, 3)
        level.add_victim(4, 3)

        return level

    @staticmethod
    def s5_s08():

        level = Level('Slayaway Camp 5, Scene 8 - Rearranger Dangers', 7, 7,
            6, 6,
            6, 2)

        level.wall_south(0, 0)
        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_east(2, 0)

        level.wall_west(4, 0)
        level.wall_south(4, 0)
        level.wall_west(5, 1)
        level.wall_south(5, 1)
        level.wall_south(6, 1)

        level.wall_box(3, 6)

        level.wall_south(1, 3)
        level.wall_south(2, 3)
        level.wall_west(6, 4)
        level.wall_west(6, 5)

        level.escape_north(3)
        level.escape_west(3)

        level.add_victim(2, 3)
        level.add_victim(3, 3)
        level.add_victim(3, 4)
        level.add_victim(4, 6)

        return level

    @staticmethod
    def s5_s09():

        level = Level('Slayaway Camp 5, Scene 9 - Cop Call Confusion', 7, 7,
            0, 2,
            5, 4)

        level.wall_box(0, 1)

        level.wall_north(0, 4)
        level.wall_east(0, 4)
        level.wall_east(0, 5)
        level.wall_north(1, 6)
        level.wall_east(1, 6)

        level.wall_west(4, 6)
        level.wall_north(4, 6)
        level.wall_north(5, 6)
        level.wall_north(6, 6)

        level.wall_west(4, 3)
        level.wall_north(4, 3)
        level.wall_south(4, 3)
        level.wall_north(5, 3)
        level.wall_south(5, 3)
        level.wall_east(5, 3)

        level.wall_west(2, 4)
        level.wall_south(2, 4)

        level.wall_south(2, 0)
        level.wall_south(3, 0)
        level.wall_south(5, 4)

        level.add_phone_pair(0, 0, 6, 5)
        level.add_phone_pair(2, 4, 3, 1)

        level.add_swat(4, 2, DIR_N)
        level.add_swat(4, 4, DIR_E)
        level.add_cop(1, 0, DIR_S)
        level.add_cop(2, 0, DIR_S)

        level.add_victim(5, 0)
        level.add_victim(6, 1)
        level.add_victim(3, 2)

        return level

    @staticmethod
    def s5_s10():

        level = Level('Slayaway Camp 5, Scene 10 - Nighttime on Fridge Beach', 7, 6,
            1, 4,
            3, 5,
            14)

        level.wall_box(2, 3)

        level.wall_north(4, 3)
        level.wall_west(4, 3)
        level.wall_east(4, 3)
        level.wall_west(4, 4)
        level.wall_east(4, 4)
        level.wall_south(4, 4)

        level.wall_south(5, 1)
        level.wall_south(1, 4)

        level.escape_north(3)

        level.add_cabinet_we(5, 0)
        level.add_cabinet_ns(0, 3)

        level.add_victim(1, 2)
        level.add_victim(3, 3)

        return level

    @staticmethod
    def s5_s11():

        level = Level('Slayaway Camp 5, Scene 11 - Cabana Carnage', 8, 7,
            1, 3,
            1, 1)

        level.wall_west(4, 0)
        level.wall_west(4, 1)
        level.wall_south(4, 1)
        level.wall_south(5, 1)
        level.wall_east(5, 1)
        level.wall_south(6, 0)
        level.wall_east(6, 0)

        level.wall_west(6, 6)
        level.wall_north(6, 6)
        level.wall_north(7, 6)

        level.wall_south(1, 0)
        level.wall_south(0, 2)
        level.wall_east(1, 3)
        level.wall_east(2, 6)

        level.wall_west(7, 2)
        level.wall_west(7, 3)
        level.wall_west(7, 4)

        level.escape_north(2)
        level.escape_west(5)

        level.set_mine(2, 6)

        level.add_swat(5, 4, DIR_W)
        level.add_swat(3, 6, DIR_N)

        level.add_victim(2, 1)
        level.add_victim(2, 5)
        level.add_victim(1, 6)
        level.add_victim(5, 5)

        return level

    @staticmethod
    def s5_s12():

        level = Level('Slayaway Camp 5, Scene 12 - Sandy Sophomore Sacrifices', 7, 7,
            1, 2,
            0, 1)

        level.wall_west(5, 5)
        level.wall_north(5, 5)
        level.wall_south(5, 5)
        level.wall_north(6, 5)
        level.wall_south(6, 5)

        level.wall_north(1, 1)
        level.wall_east(1, 1)
        level.wall_north(2, 1)
        level.wall_north(3, 1)
        level.wall_east(3, 1)
        level.wall_south(4, 1)

        level.wall_east(0, 2)
        level.wall_east(0, 3)

        level.wall_south(2, 2)
        level.wall_east(2, 2)

        level.wall_west(3, 4)
        level.wall_north(3, 4)

        level.wall_north(5, 3)
        level.wall_east(5, 3)

        level.set_mine(1, 6)
        level.set_mine(5, 6)

        level.add_victim(2, 3)
        level.add_victim(3, 5)
        level.add_victim(0, 6)
        level.add_victim(6, 6)

        return level

    @staticmethod
    def s5_s13():

        # The usual amount of exit shenanigans

        level = Level('Slayaway Camp 5, Scene 13 - Sharks and Lasers', 9, 9,
            3, 8,
            3, 7)

        level.wall_box(0, 0)
        level.wall_box(0, 8)

        level.wall_north(8, 7)
        level.wall_west(8, 7)
        level.wall_west(8, 8)

        level.wall_west(4, 7)
        level.wall_north(4, 7)
        level.wall_south(4, 7)
        level.wall_north(5, 7)
        level.wall_south(5, 7)
        level.wall_east(5, 7)

        level.wall_north(6, 6)
        level.short_wall_west(6, 6)

        level.short_wall_south(1, 2)
        level.short_wall_east(1, 2)

        level.short_wall_west(4, 1)
        level.short_wall_south(4, 1)
        level.short_wall_south(5, 1)
        level.short_wall_east(5, 2)

        level.short_wall_north(7, 1)
        level.short_wall_west(7, 1)
        level.short_wall_west(7, 2)
        level.short_wall_west(7, 3)

        level.set_hazard(3, 4)
        level.set_hazard(4, 4)
        level.set_hazard(3, 5)
        level.set_hazard(4, 5)

        level.add_cabinet_ns(8, 2)
        level.add_cabinet_ns(7, 3)

        level.add_swat(8, 1, DIR_W)
        level.add_swat(2, 4, DIR_E)
        level.add_swat(2, 6, DIR_E)
        level.add_cop(6, 0, DIR_S)

        level.add_victim(4, 1)
        level.add_victim(2, 2)
        level.add_victim(3, 6)

        return level

    @staticmethod
    def s5_d1():

        level = Level('Slayaway Camp 5, Deleted Scene 1 - Escape Routes', 8, 6,
            5, 3,
            0, 3)

        level.wall_east(2, 0)
        level.wall_south(0, 1)
        level.wall_south(1, 1)
        level.wall_south(7, 1)
        level.wall_east(1, 3)
        level.wall_east(1, 4)
        level.wall_east(5, 4)
        level.wall_east(5, 5)

        level.escape_north(3)
        level.escape_north(5)
        level.escape_west(1)
        level.escape_west(2)
        level.escape_west(5)

        level.add_victim(3, 1)
        level.add_victim(5, 1)
        level.add_victim(4, 2)
        level.add_cat(3, 5)

        return level

    @staticmethod
    def s5_d2():

        level = Level('Slayaway Camp 5, Deleted Scene 2 - My Summer Crush', 7, 8,
            5, 1,
            6, 5)

        level.wall_west(5, 7)
        level.wall_north(5, 7)
        level.wall_north(6, 7)

        level.wall_south(2, 0)
        level.wall_south(1, 1)
        level.wall_east(5, 1)
        level.wall_east(2, 2)
        level.wall_south(5, 2)
        level.wall_east(0, 3)
        level.wall_south(2, 3)
        level.wall_south(1, 4)
        level.wall_east(4, 5)
        level.wall_east(4, 6)

        level.short_wall_east(3, 0)
        level.short_wall_east(3, 1)

        level.add_cabinet_ns(0, 6)
        level.add_cabinet_we(5, 4)

        level.add_swat(6, 4, DIR_N)

        level.add_victim(4, 2)
        level.add_victim(6, 3)
        level.add_victim(1, 4)
        level.add_victim(1, 6)

        return level

    @staticmethod
    def s5_d3():

        level = Level('Slayaway Camp 5, Deleted Scene 3 - Island of Terror', 9, 8,
            3, 1,
            2, 3)

        for x in range(9):
            level.set_hazard(x, 0)
        for y in range(1, 8):
            level.set_hazard(0, y)
        for x in [1, 2, 4, 5, 6, 7, 8]:
            level.set_hazard(x, 7)
        level.set_hazard(8, 4)
        level.set_hazard(8, 5)
        level.set_hazard(8, 6)

        level.wall_west(1, 1)
        level.wall_north(1, 1)
        level.wall_south(1, 1)
        level.wall_north(2, 1)
        level.wall_south(2, 1)
        level.wall_east(2, 1)

        level.wall_west(6, 1)
        level.wall_north(6, 1)
        level.wall_south(6, 1)
        level.wall_north(7, 1)
        level.wall_south(7, 1)
        level.wall_north(8, 1)
        level.wall_south(8, 1)

        level.wall_box(1, 6)

        level.wall_west(5, 2)
        level.wall_east(5, 2)
        level.wall_south(8, 3)
        level.wall_east(3, 4)
        level.wall_south(5, 4)
        level.wall_south(6, 4)
        level.wall_west(1, 5)
        level.wall_east(7, 5)
        level.wall_south(5, 6)
        level.wall_east(5, 6)
        level.wall_south(6, 6)
        level.wall_south(7, 6)
        level.wall_east(7, 6)

        level.add_victim(2, 2)
        level.add_victim(5, 2)
        level.add_victim(4, 3)
        level.add_victim(3, 7)

        return level

    @staticmethod
    def s5_d4():

        level = Level('Slayaway Camp 5, Deleted Scene 4 - Stinky Sands Beach', 9, 9,
            0, 8,
            4, 4)

        level.wall_south(0, 1)
        level.wall_east(0, 1)
        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_east(2, 0)

        level.wall_box(7, 1)
        level.wall_box(3, 4)

        level.wall_east(1, 2)
        level.wall_south(1, 3)
        level.wall_east(7, 3)
        level.wall_east(5, 4)
        level.wall_south(6, 6)
        level.wall_east(3, 7)

        level.add_cabinet_we(2, 6)
        level.add_cabinet_ns(4, 6)
        level.add_cabinet_we(7, 6)

        level.add_victim(2, 5)
        level.add_victim(7, 5)

        return level

    @staticmethod
    def s6_s01():

        level = Level('Slayaway Camp 6, Scene 1 - Lights Out', 6, 6,
            0, 5,
            4, 3)

        level.wall_south(0, 1)
        level.wall_east(0, 1)
        level.wall_east(0, 0)

        level.wall_west(3, 0)
        level.wall_south(3, 0)
        level.wall_south(4, 0)
        level.wall_east(4, 1)
        level.wall_south(4, 1)
        level.wall_south(3, 1)
        level.wall_west(3, 2)
        level.wall_south(3, 2)
        level.wall_south(4, 2)
        level.wall_south(5, 2)

        level.wall_west(3, 5)
        level.wall_north(3, 5)
        level.wall_north(4, 5)
        level.wall_east(4, 5)

        level.wall_east(0, 3)
        level.wall_east(0, 4)
        level.wall_east(0, 5)

        level.switch_north(0, 2)

        level.add_swat(2, 2, DIR_S)
        level.add_cop(5, 3, DIR_S)
        level.add_victim(1, 5)

        return level

    @staticmethod
    def s6_s02():

        level = Level('Slayaway Camp 6, Scene 2 - SWAT Stealth Slash', 6, 6,
            2, 5,
            5, 1)

        level.wall_box(0, 0)
        level.wall_box(2, 2)
        level.wall_box(4, 4)

        level.wall_south(1, 2)
        level.wall_east(2, 0)
        level.wall_east(2, 1)
        level.wall_east(2, 5)

        level.switch_north(2, 0)

        level.add_swat(2, 3, DIR_E)
        level.add_swat(5, 2, DIR_W)
        level.add_victim(3, 1)

        return level

    @staticmethod
    def s6_s03():

        level = Level('Slayaway Camp 6, Scene 3 - Fatality Ward', 8, 8,
            0, 0,
            2, 1,
            10)

        level.wall_box(4, 7)
        level.wall_box(6, 2)
        
        level.wall_north(7, 6)
        level.wall_west(7, 6)
        level.wall_west(7, 7)

        level.wall_west(1, 2)
        level.wall_west(1, 1)
        level.wall_north(1, 1)
        level.wall_north(2, 1)
        level.wall_north(3, 1)
        level.wall_east(3, 1)
        level.wall_east(3, 2)

        level.wall_west(1, 4)
        level.wall_west(1, 5)
        level.wall_south(1, 5)
        level.wall_south(2, 5)

        level.wall_east(2, 4)

        level.wall_north(4, 5)
        level.wall_south(4, 5)
        level.wall_north(5, 5)
        level.wall_south(5, 5)
        level.wall_north(6, 5)
        level.wall_north(7, 5)

        level.add_cabinet_ns(3, 5)

        level.add_victim(7, 1)
        level.add_victim(6, 4)
        level.add_victim(5, 5)

        return level

    @staticmethod
    def s6_s04():

        level = Level('Slayaway Camp 6, Scene 4 - Kitty Care', 7, 6,
            5, 5,
            0, 3)

        level.wall_box(0, 0)
        level.wall_box(4, 0)
        level.wall_box(0, 5)
        level.wall_box(4, 5)

        level.wall_east(1, 1)
        level.wall_east(1, 2)
        level.wall_east(1, 3)

        level.wall_north(6, 3)
        level.wall_west(6, 3)
        level.wall_west(6, 4)
        level.wall_west(6, 5)

        level.escape_north(2)
        level.escape_west(4)

        level.switch_north(5, 0)

        level.add_victim(2, 1)
        level.add_victim(2, 5)
        level.add_cat(2, 3)

        return level

    @staticmethod
    def s6_s05():

        level = Level('Slayaway Camp 6, Scene 5 - A Phone in the Dark', 7, 6,
            1, 4,
            2, 0)

        level.wall_south(0, 2)
        level.wall_east(0, 2)
        level.wall_east(0, 1)
        level.wall_east(0, 0)

        level.wall_west(3, 0)
        level.wall_south(3, 0)
        level.wall_south(4, 0)
        level.wall_south(5, 0)
        level.wall_south(6, 0)

        level.wall_west(4, 3)
        level.wall_north(4, 3)
        level.wall_south(4, 3)
        level.wall_north(5, 3)
        level.wall_south(5, 3)
        level.wall_east(5, 3)

        level.wall_box(6, 5)

        level.short_wall_west(2, 0)
        level.short_wall_west(2, 1)
        level.short_wall_south(2, 1)
        level.short_wall_east(2, 2)

        level.switch_west(1, 1)

        level.add_phone_pair(6, 1, 5, 5)

        level.add_swat(4, 1, DIR_W)
        level.add_swat(2, 5, DIR_E)

        level.add_victim(1, 0)
        level.add_victim(3, 2)
        level.add_victim(0, 5)

        return level

    @staticmethod
    def s6_s06():

        level = Level('Slayaway Camp 6, Scene 6 - Visiting Hours', 7, 7,
            2, 4,
            4, 0)

        level.wall_east(0, 0)
        level.wall_east(0, 1)
        level.wall_east(0, 2)
        level.wall_east(0, 3)
        level.wall_south(0, 3)

        level.wall_north(0, 5)
        level.wall_east(0, 5)
        level.wall_north(1, 6)
        level.wall_north(2, 6)
        level.wall_east(2, 6)

        level.wall_south(5, 0)
        level.wall_south(6, 0)

        level.wall_east(3, 1)

        level.wall_east(5, 3)
        level.wall_east(5, 4)
        level.wall_south(5, 4)
        level.wall_south(4, 4)

        level.short_wall_west(2, 0)

        level.short_wall_west(2, 2)
        level.short_wall_west(2, 3)
        level.short_wall_south(2, 3)
        level.short_wall_south(3, 3)

        level.add_phone_pair(0, 4, 3, 1)

        level.add_swat(1, 1, DIR_S)

        level.add_victim(1, 0)
        level.add_victim(2, 1)
        level.add_victim(3, 5)

        return level

    @staticmethod
    def s6_s07():

        level = Level('Slayaway Camp 6, Scene 7 - No Escape', 8, 7,
            1, 5,
            1, 1)

        level.wall_north(2, 1)
        level.wall_west(2, 1)
        level.wall_east(2, 1)
        level.wall_west(2, 2)
        level.wall_east(2, 2)
        level.wall_south(2, 2)

        level.wall_north(5, 1)
        level.wall_west(5, 1)
        level.wall_east(5, 1)
        level.wall_west(5, 2)
        level.wall_east(5, 2)
        level.wall_south(5, 2)

        level.wall_north(0, 6)
        level.wall_north(1, 6)
        level.wall_east(1, 6)

        level.wall_box(7, 6)

        level.wall_east(3, 5)
        level.wall_east(5, 6)

        level.short_wall_south(1, 3)
        level.short_wall_south(2, 3)
        level.short_wall_south(3, 3)
        level.short_wall_south(4, 3)

        level.escape_north(3)
        level.escape_north(4)
        level.escape_west(3)

        level.add_cabinet_we(2, 0)
        level.add_cabinet_we(5, 0)

        level.set_hazard(2, 3)

        level.add_victim(3, 3)
        level.add_victim(4, 3)
        level.add_cat(1, 3)
        level.add_cat(6, 3)

        return level

    @staticmethod
    def s6_s08():

        level = Level('Slayaway Camp 6, Scene 8 - The Burn Ward', 8, 8,
            3, 4,
            7, 2)

        level.wall_north(0, 5)
        level.wall_east(0, 5)
        level.wall_south(1, 5)
        level.wall_east(0, 6)
        level.wall_east(0, 7)

        level.wall_box(7, 0)
        level.wall_box(7, 3)
        level.wall_box(5, 7)

        level.wall_south(4, 0)
        level.wall_east(4, 4)
        level.short_wall_east(2, 1)
        level.short_wall_east(2, 2)

        level.set_hazard(1, 1)
        level.switch_west(0, 0)

        level.add_swat(6, 0, DIR_W)
        level.add_swat(7, 1, DIR_N)

        level.add_victim(0, 3)
        level.add_victim(1, 3)
        level.add_victim(5, 3)
        level.add_cat(3, 2)

        return level

    @staticmethod
    def s6_s09():

        level = Level('Slayaway Camp 6, Scene 9 - Pre-Op Peril', 7, 7,
            4, 3,
            3, 4)

        level.wall_box(3, 5)
        level.wall_box(5, 4)
        level.wall_box(6, 6)

        level.wall_east(5, 0)
        level.wall_south(5, 0)
        level.wall_west(5, 1)
        level.wall_south(5, 1)
        level.wall_west(6, 2)
        level.wall_south(6, 2)

        level.wall_east(3, 2)
        level.wall_east(2, 4)

        level.switch_north(5, 0)

        level.add_phone_pair(0, 4, 1, 0)

        level.add_swat(2, 4, DIR_N)
        level.add_swat(2, 5, DIR_S)

        level.add_victim(1, 3)

        return level

    @staticmethod
    def s6_s10():

        level = Level('Slayaway Camp 6, Scene 10 - Dumcops in the Dark', 7, 7,
            1, 5,
            5, 6,
            10)

        level.wall_north(0, 5)
        level.wall_east(0, 5)
        level.wall_north(1, 6)
        level.wall_east(1, 6)

        level.wall_west(6, 0)
        level.wall_west(6, 1)
        level.wall_south(6, 1)

        level.short_wall_north(2, 1)
        level.short_wall_north(3, 1)
        level.short_wall_north(4, 1)
        level.short_wall_west(4, 1)

        level.short_wall_south(3, 4)
        level.short_wall_south(4, 4)

        level.short_wall_east(5, 3)
        level.short_wall_east(5, 4)
        level.short_wall_east(5, 5)

        level.switch_north(0, 0)
        level.switch_north(1, 0)

        level.set_mine(3, 2)
        level.set_mine(2, 3)
        level.set_mine(4, 3)
        level.set_mine(5, 1)

        level.add_phone_pair(3, 3, 5, 0)

        level.add_cop(6, 2, DIR_W)
        level.add_cop(2, 4, DIR_W)

        level.add_victim(3, 1)
        level.add_victim(2, 2)
        level.add_victim(5, 3)
        level.add_victim(5, 4)

        return level

    @staticmethod
    def s6_s11():

        level = Level('Slayaway Camp 6, Scene 11 - The Operating Doom', 7, 7,
            3, 2,
            0, 4)

        level.wall_box(4, 1)

        level.wall_south(0, 0)
        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_east(2, 0)

        level.wall_west(6, 0)
        level.wall_west(6, 1)
        level.wall_south(6, 1)

        level.wall_west(1, 2)
        level.wall_north(1, 2)
        level.wall_south(1, 2)
        level.wall_north(2, 2)
        level.wall_south(2, 2)
        level.wall_east(2, 2)

        level.wall_north(0, 6)
        level.wall_north(1, 6)
        level.wall_west(2, 5)
        level.wall_north(2, 5)
        level.wall_east(2, 5)
        level.wall_east(2, 6)

        level.wall_south(0, 3)
        level.wall_south(1, 3)
        level.wall_east(3, 3)
        level.wall_east(3, 4)
        level.wall_north(5, 3)
        level.wall_east(5, 3)

        level.short_wall_south(3, 5)
        level.short_wall_south(4, 5)
        level.short_wall_south(5, 5)
        level.short_wall_east(5, 5)

        level.add_cop(1, 3, DIR_E)
        level.add_victim(2, 4)
        level.add_victim(4, 4)

        return level

    @staticmethod
    def s6_s12():

        level = Level('Slayaway Camp 6, Scene 12 - Light vs. Dark', 8, 8,
            3, 0,
            4, 4)

        level.wall_east(0, 0)
        level.wall_east(0, 1)
        level.wall_south(0, 1)

        level.wall_north(0, 3)
        level.wall_east(0, 3)
        level.wall_north(1, 4)
        level.wall_east(1, 4)
        level.wall_east(1, 5)
        level.wall_south(1, 5)
        level.wall_east(0, 6)
        level.wall_east(0, 7)

        level.wall_west(4, 7)
        level.wall_north(4, 7)
        level.wall_north(5, 7)
        level.wall_east(5, 7)

        level.wall_east(6, 6)

        level.short_wall_east(6, 1)
        level.short_wall_east(6, 2)
        level.short_wall_south(6, 2)
        level.short_wall_south(5, 2)
        level.short_wall_west(5, 3)

        level.escape_north(5)
        level.escape_west(2)

        level.switch_west(2, 5)

        level.add_victim(5, 2)
        level.add_victim(6, 3)
        level.add_victim(2, 4)
        level.add_victim(5, 6)

        return level

    @staticmethod
    def s6_s13():

        # More fudging than usual on this one, actually.  In the game itself,
        # the victim at (4,1) isn't "real" and the game doesn't actually ever
        # let you kill him.  Instead, the victory condition is just reaching
        # the light switch at (6,0) - as soon as you do so, the conceit is that
        # you've turned off life support to (4,1) and he dies that way.  There
        # are a few ways I could support this scenario in the app, including
        # just putting some custom condition in place, but it's actually quite
        # easy to get to the victim and kill him normally after doing the switch,
        # so I figure I left that in.  The only real level modification I've done
        # here (apart from the usual explicit exit cell) is ensuring that the
        # victim at (4,1) is actually accessible (as opposed to enclosed within
        # 'walls' as he appears to be in the game).

        level = Level('Slayaway Camp 6, Scene 13 - Life Support (MODIFIED)', 8, 8,
            1, 0,
            4, 2)

        level.wall_south(1, 2)
        level.wall_east(2, 1)
        level.wall_east(2, 2)
        level.wall_north(3, 5)
        level.wall_east(3, 5)
        level.wall_south(7, 3)

        level.wall_north(0, 7)
        level.wall_north(1, 7)
        level.wall_east(1, 7)

        level.wall_west(4, 0)
        level.wall_west(4, 1)

        # Fudging here...
        #level.wall_south(4, 1)
        level.wall_north(4, 1)
        level.wall_east(4, 1)

        level.wall_west(4, 2)
        level.wall_east(4, 3)
        level.wall_east(5, 0)
        level.wall_east(5, 1)
        level.wall_east(5, 2)
        level.wall_west(5, 2)
        level.wall_south(5, 2)

        level.wall_box(7, 7)

        level.switch_north(6, 0)

        level.add_phone_pair(2, 7, 6, 7)

        level.add_cabinet_ns(0, 3)

        level.add_swat(7, 2, DIR_W)
        level.add_swat(4, 3, DIR_S)

        level.add_victim(2, 1)
        level.add_victim(4, 1)
        level.add_victim(6, 1)
        level.add_victim(5, 6)

        return level

    @staticmethod
    def s6_d1():

        level = Level('Slayaway Camp 6, Deleted Scene 1 - Fractured Instinct', 7, 7,
            0, 1,
            5, 3)

        level.wall_box(0, 0)

        level.wall_north(5, 4)
        level.wall_west(5, 4)
        level.wall_east(5, 4)
        level.wall_west(5, 5)
        level.wall_east(5, 5)
        level.wall_south(5, 5)

        level.wall_south(2, 0)
        level.wall_south(1, 1)
        level.wall_east(3, 1)
        level.wall_east(4, 1)
        level.wall_south(6, 1)
        level.wall_south(0, 2)
        level.wall_south(1, 2)
        level.wall_east(2, 2)
        level.wall_south(5, 2)
        level.wall_south(0, 3)
        level.wall_east(5, 3)
        level.wall_east(1, 4)

        level.set_mine(4, 3)

        level.switch_west(0, 6)

        level.add_swat(1, 3, DIR_E)
        level.add_swat(0, 5, DIR_S)
        level.add_swat(5, 6, DIR_W)

        level.add_victim(4, 2)
        level.add_victim(2, 3)
        level.add_victim(2, 6)

        return level

    @staticmethod
    def s6_d2():

        level = Level('Slayaway Camp 6, Deleted Scene 2 - Die-Chotomy.', 8, 6,
            0, 1,
            3, 1)

        level.wall_west(6, 5)
        level.wall_north(6, 5)
        level.wall_north(7, 5)

        level.wall_east(5, 0)
        level.wall_south(5, 1)
        level.wall_east(6, 1)
        level.wall_south(0, 3)
        level.wall_east(5, 3)
        level.wall_south(1, 4)
        level.wall_east(3, 5)

        level.short_wall_north(1, 1)
        level.short_wall_north(2, 1)
        level.short_wall_east(2, 1)
        level.short_wall_north(3, 1)
        level.short_wall_east(3, 1)
        level.short_wall_east(3, 2)
        level.short_wall_south(3, 2)
        level.short_wall_south(2, 2)
        level.short_wall_west(2, 2)
        level.short_wall_east(2, 3)

        level.switch_west(0, 4)
        level.switch_north(5, 2)

        level.set_mine(2, 1)

        level.add_victim(3, 2)
        level.add_victim(6, 2)

        return level

    @staticmethod
    def s6_d3():

        level = Level('Slayaway Camp 6, Deleted Scene 3 - Surgical Stealth', 8, 7,
            6, 3,
            2, 4)

        level.wall_box(0, 0)
        level.wall_box(4, 0)

        level.wall_west(1, 5)
        level.wall_north(1, 5)
        level.wall_south(1, 5)
        level.wall_north(2, 5)
        level.wall_south(2, 5)
        level.wall_east(2, 5)

        level.wall_south(6, 0)
        level.wall_south(7, 0)
        level.wall_south(7, 2)

        level.short_wall_south(1, 2)
        level.short_wall_south(1, 3)
        level.short_wall_north(3, 2)
        level.short_wall_west(3, 2)
        level.short_wall_south(4, 2)
        level.short_wall_north(5, 2)
        level.short_wall_east(5, 2)
        level.short_wall_east(5, 3)
        level.short_wall_west(4, 4)
        level.short_wall_south(4, 4)
        level.short_wall_south(6, 4)

        level.escape_west(3)
        level.escape_west(4)

        level.switch_north(1, 0)
        level.switch_north(7, 0)

        level.set_hazard(3, 5)
        level.set_hazard(4, 5)
        level.set_hazard(5, 5)

        level.add_swat(1, 3, DIR_W)
        level.add_cop(2, 0, DIR_W)
        level.add_cop(6, 0, DIR_E)
        level.add_victim(4, 1)
        level.add_victim(5, 2)
        level.add_victim(1, 4)
        level.add_cat(3, 3)

        return level

    @staticmethod
    def s6_d4():

        level = Level('Slayaway Camp 6, Deleted Scene 4 - Storage Room Squishes', 9, 9,
            8, 1,
            4, 4,
            13)

        # Custom map elements follow - walls.
        level.short_wall_east(1, 0)
        level.short_wall_east(4, 1)
        level.short_wall_south(2, 1)
        level.short_wall_east(5, 4)
        level.short_wall_south(5, 4)
        level.short_wall_south(1, 4)
        level.short_wall_south(7, 4)
        level.short_wall_east(0, 5)
        level.short_wall_east(6, 6)
        level.short_wall_south(8, 6)
        level.short_wall_south(6, 7)
        level.short_wall_south(7, 7)
        level.short_wall_east(5, 8)

        # Technically this is a box.  Call it a collection of short_walls
        level.short_wall_box(1, 7)

        # Cabinets
        level.add_cabinet_we(1, 2)
        level.add_cabinet_ns(4, 2)
        level.add_cabinet_we(6, 2)

        # Victims
        level.add_victim(1, 3)
        level.add_victim(6, 3)

        # Return
        return level

    @staticmethod
    def s7_s01():

        level = Level('Slayaway Camp 7, Scene 1 - Avoid the Electrical Fences!', 6, 6,
            3, 2,
            3, 5)

        level.wall_north(0, 2)
        level.wall_east(0, 2)
        level.wall_east(0, 3)
        level.wall_south(0, 3)

        level.wall_north(5, 2)
        level.wall_west(5, 2)
        level.wall_west(5, 3)
        level.wall_south(5, 3)

        level.electric_north(0, 0)
        level.electric_north(1, 0)
        level.electric_north(2, 0)
        level.electric_north(3, 0)
        level.electric_north(4, 0)

        level.electric_north(0, 5)
        level.electric_north(1, 5)
        level.short_wall_east(1, 5)

        level.short_wall_west(4, 5)
        level.electric_north(4, 5)
        level.electric_north(5, 5)

        level.wall_south(2, 0)

        level.add_victim(2, 0)

        return level

    @staticmethod
    def s7_s02():

        level = Level('Slayaway Camp 7, Scene 2 - Circuit Breaker', 6, 7,
            3, 5,
            4, 2)

        level.wall_south(0, 1)
        level.wall_east(0, 1)
        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_east(2, 0)

        level.wall_box(4, 1)

        level.electric_south(5, 2)

        level.electric_west(1, 4)
        level.electric_west(1, 5)
        level.electric_south(1, 5)
        level.electric_south(2, 5)
        level.electric_south(3, 5)

        level.electric_north(3, 0)
        level.electric_north(4, 0)

        level.switch_north(5, 0)

        level.add_victim(1, 1)
        level.add_victim(5, 4)

        return level

    @staticmethod
    def s7_s03():

        level = Level('Slayaway Camp 7, Scene 3 - Office Security', 7, 8,
            0, 5,
            3, 0)

        level.wall_west(2, 0)
        level.wall_west(2, 1)
        level.wall_south(2, 1)
        level.wall_south(1, 1)
        level.wall_south(0, 1)

        level.wall_east(4, 0)
        level.wall_east(4, 1)
        level.wall_south(4, 1)
        level.wall_south(5, 1)
        level.wall_south(6, 1)

        level.wall_north(0, 3)
        level.wall_east(0, 3)
        level.wall_east(0, 4)
        level.wall_south(0, 4)

        level.wall_north(0, 6)
        level.wall_east(0, 6)
        level.wall_east(0, 7)

        level.wall_north(6, 6)
        level.wall_west(6, 6)
        level.wall_west(6, 7)

        level.wall_box(5, 3)
        level.wall_box(4, 7)

        level.wall_north(2, 5)
        level.wall_east(3, 5)
        level.wall_west(3, 7)

        level.add_phone_pair(1, 3, 3, 7)
        level.add_phone_pair(6, 2, 6, 5)

        level.add_cop(2, 1, DIR_E)
        level.add_cop(4, 1, DIR_W)

        level.add_victim(0, 2)
        level.add_victim(3, 4)
        level.add_victim(4, 5)

        return level

    @staticmethod
    def s7_s04():

        level = Level('Slayaway Camp 7, Scene 4 - Copy Room Calamity', 8, 8,
            6, 3,
            1, 1)

        level.wall_north(0, 3)
        level.wall_east(0, 3)
        level.wall_north(1, 4)
        level.wall_south(1, 4)
        level.wall_east(0, 5)
        level.wall_east(0, 6)
        level.wall_east(0, 7)

        level.wall_east(2, 0)

        level.wall_south(6, 0)
        level.wall_south(7, 0)

        level.electric_north(0, 1)
        level.electric_north(1, 1)
        level.electric_east(1, 1)
        level.electric_south(1, 1)
        level.electric_north(2, 1)
        level.electric_north(3, 1)

        level.electric_west(2, 4)
        level.electric_south(2, 4)
        level.electric_south(4, 4)
        level.electric_south(6, 4)

        level.electric_south(3, 6)
        level.electric_south(4, 6)
        level.electric_south(5, 6)

        level.short_wall_east(5, 0)
        level.short_wall_east(5, 1)
        level.short_wall_south(7, 2)
        level.short_wall_north(3, 3)
        level.short_wall_east(3, 3)
        level.short_wall_east(6, 5)
        level.short_wall_west(2, 6)
        level.short_wall_south(2, 6)
        level.short_wall_south(6, 6)

        level.switch_north(4, 0)

        level.add_victim(4, 2)
        level.add_victim(3, 6)
        level.add_victim(5, 6)

        return level

    @staticmethod
    def s7_s05():

        level = Level('Slayaway Camp 7, Scene 5 - Administration Assassination', 8, 8,
            6, 7,
            4, 0,
            10)

        level.wall_south(0, 0)
        level.wall_south(1, 0)
        level.wall_east(1, 0)
        level.wall_south(2, 0)
        level.wall_south(3, 0)
        level.wall_south(6, 0)
        level.wall_south(1, 1)
        level.wall_south(2, 1)
        level.wall_east(3, 1)
        level.wall_east(4, 1)
        level.wall_east(6, 1)
        level.wall_east(0, 2)
        level.wall_south(2, 2)
        level.wall_south(4, 2)
        level.wall_east(4, 2)
        level.wall_east(5, 2)
        level.wall_south(4, 3)
        level.wall_east(2, 4)
        level.wall_east(3, 4)
        level.wall_south(6, 4)
        level.wall_south(4, 5)
        level.wall_east(6, 5)
        level.wall_east(2, 6)
        level.wall_south(4, 6)
        level.wall_south(5, 6)
        level.wall_east(6, 6)

        level.wall_north(0, 6)
        level.wall_north(1, 6)
        level.wall_east(1, 6)
        level.wall_east(1, 7)

        level.wall_box(1, 4)
        level.wall_box(7, 3)

        level.add_victim(3, 5)

        return level

    @staticmethod
    def s7_s06():

        level = Level('Slayaway Camp 7, Scene 6 - Involuntary Liquidation', 7, 7,
            1, 3,
            5, 2)

        level.wall_east(0, 0)
        level.wall_east(0, 1)
        level.wall_south(0, 1)

        level.wall_west(4, 0)
        level.wall_south(4, 0)
        level.wall_south(5, 0)
        level.wall_south(6, 0)

        level.wall_box(4, 2)

        level.wall_north(0, 6)
        level.electric_north(1, 6)
        level.wall_east(1, 6)

        level.wall_west(5, 6)
        level.wall_north(5, 6)
        level.wall_west(6, 5)
        level.wall_north(6, 5)

        level.electric_box(2, 4)

        level.electric_east(6, 3)
        level.electric_east(6, 4)

        level.escape_north(3)

        level.switch_north(4, 3)

        level.add_cabinet_ns(3, 4)

        level.add_victim(3, 1)
        level.add_victim(2, 2)
        level.add_victim(4, 4)

        return level

    @staticmethod
    def s7_s07():

        level = Level('Slayaway Camp 7, Scene 7 - The HR Department', 7, 8,
            2, 2,
            4, 0,
            9)

        level.wall_north(0, 6)
        level.wall_north(1, 6)
        level.wall_north(2, 6)
        level.wall_east(2, 6)
        level.wall_north(3, 7)
        level.wall_north(4, 7)
        level.wall_east(4, 7)

        level.short_wall_east(1, 0)
        level.short_wall_east(1, 1)

        level.wall_east(4, 0)
        level.wall_east(2, 1)
        level.wall_south(5, 1)
        level.wall_south(2, 3)
        level.wall_east(5, 3)
        level.wall_south(6, 5)

        level.set_mine(1, 4)

        level.add_phone_pair(0, 4, 5, 4)

        level.add_cop(4, 4, DIR_S)
        level.add_victim(1, 1)
        level.add_victim(5, 5)

        return level

    @staticmethod
    def s7_s08():

        level = Level('Slayaway Camp 7, Scene 8 - Executive Execution', 8, 7,
            5, 6,
            3, 4)

        level.wall_east(1, 0)
        level.wall_south(1, 0)
        level.wall_east(0, 1)
        level.wall_south(0, 1)

        level.wall_box(7, 0)
        level.wall_box(4, 4)
        level.wall_box(1, 5)
        level.wall_box(3, 6)

        level.wall_north(7, 3)
        level.wall_west(7, 3)
        level.wall_west(7, 4)
        level.wall_west(7, 5)
        level.wall_west(7, 6)

        level.electric_south(2, 0)
        level.electric_south(4, 0)
        level.electric_south(6, 0)

        level.short_wall_south(2, 1)
        level.wall_south(4, 1)
        level.short_wall_south(6, 1)

        level.wall_south(2, 2)
        level.short_wall_south(3, 2)
        level.short_wall_south(4, 2)
        level.short_wall_south(5, 2)
        level.electric_east(5, 2)

        level.short_wall_east(0, 3)
        level.short_wall_east(0, 4)
        level.short_wall_east(0, 5)

        level.add_swat(2, 0, DIR_S)
        level.add_swat(4, 0, DIR_S)
        level.add_swat(6, 0, DIR_S)

        level.add_victim(3, 2)
        level.add_victim(5, 2)
        level.add_victim(6, 4)

        return level

    @staticmethod
    def s7_s09():

        level = Level('Slayaway Camp 7, Scene 9 - Professional Misconduct', 8, 7,
            5, 3,
            1, 2)

        level.wall_box(1, 1)

        level.wall_north(2, 3)
        level.wall_west(2, 3)
        level.wall_east(2, 3)
        level.wall_west(2, 4)
        level.wall_east(2, 4)
        level.wall_south(2, 4)

        level.wall_north(7, 5)
        level.wall_west(7, 5)
        level.wall_west(7, 6)

        level.short_wall_north(2, 1)
        level.short_wall_north(3, 1)
        level.short_wall_north(4, 1)
        level.short_wall_north(5, 1)
        level.short_wall_east(5, 1)
        level.short_wall_east(5, 2)
        level.short_wall_south(5, 2)
        level.short_wall_south(4, 2)
        level.short_wall_south(3, 2)

        level.short_wall_west(1, 3)
        level.short_wall_west(1, 4)
        level.short_wall_west(1, 5)
        level.short_wall_south(1, 5)
        level.short_wall_south(2, 5)
        level.short_wall_south(3, 5)
        level.short_wall_south(4, 5)

        level.short_wall_south(3, 3)
        level.short_wall_south(4, 3)
        level.short_wall_east(6, 3)

        level.add_phone_pair(3, 0, 3, 3)

        level.add_swat(3, 1, DIR_S)
        level.add_cop(3, 5, DIR_N)

        level.add_victim(5, 2)
        level.add_victim(1, 6)

        return level

    @staticmethod
    def s7_s10():

        level = Level('Slayaway Camp 7, Scene 10 - Corporate Takedown', 8, 8,
            4, 3,
            1, 6)

        level.wall_box(1, 1)
        level.wall_box(0, 5)
        level.wall_south(2, 0)

        level.wall_west(6, 0)
        level.wall_south(6, 0)
        level.wall_west(7, 1)
        level.wall_south(7, 1)

        level.wall_north(4, 1)
        level.wall_west(4, 1)
        level.wall_east(4, 1)
        level.wall_west(4, 2)
        level.wall_east(4, 2)
        level.wall_south(4, 2)

        level.wall_east(2, 4)

        level.wall_west(1, 6)
        level.wall_north(1, 6)
        level.wall_west(2, 6)
        level.wall_north(2, 6)
        level.wall_east(2, 6)
        level.wall_east(3, 6)
        level.wall_east(4, 5)
        level.wall_east(4, 6)
        level.wall_east(5, 4)
        level.wall_east(5, 5)
        level.wall_east(5, 6)
        level.wall_north(6, 6)
        level.wall_east(6, 6)
        level.wall_north(7, 6)

        level.add_victim(2, 2)
        level.add_victim(6, 2)
        level.add_victim(6, 6)

        return level

    @staticmethod
    def s7_s11():

        level = Level('Slayaway Camp 7, Scene 11 - Supervisor Slaughter', 6, 8,
            0, 5,
            5, 7,
            13)

        level.wall_north(0, 6)
        level.wall_east(0, 6)
        level.wall_east(0, 7)

        level.wall_north(2, 2)
        level.switch_north(2, 2)

        level.wall_south(5, 2)

        level.wall_west(3, 5)
        level.switch_west(3, 5)

        level.wall_south(2, 6)
        level.wall_south(3, 6)
        level.wall_south(4, 6)

        level.add_swat(5, 4, DIR_W)
        level.add_swat(4, 6, DIR_N)
        level.add_victim(0, 0)
        level.add_victim(1, 1)
        level.add_victim(4, 3)

        return level

    @staticmethod
    def s7_s12():

        level = Level('Slayaway Camp 7, Scene 12 - Don\'t Zap the Cats!', 8, 8,
            4, 3,
            7, 0)

        level.wall_east(2, 0)
        level.wall_south(4, 0)
        level.wall_east(0, 1)
        level.wall_south(6, 1)
        level.wall_east(6, 3)
        level.wall_south(4, 4)
        level.wall_east(0, 5)
        level.wall_east(4, 5)
        level.wall_south(6, 5)
        level.wall_east(6, 5)
        level.wall_south(0, 6)
        level.wall_east(1, 6)

        level.switch_north(4, 5)

        level.electric_east(5, 1)
        level.electric_east(1, 2)
        level.electric_south(1, 3)
        level.electric_east(5, 4)
        level.electric_south(2, 5)
        level.electric_east(0, 7)

        level.add_victim(2, 1)
        level.add_victim(1, 5)
        level.add_victim(5, 7)
        level.add_cat(2, 2)
        level.add_cat(3, 6)

        return level

    @staticmethod
    def s7_s13():

        level = Level('Slayaway Camp 7, Scene 13 - Cabinet Crunch', 7, 7,
            5, 2,
            2, 2)

        level.wall_box(6, 0)
        level.wall_box(6, 6)

        level.short_wall_south(2, 0)
        level.short_wall_south(4, 0)
        level.short_wall_east(4, 1)
        level.short_wall_east(1, 2)
        level.short_wall_south(2, 2)
        level.short_wall_south(6, 2)
        level.short_wall_east(1, 3)
        level.short_wall_south(5, 3)
        level.short_wall_east(3, 4)
        level.short_wall_south(4, 4)
        level.short_wall_east(5, 4)
        level.short_wall_south(1, 5)
        level.short_wall_south(2, 5)
        level.short_wall_south(3, 5)
        level.short_wall_east(3, 5)

        level.escape_north(3)
        level.escape_west(5)

        level.set_mine(3, 3)

        level.add_cabinet_we(2, 0)
        level.add_cabinet_we(4, 0)
        level.add_cabinet_ns(0, 4)

        level.add_victim(3, 4)
        level.add_victim(3, 5)
        level.add_victim(3, 6)

        return level

    @staticmethod
    def s7_s14():

        # As usual, a bit of finagling with the exit.

        level = Level('Slayaway Camp 7, Scene 14 - Maximum Security', 7, 9,
            0, 0,
            3, 4)

        level.wall_west(2, 2)
        level.wall_north(2, 2)
        level.wall_north(3, 2)
        level.wall_north(4, 2)
        level.wall_east(4, 2)

        level.wall_west(6, 0)
        level.wall_west(6, 1)
        level.wall_west(6, 2)
        level.wall_west(6, 3)

        level.short_wall_west(1, 1)
        level.short_wall_west(1, 2)
        level.short_wall_west(1, 3)
        level.short_wall_south(1, 3)
        level.short_wall_south(2, 3)
        level.short_wall_south(3, 3)
        level.short_wall_south(4, 3)

        level.short_wall_east(0, 5)
        level.short_wall_east(0, 6)

        level.short_wall_east(1, 6)

        level.short_wall_south(3, 6)

        level.short_wall_east(5, 4)
        level.short_wall_east(5, 5)
        level.short_wall_east(5, 6)
        level.short_wall_south(5, 6)

        level.short_wall_south(0, 7)
        level.short_wall_east(4, 8)

        level.electric_south(2, 5)
        level.electric_west(2, 5)
        level.electric_west(2, 4)
        level.electric_west(2, 3)
        level.electric_north(2, 3)
        level.electric_north(3, 3)
        level.electric_north(4, 3)
        level.electric_east(4, 3)
        level.electric_east(4, 4)
        level.electric_east(4, 5)
        level.electric_south(4, 5)

        level.switch_north(5, 0)

        level.set_mine(6, 2)

        level.add_phone_pair(6, 0, 3, 8)

        level.add_swat(3, 4, DIR_S)
        level.add_swat(5, 6, DIR_W)
        level.add_swat(6, 8, DIR_W)

        level.add_cop(6, 3, DIR_E)
        level.add_cop(0, 8, DIR_S)

        level.add_victim(1, 1)
        level.add_victim(3, 3)
        level.add_victim(6, 5)
        level.add_victim(0, 7)

        return level

    @staticmethod
    def s7_d1():

        level = Level('Slayaway Camp 7, Deleted Scene 1 - SWAT Cop Spiral', 8, 8,
            6, 3,
            7, 3)

        level.wall_north(4, 1)
        level.wall_north(3, 1)
        level.wall_north(2, 1)
        level.wall_north(1, 1)
        level.wall_west(1, 1)
        level.wall_west(1, 2)
        level.wall_west(1, 3)
        level.wall_west(1, 4)
        level.wall_west(1, 5)
        level.wall_west(1, 6)

        level.short_wall_south(7, 0)

        level.short_wall_north(4, 3)
        level.wall_north(3, 3)
        level.short_wall_west(3, 3)
        level.short_wall_west(3, 4)
        level.short_wall_west(3, 5)

        level.short_wall_east(5, 3)
        level.short_wall_east(5, 4)
        level.wall_east(5, 5)
        level.short_wall_south(5, 5)
        level.short_wall_south(4, 5)

        level.short_wall_south(5, 6)
        level.short_wall_south(6, 6)

        level.short_wall_box(4, 4)

        level.add_cabinet_we(6, 0)

        level.add_phone_pair(4, 1, 7, 4)
        level.add_phone_pair(1, 4, 4, 7)

        level.add_swat(4, 4, DIR_E)
        level.add_victim(7, 0)
        level.add_victim(5, 5)
        level.add_victim(3, 6)
        level.add_cat(5, 1)
        level.add_cat(5, 6)

        return level

    @staticmethod
    def s7_d2():

        # Aside: I am delighted that the solution slaysolver finds for this level is
        # basically completely different than the solution I'd come up with when
        # playing the level myself.  Many solutions for previous levels differ from
        # my own in various ways, but generally maintained the same general approach
        # to solving the level.  This one's got at least two very distinct solutions,
        # though!

        level = Level('Slayaway Camp 7, Deleted Scene 2 - Call Centre Claustrophobia', 8, 7,
            6, 4,
            3, 0)

        level.wall_east(0, 0)
        level.wall_east(0, 1)
        level.short_wall_east(0, 2)
        level.wall_south(0, 2)

        level.wall_north(2, 1)
        level.wall_box(3, 1)
        level.wall_north(4, 1)

        level.wall_west(5, 0)
        level.wall_west(5, 1)
        level.wall_south(5, 1)
        level.wall_east(5, 1)
        level.wall_south(6, 0)
        level.wall_south(7, 0)

        level.wall_box(0, 6)
        level.wall_box(2, 6)
        level.wall_box(4, 6)

        level.wall_west(6, 6)
        level.wall_north(6, 6)
        level.wall_west(7, 5)
        level.wall_north(7, 5)

        level.short_wall_east(0, 4)
        level.short_wall_east(0, 5)
        level.short_wall_east(2, 2)
        level.short_wall_south(4, 2)
        level.short_wall_east(4, 5)
        level.short_wall_east(6, 2)
        level.short_wall_east(6, 3)
        level.short_wall_east(6, 5)

        level.add_phone_pair(2, 1, 5, 6)
        level.add_phone_pair(6, 1, 3, 6)
        level.add_phone_pair(4, 1, 1, 6)

        level.add_cop(1, 0, DIR_S)
        level.add_cop(3, 2, DIR_E)
        level.add_cop(4, 5, DIR_W)
        level.add_cop(6, 5, DIR_W)

        level.add_victim(1, 1)
        level.add_victim(2, 5)
        level.add_victim(5, 3)
        level.add_victim(7, 1)

        return level

    @staticmethod
    def s7_d3():

        level = Level('Slayaway Camp 7, Deleted Scene 3 - Customer Service', 8, 8,
            3, 7,
            4, 1)

        level.wall_south(0, 1)
        
        level.wall_north(1, 1)
        level.wall_east(1, 1)
        level.wall_east(1, 2)

        level.wall_west(3, 1)
        level.wall_north(3, 1)
        level.wall_north(4, 1)
        level.wall_north(5, 1)
        level.wall_north(6, 1)
        level.wall_west(6, 1)

        level.wall_south(7, 1)

        level.wall_south(3, 2)
        level.wall_south(5, 2)

        level.wall_north(1, 4)
        level.wall_south(1, 4)
        level.wall_north(2, 4)
        level.wall_south(2, 4)
        level.wall_north(3, 4)
        level.wall_south(3, 4)
        level.wall_north(5, 4)
        level.wall_south(5, 4)

        level.wall_west(5, 7)
        level.wall_north(5, 7)
        level.wall_north(6, 7)
        level.wall_east(6, 7)

        level.set_hazard(1, 4)
        level.set_hazard(2, 4)
        level.set_hazard(3, 4)
        level.set_hazard(4, 4)
        level.set_hazard(5, 4)

        level.add_cabinet_ns(6, 5)

        level.add_phone_pair(0, 7, 4, 7)

        level.add_swat(4, 2, DIR_S)
        level.add_cop(3, 2, DIR_W)
        level.add_cop(5, 2, DIR_E)

        level.add_victim(2, 3)
        level.add_victim(6, 2)
        level.add_victim(4, 5)
        level.add_victim(2, 6)
        
        return level

    @staticmethod
    def s8_s01():

        level = Level('Slayaway Camp 8, Scene 1 - Gummed Up', 7, 7,
            0, 6,
            6, 6)

        level.wall_south(0, 1)
        level.wall_south(1, 1)
        level.wall_east(1, 1)
        level.wall_east(1, 0)

        level.wall_south(0, 5)
        level.wall_south(1, 5)
        level.wall_south(2, 5)
        level.wall_east(2, 5)

        level.wall_west(4, 5)
        level.wall_south(4, 5)
        level.wall_south(5, 5)
        level.wall_south(6, 5)
        level.wall_west(6, 5)
        level.wall_west(6, 4)
        level.wall_north(6, 4)

        level.set_sticky(3, 3)
        level.set_sticky(3, 6)

        level.add_victim(0, 3)
        level.add_victim(3, 2)

        return level

    @staticmethod
    def s8_s02():

        level = Level('Slayaway Camp 8, Scene 2 - Stopped In His Tracks', 7, 7,
            0, 0,
            3, 4)

        level.wall_south(0, 0)
        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_south(3, 0)

        level.wall_west(6, 0)
        level.wall_west(6, 1)
        level.wall_west(6, 2)
        level.wall_south(6, 2)

        level.wall_north(0, 6)
        level.wall_north(1, 6)
        level.wall_east(1, 6)

        level.short_wall_west(3, 4)
        level.short_wall_south(3, 4)

        level.set_sticky(5, 5)

        level.add_victim(5, 1)
        level.add_victim(0, 3)
        level.add_victim(2, 5)

        return level

    @staticmethod
    def s8_s03():

        level = Level('Slayaway Camp 8, Scene 3 - Graveyard Shift', 8, 8,
            2, 7,
            7, 2)

        level.wall_south(0, 1)
        level.wall_south(1, 1)
        level.wall_east(1, 1)
        level.wall_south(2, 0)
        level.wall_south(3, 0)
        level.wall_south(4, 0)
        level.wall_east(4, 0)
        level.wall_west(6, 0)
        level.wall_south(6, 0)
        level.wall_south(7, 0)

        level.short_wall_west(2, 2)
        level.short_wall_north(3, 2)
        level.short_wall_east(3, 2)
        level.short_wall_west(3, 3)

        level.short_wall_west(1, 4)
        level.short_wall_north(1, 4)
        level.short_wall_south(1, 4)
        level.short_wall_north(2, 4)
        level.short_wall_south(2, 4)
        level.short_wall_north(3, 4)
        level.short_wall_south(3, 4)
        level.short_wall_south(4, 4)
        level.short_wall_south(5, 4)
        level.short_wall_south(6, 4)
        level.short_wall_north(7, 4)
        level.short_wall_south(7, 4)

        level.wall_west(4, 5)
        level.wall_south(4, 5)
        level.wall_east(4, 5)

        level.electric_north(0, 7)
        level.electric_east(0, 7)

        level.electric_east(7, 1)
        level.electric_east(7, 2)
        level.electric_east(7, 3)
        level.electric_east(7, 4)
        level.electric_east(7, 5)
        level.electric_east(7, 6)
        level.electric_west(7, 5)
        level.electric_south(7, 5)

        level.set_hazard(5, 0)
        level.set_hazard(0, 6)

        level.switch_west(2, 1)
        level.switch_north(7, 1)
        level.switch_west(0, 5)
        level.switch_west(5, 5)

        level.add_victim(4, 2)
        level.add_victim(0, 3)
        level.add_victim(5, 4)
        level.add_victim(4, 7)
        level.add_cat(1, 4)

        return level

    @staticmethod
    def s8_s04():

        level = Level('Slayaway Camp 8, Scene 4 - Cafeteria Cleanup', 7, 8,
            3, 0,
            3, 4)

        level.short_wall_west(1, 0)
        level.electric_west(1, 1)
        level.short_wall_south(1, 1)
        level.short_wall_south(2, 1)
        level.short_wall_east(2, 1)
        level.short_wall_east(2, 0)

        level.short_wall_west(4, 0)
        level.short_wall_west(4, 1)
        level.short_wall_south(4, 1)
        level.short_wall_south(5, 1)
        level.electric_east(5, 1)
        level.short_wall_east(5, 0)

        level.short_wall_south(0, 4)
        level.short_wall_south(1, 4)
        level.short_wall_south(5, 4)
        level.short_wall_south(6, 4)

        level.wall_box(4, 7)

        level.set_sticky(1, 2)
        level.set_sticky(3, 2)
        level.set_sticky(5, 2)
        level.set_sticky(2, 4)
        level.set_sticky(4, 4)
        level.set_sticky(0, 6)
        level.set_sticky(3, 6)
        level.set_sticky(6, 6)

        level.add_phone_pair(2, 3, 4, 3)

        level.add_cop(3, 7, DIR_W)
        level.add_victim(1, 1)
        level.add_victim(5, 1)
        level.add_victim(1, 6)
        level.add_victim(5, 6)

        return level

    @staticmethod
    def s8_s05():

        level = Level('Slayaway Camp 8, Scene 5 - The Long Way \'Round', 8, 8,
            3, 4,
            6, 1)

        level.wall_box(5, 5)
        level.wall_box(7, 5)
        level.wall_box(0, 7)

        level.short_wall_south(3, 0)

        level.wall_south(0, 1)
        level.wall_east(1, 2)
        level.wall_east(2, 2)
        level.wall_east(2, 3)
        level.wall_south(4, 3)
        level.wall_east(5, 3)
        level.wall_east(3, 4)
        level.wall_south(3, 6)

        level.set_hazard(0, 0)
        level.set_hazard(1, 3)

        level.escape_north(2)
        level.escape_west(6)

        level.add_cabinet_we(4, 0)

        level.add_victim(3, 1)
        level.add_victim(2, 5)
        level.add_victim(1, 6)
        level.add_victim(6, 6)

        return level

    @staticmethod
    def s8_s06():

        level = Level('Slayaway Camp 8, Scene 6 - Hubba Trubba', 8, 8,
            0, 6,
            0, 0)

        level.wall_north(0, 1)
        level.wall_south(0, 1)
        level.wall_north(1, 1)
        level.wall_south(1, 1)
        level.wall_east(1, 1)
        level.wall_north(2, 1)

        level.wall_west(5, 0)
        level.wall_south(5, 0)
        level.wall_west(5, 1)
        level.wall_south(6, 0)
        level.wall_south(7, 0)

        level.wall_north(2, 4)
        level.wall_south(2, 4)
        level.wall_north(3, 4)
        level.wall_south(3, 4)
        level.wall_north(4, 4)
        level.wall_south(4, 4)

        level.wall_south(6, 2)

        level.wall_north(0, 7)
        level.wall_north(1, 7)
        level.wall_east(1, 7)

        level.wall_west(5, 7)
        level.wall_north(5, 7)
        level.wall_north(6, 7)
        level.wall_west(7, 6)
        level.wall_north(7, 6)

        level.set_mine(1, 0)

        for x in range(3):
            for y in range(3):
                level.set_sticky(x+2, y+1)
                level.set_sticky(x+2, y+5)
        level.set_sticky(0, 4)
        level.set_sticky(6, 4)

        level.add_victim(1, 2)
        level.add_victim(5, 6)

        return level

    @staticmethod
    def s8_s07():

        level = Level('Slayaway Camp 8, Scene 7 - Central Park Panic', 7, 7,
            3, 3,
            2, 3,
            10)

        level.set_sticky(4, 0)
        level.set_sticky(3, 1)
        level.set_sticky(3, 3)
        level.set_sticky(3, 5)
        level.set_sticky(2, 6)

        level.add_cabinet_ns(0, 4)
        level.add_cabinet_ns(6, 2)

        level.add_victim(5, 1)
        level.add_victim(6, 1)
        level.add_victim(0, 5)
        level.add_victim(1, 5)

        return level

    @staticmethod
    def s8_s08():

        level = Level('Slayaway Camp 8, Scene 8 - Shop Till They Drop', 8, 8,
            4, 7,
            6, 1)

        level.wall_west(1, 2)
        level.wall_north(1, 2)
        level.wall_north(2, 2)
        level.wall_east(2, 2)
        level.wall_east(2, 3)
        level.wall_south(2, 3)
        level.wall_south(1, 3)
        level.wall_west(1, 3)

        level.wall_west(7, 0)
        level.wall_west(7, 1)
        level.wall_west(7, 2)
        level.wall_north(6, 3)
        level.wall_west(6, 3)
        level.wall_south(6, 3)
        level.wall_south(7, 3)

        level.wall_south(0, 5)
        level.wall_east(2, 6)
        level.short_wall_east(4, 5)

        level.electric_south(0, 0)
        level.electric_south(1, 0)
        level.electric_south(2, 0)
        level.electric_south(3, 0)
        level.electric_south(5, 0)
        level.electric_south(6, 0)

        level.set_hazard(0, 0)
        level.set_hazard(6, 0)

        level.switch_north(6, 4)

        level.add_victim(3, 0)
        level.add_victim(5, 0)
        level.add_victim(5, 5)
        level.add_victim(7, 5)
        level.add_cat(1, 0)
        
        return level

    @staticmethod
    def s8_s09():

        level = Level('Slayaway Camp 8, Scene 9 - Arcade Anxiety', 7, 8,
            3, 4,
            3, 6)

        level.short_wall_east(0, 0)
        level.short_wall_west(6, 0)
        for y in range(1, 8):
            level.electric_east(0, y)
            level.electric_east(5, y)

        level.switch_north(1, 0)
        level.switch_north(5, 0)

        level.add_cabinet_ns(1, 3)
        level.add_cabinet_ns(5, 5)

        for y in [1, 3, 5, 7]:
            level.add_swat(0, y, DIR_E)
            level.add_swat(6, y, DIR_W)
        level.add_cop(2, 1, DIR_E)

        level.add_victim(2, 2)
        level.add_victim(4, 2)
        level.add_victim(4, 3)
        level.add_victim(2, 7)

        return level

    @staticmethod
    def s8_s10():

        level = Level('Slayaway Camp 8, Scene 10 - Bus Stop Barrage', 8, 8,
            4, 6,
            1, 3)

        level.wall_south(0, 0)
        level.wall_south(1, 0)
        level.wall_east(1, 0)

        level.wall_north(0, 5)
        level.wall_east(0, 5)
        level.wall_east(0, 6)

        level.short_wall_north(6, 1)
        level.short_wall_east(6, 1)

        level.short_wall_east(3, 2)
        level.short_wall_south(3, 2)

        level.short_wall_north(1, 3)
        level.short_wall_west(1, 3)
        level.short_wall_south(1, 3)

        level.short_wall_south(0, 6)
        level.short_wall_south(1, 6)
        level.short_wall_south(2, 6)
        level.short_wall_east(2, 6)
        level.short_wall_north(3, 6)
        level.short_wall_south(3, 6)
        level.short_wall_west(3, 5)

        level.set_mine(3, 3)

        level.set_sticky(6, 2)
        level.set_sticky(7, 3)
        level.set_sticky(6, 4)

        level.escape_north(3)
        level.escape_west(2)
        level.escape_west(7)

        level.add_cabinet_we(5, 1)

        level.add_victim(3, 2)
        level.add_victim(6, 3)
        level.add_victim(3, 5)
        level.add_victim(6, 5)
        level.add_cat(5, 7)

        return level

    @staticmethod
    def s8_s11():

        level = Level('Slayaway Camp 8, Scene 11 - Ferry Terminal Filet', 9, 9,
            4, 6,
            6, 3,
            11)

        for y in range(9):
            level.set_hazard(0, y)
            level.set_hazard(8, y)
        for x in range(3):
            for y in range(2):
                level.set_hazard(x+1, y)
                level.set_hazard(x+5, y)

        level.wall_box(4, 0)

        level.wall_west(1, 2)
        level.wall_north(1, 2)
        level.wall_north(2, 2)
        level.wall_north(3, 2)
        level.wall_west(4, 1)
        level.wall_east(4, 1)
        level.wall_north(5, 2)
        level.wall_north(6, 2)
        level.wall_east(7, 2)

        for x in [1, 7]:
            level.wall_north(x, 5)
            level.wall_west(x, 5)
            level.wall_east(x, 5)
            level.wall_west(x, 6)
            level.wall_east(x, 6)
            level.wall_west(x, 7)
            level.wall_east(x, 7)
            level.wall_west(x, 8)
            level.wall_east(x, 8)

        level.short_wall_south(2, 2)
        level.short_wall_south(6, 4)
        level.short_wall_east(2, 6)
        level.short_wall_east(5, 6)
        level.short_wall_south(3, 7)

        level.switch_north(4, 1)

        level.add_swat(2, 8, DIR_N)
        level.add_swat(6, 8, DIR_N)

        level.add_victim(2, 4)
        level.add_victim(6, 4)
        level.add_victim(4, 2)

        return level

    @staticmethod
    def s8_s12():

        level = Level('Slayaway Camp 8, Scene 12 - Apartment Complex', 7, 7,
            1, 0,
            2, 3)

        level.short_wall_south(0, 1)
        level.short_wall_east(1, 1)
        level.short_wall_south(6, 1)
        level.short_wall_east(0, 2)
        level.short_wall_south(2, 2)
        level.short_wall_east(5, 2)
        level.short_wall_south(0, 3)
        level.short_wall_south(6, 3)
        level.short_wall_south(2, 4)
        level.short_wall_east(3, 4)
        level.short_wall_south(1, 5)
        level.short_wall_east(1, 5)
        level.short_wall_south(2, 5)
        level.short_wall_south(3, 5)
        level.short_wall_east(3, 5)
        level.short_wall_south(4, 5)
        level.short_wall_south(5, 5)

        level.wall_box(6, 4)

        level.electric_west(0, 1)
        level.electric_east(6, 1)
        level.electric_west(0, 4)
        level.electric_west(0, 5)
        level.electric_east(6, 5)

        level.electric_south(1, 6)
        level.electric_south(2, 6)
        level.electric_south(3, 6)
        level.electric_south(4, 6)
        level.electric_south(5, 6)

        level.electric_box(3, 3)

        level.switch_north(0, 0)
        level.switch_north(6, 0)

        level.add_phone_pair(3, 0, 3, 3)

        level.add_victim(0, 2)
        level.add_victim(6, 2)
        level.add_victim(3, 5)

        return level

    @staticmethod
    def s8_s13():

        # Just the usual amount of exit finagling, here.

        # Another level where the found solution differs from my own pretty
        # significantly!  I'd avoided hitting the lower-right phone until I
        # scared the cat over to the little nook on the west, but this solution
        # doesn't do that at all.

        level = Level('Slayaway Camp 8, Scene 13 - Apartment Complexerer', 9, 9,
            3, 2,
            4, 2)

        level.wall_east(1, 0)
        level.wall_south(1, 0)
        level.wall_east(0, 1)
        level.wall_south(0, 1)

        level.wall_north(0, 3)
        level.wall_east(0, 3)
        level.wall_east(0, 4)
        level.wall_east(0, 5)
        level.wall_east(0, 6)
        level.wall_east(0, 7)
        level.wall_north(1, 8)
        level.wall_east(1, 8)

        level.wall_east(6, 6)

        level.short_wall_south(1, 1)
        level.short_wall_south(2, 2)
        level.short_wall_east(5, 0)
        level.short_wall_east(5, 1)
        level.short_wall_south(6, 2)
        level.short_wall_south(7, 2)
        level.short_wall_north(2, 5)
        level.short_wall_west(2, 5)
        level.short_wall_south(2, 5)
        level.short_wall_south(6, 7)
        level.short_wall_south(7, 7)

        level.switch_north(3, 0)
        level.switch_north(6, 0)

        level.add_cabinet_we(1, 2)
        level.add_cabinet_ns(5, 7)

        level.add_phone_pair(5, 1, 8, 8)

        level.add_swat(2, 0, DIR_S)
        level.add_victim(1, 1)
        level.add_victim(8, 1)
        level.add_victim(2, 3)
        level.add_victim(7, 5)
        level.add_cat(5, 5)

        return level

    @staticmethod
    def s8_d1():

        level = Level('Slayaway Camp 8, Deleted Scene 1 - Splatterhouse', 8, 8,
            6, 6,
            2, 5,
            10)

        level.short_wall_north(2, 1)
        level.short_wall_north(3, 1)
        level.short_wall_north(4, 1)
        level.short_wall_north(5, 1)
        level.short_wall_east(5, 1)

        level.short_wall_north(3, 2)
        level.short_wall_north(2, 2)
        level.short_wall_north(1, 2)
        level.short_wall_west(1, 2)
        level.short_wall_west(1, 3)
        level.short_wall_west(1, 4)

        level.short_wall_south(1, 5)
        level.short_wall_south(2, 5)
        level.short_wall_south(3, 5)
        level.short_wall_south(4, 5)
        level.short_wall_south(5, 5)
        level.short_wall_east(5, 5)
        level.short_wall_east(5, 4)
        level.short_wall_east(5, 3)

        level.short_wall_south(2, 6)
        level.short_wall_south(3, 6)
        level.short_wall_south(4, 6)
        level.short_wall_south(5, 6)

        level.short_wall_east(6, 1)
        level.short_wall_east(6, 2)
        level.short_wall_east(6, 3)
        level.short_wall_east(6, 4)
        level.short_wall_east(6, 5)
        level.short_wall_east(6, 6)

        level.switch_north(6, 0)

        level.set_sticky(6, 0)
        level.set_sticky(0, 6)

        level.add_cop(0, 0, DIR_S)
        level.add_cop(5, 1, DIR_W)
        level.add_cop(2, 3, DIR_N)
        level.add_cop(4, 4, DIR_N)

        level.add_victim(6, 1)
        level.add_victim(1, 2)
        level.add_victim(0, 5)

        return level

    @staticmethod
    def s8_d2():

        level = Level('Slayaway Camp 8, Deleted Scene 2 - Treat Sweeper', 8, 7,
            4, 1,
            7, 6,
            14)

        for x in range(1, 6):
            level.short_wall_east(x, 2)
            level.short_wall_east(x, 3)
        level.short_wall_east(3, 4)
        level.short_wall_south(3, 4)
        level.short_wall_south(4, 4)
        level.wall_east(1, 5)

        level.set_sticky(2, 1)
        level.set_sticky(5, 1)
        level.set_sticky(3, 3)
        level.set_sticky(4, 3)
        level.set_sticky(1, 4)
        level.set_sticky(6, 4)

        level.add_cabinet_we(1, 1)
        level.add_cabinet_we(6, 1)
        level.add_cabinet_we(2, 6)
        level.add_cabinet_we(5, 6)

        level.add_victim(0, 1)
        level.add_victim(3, 4)
        level.add_victim(4, 4)
        level.add_victim(6, 6)

        return level

    @staticmethod
    def s8_d3():

        # This one is quite a monster to solve, probably takes the longest
        # out of all the levels here, so far.  The basic problem is that the
        # tree is unavoidably deep - the quickest solution is 57 steps, and
        # the cabinets+goo make for a very wide tree as well.

        # (Update: s10_d4 is even worse!)

        level = Level('Slayaway Camp 8, Deleted Scene 3 - Porta-Potty Mouth', 8, 7,
            1, 2,
            6, 4)

        level.wall_south(0, 3)
        level.wall_east(0, 3)
        level.wall_east(0, 2)
        level.wall_east(0, 1)
        level.wall_east(0, 0)

        for x in range(1, 7):
            level.short_wall_east(x, 4)
            level.short_wall_east(x, 5)
            level.short_wall_south(x, 5)
            level.add_cabinet_ns(x, 1)

        level.set_sticky(1, 0)
        level.set_sticky(2, 0)
        level.set_sticky(5, 0)
        level.set_sticky(6, 0)
        level.set_sticky(4, 2)
        level.set_sticky(5, 2)
        level.set_sticky(6, 2)
        level.set_sticky(1, 3)
        level.set_sticky(2, 6)
        level.set_sticky(4, 6)
        level.set_sticky(6, 6)

        level.set_mine(3, 4)

        level.add_cop(0, 5, DIR_E)
        level.add_victim(2, 5)
        level.add_victim(3, 5)
        level.add_victim(4, 5)
        level.add_victim(6, 5)

        return level

    @staticmethod
    def s10_s01():

        level = Level('Slayaway Camp X, Scene 1 - Teleporter Torcher', 7, 7,
            0, 6,
            3, 6)

        level.wall_west(6, 0)
        level.wall_west(6, 1)
        level.wall_south(6, 1)

        level.wall_west(4, 3)
        level.wall_north(4, 3)
        level.wall_north(5, 3)
        level.wall_east(5, 3)
        level.wall_east(5, 4)
        level.wall_south(5, 4)
        level.wall_south(4, 4)
        level.wall_west(4, 4)

        for x in range(7):
            level.short_wall_north(x, 6)
            if x < 5:
                level.short_wall_south(x, 0)
        for y in range(1, 6):
            level.short_wall_east(1, y)
        level.short_wall_east(2, 5)

        level.set_hazard(0, 1)
        level.set_hazard(2, 5)

        level.add_teleporter_pair(1, 0, 5, 6)

        level.add_victim(2, 2)
        level.add_victim(1, 5)

        return level

    @staticmethod
    def s10_s02():

        level = Level('Slayaway Camp X, Scene 2 - Teleportation Agitation', 7, 7,
            6, 0,
            6, 2)

        level.short_wall_south(6, 0)

        level.short_wall_east(4, 0)
        level.short_wall_east(4, 1)
        level.short_wall_south(4, 1)
        level.short_wall_south(3, 1)

        level.short_wall_south(0, 3)
        level.short_wall_east(0, 3)
        level.short_wall_north(1, 3)

        level.short_wall_north(3, 3)
        level.short_wall_north(4, 3)
        level.short_wall_north(5, 3)
        level.short_wall_north(6, 3)

        level.short_wall_south(0, 5)
        level.short_wall_south(1, 5)
        level.short_wall_south(2, 5)
        level.short_wall_south(3, 5)
        level.short_wall_south(4, 5)
        level.short_wall_south(5, 5)
        level.short_wall_east(5, 5)

        level.set_sticky(2, 3)

        level.add_teleporter_pair(0, 0, 6, 6)

        level.add_victim(4, 0)
        level.add_victim(1, 4)

        return level

    @staticmethod
    def s10_s03():

        level = Level('Slayaway Camp X, Scene 3 - Space Experiment #13B', 7, 7,
            3, 1,
            5, 0,
            9)

        level.wall_east(1, 0)
        level.wall_east(1, 1)
        level.wall_south(0, 2)
        level.wall_south(1, 2)

        level.wall_box(0, 6)
        level.wall_box(6, 0)

        level.electric_west(2, 2)
        level.electric_south(2, 2)
        level.electric_north(3, 2)
        level.electric_south(3, 2)
        level.electric_north(4, 2)
        level.electric_east(4, 2)
        level.electric_west(2, 3)
        level.electric_south(3, 3)
        level.electric_south(4, 3)
        level.electric_east(4, 3)
        level.electric_west(2, 4)
        level.electric_south(2, 4)
        level.electric_south(3, 4)
        level.electric_south(4, 4)

        level.short_wall_south(5, 4)
        level.short_wall_east(5, 4)

        level.switch_north(2, 0)

        level.add_victim(4, 2)
        level.add_victim(2, 3)
        level.add_victim(4, 4)

        return level

    @staticmethod
    def s10_s04():

        level = Level('Slayaway Camp X, Scene 4 - Dumblight Minecat Frexit', 9, 8,
            4, 4,
            1, 3)

        level.wall_east(0, 2)
        level.wall_east(0, 3)
        level.wall_east(0, 4)
        level.wall_north(1, 5)
        level.wall_east(1, 5)

        level.wall_west(3, 2)
        level.wall_south(3, 2)
        level.wall_south(4, 2)

        level.short_wall_north(0, 1)
        level.short_wall_south(0, 1)
        level.short_wall_north(1, 1)
        level.short_wall_south(1, 1)
        level.short_wall_north(2, 1)
        level.short_wall_south(2, 1)
        level.short_wall_south(3, 1)
        level.short_wall_north(4, 1)
        level.short_wall_south(4, 1)
        level.short_wall_north(5, 1)
        level.short_wall_south(5, 1)
        level.short_wall_north(6, 1)
        level.short_wall_south(7, 1)
        level.short_wall_east(7, 1)
        level.short_wall_west(5, 2)

        level.short_wall_north(0, 6)
        level.short_wall_south(0, 6)
        level.short_wall_north(1, 6)
        level.short_wall_south(1, 6)
        level.short_wall_north(2, 6)
        level.short_wall_south(2, 6)
        level.short_wall_north(3, 6)
        level.short_wall_south(3, 6)
        level.short_wall_north(4, 6)
        level.short_wall_north(5, 6)
        level.short_wall_south(5, 6)
        level.short_wall_south(6, 6)
        level.short_wall_north(7, 6)
        level.short_wall_east(7, 6)
        level.short_wall_west(5, 5)

        level.escape_west(1)
        level.escape_west(6)

        level.set_mine(2, 1)
        level.set_mine(7, 1)
        level.set_mine(2, 6)
        level.set_mine(7, 6)

        level.set_sticky(3, 0)
        level.set_sticky(4, 7)

        level.switch_west(0, 0)
        level.switch_west(0, 7)

        level.add_cabinet_ns(8, 3)

        level.add_cop(6, 1, DIR_W)

        level.add_victim(5, 1)
        level.add_victim(2, 4)
        level.add_victim(5, 6)

        level.add_cat(1, 1)
        level.add_cat(1, 6)
        
        return level

    @staticmethod
    def s10_s05():

        level = Level('Slayaway Camp X, Scene 5 - Space Station Slay', 9, 7,
            5, 4,
            7, 0)

        level.wall_south(0, 0)
        level.wall_south(1, 0)
        level.wall_east(1, 0)

        level.wall_north(0, 5)
        level.wall_east(0, 5)
        level.wall_east(0, 6)

        level.electric_north(4, 0)
        level.electric_north(6, 0)
        level.electric_east(8, 6)

        level.short_wall_south(2, 0)
        level.short_wall_south(3, 0)
        level.short_wall_south(5, 0)
        level.short_wall_south(7, 0)

        level.short_wall_south(0, 2)
        level.short_wall_east(0, 2)
        level.short_wall_south(1, 1)
        level.short_wall_south(2, 1)
        level.short_wall_south(3, 1)
        level.short_wall_south(5, 1)
        level.short_wall_south(7, 1)

        level.short_wall_south(2, 2)
        level.short_wall_south(3, 2)
        level.short_wall_south(5, 2)
        level.short_wall_south(6, 2)
        level.short_wall_south(7, 2)
        level.short_wall_east(7, 2)
        level.short_wall_east(7, 3)

        level.short_wall_east(1, 4)
        level.short_wall_east(1, 5)
        level.short_wall_east(4, 5)

        level.set_sticky(1, 4)
        level.set_sticky(2, 5)
        level.set_sticky(7, 4)
        level.set_sticky(8, 5)

        level.add_teleporter_pair(2, 3, 6, 2)
        level.add_teleporter_pair(1, 6, 8, 0)

        level.add_victim(0, 1)
        level.add_victim(2, 2)
        level.add_victim(2, 4)
        level.add_victim(4, 6)

        return level

    @staticmethod
    def s10_s06():

        level = Level('Slayaway Camp X, Scene 6 - Reservoir Slobs', 7, 7,
            3, 2,
            5, 0)

        level.wall_east(0, 0)
        level.wall_east(0, 1)
        level.wall_south(0, 1)

        level.wall_box(6, 0)

        level.short_wall_east(4, 0)
        level.short_wall_east(4, 1)

        level.short_wall_south(1, 5)
        level.short_wall_east(1, 5)

        level.set_sticky(0, 4)
        level.set_sticky(3, 0)
        level.set_sticky(3, 3)
        level.set_sticky(5, 4)
        level.set_sticky(6, 4)
        level.set_sticky(2, 6)
        level.set_sticky(4, 6)

        level.switch_north(2, 0)
        level.switch_north(4, 0)

        level.add_swat(1, 1, DIR_E)
        level.add_swat(5, 1, DIR_S)
        level.add_swat(5, 5, DIR_W)
        level.add_swat(1, 5, DIR_N)

        level.add_victim(2, 3)
        level.add_victim(4, 3)
        level.add_victim(3, 4)

        return level

    @staticmethod
    def s10_s07():

        # Rather different solution here than the one I'd found,
        # forcing one of the victims up north through the second
        # portal to clear the mine.

        level = Level('Slayaway Camp X, Scene 7 - Still Alive', 8, 8,
            7, 4,
            7, 7)

        level.short_wall_east(0, 0)
        level.short_wall_south(2, 0)
        level.short_wall_south(3, 0)
        level.short_wall_south(5, 0)
        level.short_wall_east(5, 0)
        level.short_wall_east(2, 1)
        level.short_wall_east(5, 1)
        level.short_wall_east(6, 1)
        level.short_wall_east(2, 3)
        level.short_wall_south(3, 3)
        level.short_wall_east(2, 5)
        level.short_wall_south(0, 6)
        level.short_wall_south(2, 6)
        level.short_wall_south(3, 6)
        level.short_wall_south(5, 6)
        level.short_wall_south(7, 6)

        level.set_mine(6, 0)

        level.add_cabinet_we(1, 1)
        level.add_cabinet_we(4, 1)

        level.add_teleporter_pair(1, 0, 4, 7)
        level.add_teleporter_pair(4, 0, 6, 7)
        level.add_teleporter_pair(7, 0, 1, 7)

        level.add_victim(5, 2)
        level.add_victim(0, 3)
        level.add_victim(3, 5)

        return level

    @staticmethod
    def s10_s08():

        level = Level('Slayaway Camp X, Scene 8 - Illusion of Safety', 7, 8,
            6, 2,
            3, 0,
            12)

        level.wall_south(0, 1)
        level.wall_south(1, 1)
        level.wall_south(2, 1)
        level.wall_east(2, 1)
        level.wall_east(2, 0)

        level.wall_east(3, 0)
        level.wall_east(3, 1)
        level.wall_east(3, 2)
        level.wall_south(4, 1)
        level.wall_south(5, 1)
        level.wall_south(6, 1)

        level.wall_south(5, 2)
        level.wall_east(1, 3)
        level.wall_east(3, 6)
        level.wall_box(6, 6)

        level.add_cabinet_we(5, 7)

        level.add_cop(3, 2, DIR_W)
        level.add_cop(3, 5, DIR_W)
        level.add_cop(2, 6, DIR_N)

        level.add_victim(1, 2)
        level.add_victim(4, 3)
        level.add_victim(1, 6)

        return level

    @staticmethod
    def s10_s09():

        level = Level('Slayaway Camp X, Scene 9 - Co-operative Testing Initiative', 7, 8,
            1, 2,
            3, 0)

        level.wall_north(0, 1)
        level.wall_south(0, 1)
        level.wall_north(1, 1)
        level.wall_south(1, 1)
        level.wall_east(1, 1)
        level.short_wall_south(2, 1)
        level.short_wall_east(2, 1)

        level.short_wall_south(3, 2)
        level.short_wall_east(3, 2)
        level.short_wall_west(4, 1)
        level.short_wall_south(4, 1)
        level.wall_east(4, 1)
        level.wall_north(5, 1)
        level.wall_south(5, 1)
        level.wall_north(6, 1)
        level.wall_south(6, 1)

        level.short_wall_south(0, 3)
        level.short_wall_south(3, 3)
        level.wall_west(4, 4)
        level.wall_north(4, 4)
        level.wall_south(4, 4)
        level.wall_north(5, 4)
        level.wall_south(5, 4)
        level.wall_east(5, 4)

        for x in range(7):
            level.short_wall_south(x, 6)

        level.set_sticky(1, 2)
        level.set_sticky(2, 5)
        level.switch_west(0, 3)

        level.add_teleporter_pair(0, 7, 6, 0)
        level.add_teleporter_pair(3, 3, 3, 7)
        level.add_teleporter_pair(0, 0, 6, 7)

        level.add_swat(6, 3, DIR_W)
        level.add_victim(2, 1)
        level.add_victim(4, 1)
        level.add_victim(4, 6)

        return level

    @staticmethod
    def s10_s10():

        level = Level('Slayaway Camp X, Scene 10 - Dial-A-Portal', 7, 7,
            6, 6,
            5, 1,
            8)

        level.wall_box(1, 1)
        level.wall_box(1, 5)

        level.short_wall_west(5, 1)
        level.short_wall_west(5, 2)
        level.short_wall_south(5, 2)
        level.short_wall_south(6, 2)

        level.add_teleporter_pair(0, 0, 3, 3)
        level.add_phone_pair(3, 6, 6, 3)

        level.add_victim(3, 0)
        level.add_victim(0, 3)

        return level

    @staticmethod
    def s10_s11():

        level = Level('Slayaway Camp X, Scene 11 - Space Kitchen Slam', 8, 8,
            5, 2,
            4, 2)

        level.wall_south(0, 0)
        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_east(2, 0)
        level.wall_box(4, 0)
        level.wall_west(6, 0)
        level.wall_south(6, 0)
        level.wall_south(7, 0)

        level.wall_box(0, 7)
        level.wall_box(2, 5)

        level.wall_north(7, 6)
        level.wall_west(7, 6)
        level.wall_west(7, 7)

        level.short_wall_south(4, 2)
        level.short_wall_east(4, 3)
        level.short_wall_east(6, 3)
        level.short_wall_east(0, 4)
        level.short_wall_south(4, 4)
        level.short_wall_south(6, 4)
        level.short_wall_east(0, 5)
        level.short_wall_south(4, 5)
        level.short_wall_south(5, 5)
        level.short_wall_east(6, 5)
        level.short_wall_east(0, 6)
        level.short_wall_south(2, 6)
        level.short_wall_south(3, 6)
        level.short_wall_south(4, 6)
        level.short_wall_south(5, 6)

        level.set_mine(3, 0)
        level.set_mine(5, 0)
        level.set_mine(1, 4)
        level.set_mine(1, 7)
        level.set_mine(6, 7)

        level.add_cabinet_we(2, 1)
        level.add_cabinet_we(1, 2)
        level.add_cabinet_we(5, 4)

        level.add_victim(2, 4)
        level.add_victim(6, 5)
        level.add_victim(1, 6)
        level.add_victim(5, 7)

        return level

    @staticmethod
    def s10_s12():

        level = Level('Slayaway Camp X, Scene 12 - Beam Me Up', 8, 9,
            4, 4,
            4, 2)

        level.escape_north(2)
        level.escape_west(3)

        level.short_wall_north(1, 1)
        level.short_wall_west(1, 1)
        level.short_wall_west(1, 2)
        level.short_wall_east(3, 0)
        level.short_wall_east(2, 1)
        level.short_wall_south(2, 2)
        level.short_wall_east(1, 5)

        level.short_wall_east(5, 1)
        level.short_wall_east(5, 2)
        level.short_wall_east(5, 3)
        level.short_wall_east(5, 4)
        level.short_wall_east(5, 5)
        level.short_wall_south(5, 5)
        level.short_wall_east(5, 6)
        level.short_wall_south(5, 6)
        level.short_wall_south(4, 6)
        level.short_wall_south(3, 6)
        level.short_wall_south(2, 6)
        level.short_wall_south(1, 6)

        for z in range(7):
            level.short_wall_south(z, 7)
            level.short_wall_east(6, z)
        level.short_wall_east(6, 7)

        level.add_teleporter_pair(2, 2, 5, 0)
        level.add_teleporter_pair(0, 6, 3, 3)
        level.add_teleporter_pair(4, 0, 7, 8)

        level.add_victim(7, 1)
        level.add_victim(5, 3)
        level.add_victim(3, 6)
        level.add_victim(1, 8)

        return level

    @staticmethod
    def s10_s13():

        # The usual amount of exit fiddling here.  In the game there's actually
        # two different locations the last victim can end up in; the shortest
        # possible solution is when the 'exit' is at (6,4) (with the last victim
        # at (6,5), which will be one turn quicker than the alternative (exit
        # at (6,3) and victim at (6,2))

        level = Level('Slayaway Camp X, Scene 13 - Engine Room Rampage', 8, 9,
            2, 3,
            6, 4)

        for y in range(1, 9):
            level.short_wall_east(0, y)
            level.short_wall_east(6, y)
        level.short_wall_south(6, 1)
        level.short_wall_south(6, 5)
        level.short_wall_east(2, 3)
        level.short_wall_east(2, 4)

        level.short_wall_south(3, 7)
        level.short_wall_south(4, 7)

        level.set_sticky(2, 1)
        level.set_sticky(5, 1)
        level.set_sticky(1, 7)
        level.set_sticky(6, 7)
        level.set_sticky(3, 8)
        level.set_sticky(4, 8)

        level.set_hazard(0, 0)
        level.set_hazard(7, 0)

        level.add_cabinet_ns(0, 4)
        level.add_cabinet_ns(7, 3)
        level.add_cabinet_we(2, 7)
        level.add_cabinet_we(5, 7)

        level.add_swat(0, 5, DIR_E)
        level.add_swat(7, 4, DIR_W)

        level.add_cat(0, 1)
        level.add_cat(7, 1)

        level.add_victim(1, 5)
        level.add_victim(6, 5)
        level.add_victim(3, 7)
        level.add_victim(4, 7)

        return level

    @staticmethod
    def s10_d1():

        level = Level('Slayaway Camp X, Deleted Scene 1 - A Maze In Space', 9, 9,
            0, 8,
            4, 4)

        level.short_wall_south(2, 0)
        level.short_wall_east(3, 0)
        level.short_wall_south(7, 0)
        level.short_wall_east(2, 1)
        level.short_wall_south(8, 1)
        level.short_wall_south(0, 2)
        level.short_wall_east(1, 2)
        level.short_wall_south(5, 2)
        level.short_wall_east(2, 3)
        level.short_wall_east(5, 3)
        level.short_wall_south(8, 3)
        level.short_wall_east(3, 4)
        level.short_wall_south(4, 4)
        level.short_wall_east(4, 4)
        level.short_wall_south(6, 4)
        level.short_wall_south(1, 5)
        level.short_wall_east(2, 5)
        level.short_wall_south(3, 5)
        level.short_wall_south(5, 5)
        level.short_wall_east(5, 5)
        level.short_wall_south(2, 6)
        level.short_wall_east(7, 6)
        level.short_wall_east(5, 7)

        for x in range(9):
            level.short_wall_south(x, 7)

        level.set_sticky(1, 0)
        level.set_sticky(4, 2)
        level.set_sticky(7, 7)
        level.set_sticky(1, 8)

        level.add_teleporter_pair(3, 8, 8, 7)
        level.add_teleporter_pair(0, 0, 4, 3)

        level.add_victim(2, 8)
        level.add_cat(3, 6)

        return level

    @staticmethod
    def s10_d2():

        level = Level('Slayaway Camp X, Deleted Scene 2 - Transport Protocol', 7, 7,
            2, 6,
            2, 5,
            11)

        level.short_wall_east(0, 0)
        level.short_wall_east(0, 1)
        level.short_wall_east(0, 3)
        level.short_wall_east(0, 5)

        level.short_wall_west(2, 0)
        level.short_wall_south(2, 0)
        level.short_wall_south(3, 0)
        level.short_wall_south(4, 0)
        level.short_wall_south(5, 0)
        level.short_wall_east(5, 1)
        level.short_wall_east(5, 3)
        level.short_wall_east(5, 5)

        level.wall_east(2, 5)

        level.set_hazard(6, 6)
        level.set_sticky(4, 1)

        level.add_cabinet_ns(4, 2)
        level.add_cabinet_ns(2, 4)
        level.add_cabinet_ns(3, 5)

        level.add_teleporter_pair(0, 2, 6, 4)
        level.add_teleporter_pair(0, 4, 6, 0)
        level.add_teleporter_pair(0, 6, 6, 2)

        level.add_victim(2, 0)

        return level

    @staticmethod
    def s10_d3():

        level = Level('Slayaway Camp X, Deleted Scene 3 - Generator Gymnastics', 9, 9,
            1, 2,
            2, 8)

        for x in [0, 1, 2, 3, 5, 6]:
            level.short_wall_north(x, 4)
            level.short_wall_south(x, 4)
        for y in [0, 1, 2, 3, 5, 6]:
            level.short_wall_west(4, y)
            level.short_wall_east(4, y)

        level.short_wall_east(2, 1)
        level.short_wall_north(2, 1)
        level.short_wall_north(1, 1)
        level.wall_west(1, 1)
        level.wall_west(1, 2)
        level.wall_south(1, 2)
        level.wall_south(2, 2)
        level.wall_south(3, 2)

        level.short_wall_east(6, 0)
        level.short_wall_east(6, 2)
        level.short_wall_east(6, 3)
        level.short_wall_east(6, 4)
        level.short_wall_east(7, 0)
        level.short_wall_east(7, 1)
        level.short_wall_east(7, 2)

        level.short_wall_east(3, 7)
        level.short_wall_east(3, 8)

        level.wall_west(5, 8)
        level.wall_west(5, 7)
        level.wall_north(5, 7)
        level.wall_west(7, 5)
        level.wall_north(7, 5)
        level.wall_north(8, 5)
        level.short_wall_south(7, 6)

        level.set_mine(7, 1)
        level.set_mine(8, 1)
        level.set_sticky(6, 1)
        level.set_sticky(0, 6)
        level.set_sticky(1, 6)
        level.set_sticky(1, 7)
        level.set_sticky(2, 5)

        level.add_teleporter_pair(2, 1, 5, 0)
        level.add_teleporter_pair(0, 0, 8, 8)
        level.add_teleporter_pair(2, 6, 6, 6)

        level.add_phone_pair(3, 3, 5, 3)
        level.add_phone_pair(5, 5, 7, 0)
        level.add_phone_pair(0, 8, 8, 0)

        level.add_swat(5, 1, DIR_W)
        level.add_swat(0, 5, DIR_S)
        level.add_swat(1, 8, DIR_E)

        level.add_victim(7, 3)
        level.add_victim(8, 2)
        level.add_victim(3, 8)

        return level

    @staticmethod
    def s10_d4():

        # This is another monster to solve - much worse than 8.D3, in fact.  On my
        # system, after compiling app.py with Cython, it takes a little over 24
        # minutes to find the first solution, which sits at 176 steps.

        level = Level('Slayaway Camp X, Deleted Scene 4 - As Hard as it Looks', 9, 9,
            1, 8,
            7, 6)

        level.return_first_solution = True

        level.electric_east(1, 2)
        level.electric_south(1, 2)
        level.short_wall_west(1, 2)
        level.short_wall_west(1, 1)
        level.short_wall_north(1, 1)
        level.short_wall_north(2, 1)
        level.short_wall_north(3, 1)
        level.electric_east(3, 1)

        level.short_wall_west(6, 1)
        level.short_wall_north(6, 1)
        level.short_wall_north(7, 1)
        level.short_wall_east(7, 1)
        level.electric_east(7, 2)
        level.electric_east(7, 3)
        level.short_wall_south(7, 3)

        level.short_wall_north(1, 5)
        level.short_wall_west(1, 5)
        level.short_wall_west(1, 6)
        level.short_wall_west(1, 7)
        level.short_wall_south(1, 7)
        level.short_wall_south(2, 7)
        level.electric_east(2, 7)

        level.electric_north(5, 7)
        level.short_wall_west(5, 7)
        level.short_wall_south(5, 7)
        level.short_wall_south(6, 7)
        level.short_wall_south(7, 7)
        level.short_wall_east(7, 7)
        level.short_wall_east(7, 6)
        level.short_wall_north(7, 6)

        level.short_wall_east(3, 4)
        level.short_wall_east(3, 5)
        level.short_wall_east(3, 6)

        level.switch_north(0, 0)
        level.switch_north(8, 0)

        level.set_sticky(4, 0)
        level.set_sticky(5, 0)
        level.set_sticky(3, 8)
        level.set_sticky(4, 8)
        level.set_sticky(0, 3)
        level.set_sticky(0, 4)
        level.set_sticky(8, 4)
        level.set_sticky(8, 5)

        level.add_teleporter_pair(2, 1, 7, 7)
        level.add_teleporter_pair(7, 1, 5, 6)
        level.add_teleporter_pair(1, 7, 5, 3)

        level.add_cabinet_ns(4, 1)
        level.add_cabinet_ns(5, 1)
        level.add_cabinet_ns(3, 7)
        level.add_cabinet_ns(4, 7)
        level.add_cabinet_we(1, 3)
        level.add_cabinet_we(1, 4)
        level.add_cabinet_we(7, 4)
        level.add_cabinet_we(7, 5)

        level.add_cop(3, 0, DIR_S)
        level.add_cop(0, 5, DIR_E)
        level.add_cop(8, 6, DIR_W)
        level.add_cop(6, 8, DIR_N)

        level.add_victim(3, 1)
        level.add_victim(6, 3)
        level.add_victim(1, 5)
        level.add_victim(3, 6)

        return level

    @staticmethod
    def nc17_s1_s01():

        level = Level('Slayaway Camp 1 (NC17), Scene 1 - Last Day of Camp', 7, 2,
            3, 1,
            6, 1)

        level.electric_south(2, 0)
        level.electric_east(2, 0)
        level.electric_south(3, 0)
        level.electric_east(3, 0)
        level.electric_south(4, 0)

        level.set_sticky(2, 1)
        level.set_sticky(4, 1)
        
        level.switch_west(0, 0)

        level.add_cabinet_we(1, 0)
        level.add_cabinet_we(5, 0)

        level.add_victim(2, 0)
        level.add_victim(3, 0)
        level.add_victim(4, 0)

        return level

    @staticmethod
    def nc17_s1_s02():

        level = Level('Slayaway Camp 1 (NC17), Scene 2 - Safety First', 6, 6,
            0, 1,
            0, 1)

        level.wall_east(3, 0)
        level.wall_south(3, 0)
        level.wall_east(3, 1)
        level.wall_east(3, 2)
        level.wall_south(4, 2)
        level.wall_south(5, 2)
        level.wall_south(4, 3)
        level.wall_south(5, 3)
        level.wall_east(3, 4)
        level.wall_east(3, 5)

        level.wall_box(0, 2)
        level.wall_box(1, 2)

        level.wall_south(3, 0)
        level.set_mine(1, 3)

        level.add_phone_pair(0, 3, 3, 5)

        level.add_cop(3, 0, DIR_S)
        level.add_cop(3, 3, DIR_S)
        level.add_victim(4, 3)
        level.add_victim(5, 3)

        return level

    @staticmethod
    def nc17_s1_s03():

        level = Level('Slayaway Camp 1 (NC17), Scene 3 - Camp of the Damned', 6, 7,
            2, 6,
            0, 0)

        # Walls
        level.wall_east(0, 0)

        level.wall_south(0, 3)
        level.wall_south(1, 3)
        level.wall_south(2, 3)
        level.wall_south(5, 3)

        level.wall_east(0, 4)
        level.wall_south(0, 4)

        level.wall_box(3, 5)
        level.wall_box(3, 6)

        level.wall_west(1, 1)
        level.wall_south(1, 1)
        level.wall_south(2, 1)
        level.wall_east(2, 1)
        level.wall_east(2, 0)

        level.set_sticky(4, 4)
        level.set_sticky(1, 5)

        level.add_cabinet_ns(3, 0)
        level.add_cabinet_ns(5, 0)

        level.add_swat(4, 0, DIR_S)

        level.add_victim(3, 3)
        level.add_victim(4, 3)
        level.add_victim(1, 5)
        level.add_victim(5, 5)

        return level

    @staticmethod
    def nc17_s1_s04():

        level = Level('Slayaway Camp 1 (NC17), Scene 4 - The Hills Have Noses', 6, 6,
            3, 4,
            2, 5,
            7)

        level.wall_north(0, 4)
        level.wall_east(0, 3)
        level.wall_east(0, 2)
        level.wall_east(0, 1)
        level.wall_north(0, 1)

        level.wall_box(5, 4)
        level.wall_box(3, 2)

        level.add_cabinet_ns(4, 1)
        level.add_cabinet_we(1, 5)

        level.add_victim(1, 2)
        level.add_victim(4, 3)

        return level

    @staticmethod
    def nc17_s1_s05():

        level = Level('Slayaway Camp 1 (NC17), Scene 5 - Demonwarp Woods', 7, 6,
            3, 3,
            4, 3,
            10)

        level.wall_east(0, 0)
        level.wall_east(0, 1)
        level.wall_east(0, 2)
        level.wall_east(1, 4)
        level.wall_north(3, 4)
        level.wall_west(6, 3)
        level.wall_west(6, 2)

        level.wall_west(4, 5)
        level.wall_north(4, 5)
        level.wall_north(5, 5)
        level.wall_north(6, 5)

        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_east(2, 0)

        level.add_victim(0, 4)
        level.add_victim(3, 1)
        level.add_victim(5, 2)

        return level

    @staticmethod
    def nc17_s1_s06():

        level = Level('Slayaway Camp 1 (NC17), Scene 6 - A Slash in Time', 5, 6,
            1, 5,
            3, 4)

        level.wall_east(0, 5)
        level.wall_east(0, 4)
        level.wall_north(0, 4)
        level.wall_east(0, 0)
        level.wall_south(1, 0)
        level.wall_south(2, 0)
        level.wall_south(4, 0)
        level.wall_west(3, 1)
        level.wall_east(3, 1)
        level.wall_west(3, 2)
        level.wall_east(3, 2)
        level.wall_south(3, 2)
        level.wall_box(3, 5)

        level.set_sticky(1, 1)
        level.set_sticky(1, 3)
        level.set_sticky(2, 3)

        level.add_phone_pair(0, 0, 4, 1)

        level.add_cabinet_ns(0, 2)

        level.add_cop(4, 5, DIR_N)
        level.add_victim(1, 2)
        level.add_victim(1, 3)
        level.add_victim(4, 4)
        level.add_cat(0, 1)

        return level

    @staticmethod
    def nc17_s1_s07():

        level = Level('Slayaway Camp 1 (NC17), Scene 7 - Flames of Fear', 6, 6,
            0, 3,
            5, 4,
            10)

        level.wall_box(0, 5)
        level.wall_box(3, 4)
        level.wall_box(4, 3)
        level.wall_box(1, 1)

        level.wall_east(2, 0)
        level.wall_south(3, 0)
        level.wall_west(4, 1)
        level.wall_south(4, 1)
        level.wall_south(5, 1)

        level.set_hazard(2, 2)

        level.add_victim(2, 1)
        level.add_victim(3, 2)
        level.add_victim(2, 3)
        level.add_victim(1, 4)

        return level

    @staticmethod
    def nc17_s1_s08():

        level = Level('Slayaway Camp 1 (NC17), Scene 8 - Polynesian Peril', 8, 6,
            5, 1,
            0, 0)

        level.wall_west(6, 5)
        level.wall_north(6, 5)
        level.wall_north(7, 5)

        level.wall_east(1, 5)
        level.wall_north(1, 5)
        level.wall_north(0, 5)
        level.wall_north(0, 3)
        level.wall_box(1, 0)
        level.wall_box(5, 0)
        level.wall_box(7, 0)
        level.wall_box(7, 1)

        level.wall_south(3, 2)
        level.wall_box(4, 2)

        level.wall_south(2, 3)
        level.wall_south(3, 3)
        level.wall_south(4, 3)
        level.wall_south(5, 3)

        level.set_hazard(1, 3)
        level.set_hazard(6, 3)

        level.set_sticky(1, 1)
        level.set_sticky(3, 1)
        level.set_sticky(4, 1)
        level.set_sticky(5, 1)
        level.set_sticky(5, 2)

        level.set_mine(4, 4)

        level.add_phone_pair(0, 3, 4, 0)
        level.add_phone_pair(3, 0, 7, 4)
        level.add_phone_pair(2, 0, 6, 0)

        level.add_victim(0, 4)
        level.add_victim(1, 4)
        level.add_victim(2, 3)
        level.add_victim(7, 2)
        level.add_cat(6, 2)

        return level

    @staticmethod
    def nc17_s1_s09():

        level = Level('Slayaway Camp 1 (NC17), Scene 9 - Death Becomes You', 5, 6,
            3, 1,
            3, 3,
            10)

        level.wall_box(3, 5)
        level.wall_box(4, 3)
        level.wall_box(4, 0)

        level.wall_east(0, 5)
        level.wall_east(0, 4)
        level.wall_north(0, 4)

        level.electric_north(1, 1)
        level.electric_south(2, 1)
        level.electric_south(3, 1)
        level.electric_south(1, 2)
        level.electric_south(2, 2)

        level.switch_north(0, 0)

        level.add_victim(1, 2)
        level.add_victim(1, 3)
        
        return level

    @staticmethod
    def nc17_s1_s10():

        # Fudging the exit a bit, here.  The actual level
        # is special-cased so that you win when you scare
        # the victim into the hole.
        level = Level('Slayaway Camp 1 (NC17), Scene 10 - Hole In One', 6, 6,
            5, 0,
            4, 5)

        level.set_hazard(5, 5)
        level.set_hazard(1, 5)

        level.wall_west(1, 0)
        level.wall_south(1, 0)
        level.wall_east(1, 1)
        level.wall_south(3, 0)
        level.wall_east(4, 0)
        level.wall_south(5, 1)
        level.wall_south(0, 2)
        level.wall_east(3, 2)
        level.wall_south(3, 2)
        level.wall_east(1, 3)
        level.wall_south(3, 3)
        level.wall_south(5, 3)
        level.wall_south(2, 4)
        level.wall_south(3, 4)

        level.set_sticky(3, 1)
        level.set_sticky(2, 3)
        level.set_sticky(3, 3)
        level.set_sticky(1, 4)
        level.set_sticky(2, 4)

        level.add_phone_pair(0, 0, 4, 2)

        level.add_swat(0, 2, DIR_E)
        level.add_victim(2, 2)
        level.add_victim(2, 4)
        level.add_victim(3, 5)
        level.add_victim(4, 5)

        return level
