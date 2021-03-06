#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4 fileencoding=utf-8:

# Solver (and interactive player) for Slayaway Camp levels.
#
# The main intent for this is a brute-force solver for "timed"
# Slayaway Camp levels, though it can also be used on regular
# levels if you put in a pretend level cap.  There is literally
# no attempt at logic in the app - it's just brute force all the
# way.
# 
# Performance is optimized in two ways:
#
#  1) Once we find a solution, the app will only look for shorter
#     solutions
#  2) A log of all seen states is recorded while looping through.
#     A branch will only be explored if its state is either not
#     seen already, or if the seen state occurs at an earlier
#     point in the tree.
#
# The second point in particular makes a HUGE difference once you
# start to get beyond max_step counts of 14, 15 or so.  Without
# comparing checksums of the seen states, a max_step of 17 can take
# many tens of seconds, but returns nearly instantly when pruning.
#
# All map elements through Scareaway Camp X are supported:
#   * Walls
#   * Short Walls
#   * Bookcases (though I call them Cabinets)
#   * Victims
#   * Cats
#   * Police
#   * SWAT
#   * Hazards (fire, water, holes - all just considered a "hazard")
#   * Telephones
#   * Mines
#   * Escapes
#   * Light Switches
#   * Electric fences (just a type of wall)
#   * Gum ("sticky")
#   * Teleporters
#
# This can be run interactively with the -i/--interactive flag.
# While running interactive, 'q' will quit, 'u' will undo,
# 'r' will reset, and n/e/s/w will move in the specified
# direction.
#
# Each space will be drawn w/ 3x3 characters, with some unicode block
# characters to indicate walls.  Regular walls are black (well, your
# default terminal text color), short/low walls will be in red, and
# electric fences/walls will be in blue (and move to a darker blue when
# turned off).  Note that the colors are currently only optimized for
# a default of black text on white background; it'll probably look
# bad on a black background.
#
# Symbols in the middle of the cell render:
#   P - Player
#   V - Victim
#   C - Cat
#   L - Police (will use ←↑→↓ to show which way they're facing)
#   S - SWAT Cop (will use ←↑→↓ to show which way they're facing)
#   O - Police targeting reticle
#   H - Hazard
#   M - Mine
#   1/2/3 - Phones
#   | - Bookcase/Cabinet which can be knocked over west or east
#   = - Bookcase/Cabinet which can be knocked over north or south
#   X - Bookcase/Cabinet which has been knocked over
#   ^>V< - Escapes (only along map edges)
#   ~~~ - Light switches
#   ▒ - Gum (sticky patch)
#   ◉ ◧ ◈ - Teleporters (chosen basically at random)
#
# TODO: Should probably get rid of Victim.can_hit() and just start
# using a boolean as we do for switches.  Basically just need to
# find out what items cats can trigger, 'cause the only one I
# *know* they can't trigger is phones.  Update: Cats *can* trigger
# cabinets.
#
# TODO: I suspect that our logic of the order of operations when
# killed by SWAT/Police could use some work.  We DO correctly make
# sure that the player is killed before a phone or light switch
# can be directly activated.  In the game, the player CAN kill
# a victim while in a targetting reticle, but will get captured/
# killed afterwards, but another question I have is related to
# victim reactions to that death.  I suspect that in the game,
# the player is killed before other victims have a chance to run
# around changing things, whereas in our code the victims'
# reactions would all chain-react and potentially change things.
# (It would be possible to set up a scenario where killing a
# victim causes a chain reaction where another victim runs in
# front of a SWAT sightline, for instance.)
#
# TODO: We've always played fast-and-loose with how we set up
# walls, and it doesn't QUITE match what the game does.  For
# instance, it looks like the game can have different wall
# types on both side of the cell dividing line - I'd first
# noticed it in SC7, with the electric walls, and it's something
# which could potentially affect the solution, particularly if
# SWAT cops are involved.  There's one in SC7, for instance,
# which has a wall_box() surrounded by electric walls.  In our
# code, this is going to be implemented just as an electric wall
# box, but if a SWAT cop were capable of pointing into that
# "box", the laser sight would pass through in our app but be
# blocked in the game itself.  Will have to be on the lookout
# for situations where that might actually affect things.
#
# TODO: Would probably be nice to not quit automatically on lose,
# when playing interactively.  Should be able to undo/reset from
# there.

import sys
import struct

DIR_N = 0
DIR_E = 1
DIR_S = 2
DIR_W = 3
DIRS = [DIR_N, DIR_E, DIR_S, DIR_W]
DIR_T = {
    DIR_N: 'North',
    DIR_E: 'East',
    DIR_S: 'South',
    DIR_W: 'West',
}
DIR_CMD = {
    'w': DIR_N,
    's': DIR_S,
    'a': DIR_W,
    'd': DIR_E,
    '\x1b[a': DIR_N,
    '\x1b[b': DIR_S,
    '\x1b[d': DIR_W,
    '\x1b[c': DIR_E,
}
def rev_dir(direction):
    return (direction+2)%4

# Obstacle types.  Might have made more sense to process
# these separately, esp. since we have to process light
# switches differently anyway.
OBS_CABINET = 0
OBS_PHONE = 1

# Colors
try:
    import colorama
    colors_bg_lt = [colorama.Back.RESET, colorama.Back.YELLOW]
    colors_bg_dk = [colorama.Back.CYAN, colorama.Back.YELLOW]
    color_exit_active = {
        True: colorama.Fore.GREEN,
        False: colorama.Fore.BLUE,
    }

    color_short_wall = colorama.Fore.RED
    color_reticle = colorama.Fore.RED
    color_exit_inactive = colorama.Fore.MAGENTA
    color_electric_on = colorama.Style.BRIGHT + colorama.Fore.CYAN
    color_electric_off = colorama.Style.BRIGHT + colorama.Fore.BLUE
    color_sticky = colorama.Fore.MAGENTA
    color_death_notice = colorama.Fore.RED
