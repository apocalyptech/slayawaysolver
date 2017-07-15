#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4 fileencoding=utf-8:

from slaysolver.app import Level, DIR_N, DIR_S, DIR_E, DIR_W

def s6_s01():

    level = Level('Slayaway Camp 6, Scene 1 - Lights Out', 6, 6,
        0, 5,
        4, 3)

    level.wall_south(0, 1)
    level.wall_east(0, 1)
    level.wall_east(0, 0)

    level.wall_west(3, 0)
    level.wall_south(3, 0)
    level.wall_south(4, 0)
    level.wall_east(4, 1)
    level.wall_south(4, 1)
    level.wall_south(3, 1)
    level.wall_west(3, 2)
    level.wall_south(3, 2)
    level.wall_south(4, 2)
    level.wall_south(5, 2)

    level.wall_west(3, 5)
    level.wall_north(3, 5)
    level.wall_north(4, 5)
    level.wall_east(4, 5)

    level.wall_east(0, 3)
    level.wall_east(0, 4)
    level.wall_east(0, 5)

    level.switch_north(0, 2)

    level.add_swat(2, 2, DIR_S)
    level.add_cop(5, 3, DIR_S)
    level.add_victim(1, 5)

    return level

def s6_s02():

    level = Level('Slayaway Camp 6, Scene 2 - SWAT Stealth Slash', 6, 6,
        2, 5,
        5, 1)

    level.wall_box(0, 0)
    level.wall_box(2, 2)
    level.wall_box(4, 4)

    level.wall_south(1, 2)
    level.wall_east(2, 0)
    level.wall_east(2, 1)
    level.wall_east(2, 5)

    level.switch_north(2, 0)

    level.add_swat(2, 3, DIR_E)
    level.add_swat(5, 2, DIR_W)
    level.add_victim(3, 1)

    return level

def s6_s03():

    level = Level('Slayaway Camp 6, Scene 3 - Fatality Ward', 8, 8,
        0, 0,
        2, 1,
        10)

    level.wall_box(4, 7)
    level.wall_box(6, 2)
    
    level.wall_north(7, 6)
    level.wall_west(7, 6)
    level.wall_west(7, 7)

    level.wall_west(1, 2)
    level.wall_west(1, 1)
    level.wall_north(1, 1)
    level.wall_north(2, 1)
    level.wall_north(3, 1)
    level.wall_east(3, 1)
    level.wall_east(3, 2)

    level.wall_west(1, 4)
    level.wall_west(1, 5)
    level.wall_south(1, 5)
    level.wall_south(2, 5)

    level.wall_east(2, 4)

    level.wall_north(4, 5)
    level.wall_south(4, 5)
    level.wall_north(5, 5)
    level.wall_south(5, 5)
    level.wall_north(6, 5)
    level.wall_north(7, 5)

    level.add_cabinet_ns(3, 5)

    level.add_victim(7, 1)
    level.add_victim(6, 4)
    level.add_victim(5, 5)

    return level

def s6_s04():

    level = Level('Slayaway Camp 6, Scene 4 - Kitty Care', 7, 6,
        5, 5,
        0, 3)

    level.wall_box(0, 0)
    level.wall_box(4, 0)
    level.wall_box(0, 5)
    level.wall_box(4, 5)

    level.wall_east(1, 1)
    level.wall_east(1, 2)
    level.wall_east(1, 3)

    level.wall_north(6, 3)
    level.wall_west(6, 3)
    level.wall_west(6, 4)
    level.wall_west(6, 5)

    level.escape_north(2)
    level.escape_west(4)

    level.switch_north(5, 0)

    level.add_victim(2, 1)
    level.add_victim(2, 5)
    level.add_cat(2, 3)

    return level

def s6_s05():

    level = Level('Slayaway Camp 6, Scene 5 - A Phone in the Dark', 7, 6,
        1, 4,
        2, 0)

    level.wall_south(0, 2)
    level.wall_east(0, 2)
    level.wall_east(0, 1)
    level.wall_east(0, 0)

    level.wall_west(3, 0)
    level.wall_south(3, 0)
    level.wall_south(4, 0)
    level.wall_south(5, 0)
    level.wall_south(6, 0)

    level.wall_west(4, 3)
    level.wall_north(4, 3)
    level.wall_south(4, 3)
    level.wall_north(5, 3)
    level.wall_south(5, 3)
    level.wall_east(5, 3)

    level.wall_box(6, 5)

    level.short_wall_west(2, 0)
    level.short_wall_west(2, 1)
    level.short_wall_south(2, 1)
    level.short_wall_east(2, 2)

    level.switch_west(1, 1)

    level.add_phone_pair(6, 1, 5, 5)

    level.add_swat(4, 1, DIR_W)
    level.add_swat(2, 5, DIR_E)

    level.add_victim(1, 0)
    level.add_victim(3, 2)
    level.add_victim(0, 5)

    return level

