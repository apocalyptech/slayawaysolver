#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import re
from slaysolver.app import Level, DIR_N, DIR_S, DIR_E, DIR_W

class Levels(object):

    def __init__(self):
        self.levels = {}
        self.level_names = []
        levelre = re.compile('^s\d+_[sd]\d+$')
        for (name, method) in Levels.__dict__.items():
            match = levelre.match(name)
            if match:
                self.level_names.append(name)
                self.levels[name] = method.__func__
        self.level_names.sort()

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
    def s1_s06():

        level = Level('Slayaway Camp 1, Scene 6', 5, 6,
            1, 4,
            0, 0)

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

        level.add_victim(4, 3)
        level.add_victim(4, 4)

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

        level.add_phone_pair(2, 0, 6, 6, '1')

        level.add_cop(2, 3, DIR_S)
        level.add_victim(3, 6)

        return level

    @staticmethod
    def s6_d4():

        level = Level('Slayaway Camp 6, Deleted Scene 4', 9, 9,
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
