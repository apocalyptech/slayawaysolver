#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4 fileencoding=utf-8:

from slaysolver.app import Level, DIR_N, DIR_S, DIR_E, DIR_W

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

def s8_d3():

    # One of our harder levels to solve, though s10_d4 beats it out.  All
    # the cabinets + goo make for a very wide solve tree.

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
