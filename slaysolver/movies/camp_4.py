#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4 fileencoding=utf-8:

from slaysolver.app import Level, DIR_N, DIR_S, DIR_E, DIR_W

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