except ModuleNotFoundError:
    colors_bg_lt = ['', '']
    colors_bg_dk = ['', '']
    color_exit_active = {
        True: '',
        False: '',
    }

    color_short_wall = ''
    color_reticle = ''
    color_exit_inactive = ''
    color_electric_on = ''
    color_electric_off = ''
    color_sticky = ''
    color_death_notice = ''

# Wall types
WALL_NONE = 0
WALL_REG = 1
WALL_SHORT = 2
WALL_ELEC = 3

# Teleporter chars
teleporter_chars = ['◉', '◧', '◈', 'a', 'b', 'c', 'd', 'e']

class PlayerLose(Exception):
    """
    Custom exception to handle player loss
    """

class Cell(object):

    def __init__(self, x, y, level=None):
        self.x = x
        self.y = y
        self.level = level
        self.exit = False
        self.hazard = False
        self.mine = False
        self.sticky = False
        self.walls = [WALL_NONE]*4
        self.escapes = [False]*4
        self.switches = [False]*4
        self.victim = None
        self.obstacle = None
        self.teleporter = None
        self.reticles = {}

        # Set our background color here, too.  Hash key is meant to be
        # the level light state.
        self.color_bg = {
            True: colors_bg_lt[(x+y)%2],
            False: colors_bg_dk[(x+y)%2],
        }

        if level is not None:
            if self.x == 0:
                self.walls[DIR_W] = WALL_REG
            if self.x == level.width - 1:
                self.walls[DIR_E] = WALL_REG
            if self.y == 0:
                self.walls[DIR_N] = WALL_REG
            if self.y == level.height - 1:
                self.walls[DIR_S] = WALL_REG

    def set_victim(self, victim):
        if victim.cell is not None:
            victim.cell.victim = None
        self.victim = victim
        victim.cell = self

    def kill_victim(self):
        """
        Used when a victim is killed by an environmental factor
        """
        if self.victim:
            self.victim.die()
            self.victim = None

    def attack_victim(self, from_direction):
        """
        Used for player physically attacking a victim
        """
        if self.victim:
            if self.victim.assault(from_direction):
                self.victim = None

    def set_obstacle(self, obstacle):
        if obstacle.cell is not None:
            obstacle.cell.obstacle = None
        self.obstacle = obstacle
        self.obstacle.cell = self

    def set_mine(self, mine):
        self.mine = mine
        self.mine.cell = self

    def set_teleporter(self, teleporter):
        self.teleporter = teleporter
        self.teleporter.cell = self

    def explode(self):
        if self.mine:
            self.kill_victim()
            self.mine = None

    def set_reticle(self, victim):
        self.reticles[victim] = True

    def clear_reticle(self, victim):
        if victim in self.reticles:
            del self.reticles[victim]

    def get_reticles(self):
        return self.reticles.keys()

    def has_reticles(self):
        if len(self.reticles) > 0:
            return True
        else:
            return False

    def checksum(self):
        return struct.pack('BB', self.x, self.y)

    def clone(self):
        newobj = Cell(self.x, self.y)
        return newobj

    def has_wall(self, direction):
        """
        Returns True if we have a wall of *any* type
        """
        return self.walls[direction] != WALL_NONE

    def get_color_corner(self, dir1, dir2):
        if self.walls[dir1] == WALL_ELEC or self.walls[dir2] == WALL_ELEC:
            if self.level.lights:
                return color_electric_on
            else:
                return color_electric_off
        elif self.walls[dir1] == WALL_REG or self.walls[dir2] == WALL_REG:
            return ''
        elif self.walls[dir1] == WALL_SHORT or self.walls[dir2] == WALL_SHORT:
            return color_short_wall
        else:
            return ''

    def get_color_cardinal(self, direction):
        if self.walls[direction] == WALL_REG:
            return ''
        elif self.walls[direction] == WALL_ELEC:
            if self.level.lights:
                return color_electric_on
            else:
                return color_electric_off
        elif self.walls[direction] == WALL_SHORT:
            return color_short_wall
        else:
            return ''

    def get_print_corner(self, dom, sec, dom_escape, sec_escape,
            both_char, dom_char, sec_char):
        """
        Gets the value to print in a corner.  Pass in the dominant
        and secondary direction, the dominant/secondary escape char,
        and chars to use in the three combinations of wall presence.
        """
        if self.escapes[dom]:
            return dom_escape
        elif self.switches[dom]:
            return '~'
        elif self.escapes[sec]:
            return sec_escape
        elif self.switches[sec]:
            return '~'
        elif self.has_wall(dom) and self.has_wall(sec):
            return self.get_color_corner(dom, sec) + both_char
        elif self.has_wall(dom):
            return self.get_color_corner(dom, sec) + dom_char
        elif self.has_wall(sec):
            return self.get_color_corner(dom, sec) + sec_char
        else:
            return ' '

    def get_print_cardinal(self, direction, escape, character, facing_char):
        """
        Gets the value to print in a cardinal direction.
        """
        if self.victim and self.victim.facing is not None and self.victim.facing == direction:
            return facing_char
        elif self.escapes[direction]:
            return escape
        elif self.switches[direction]:
            return '~'
        elif self.has_wall(direction):
            return self.get_color_cardinal(direction) + character
        else:
            return ' '

    def get_print_nw(self):
        return self.get_print_corner(DIR_N, DIR_W, '^', '<', '▛', '▀', '▌')

    def get_print_ne(self):
        return self.get_print_corner(DIR_N, DIR_E, '^', '>', '▜', '▀', '▐')

    def get_print_sw(self):
        return self.get_print_corner(DIR_S, DIR_W, 'v', '<', '▙', '▄', '▌')

    def get_print_se(self):
        return self.get_print_corner(DIR_S, DIR_E, 'v', '>', '▟', '▄', '▐')

    def get_print_n(self):
        return self.get_print_cardinal(DIR_N, '^', '▀', '↑')

    def get_print_e(self):
        return self.get_print_cardinal(DIR_E, '>', '▐', '→')

    def get_print_s(self):
        return self.get_print_cardinal(DIR_S, 'v', '▄', '↓')

    def get_print_w(self):
        return self.get_print_cardinal(DIR_W, '<', '▌', '←')

    def get_print_center_color(self):
        colors = []
        if self.sticky:
            colors.append(color_sticky)
        if self.exit:
            if self.level.num_alive() == 0:
                colors.append(color_exit_active[self.level.lights])
            else:
                colors.append(color_exit_inactive)
        if self.has_reticles():
            colors.append(color_reticle)
        return ''.join(colors)

    def get_print_center_char(self):
        if self.obstacle:
            return self.obstacle.get_interactive_character()
        elif self == self.level.player.cell:
            return 'P'
        elif self.victim:
            if self.victim.type == Victim.T_COP:
                return 'L'
            elif self.victim.type == Victim.T_SWAT:
                return 'S'
            elif self.victim.type == Victim.T_CAT:
                return 'C'
            else:
                return 'V'
        elif self.hazard:
            return 'H'
        elif self.mine:
            return 'M'
        elif self.teleporter:
            return self.teleporter.get_interactive_character()
        elif self.has_reticles():
            return 'O'
        elif self.exit:
            return 'E'
        elif self.sticky:
            return '▒'
        else:
            return ' '

    def print_top_row(self):
        color = self.color_bg[self.level.lights]
        sys.stdout.write(color + self.get_print_nw())
        sys.stdout.write(color + self.get_print_n())
        sys.stdout.write(color + self.get_print_ne())

    def print_middle_row(self):
        color = self.color_bg[self.level.lights]
        sys.stdout.write(color + self.get_print_w())
        sys.stdout.write(color + self.get_print_center_color() + self.get_print_center_char())
        sys.stdout.write(color + self.get_print_e())

    def print_bottom_row(self):
        color = self.color_bg[self.level.lights]
        sys.stdout.write(color + self.get_print_sw())
        sys.stdout.write(color + self.get_print_s())
        sys.stdout.write(color + self.get_print_se())

