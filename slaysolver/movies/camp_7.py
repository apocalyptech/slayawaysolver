#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4 fileencoding=utf-8:

from slaysolver.app import Level, DIR_N, DIR_S, DIR_E, DIR_W

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
