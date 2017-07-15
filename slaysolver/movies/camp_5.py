#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4 fileencoding=utf-8:

from slaysolver.app import Level, DIR_N, DIR_S, DIR_E, DIR_W

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