class Cabinet(object):

    def __init__(self, fall_dirs, level):
        self.cell = None
        self.fall_dirs = fall_dirs
        self.level = level
        self.obs_type = OBS_CABINET

    def get_interactive_character(self):
        if DIR_N in self.fall_dirs:
            return '='
        elif DIR_W in self.fall_dirs:
            return '|'
        else:
            return 'X'

    def interactable(self, direction):
        if direction in self.fall_dirs:
            return True
        else:
            return False

    def hit(self, direction):
        if direction in self.fall_dirs:
            dest_cell = self.level.get_cell_relative(self.cell.x, self.cell.y, direction)
            if dest_cell is None:
                return

            self.cell.obstacle = None

            dest_cell.kill_victim()
            dest_cell.obstacle = self
            self.cell = dest_cell
            self.fall_dirs = []

            # Check to see if we fell on the player.  Can happen at least in X.11
            if dest_cell == self.level.player.cell:
                raise PlayerLose('Crushed by falling cabinet!')

    def clone(self):
        dirs = []
        for direction in self.fall_dirs:
            dirs.append(direction)
        newobj = Cabinet(dirs, self.level)
        newobj.cell = self.cell.clone()
        return newobj

    def apply_clone(self, newobj):
        self.fall_dirs = []
        for direction in newobj.fall_dirs:
            self.fall_dirs.append(direction)
        self.level.get_cell(newobj.cell.x, newobj.cell.y).set_obstacle(self)

    def checksum(self):
        return b'{}{}'.join([
            self.cell.checksum(),
            b''.join([struct.pack('B', d) for d in self.fall_dirs]),
            ])

class Phone(object):

    def __init__(self, level, name):
        """
        'name' should be a single digit
        """
        self.level = level
        self.name = name
        self.cell = None
        self.other = None
        self.obs_type = OBS_PHONE

    def get_interactive_character(self):
        return self.name[0]

    def interactable(self, direction):
        return True

    def hit(self, direction):
        if self.other:
            self.other.ring()

    def ring(self):
        for direction in [DIR_N, DIR_E, DIR_W, DIR_S]:
            cur_cell = self.cell
            while True:
                # TODO: I don't *think* short walls block phone sounds?
                if cur_cell.walls[direction] == WALL_REG:
                    break
                next_cell = self.level.get_cell_relative_cell(cur_cell, direction)
                if next_cell:
                    if next_cell.obstacle:
                        break
                    elif next_cell.victim:
                        next_cell.victim.scare(rev_dir(direction), lure_object=self)
                        break
                    else:
                        cur_cell = next_cell
                else:
                    break

    # Next three methods just here to pretend like our state is important.
    # In the end I think that's better than trying to exclude this type of
    # obstacle from our checksumming methods.

    def clone(self):
        return self

    def apply_clone(self, newobj):
        self.cell.obstacle = self

    def checksum(self):
        return b''

class Teleporter(object):

    def __init__(self, level, character):
        """
        ``char`` should be a single printable char
        """
        self.level = level
        self.character = character
        self.cell = None
        self.other = None

    def get_interactive_character(self):
        return self.character[0]

class Mine(object):

    def __init__(self):
        self.cell = None
        self.active = True

    def explode(self):
        self.active = False
        if self.cell is not None:
            self.cell.explode()

    def clone(self):
        newobj = Mine()
        newobj.active = self.active
        return newobj

    def apply_clone(self, newobj):
        self.active = newobj.active
        if self.active and self.cell:
            self.cell.set_mine(self)

    def checksum(self):
        if self.active:
            return b'\x01'
        else:
            return b'\x00'