def s6_s06():

    level = Level('Slayaway Camp 6, Scene 6 - Visiting Hours', 7, 7,
        2, 4,
        4, 0)

    level.wall_east(0, 0)
    level.wall_east(0, 1)
    level.wall_east(0, 2)
    level.wall_east(0, 3)
    level.wall_south(0, 3)

    level.wall_north(0, 5)
    level.wall_east(0, 5)
    level.wall_north(1, 6)
    level.wall_north(2, 6)
    level.wall_east(2, 6)

    level.wall_south(5, 0)
    level.wall_south(6, 0)

    level.wall_east(3, 1)

    level.wall_east(5, 3)
    level.wall_east(5, 4)
    level.wall_south(5, 4)
    level.wall_south(4, 4)

    level.short_wall_west(2, 0)

    level.short_wall_west(2, 2)
    level.short_wall_west(2, 3)
    level.short_wall_south(2, 3)
    level.short_wall_south(3, 3)

    level.add_phone_pair(0, 4, 3, 1)

    level.add_swat(1, 1, DIR_S)

    level.add_victim(1, 0)
    level.add_victim(2, 1)
    level.add_victim(3, 5)

    return level

def s6_s07():

    level = Level('Slayaway Camp 6, Scene 7 - No Escape', 8, 7,
        1, 5,
        1, 1)

    level.wall_north(2, 1)
    level.wall_west(2, 1)
    level.wall_east(2, 1)
    level.wall_west(2, 2)
    level.wall_east(2, 2)
    level.wall_south(2, 2)

    level.wall_north(5, 1)
    level.wall_west(5, 1)
    level.wall_east(5, 1)
    level.wall_west(5, 2)
    level.wall_east(5, 2)
    level.wall_south(5, 2)

    level.wall_north(0, 6)
    level.wall_north(1, 6)
    level.wall_east(1, 6)

    level.wall_box(7, 6)

    level.wall_east(3, 5)
    level.wall_east(5, 6)

    level.short_wall_south(1, 3)
    level.short_wall_south(2, 3)
    level.short_wall_south(3, 3)
    level.short_wall_south(4, 3)

    level.escape_north(3)
    level.escape_north(4)
    level.escape_west(3)

    level.add_cabinet_we(2, 0)
    level.add_cabinet_we(5, 0)

    level.set_hazard(2, 3)

    level.add_victim(3, 3)
    level.add_victim(4, 3)
    level.add_cat(1, 3)
    level.add_cat(6, 3)

    return level

def s6_s08():

    level = Level('Slayaway Camp 6, Scene 8 - The Burn Ward', 8, 8,
        3, 4,
        7, 2)

    level.wall_north(0, 5)
    level.wall_east(0, 5)
    level.wall_south(1, 5)
    level.wall_east(0, 6)
    level.wall_east(0, 7)

    level.wall_box(7, 0)
    level.wall_box(7, 3)
    level.wall_box(5, 7)

    level.wall_south(4, 0)
    level.wall_east(4, 4)
    level.short_wall_east(2, 1)
    level.short_wall_east(2, 2)

    level.set_hazard(1, 1)
    level.switch_west(0, 0)

    level.add_swat(6, 0, DIR_W)
    level.add_swat(7, 1, DIR_N)

    level.add_victim(0, 3)
    level.add_victim(1, 3)
    level.add_victim(5, 3)
    level.add_cat(3, 2)

    return level

def s6_s09():

    level = Level('Slayaway Camp 6, Scene 9 - Pre-Op Peril', 7, 7,
        4, 3,
        3, 4)

    level.wall_box(3, 5)
    level.wall_box(5, 4)
    level.wall_box(6, 6)

    level.wall_east(5, 0)
    level.wall_south(5, 0)
    level.wall_west(5, 1)
    level.wall_south(5, 1)
    level.wall_west(6, 2)
    level.wall_south(6, 2)

    level.wall_east(3, 2)
    level.wall_east(2, 4)

    level.switch_north(5, 0)

    level.add_phone_pair(0, 4, 1, 0)

    level.add_swat(2, 4, DIR_N)
    level.add_swat(2, 5, DIR_S)

    level.add_victim(1, 3)

    return level

