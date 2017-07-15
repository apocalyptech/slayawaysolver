#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4 fileencoding=utf-8:

from slaysolver.app import Level, DIR_N, DIR_S, DIR_E, DIR_W

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