class Victim(object):
    """
    Victim
    """

    T_VICTIM = 0
    T_COP = 1
    T_SWAT = 2
    T_CAT = 3

    def __init__(self, level):
        self.cell = None
        self.alive = True
        self.required_to_kill = True
        self.level = level
        self.scareable = True
        self.type = Victim.T_VICTIM
        self.facing = None
        self.occupied = False
        self.scare_on_lure = False
        self.can_hit_switch = True
        self.can_see_in_dark = False

    def update_facing_vars(self, facing=None):
        return

    def die(self):
        self.alive = False
        
        # Check for adjacent victims who might have been scared by our death
        self.level.scare_from_cell(self.cell)

        return True

    def assault(self, from_direction):
        return self.die()

    def scare(self, direction, lure_object=None):
        """
        Scare the victim, or, if you pass in a lure object, lure them (the
        movement logic is the same either way, for the most part)
        """

        if lure_object is None and not self.scareable:
            return

        if self.occupied:
            return

        if lure_object is None and not self.level.lights and not self.can_see_in_dark:
            return

        if self.scare_on_lure and lure_object is not None:
            direction=rev_dir(direction)

        self.occupied = True
        self.update_facing_vars(facing=direction)

        first_move = True
        while True:
            cur_cell = self.cell
            if cur_cell.sticky and not first_move:
                break
            if cur_cell.escapes[direction]:
                raise PlayerLose('Victim escaped!')
            if self.level.lights and cur_cell.walls[direction] == WALL_ELEC:
                cur_cell.kill_victim()
                break
            if direction not in self.level.possible_moves(from_cell=cur_cell):
                break
            if cur_cell.switches[direction]:
                if self.can_hit_switch:
                    self.level.flip_lights()
                break
            next_cell = self.level.get_cell_relative_cell(cur_cell, direction)
            if next_cell.obstacle:
                if self.can_hit(next_cell.obstacle) and (lure_object is None or
                        next_cell.obstacle != lure_object):
                    next_cell.obstacle.hit(direction)
                break
            if next_cell.victim:
                break
            if next_cell.teleporter and not next_cell.teleporter.other.cell.victim:
                next_cell.teleporter.other.cell.set_victim(self)
            else:
                next_cell.set_victim(self)
            self.update_facing_vars(facing=direction)
            if next_cell.hazard:
                next_cell.kill_victim()
                break
            if next_cell.mine:
                next_cell.mine.explode()
                break

            first_move = False

        return False

    def can_hit(self, obstacle):
        return True

    def checksum(self):
        if self.alive:
            return self.cell.checksum()
        else:
            return b'\xff'

    def clone(self):
        newobj = Victim(self.level)
        newobj.alive = self.alive
        newobj.cell = self.cell.clone()
        return newobj

    def apply_clone(self, newobj):
        self.alive = newobj.alive
        if self.alive:
            self.level.get_cell(newobj.cell.x, newobj.cell.y).set_victim(self)

class Cat(Victim):

    def __init__(self, level):
        super(Cat, self).__init__(level)
        self.type = Victim.T_CAT
        self.required_to_kill = False
        self.scare_on_lure = True
        self.can_hit_switch = True
        self.can_see_in_dark = True

    def can_hit(self, obstacle):
        if obstacle.obs_type == OBS_CABINET:
            return True
        else:
            return False

    def die(self):
        raise PlayerLose('Cat was killed!')

    def checksum(self):
        return self.cell.checksum()

    def clone(self):
        newobj = Cat(self.level)
        newobj.cell = self.cell.clone()
        return newobj

    def apply_clone(self, newobj):
        self.level.get_cell(newobj.cell.x, newobj.cell.y).set_victim(self)

class Cop(Victim):

    def __init__(self, level, facing=DIR_N):
        super(Cop, self).__init__(level)
        self.scareable = False
        self.required_to_kill = False
        self.facing = facing
        self.reticles = []
        self.type = Victim.T_COP
        self.reticles_need_lights = True

    def update_facing_vars(self, facing=None):

        if facing is not None:
            self.facing = facing

        for reticle in self.reticles:
            reticle.clear_reticle(self)
        self.reticles = []

        if not self.alive:
            return

        if not self.level.lights:
            return

        cur_cell = self.cell
        if cur_cell is not None:
            if cur_cell.has_wall(self.facing):
                return

            rel_cell = self.level.get_cell_relative_cell(cur_cell, self.facing)
            if rel_cell:
                self.reticles.append(rel_cell)
                rel_cell.set_reticle(self)

                # Check to see if the player is in our reticle.
                if rel_cell == self.level.player.cell:
                    raise PlayerLose('Apprehended by Police')

    def die(self):
        super(Cop, self).die()
        for reticle in self.reticles:
            reticle.clear_reticle(self)

    def assault(self, from_direction):
        if self.level.lights and from_direction == self.facing:
            raise PlayerLose('Apprehended by Police')
        else:
            self.die()
            return True

    def active(self):
        """
        Used in the context of a targetting reticle - are we active?
        """
        if self.level.lights:
            return True
        elif self.reticles_need_lights:
            return False
        else:
            return True

    def checksum(self):
        if self.alive:
            return b''.join([
                self.cell.checksum(),
                struct.pack('B', self.facing),
                ])
        else:
            return b'\xff'

    def clone(self):
        newobj = Cop(self.level, self.facing)
        newobj.alive = self.alive
        newobj.cell = self.cell.clone()
        return newobj

    def apply_clone(self, newobj):
        super(Cop, self).apply_clone(newobj)
        self.facing = newobj.facing

class Swat(Cop):

    def __init__(self, level, facing=DIR_N):
        super(Swat, self).__init__(level, facing)
        self.type = Victim.T_SWAT
        self.reticles_need_lights = False

    def update_facing_vars(self, facing=None):

        if facing is not None:
            self.facing = facing

        for reticle in self.reticles:
            reticle.clear_reticle(self)
        self.reticles = []

        if not self.alive:
            return

        cur_cell = self.cell
        if cur_cell is not None:
            while True:
                if cur_cell.walls[self.facing] == WALL_REG:
                    break

                rel_cell = self.level.get_cell_relative_cell(cur_cell, self.facing)
                if rel_cell:
                    if rel_cell.victim or rel_cell.obstacle:
                        break
                    self.reticles.append(rel_cell)
                    rel_cell.set_reticle(self)

                    # Check to see if the player is in our reticle.
                    if rel_cell == self.level.player.cell:
                        raise PlayerLose('Shot by SWAT Cop')

                    cur_cell = rel_cell

                else:
                    break

    def assault(self, from_direction):
        if self.level.lights:
            raise PlayerLose('Killed by SWAT Cop')
        elif from_direction == self.facing:
            raise PlayerLose('Shot by SWAT Cop')
        else:
            self.die()
            return True

    def clone(self):
        newobj = Swat(self.level, self.facing)
        newobj.alive = self.alive
        newobj.cell = self.cell.clone()
        return newobj