def s6_s10():

    level = Level('Slayaway Camp 6, Scene 10 - Dumcops in the Dark', 7, 7,
        1, 5,
        5, 6,
        10)

    level.wall_north(0, 5)
    level.wall_east(0, 5)
    level.wall_north(1, 6)
    level.wall_east(1, 6)

    level.wall_west(6, 0)
    level.wall_west(6, 1)
    level.wall_south(6, 1)

    level.short_wall_north(2, 1)
    level.short_wall_north(3, 1)
    level.short_wall_north(4, 1)
    level.short_wall_west(4, 1)

    level.short_wall_south(3, 4)
    level.short_wall_south(4, 4)

    level.short_wall_east(5, 3)
    level.short_wall_east(5, 4)
    level.short_wall_east(5, 5)

    level.switch_north(0, 0)
    level.switch_north(1, 0)

    level.set_mine(3, 2)
    level.set_mine(2, 3)
    level.set_mine(4, 3)
    level.set_mine(5, 1)

    level.add_phone_pair(3, 3, 5, 0)

    level.add_cop(6, 2, DIR_W)
    level.add_cop(2, 4, DIR_W)

    level.add_victim(3, 1)
    level.add_victim(2, 2)
    level.add_victim(5, 3)
    level.add_victim(5, 4)

    return level

def s6_s11():

    level = Level('Slayaway Camp 6, Scene 11 - The Operating Doom', 7, 7,
        3, 2,
        0, 4)

    level.wall_box(4, 1)

    level.wall_south(0, 0)
    level.wall_south(1, 0)
    level.wall_south(2, 0)
    level.wall_east(2, 0)

    level.wall_west(6, 0)
    level.wall_west(6, 1)
    level.wall_south(6, 1)

    level.wall_west(1, 2)
    level.wall_north(1, 2)
    level.wall_south(1, 2)
    level.wall_north(2, 2)
    level.wall_south(2, 2)
    level.wall_east(2, 2)

    level.wall_north(0, 6)
    level.wall_north(1, 6)
    level.wall_west(2, 5)
    level.wall_north(2, 5)
    level.wall_east(2, 5)
    level.wall_east(2, 6)

    level.wall_south(0, 3)
    level.wall_south(1, 3)
    level.wall_east(3, 3)
    level.wall_east(3, 4)
    level.wall_north(5, 3)
    level.wall_east(5, 3)

    level.short_wall_south(3, 5)
    level.short_wall_south(4, 5)
    level.short_wall_south(5, 5)
    level.short_wall_east(5, 5)

    level.add_cop(1, 3, DIR_E)
    level.add_victim(2, 4)
    level.add_victim(4, 4)

    return level

def s6_s12():

    level = Level('Slayaway Camp 6, Scene 12 - Light vs. Dark', 8, 8,
        3, 0,
        4, 4)

    level.wall_east(0, 0)
    level.wall_east(0, 1)
    level.wall_south(0, 1)

    level.wall_north(0, 3)
    level.wall_east(0, 3)
    level.wall_north(1, 4)
    level.wall_east(1, 4)
    level.wall_east(1, 5)
    level.wall_south(1, 5)
    level.wall_east(0, 6)
    level.wall_east(0, 7)

    level.wall_west(4, 7)
    level.wall_north(4, 7)
    level.wall_north(5, 7)
    level.wall_east(5, 7)

    level.wall_east(6, 6)

    level.short_wall_east(6, 1)
    level.short_wall_east(6, 2)
    level.short_wall_south(6, 2)
    level.short_wall_south(5, 2)
    level.short_wall_west(5, 3)

    level.escape_north(5)
    level.escape_west(2)

    level.switch_west(2, 5)

    level.add_victim(5, 2)
    level.add_victim(6, 3)
    level.add_victim(2, 4)
    level.add_victim(5, 6)

    return level

def s6_s13():

    # More fudging than usual on this one, actually.  In the game itself,
    # the victim at (4,1) isn't "real" and the game doesn't actually ever
    # let you kill him.  Instead, the victory condition is just reaching
    # the light switch at (6,0) - as soon as you do so, the conceit is that
    # you've turned off life support to (4,1) and he dies that way.  There
    # are a few ways I could support this scenario in the app, including
    # just putting some custom condition in place, but it's actually quite
    # easy to get to the victim and kill him normally after doing the switch,
    # so I figure I left that in.  The only real level modification I've done
    # here (apart from the usual explicit exit cell) is ensuring that the
    # victim at (4,1) is actually accessible (as opposed to enclosed within
    # 'walls' as he appears to be in the game).

    level = Level('Slayaway Camp 6, Scene 13 - Life Support (MODIFIED)', 8, 8,
        1, 0,
        4, 2)

    level.wall_south(1, 2)
    level.wall_east(2, 1)
    level.wall_east(2, 2)
    level.wall_north(3, 5)
    level.wall_east(3, 5)
    level.wall_south(7, 3)

    level.wall_north(0, 7)
    level.wall_north(1, 7)
    level.wall_east(1, 7)

    level.wall_west(4, 0)
    level.wall_west(4, 1)

    # Fudging here...
    #level.wall_south(4, 1)
    level.wall_north(4, 1)
    level.wall_east(4, 1)

    level.wall_west(4, 2)
    level.wall_east(4, 3)
    level.wall_east(5, 0)
    level.wall_east(5, 1)
    level.wall_east(5, 2)
    level.wall_west(5, 2)
    level.wall_south(5, 2)

    level.wall_box(7, 7)

    level.switch_north(6, 0)

    level.add_phone_pair(2, 7, 6, 7)

    level.add_cabinet_ns(0, 3)

    level.add_swat(7, 2, DIR_W)
    level.add_swat(4, 3, DIR_S)

    level.add_victim(2, 1)
    level.add_victim(4, 1)
    level.add_victim(6, 1)
    level.add_victim(5, 6)

    return level

