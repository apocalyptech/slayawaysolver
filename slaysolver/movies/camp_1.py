#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4 fileencoding=utf-8:

from slaysolver.app import Level, DIR_N, DIR_S, DIR_E, DIR_W

def s1_s01():

    level = Level('Slayaway Camp 1, Scene 1', 7, 2,
        0, 1,
        0, 1)

    # Victim
    level.add_victim(4, 0)

    # Return
    return level

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