class Player(object):
    """
    Player
    """

    def __init__(self, cell, level):
        self.cell = cell
        self.level = level

    def clone(self):
        newobj = Player(self.cell.clone(), self.level)
        return newobj

    def apply_clone(self, newobj):
        self.cell = self.level.get_cell(newobj.cell.x, newobj.cell.y)

class Level(object):

    def __init__(self, desc, width, height,
            player_x, player_y,
            exit_x, exit_y,
            max_steps=None):

        self.desc = desc
        self.max_steps = max_steps

        self.width = width
        self.height = height

        self.lights = True
        self.cells = []
        self.victims = []
        self.obstacles = []
        self.mines = []
        for y in range(height):
            self.cells.append([])
            for x in range(width):
                self.cells[y].append(Cell(x, y, self))
        player_cell = self.get_cell(player_x, player_y)
        self.player = Player(player_cell, self)
        self.won = False
        self.set_exit(exit_x, exit_y)

        self.latest_phone_pair = 0
        self.latest_teleporter_pair = 0

        self.return_first_solution = False

    def add_victim_obj(self, x, y, victim):
        self.victims.append(victim)
        self.cells[y][x].set_victim(victim)
        victim.update_facing_vars()

    def add_victim(self, x, y):
        self.add_victim_obj(x, y, Victim(self))

    def add_cat(self, x, y):
        self.add_victim_obj(x, y, Cat(self))

    def add_cop(self, x, y, direction):
        self.add_victim_obj(x, y, Cop(self, direction))

    def add_swat(self, x, y, direction):
        self.add_victim_obj(x, y, Swat(self, direction))

    def add_obstacle(self, x, y, obstacle):
        self.obstacles.append(obstacle)
        self.get_cell(x, y).set_obstacle(obstacle)

    def add_cabinet_ns(self, x, y):
        self.add_obstacle(x, y, Cabinet([DIR_N, DIR_S], self))

    def add_cabinet_we(self, x, y):
        self.add_obstacle(x, y, Cabinet([DIR_W, DIR_E], self))

    def add_phone_pair(self, x1, y1, x2, y2):
        self.latest_phone_pair += 1
        p1 = Phone(self, str(self.latest_phone_pair))
        p2 = Phone(self, str(self.latest_phone_pair))
        p1.other = p2
        p2.other = p1
        self.add_obstacle(x1, y1, p1)
        self.add_obstacle(x2, y2, p2)

    def add_teleporter(self, x, y, teleporter):
        self.get_cell(x, y).set_teleporter(teleporter)

    def add_teleporter_pair(self, x1, y1, x2, y2):
        character = teleporter_chars[self.latest_teleporter_pair]
        self.latest_teleporter_pair += 1
        t1 = Teleporter(self, character)
        t2 = Teleporter(self, character)
        t1.other = t2
        t2.other = t1
        self.add_teleporter(x1, y1, t1)
        self.add_teleporter(x2, y2, t2)

    def wall_generic_west(self, x, y, walltype):
        self.cells[y][x].walls[DIR_W] = walltype
        if x > 0:
            self.cells[y][x-1].walls[DIR_E] = walltype

    def wall_generic_east(self, x, y, walltype):
        self.cells[y][x].walls[DIR_E] = walltype
        if x < (self.width-1):
            self.cells[y][x+1].walls[DIR_W] = walltype

    def wall_generic_south(self, x, y, walltype):
        self.cells[y][x].walls[DIR_S] = walltype
        if y < (self.height-1):
            self.cells[y+1][x].walls[DIR_N] = walltype

    def wall_generic_north(self, x, y, walltype):
        self.cells[y][x].walls[DIR_N] = walltype
        if y > 0:
            self.cells[y-1][x].walls[DIR_S] = walltype

    def wall_west(self, x, y):
        self.wall_generic_west(x, y, WALL_REG)

    def wall_east(self, x, y):
        self.wall_generic_east(x, y, WALL_REG)

    def wall_south(self, x, y):
        self.wall_generic_south(x, y, WALL_REG)

    def wall_north(self, x, y):
        self.wall_generic_north(x, y, WALL_REG)

    def short_wall_west(self, x, y):
        self.wall_generic_west(x, y, WALL_SHORT)

    def short_wall_east(self, x, y):
        self.wall_generic_east(x, y, WALL_SHORT)

    def short_wall_south(self, x, y):
        self.wall_generic_south(x, y, WALL_SHORT)

    def short_wall_north(self, x, y):
        self.wall_generic_north(x, y, WALL_SHORT)

    def electric_west(self, x, y):
        self.wall_generic_west(x, y, WALL_ELEC)

    def electric_east(self, x, y):
        self.wall_generic_east(x, y, WALL_ELEC)

    def electric_south(self, x, y):
        self.wall_generic_south(x, y, WALL_ELEC)

    def electric_north(self, x, y):
        self.wall_generic_north(x, y, WALL_ELEC)

    def escape_north(self, x):
        self.cells[0][x].escapes[DIR_N] = True

    def escape_south(self, x):
        self.cells[self.height-1][x].escapes[DIR_S] = True

    def escape_west(self, y):
        self.cells[y][0].escapes[DIR_W] = True

    def escape_east(self, y):
        self.cells[y][self.width-1].escapes[DIR_E] = True

    def switch_north(self, x, y):
        self.cells[y][x].switches[DIR_N] = True

    def switch_south(self, x, y):
        self.cells[y][x].switches[DIR_S] = True

    def switch_west(self, x, y):
        self.cells[y][x].switches[DIR_W] = True

    def switch_east(self, x, y):
        self.cells[y][x].switches[DIR_E] = True

    def wall_box(self, x, y):
        self.wall_north(x, y)
        self.wall_south(x, y)
        self.wall_east(x, y)
        self.wall_west(x, y)

    def short_wall_box(self, x, y):
        self.short_wall_north(x, y)
        self.short_wall_south(x, y)
        self.short_wall_east(x, y)
        self.short_wall_west(x, y)

    def electric_box(self, x, y):
        self.electric_north(x, y)
        self.electric_south(x, y)
        self.electric_east(x, y)
        self.electric_west(x, y)

    def get_cell(self, x, y):
        return self.cells[y][x]

    def get_cell_relative_cell(self, cell, direction):
        return self.get_cell_relative(cell.x, cell.y, direction)

    def get_cell_relative(self, x, y, direction):
        if direction == DIR_W:
            if x == 0:
                return None
            else:
                return self.cells[y][x-1]
        if direction == DIR_E:
            if x == self.width-1:
                return None
            else:
                return self.cells[y][x+1]
        if direction == DIR_N:
            if y == 0:
                return None
            else:
                return self.cells[y-1][x]
        if direction == DIR_S:
            if y == self.height-1:
                return None
            else:
                return self.cells[y+1][x]

    def scare_from_cell(self, cell):
        """
        Scares anyone adjacent to the given cell
        """
        for direction in DIRS:
            if cell.walls[direction] == WALL_REG:
                continue
            adj_cell = self.get_cell_relative_cell(cell, direction)
            if adj_cell is not None:
                if adj_cell.victim is not None:
                    adj_cell.victim.scare(direction)

    def move_player(self, direction):

        # Some actions we take need to wait until we resolve targetting
        # reticles and the like.
        flip_lights = False
        hit_obstacle = None

        first_move = True
        while True:

            # Reset all the victims' "occupied" flags first.
            for victim in self.victims:
                victim.occupied = False

            cur_cell = self.player.cell
            if cur_cell.exit and self.num_alive() == 0:
                # Before we get too excited about winning, make sure there's
                # not an active reticle where we are.  If there IS then I
                # guess just continue to move through; not quite sure how
                # that would work in the game, honestly.
                # TODO: Find a level to answer this question: ^
                keep_moving = False
                if cur_cell.has_reticles():
                    for reticle in cur_cell.get_reticles():
                        if reticle.active():
                            keep_moving = True
                if not keep_moving:
                    self.won = True
                    return True
            if not first_move and cur_cell.sticky:
                break
            if cur_cell.walls[direction] == WALL_ELEC and self.lights:
                raise PlayerLose('Electrocuted!')
            if direction not in self.possible_moves(from_cell=cur_cell):
                break
            if cur_cell.switches[direction]:
                flip_lights = True
                break
            next_cell = self.get_cell_relative_cell(cur_cell, direction)
            if next_cell.obstacle:
                hit_obstacle = (next_cell.obstacle, direction)
                break
            if next_cell.victim:
                next_cell.attack_victim(rev_dir(direction))
                break

            if next_cell.teleporter:
                # Check to see if any victim is *on* the other side.  If
                # so, call a custom scare method and just continue on.
                if next_cell.teleporter.other.cell.victim:
                    self.player.cell = next_cell
                else:

                    # Hopping into a teleporter scares adjacent victims
                    self.scare_from_cell(next_cell)
                    self.player.cell = next_cell.teleporter.other.cell

                    # Hopping *out* of a teleporter on the far end might
                    # potentially scare adjacent victims, but I have yet
                    # to run into a level in which that seems to matter for
                    # finding solutions.  If you come out heading directly
                    # *for* an adjacent victim, you'll kill that victim
                    # rather than scaring 'em away.
                    # TODO: See if I can find an example of zooming out of
                    # a teleporter, with a victim adjacent, to see if anything
                    # needs to be done here.
                    #self.scare_from_cell(self.player.cell)
            else:
                self.player.cell = next_cell

            if next_cell.hazard:
                raise PlayerLose('Fell into a hazard')
            if next_cell.mine:
                raise PlayerLose('Walked into a mine')

            first_move = False

        # If we landed on a reticle, we're dead
        for reticle in self.player.cell.get_reticles():
            if reticle.reticles_need_lights and not self.lights:
                continue
            raise PlayerLose('Shot/Apprehended by the police')

        # If we're not dead yet, though, perform some delayed actions.
        if flip_lights:
            self.flip_lights()
        if hit_obstacle is not None:
            (obstacle, direction) = hit_obstacle
            obstacle.hit(direction)

        # check for adjacent victims to scare
        self.scare_from_cell(self.player.cell)

        # Loop through victims and update their 'facing' parameters;
        # this is only actually important for SWAT Cops (to make sure
        # that their reticles get updated), but it won't hurt the
        # others.
        self.update_all_facing_vars()

        # Do one more check here, to see if we've won.  It's possible
        # in at least one level to scare a victim into a hole on the
        # same turn you land on the exit.
        if cur_cell.exit and self.num_alive() == 0:
            self.won = True
            return True

        # exit
        return False

    def possible_moves(self, from_cell=None):
        moves = []
        if from_cell is None:
            from_cell = self.player.cell
        for direction in DIRS:
            if from_cell.switches[direction]:
                moves.append(direction)
            # NOTE: We exclude electrics from possible moves, because we
            # don't want to waste time walking directly into them, but we
            # CAN run into them once we've stepped, so we have to check for
            # it in move_player, *before* we check for possible_moves in there.
            if from_cell.has_wall(direction):
                continue
            else:
                rel_cell = self.get_cell_relative_cell(from_cell, direction)
                if rel_cell.obstacle:
                    if not rel_cell.obstacle.interactable(direction):
                        continue
                moves.append(direction)
        return moves

    def set_exit(self, x, y):
        self.get_cell(x, y).exit = True

    def set_hazard(self, x, y):
        self.get_cell(x, y).hazard = True

    def set_mine(self, x, y):
        mine = Mine()
        self.mines.append(mine)
        self.get_cell(x, y).set_mine(mine)

    def set_sticky(self, x, y):
        self.get_cell(x, y).sticky = True

    def num_alive(self):
        alive = 0
        for victim in self.victims:
            if victim.required_to_kill and victim.alive:
                alive += 1
        return alive

    def update_all_facing_vars(self):
        """
        Method to loop through and update all victim facing vars.  Only
        really important for SWAT, but whatever.
        """
        for victim in self.victims:
            victim.update_facing_vars()

    def flip_lights(self):
        """
        Flips our light switches.
        """
        self.lights = not self.lights
        self.update_all_facing_vars()

    def print_level(self):

        print(self.desc)
        for col in self.cells:
            for cell in col:
                cell.print_top_row()
            sys.stdout.write("\n")
            for cell in col:
                cell.print_middle_row()
            sys.stdout.write("\n")
            for cell in col:
                cell.print_bottom_row()
            sys.stdout.write("\n")
        if not self.lights:
            print('Lights are OFF')

    def print_debug_info(self):
        """
        Print information useful to someone debugging the app.  Will
        print out the whole level and then a bunch of information
        about the internal vars.
        """
        # TODO: incomplete, just putting in what I need at the moment
        self.print_level()
        print('Player at: ({},{})'.format(self.player.cell.x, self.player.cell.y))
        for col in self.cells:
            for cell in col:
                if cell.obstacle is not None:
                    print('({},{}) - Obstacle {}'.format(cell.x, cell.y, cell.obstacle))
                if cell.victim is not None:
                    print('({},{}) - Victim {}'.format(cell.x, cell.y, cell.victim))
                if len(cell.reticles) > 0:
                    print('({},{}) - Reticles: {}'.format(cell.x, cell.y, cell.reticles))