def s6_d1():

    level = Level('Slayaway Camp 6, Deleted Scene 1 - Fractured Instinct', 7, 7,
        0, 1,
        5, 3)

    level.wall_box(0, 0)

    level.wall_north(5, 4)
    level.wall_west(5, 4)
    level.wall_east(5, 4)
    level.wall_west(5, 5)
    level.wall_east(5, 5)
    level.wall_south(5, 5)

    level.wall_south(2, 0)
    level.wall_south(1, 1)
    level.wall_east(3, 1)
    level.wall_east(4, 1)
    level.wall_south(6, 1)
    level.wall_south(0, 2)
    level.wall_south(1, 2)
    level.wall_east(2, 2)
    level.wall_south(5, 2)
    level.wall_south(0, 3)
    level.wall_east(5, 3)
    level.wall_east(1, 4)

    level.set_mine(4, 3)

    level.switch_west(0, 6)

    level.add_swat(1, 3, DIR_E)
    level.add_swat(0, 5, DIR_S)
    level.add_swat(5, 6, DIR_W)

    level.add_victim(4, 2)
    level.add_victim(2, 3)
    level.add_victim(2, 6)

    return level

def s6_d2():

    level = Level('Slayaway Camp 6, Deleted Scene 2 - Die-Chotomy.', 8, 6,
        0, 1,
        3, 1)

    level.wall_west(6, 5)
    level.wall_north(6, 5)
    level.wall_north(7, 5)

    level.wall_east(5, 0)
    level.wall_south(5, 1)
    level.wall_east(6, 1)
    level.wall_south(0, 3)
    level.wall_east(5, 3)
    level.wall_south(1, 4)
    level.wall_east(3, 5)

    level.short_wall_north(1, 1)
    level.short_wall_north(2, 1)
    level.short_wall_east(2, 1)
    level.short_wall_north(3, 1)
    level.short_wall_east(3, 1)
    level.short_wall_east(3, 2)
    level.short_wall_south(3, 2)
    level.short_wall_south(2, 2)
    level.short_wall_west(2, 2)
    level.short_wall_east(2, 3)

    level.switch_west(0, 4)
    level.switch_north(5, 2)

    level.set_mine(2, 1)

    level.add_victim(3, 2)
    level.add_victim(6, 2)

    return level

def s6_d3():

    level = Level('Slayaway Camp 6, Deleted Scene 3 - Surgical Stealth', 8, 7,
        6, 3,
        2, 4)

    level.wall_box(0, 0)
    level.wall_box(4, 0)

    level.wall_west(1, 5)
    level.wall_north(1, 5)
    level.wall_south(1, 5)
    level.wall_north(2, 5)
    level.wall_south(2, 5)
    level.wall_east(2, 5)

    level.wall_south(6, 0)
    level.wall_south(7, 0)
    level.wall_south(7, 2)

    level.short_wall_south(1, 2)
    level.short_wall_south(1, 3)
    level.short_wall_north(3, 2)
    level.short_wall_west(3, 2)
    level.short_wall_south(4, 2)
    level.short_wall_north(5, 2)
    level.short_wall_east(5, 2)
    level.short_wall_east(5, 3)
    level.short_wall_west(4, 4)
    level.short_wall_south(4, 4)
    level.short_wall_south(6, 4)

    level.escape_west(3)
    level.escape_west(4)

    level.switch_north(1, 0)
    level.switch_north(7, 0)

    level.set_hazard(3, 5)
    level.set_hazard(4, 5)
    level.set_hazard(5, 5)

    level.add_swat(1, 3, DIR_W)
    level.add_cop(2, 0, DIR_W)
    level.add_cop(6, 0, DIR_E)
    level.add_victim(4, 1)
    level.add_victim(5, 2)
    level.add_victim(1, 4)
    level.add_cat(3, 3)

    return level

def s6_d4():

    level = Level('Slayaway Camp 6, Deleted Scene 4 - Storage Room Squishes', 9, 9,
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
