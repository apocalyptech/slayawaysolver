#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

import re
from slaysolver.app import Level

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

    @staticmethod
    def s1_s01():

        level = Level('Slayaway Camp 1, Scene 1',
            2, 8,
            2, 8)

        # Simplifying the walls in here, very limited level
        for x in range(2, 9):
            level.wall_south(x, 6)
        level.wall_east(1, 7)
        level.wall_east(1, 8)

        # Victim
        level.add_victim(6, 7)

        # Return
        return level

    @staticmethod
    def s1_s02():

        level = Level('Slayaway Camp 1, Scene 2',
            3, 4,
            3, 4)

        # Walls
        level.wall_east(2, 3)
        level.wall_east(2, 4)
        level.wall_east(2, 6)
        level.wall_east(2, 7)
        level.wall_east(2, 8)
        level.wall_south(3, 2)
        level.wall_south(4, 2)
        level.wall_south(5, 2)
        level.wall_south(6, 2)
        level.wall_east(6, 3)
        level.wall_south(6, 3)
        level.wall_east(6, 4)
        level.wall_east(6, 5)
        level.wall_south(7, 5)
        level.wall_south(8, 5)
        level.wall_south(7, 6)
        level.wall_south(8, 6)
        level.wall_east(6, 7)
        level.wall_east(6, 8)

        level.wall_box(3, 5)
        level.wall_box(4, 5)

        # Victim
        level.add_victim(8, 6)

        # Return
        return level

    @staticmethod
    def s1_s03():

        level = Level('Slayaway Camp 1, Scene 3',
            4, 7,
            3, 2)

        # Walls
        level.wall_west(3, 2)
        level.wall_north(3, 2)
        level.wall_east(3, 2)

        level.wall_west(3, 3)
        level.wall_west(3, 4)
        level.wall_west(3, 5)
        level.wall_south(3, 5)
        level.wall_south(4, 5)
        level.wall_south(5, 5)
        level.wall_south(8, 5)

        level.wall_east(3, 6)
        level.wall_south(3, 6)
        level.wall_west(3, 7)
        level.wall_west(3, 8)

        level.wall_box(6, 7)
        level.wall_box(6, 8)

        level.wall_west(4, 3)
        level.wall_south(4, 3)
        level.wall_south(5, 3)
        level.wall_east(5, 3)
        level.wall_east(5, 2)
        level.wall_north(6, 2)
        level.wall_north(7, 2)
        level.wall_north(8, 2)

        level.add_victim(7, 2)
        level.add_victim(4, 5)

        return level

    @staticmethod
    def s1_s04():

        level = Level('Slayaway Camp 1, Scene 4',
            3, 7,
            5, 7)

        level.wall_west(3, 8)
        level.wall_west(3, 7)
        level.wall_north(3, 7)
        level.wall_east(3, 6)
        level.wall_east(3, 5)
        level.wall_east(3, 4)
        level.wall_north(3, 4)
        level.wall_west(3, 3)
        level.wall_north(3, 3)
        level.wall_north(4, 3)
        level.wall_north(5, 3)
        level.wall_north(6, 3)
        level.wall_north(7, 3)
        level.wall_north(8, 3)

        level.wall_box(8, 7)
        level.wall_box(6, 5)

        level.add_victim(4, 5)
        level.add_victim(7, 6)

        return level

    @staticmethod
    def s1_s05():

        level = Level('Slayaway Camp 1, Scene 5',
            2, 3,
            5, 3)

        level.wall_north(2, 3)
        level.wall_west(2, 3)
        level.wall_east(2, 3)
        level.wall_west(2, 4)
        level.wall_east(2, 4)
        level.wall_west(2, 5)
        level.wall_east(2, 5)
        level.wall_west(2, 6)
        level.wall_west(2, 7)
        level.wall_west(2, 8)
        level.wall_east(3, 7)
        level.wall_north(5, 7)
        level.wall_west(8, 6)
        level.wall_west(8, 5)

        level.wall_west(6, 8)
        level.wall_north(6, 8)
        level.wall_north(7, 8)
        level.wall_north(8, 8)

        level.wall_south(3, 3)
        level.wall_south(4, 3)
        level.wall_east(4, 3)
        level.wall_north(5, 3)
        level.wall_north(6, 3)
        level.wall_north(7, 3)
        level.wall_north(8, 3)

        level.add_victim(2, 6)
        level.add_victim(3, 6)
        level.add_victim(7, 5)

        return level

    @staticmethod
    def s1_s06():

        level = Level('Slayaway Camp 1, Scene 6',
            5, 7,
            4, 3)

        level.wall_east(4, 8)
        level.wall_east(4, 7)
        level.wall_north(4, 7)
        level.wall_west(4, 6)
        level.wall_west(4, 5)
        level.wall_west(4, 4)
        level.wall_west(4, 3)
        level.wall_north(4, 3)
        level.wall_east(4, 3)
        level.wall_south(5, 3)
        level.wall_south(6, 3)
        level.wall_south(8, 3)
        level.wall_west(7, 4)
        level.wall_east(7, 4)
        level.wall_west(7, 5)
        level.wall_east(7, 5)
        level.wall_south(7, 5)
        level.wall_box(7, 8)

        level.add_victim(8, 6)
        level.add_victim(8, 7)

        return level

    @staticmethod
    def s1_s07():

        level = Level('Slayaway Camp 1, Scene 7',
            8, 8,
            3, 6)

        level.wall_box(3, 8)
        level.wall_box(6, 7)
        level.wall_box(7, 6)
        level.wall_box(4, 4)

        level.wall_west(3, 7)
        level.wall_west(3, 6)
        level.wall_west(3, 5)
        level.wall_west(3, 4)
        level.wall_west(3, 3)
        level.wall_north(3, 3)
        level.wall_north(4, 3)
        level.wall_north(5, 3)
        level.wall_east(5, 3)
        level.wall_south(6, 3)
        level.wall_west(7, 4)
        level.wall_south(7, 4)
        level.wall_south(8, 4)

        level.set_hazard(5, 5)

        level.add_victim(5, 4)
        level.add_victim(5, 7)
        level.add_victim(5, 8)
        level.add_victim(7, 5)

        return level

    @staticmethod
    def s1_s08():

        level = Level('Slayaway Camp 1, Scene 8',
            4, 8,
            7, 3)

        level.wall_west(7, 8)
        level.wall_north(7, 8)
        level.wall_north(8, 8)

        level.wall_east(2, 8)
        level.wall_north(2, 8)
        level.wall_north(1, 8)
        level.wall_west(1, 7)
        level.wall_west(1, 6)
        level.wall_north(1, 6)
        level.wall_west(1, 5)
        level.wall_west(1, 4)
        level.wall_west(1, 3)
        level.wall_north(1, 3)
        level.wall_box(2, 3)
        level.wall_north(3, 3)
        level.wall_north(4, 3)
        level.wall_north(5, 3)
        level.wall_box(6, 3)
        level.wall_box(8, 3)
        level.wall_box(8, 4)

        level.wall_south(4, 5)
        level.wall_box(5, 5)

        level.wall_south(3, 6)
        level.wall_south(4, 6)
        level.wall_south(5, 6)
        level.wall_south(6, 6)

        level.set_hazard(2, 6)
        level.set_hazard(7, 6)

        level.add_victim(4, 6)

        return level

    @staticmethod
    def s1_s09():

        level = Level('Slayaway Camp 1, Scene 9',
            6, 8,
            8, 8,
            6)

        level.wall_box(7, 8)
        level.wall_box(8, 6)
        level.wall_box(8, 3)

        level.wall_east(4, 8)
        level.wall_east(4, 7)
        level.wall_north(4, 7)
        level.wall_west(4, 6)
        level.wall_west(4, 5)
        level.wall_west(4, 4)
        level.wall_west(4, 3)
        level.wall_north(4, 3)
        level.wall_north(5, 3)
        level.wall_north(6, 3)
        level.wall_north(7, 3)

        level.add_victim(6, 4)
        
        return level

    @staticmethod
    def s1_s10():

        # Fudging the exit a bit, here.  The actual level
        # is special-cased so that you win when you scare
        # the victim into the hole.
        level = Level('Slayaway Camp 1, Scene 10',
            8, 7,
            7, 8)

        level.set_hazard(8, 8)
        level.set_hazard(4, 8)

        level.add_victim(6, 8)

        for y in range(3, 9):
            level.wall_west(3, y)
        for x in range(3, 9):
            level.wall_north(x, 3)

        level.short_wall_west(4, 3)
        level.short_wall_south(4, 3)
        level.short_wall_east(4, 4)

        level.short_wall_south(6, 3)

        level.short_wall_east(7, 3)

        level.short_wall_south(8, 4)

        level.short_wall_south(3, 5)

        level.short_wall_east(6, 5)
        level.short_wall_south(6, 5)

        level.short_wall_east(4, 6)

        level.short_wall_south(6, 6)

        level.wall_south(8, 6)

        level.wall_south(5, 7)
        level.wall_south(6, 7)

        return level

    @staticmethod
    def s1_d1():

        level = Level('Slayaway Camp 1, Deleted Scene 1',
            7, 8,
            5, 6)

        level.wall_west(2, 8)
        level.wall_west(2, 7)
        level.wall_west(2, 6)
        level.wall_west(2, 5)
        level.wall_south(2, 4)
        level.wall_east(2, 4)
        level.wall_south(3, 3)
        level.wall_east(3, 3)
        level.wall_east(3, 2)
        level.wall_north(4, 2)
        level.wall_north(5, 2)
        level.wall_north(6, 2)
        level.wall_west(7, 2)
        level.wall_south(7, 2)
        level.wall_west(8, 3)
        level.wall_west(8, 4)
        level.wall_south(8, 4)

        level.wall_box(5, 8)
        level.wall_box(8, 7)
        level.wall_box(8, 8)

        level.wall_west(4, 5)
        level.wall_east(4, 5)
        level.wall_west(4, 6)

        level.wall_south(6, 3)
        level.wall_south(6, 5)
        level.wall_south(5, 6)
        level.wall_south(7, 6)

        level.set_hazard(4, 2)
        level.set_hazard(4, 8)
        level.set_hazard(6, 4)

        level.add_victim(4, 4)

        return level

    @staticmethod
    def s1_d2():

        level = Level('Slayaway Camp 1, Deleted Scene 2',
            6, 6,
            6, 5,
            10)

        for y in range(3, 9):
            level.wall_west(3, y)
        for x in range(3, 9):
            level.wall_north(x, 3)

        level.wall_box(4, 4)
        level.wall_box(4, 5)
        level.wall_box(7, 4)
        level.wall_box(6, 7)
        level.wall_box(7, 7)
        level.wall_box(5, 8)

        level.add_victim(4, 3)
        level.add_victim(3, 8)
        level.add_victim(8, 6)

        return level

    @staticmethod
    def s1_d3():

        level = Level('Slayaway Camp 1, Deleted Scene 3',
            2, 3,
            2, 2)

        level.wall_east(4, 8)
        level.wall_north(4, 8)
        level.wall_east(3, 7)
        level.wall_north(3, 7)
        level.wall_north(2, 7)
        level.wall_west(2, 6)
        level.wall_west(2, 5)
        level.wall_south(2, 4)
        level.wall_east(2, 4)
        level.wall_north(2, 4)
        level.wall_west(2, 3)
        level.wall_west(2, 2)
        level.wall_south(2, 1)
        level.wall_east(2, 1)
        level.wall_north(3, 1)
        level.wall_west(4, 1)
        level.wall_south(4, 1)
        level.wall_east(4, 1)
        level.wall_north(5, 1)
        level.wall_west(6, 1)
        level.wall_south(6, 1)
        level.wall_west(7, 2)
        level.wall_south(7, 2)
        level.wall_east(7, 2)
        level.wall_south(8, 1)

        level.wall_north(8, 6)
        level.wall_north(7, 6)
        level.wall_west(7, 6)
        level.wall_west(7, 7)
        level.wall_south(7, 7)
        level.wall_south(8, 7)
        
        level.wall_box(5, 3)
        level.wall_box(2, 4)

        level.add_victim(7, 5)
        level.add_victim(4, 6)
        level.add_victim(3, 1)
        level.add_victim(5, 1)

        return level

    @staticmethod
    def s1_d4():

        level = Level('Slayaway Camp 1, Deleted Scene 4',
            3, 8,
            2, 8)

        for y in range(1, 9):
            level.wall_west(1, y)
        for x in range(1, 9):
            level.wall_north(x, 1)

        level.short_wall_west(4, 1)
        level.short_wall_south(4, 1)
        level.short_wall_south(6, 1)
        level.short_wall_west(7, 2)
        level.short_wall_west(7, 3)
        level.short_wall_south(7, 3)
        level.short_wall_south(8, 3)

        level.short_wall_south(3, 4)

        level.short_wall_south(1, 5)

        level.short_wall_south(7, 5)
        level.short_wall_south(8, 5)

        level.short_wall_south(6, 6)

        level.short_wall_west(5, 8)
        level.short_wall_east(6, 8)

        level.wall_box(1, 8)

        level.set_hazard(5, 1)
        level.set_hazard(2, 3)

        level.set_hazard(1, 6)
        level.set_hazard(2, 6)
        level.set_hazard(3, 6)
        level.set_hazard(1, 7)

        level.set_hazard(6, 6)
        level.set_hazard(7, 6)
        level.set_hazard(8, 6)
        level.set_hazard(7, 7)
        level.set_hazard(8, 7)
        level.set_hazard(7, 8)
        level.set_hazard(8, 8)

        level.add_victim(6, 3)
        level.add_victim(6, 4)
        level.add_victim(2, 4)
        level.add_victim(2, 7)

        return level

    @staticmethod
    def s1_d5():

        level = Level('Slayaway Camp 1, Deleted Scene 5',
            2, 3,
            6, 3)

        for y in range(1, 9):
            level.wall_west(2, y)
        for x in range(2, 9):
            level.wall_north(x, 1)

        level.wall_box(3, 1)
        level.wall_box(8, 5)

        level.wall_east(3, 3)
        level.wall_east(3, 5)
        level.wall_south(2, 7)
        level.wall_south(5, 4)
        level.wall_east(6, 5)
        level.wall_south(6, 5)
        level.wall_east(6, 6)
        level.wall_west(6, 7)
        level.wall_south(6, 7)
        level.wall_south(7, 7)

        level.set_hazard(2, 1)
        level.set_hazard(8, 3)
        level.set_hazard(8, 4)
        level.set_hazard(4, 5)
        level.set_hazard(5, 5)
        level.set_hazard(6, 5)

        level.add_victim(5, 4)
        level.add_victim(7, 5)
        level.add_victim(5, 6)

        return level

    @staticmethod
    def s6_d4():

        level = Level('Slayaway Camp 6, Deleted Scene 4',
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
        level.add_obstacle(1, 2, Cabinet([DIR_W, DIR_E], level))
        level.add_obstacle(4, 2, Cabinet([DIR_N, DIR_S], level))
        level.add_obstacle(6, 2, Cabinet([DIR_W, DIR_E], level))

        # Victims
        level.add_victim(1, 3)
        level.add_victim(6, 3)

        # Return
        return level
