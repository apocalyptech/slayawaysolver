#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4 fileencoding=utf-8:

from slaysolver.app import Level, DIR_N, DIR_S, DIR_E, DIR_W

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

def nc17_s25_s04():

    level = Level('Slayaway Camp 2.5 (NC17), Scene 4 - somethingsomething', 7, 6,
        1, 2,
        1, 1)

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

    level.electric_north(1, 1)
    level.electric_south(1, 1)
    level.electric_south(3, 1)

    level.switch_north(2, 0)
    level.switch_north(4, 0)

    level.set_mine(1, 1)
    level.set_sticky(5, 2)
    level.set_sticky(4, 3)

    level.add_cop(3, 3, DIR_S)
    level.add_cop(5, 4, DIR_S)
    level.add_cop(6, 5, DIR_W)

    level.add_victim(3, 1)
    level.add_victim(4, 1)
    level.add_victim(2, 3)
    level.add_victim(4, 4)

    return level