class State(object):

    def __init__(self, level, moves=None):

        self.level = level
        self.lights = level.lights
        self.victims = []
        self.obstacles = []
        self.mines = []
        self.player = level.player.clone()
        self.moves = moves

        for victim in level.victims:
            self.victims.append(victim.clone())
        for obstacle in level.obstacles:
            self.obstacles.append(obstacle.clone())
        for mine in level.mines:
            self.mines.append(mine.clone())

    def apply(self):

        # First clear out some existing pointers inside our "live" Cells -
        # we do this because this data isn't actually captured per se in
        # our State value...  If we're just going forward/back one step
        # at a time, the apply code on the individual items keeps the
        # pointers updated properly, but if we're hopping arouind between
        # various states all over the place, they wouldn't get cleaned
        # out properly.  This is kind of a kludge; really we should be
        # storing this information properly, but this works well enough
        # and is fast enough, so I've not bothered.  This is something that
        # needed to happen once we implemented breadth-first solving;
        # wasn't necessary before then.  This is a pretty silly way of
        # doing this; really I should figure out a more elegant solution.
        # But our performance gains using BFS more than make up for this
        # kind of inefficiency, so it'll probably just remain here.
        for v in self.level.victims:
            if v.cell is not None:
                v.cell.victim = None
        for o in self.level.obstacles:
            if o.cell is not None:
                o.cell.obstacle = None
        for m in self.level.mines:
            if m.cell is not None:
                m.cell.mine = None

        self.level.lights = self.lights

        self.level.player.apply_clone(self.player)

        for (saved, real) in zip(self.victims, self.level.victims):
            real.apply_clone(saved)

        for (saved, real) in zip(self.obstacles, self.level.obstacles):
            real.apply_clone(saved)

        for (saved, real) in zip(self.mines, self.level.mines):
            real.apply_clone(saved)

        # Don't do this until the end
        self.level.update_all_facing_vars()

        if self.moves is not None:
            return list(self.moves)

    def checksum(self):
        """
        A "checksum" of the level state, used to remember whether or not we've
        seen a particular state before.  It's actually more than a checksum, since
        it could theoretically be used to save/restore a complete state, rather
        than just being a fingerprint.

        We originally used a human-readable string for these, which worked well,
        but since switching over my Snakebird solver checksum method to binary
        worked out pretty well for that one, I figured I'd do so over here as well.
        Since the solve times in Slayaway Camp are quite reasonable to begin with,
        this doesn't really help us too much here.  It does lop off about 10
        seconds from the s10_d4 solve, which is nice, and probably consumes a bit
        less memory while it's doing so, too.
        """

        sumlist = []
        if self.level.lights:
            sumlist.append(b'\x01')
        else:
            sumlist.append(b'\x00')
        sumlist.append(self.player.cell.checksum())
        sumlist.append(b''.join([victim.checksum() for victim in self.victims]))
        sumlist.append(b''.join([obstacle.checksum() for obstacle in self.obstacles]))
        sumlist.append(b''.join([mine.checksum() for mine in self.mines]))
        return b''.join(sumlist)

