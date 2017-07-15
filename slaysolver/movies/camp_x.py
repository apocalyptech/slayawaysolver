#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4 fileencoding=utf-8:

from slaysolver.app import Level, DIR_N, DIR_S, DIR_E, DIR_W

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

def s10_d4():

    # This is another monster to solve - much worse than 8.D3, in fact.
    # Using breadth-first search and PyPy3 on my CPU yields a solve time of a
    # little over a minute.  The old depth-first algorithm took seven minutes
    # with PyPy3.  We're omitting this from our "unit" tests due to the solve
    # time, though with the new algorithm it's not really that bad.

    level = Level('Slayaway Camp X, Deleted Scene 4 - As Hard as it Looks', 9, 9,
        1, 8,
        7, 6)

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