class Game(object):
    
    def __init__(self, level):

        # Save the level
        self.level = level

        # Max steps
        self.max_steps = level.max_steps
        self.cur_steps = 0

        # And a list for states
        self.states = []

        # List of moves
        self.moves = []

        # Best solution found
        self.solution = None
        
        # Death state
        self.alive = True

        # Seen checksums
        self.checksums = {}

    def push_state(self, state=None):
        if state is None:
            state = State(self.level)
        self.states.append(state)

    def get_state(self, moves=None):
        state = State(self.level, moves)
        checksum = state.checksum()
        if checksum in self.checksums:
            if self.cur_steps >= self.checksums[checksum]:
                return (state, False)
        self.checksums[checksum] = self.cur_steps
        return (state, True)

    def pop_state(self):
        state = self.states.pop()
        state.apply()

    def move(self, direction, state=None):
        self.moves.append(direction)
        self.push_state(state)
        self.cur_steps += 1
        return self.level.move_player(direction)

    def undo(self):
        if len(self.states) > 0:
            self.moves.pop()
            self.pop_state()
            self.cur_steps -= 1
            self.level.won = False
            self.alive = True
            self.level.update_all_facing_vars()
        else:
            print('No undo states!')

    def step_limit(self):
        if self.max_steps is None:
            return False
        else:
            if self.cur_steps >= self.max_steps:
                return True
            else:
                return False

    def print_winning_move_set(self, move_set):
        print('Winning moves ({}) for {}:'.format(len(move_set), self.level.desc))
        for (n, move) in enumerate(move_set):
            print("\t{}. {}".format(n+1, DIR_T[move]))

    def store_winning_moves(self, quiet=False, display_moves=True):
        if not quiet:
            print('Found winning solution with {} moves'.format(len(self.moves)))
        self.max_steps = len(self.moves)-1
        if self.solution is None or len(self.moves) < len(self.solution):
            self.solution = []
            for direction in self.moves:
                self.solution.append(direction)
        if not quiet and display_moves:
            self.print_winning_move_set(self.moves)

    def print_status(self, death_reason=None):
        self.level.print_level()
        if self.level.won:
            print('You win!')
            print('')
            self.store_winning_moves(display_moves=True)
        elif self.alive == False:
            print('You have lost: {}{}'.format(color_death_notice, death_reason))
        else:
            if self.max_steps is not None:
                print('Steps: {}/{}'.format(self.cur_steps, self.max_steps))
            if self.step_limit():
                print('Out of moves, you lose!')
            else:
                print('Num alive: {}'.format(self.level.num_alive()))
                print('Possible moves:')
                for direction in self.level.possible_moves():
                    print("\t{}".format(DIR_T[direction]))

    def interactive(self):
        import readchar
        colorama.init(autoreset=True)
        self.level.update_all_facing_vars()
        death_reason = None
        while True:
            self.print_status(death_reason)
            full_control = True
            if self.level.won:
                return True
            elif self.step_limit():
                full_control = False
            elif self.alive == False:
                full_control = False
            else:
                death_reason = None

            if full_control:
                print('[wasd/arrows] - move, [u]ndo, [r]eset, [q]uit')
            else:
                print('[u]ndo, [r]eset, [q]uit')
            sys.stdout.write('[{}] > '.format(self.cur_steps + 1))
            sys.stdout.flush()

            valid_input = False
            while not valid_input:
                cmd = readchar.readkey().lower()
                if cmd in DIR_CMD and len(cmd) > 1:
                    report = DIR_T[DIR_CMD[cmd]]
                else:
                    report = cmd

                direction = None
                if cmd == 'q':
                    print(report)
                    return False
                elif cmd == 'u':
                    valid_input = True
                    self.undo()
                elif cmd == 'r':
                    valid_input = True
                    while len(self.states) > 0:
                        self.undo()
                elif full_control and cmd in DIR_CMD:
                    valid_input = True
                    direction = DIR_CMD[cmd]
                    if direction in self.level.possible_moves():
                        try:
                            self.move(DIR_CMD[cmd])
                        except PlayerLose as e:
                            self.alive = False
                            report_prefix = 'Player Death: '
                            report_suffix = str(e)
                            death_reason = report_suffix
                            print('-'*(len(report_prefix) + len(report_suffix)))
                            print('{}{}{}'.format(report_prefix, color_death_notice, report_suffix))
                            print('-'*(len(report_prefix) + len(report_suffix)))
                        except Exception as e:
                            print('Got exception!')
                            self.print_debug_info()
                            raise e

                if valid_input:
                    print(report)

    def solve_dfs(self):
        """
        The original solving algorithm, a recursive depth-first solver.  This
        walks out as far as possible and only backs up to try another path
        once death has occurred, we've run out of moves, or encountered a
        loop (or a gamestate we already saw at an earlier point).  When a
        solution is found, we'll try going back up the tree to see if we
        can find a shorter solution, until we've exhausted all possibilities
        and know that we've gotten the best.  This works fine, really, and
        our solve times are generally quite good regardless.  However, doing
        a breadth-first search beats us on speed pretty much every time.
        So, nothing's actually using this anymore!  Alas.
        """
        if self.level.return_first_solution and self.solution is not None:
            return
        (state, new_checksum) = self.get_state()
        if not new_checksum:
            return
        for direction in self.level.possible_moves():
            try:
                if (self.move(direction, state)):
                    self.store_winning_moves(quiet=True, display_moves=False)
                    if self.level.return_first_solution:
                        return
                    self.undo()
                else:
                    if self.step_limit():
                        self.undo()
                    else:
                        self.solve_dfs()
                        self.undo()
            except PlayerLose:
                self.undo()

    def solve_bfs(self, quiet=False):
        """
        Breadth-first search algorithm.  Technically this is more memory-intensive
        than Depth-first, since we've got to keep track of the state of the game
        at every concurrent possibility, but it's also quite a bit faster.  Our
        solve times aren't awful to begin with, but there's no reason NOT to use
        the fastest one, so we've switched over to using this.
        """
        queue = [self.get_state(self.moves)[0]]
        if self.max_steps is None:
            # "999 steps ought to be enough for anybody"
            max_steps = 999
        else:
            max_steps = self.max_steps
        debug_moves = [DIR_N, DIR_E, DIR_N, DIR_W, DIR_N, DIR_E, DIR_S, DIR_W, DIR_N]
        for i in range(max_steps):
            next_queue = []
            if not quiet:
                sys.stdout.write("\rAt depth: {}...".format(i))
                sys.stdout.flush()
            for state in queue:
                self.moves = state.apply()
                for direction in self.level.possible_moves():
                    self.moves = state.apply()
                    try:
                        if (self.move(direction, state)):
                            if not quiet:
                                print('')
                            self.store_winning_moves(quiet=quiet, display_moves=False)
                            return
                        (new_state, is_new_state) = self.get_state(self.moves)
                        if is_new_state:
                            next_queue.append(new_state)
                    except PlayerLose:
                        pass
            queue = next_queue
            if len(next_queue) == 0:
                break
        if not quiet:
            print('')

    def solve(self, quiet=True):
        """
        Frontend for solving - mostly just to make sure that SWAT
        reticles are updated properly after all map components have
        been added.
        """
        self.level.update_all_facing_vars()
        return self.solve_bfs(quiet=quiet)
