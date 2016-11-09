#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

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
# Currently the objects supported are:
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
#
# Stuff not yet implemented:
#   * Electric Walls
#   * Anything beyond Slayaway Camp 7
#
# This can be run interactively with the -i/--interactive flag.
# While running interactive, 'q' will quit, 'u' will undo,
# 'r' will reset, and n/e/s/w will move in the specified
# direction.
#
# Each space will be drawn w/ 3x3 characters, with some unicode block
# characters to indicate walls ("low" walls will be in red).
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
#
# TODO: Should probably get rid of Victim.can_hit() and just start
# using a boolean as we do for switches.  Basically just need to
# find out what items cats can trigger, 'cause the only one I
# *know* they can't trigger is phones.

import sys
import colorama

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
    'n': DIR_N,
    's': DIR_S,
    'w': DIR_W,
    'e': DIR_E,
}
def rev_dir(direction):
    return (direction+2)%4

class PlayerLose(Exception):
    """
    Custom exception to handle player loss
    """

class Cell(object):

    def __init__(self, x, y, level=None):
        self.x = x
        self.y = y
        self.exit = False
        self.hazard = False
        self.mine = False
        self.walls = [False]*4
        self.short_walls = [False]*4
        self.escapes = [False]*4
        self.switches = [False]*4
        self.victim = None
        self.obstacle = None
        self.reticles = {}

        if level is not None:
            if self.x == 0:
                self.walls[DIR_W] = True
            if self.x == level.width - 1:
                self.walls[DIR_E] = True
            if self.y == 0:
                self.walls[DIR_N] = True
            if self.y == level.height - 1:
                self.walls[DIR_S] = True

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
        return '%d,%d' % (self.x, self.y)

    def clone(self):
        newobj = Cell(self.x, self.y)
        return newobj

class Cabinet(object):

    def __init__(self, fall_dirs, level):
        self.cell = None
        self.fall_dirs = fall_dirs
        self.level = level

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
        return '%s;%s' % (self.cell.checksum(),
            ','.join([str(d) for d in self.fall_dirs]))

class Phone(object):

    def __init__(self, level, name):
        """
        'name' should be a single digit
        """
        self.level = level
        self.name = name
        self.cell = None
        self.other = None

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
                if cur_cell.walls[direction]:
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
        pass

    def checksum(self):
        return 'p'

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
            return '1'
        else:
            return '0'

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
        for direction in DIRS:
            if self.cell.walls[direction]:
                continue
            rel_cell = self.level.get_cell_relative_cell(self.cell, direction)
            if rel_cell.victim:
                rel_cell.victim.scare(direction)

        return True

    def assault(self, from_direction):
        return self.die()

    def scare(self, direction, lure_object=None):

        if lure_object is None and not self.scareable:
            return

        if self.occupied:
            return

        if not self.level.lights and not self.can_see_in_dark:
            return

        if self.scare_on_lure and lure_object is not None:
            direction=rev_dir(direction)

        self.occupied = True
        self.update_facing_vars(facing=direction)

        while True:
            cur_cell = self.cell
            if cur_cell.escapes[direction]:
                raise PlayerLose('Victim escaped!')
            if direction not in self.level.possible_moves(from_cell=cur_cell):
                break
            if cur_cell.switches[direction]:
                if self.can_hit_switch:
                    self.flip_lights()
                break
            next_cell = self.level.get_cell_relative_cell(cur_cell, direction)
            if next_cell.obstacle:
                if self.can_hit(next_cell.obstacle) and (lure_object is None or
                        next_cell.obstacle != lure_object):
                    next_cell.obstacle.hit(direction)
                break
            if next_cell.victim:
                break
            next_cell.set_victim(self)
            self.update_facing_vars(facing=direction)
            if next_cell.hazard:
                next_cell.kill_victim()
                break
            if next_cell.mine:
                next_cell.mine.explode()
                break

        return False

    def can_hit(self, obstacle):
        return True

    def checksum(self):
        if self.alive:
            return self.cell.checksum()
        else:
            return 'd'

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
        self.can_hit_switch = False
        self.can_see_in_dark = True

    def can_hit(self, obstacle):
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
            if cur_cell.walls[self.facing] or cur_cell.short_walls[self.facing]:
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
            return '%s;f%d' % (self.cell.checksum(), self.facing)
        else:
            return 'd'

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
                if cur_cell.walls[self.facing]:
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

    def wall_west(self, x, y):
        self.cells[y][x].walls[DIR_W] = True
        if x > 0:
            self.cells[y][x-1].walls[DIR_E] = True

    def wall_east(self, x, y):
        self.cells[y][x].walls[DIR_E] = True
        if x < (self.width-1):
            self.cells[y][x+1].walls[DIR_W] = True

    def wall_south(self, x, y):
        self.cells[y][x].walls[DIR_S] = True
        if y < (self.height-1):
            self.cells[y+1][x].walls[DIR_N] = True

    def wall_north(self, x, y):
        self.cells[y][x].walls[DIR_N] = True
        if y > 0:
            self.cells[y-1][x].walls[DIR_S] = True

    def short_wall_west(self, x, y):
        self.cells[y][x].short_walls[DIR_W] = True
        if x > 0:
            self.cells[y][x-1].short_walls[DIR_E] = True

    def short_wall_east(self, x, y):
        self.cells[y][x].short_walls[DIR_E] = True
        if x < (self.width-1):
            self.cells[y][x+1].short_walls[DIR_W] = True

    def short_wall_south(self, x, y):
        self.cells[y][x].short_walls[DIR_S] = True
        if y < (self.height-1):
            self.cells[y+1][x].short_walls[DIR_N] = True

    def short_wall_north(self, x, y):
        self.cells[y][x].short_walls[DIR_N] = True
        if y > 0:
            self.cells[y-1][x].short_walls[DIR_S] = True

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

    def move_player(self, direction):

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
            if direction not in self.possible_moves(from_cell=cur_cell):
                break
            if cur_cell.switches[direction]:
                self.flip_lights()
                break
            next_cell = self.get_cell_relative_cell(cur_cell, direction)
            if next_cell.obstacle:
                next_cell.obstacle.hit(direction)
                break
            if next_cell.victim:
                next_cell.attack_victim(rev_dir(direction))
                break
            self.player.cell = next_cell
            if next_cell.hazard:
                raise PlayerLose('Fell into a hazard')
            if next_cell.mine:
                raise PlayerLose('Walked into a mine')

        # If we landed on a reticle, we're dead
        for reticle in self.player.cell.get_reticles():
            if reticle.reticles_need_lights and not self.lights:
                continue
            raise PlayerLose('Shot/Apprehended by the police')

        # check for adjacent victims to scare
        for direction in DIRS:
            if self.player.cell.walls[direction]:
                continue
            adj_cell = self.get_cell_relative_cell(self.player.cell, direction)
            if adj_cell is None:
                continue
            if adj_cell.victim is not None:
                adj_cell.victim.scare(direction)

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
            if from_cell.walls[direction] or from_cell.short_walls[direction]:
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

    def print(self):

        # Colors
        if self.lights:
            color_bg_1 = colorama.Back.RESET
            color_bg_2 = colorama.Back.YELLOW
            color_exit_active = colorama.Fore.GREEN
        else:
            color_bg_1 = colorama.Back.CYAN
            color_bg_2 = colorama.Back.YELLOW
            color_exit_active = colorama.Fore.BLUE
        color_short_wall = colorama.Fore.RED
        color_reticle = colorama.Fore.RED
        color_exit_inactive = colorama.Fore.MAGENTA

        print(self.desc)
        for (y, col) in enumerate(self.cells):
            for (x, row) in enumerate(col):
                if y % 2 == 0:
                    if x % 2 == 0:
                        color = color_bg_1
                    else:
                        color = color_bg_2
                else:
                    if x % 2 == 0:
                        color = color_bg_2
                    else:
                        color = color_bg_1
                if row.escapes[DIR_N]:
                    sys.stdout.write(color + '^^^')
                elif row.switches[DIR_N]:
                    sys.stdout.write(color + '~~~')
                elif row.walls[DIR_N] or row.short_walls[DIR_N]:
                    if row.escapes[DIR_W]:
                        sys.stdout.write(color + '<')
                    elif row.switches[DIR_W]:
                        sys.stdout.write(color + '~')
                    elif row.walls[DIR_W] or row.short_walls[DIR_W]:
                        if row.short_walls[DIR_N] and row.short_walls[DIR_W]:
                            extra = color_short_wall
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '▛')
                    else:
                        if row.short_walls[DIR_N]:
                            extra = color_short_wall
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '▀')
                    if row.short_walls[DIR_N]:
                        extra = color_short_wall
                    else:
                        extra = ''
                    if row.victim and row.victim.facing is not None and row.victim.facing == DIR_N:
                        sys.stdout.write(color + extra + '↑')
                    else:
                        sys.stdout.write(color + extra + '▀')
                    if row.escapes[DIR_E]:
                        sys.stdout.write(color + '>')
                    elif row.switches[DIR_E]:
                        sys.stdout.write(color + '~')
                    elif row.walls[DIR_E] or row.short_walls[DIR_E]:
                        if row.short_walls[DIR_N] and row.short_walls[DIR_E]:
                            extra = color_short_wall
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '▜')
                    else:
                        if row.short_walls[DIR_N]:
                            extra = color_short_wall
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '▀')
                else:
                    if row.escapes[DIR_W]:
                        sys.stdout.write(color + '<')
                    elif row.switches[DIR_W]:
                        sys.stdout.write(color + '~')
                    elif row.walls[DIR_W] or row.short_walls[DIR_W]:
                        if row.short_walls[DIR_W]:
                            extra = color_short_wall
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '▌')
                    else:
                        sys.stdout.write(color + ' ')
                    if row.victim and row.victim.facing is not None and row.victim.facing == DIR_N:
                        sys.stdout.write(color + '↑')
                    else:
                        sys.stdout.write(color + ' ')
                    if row.escapes[DIR_E]:
                        sys.stdout.write(color + '>')
                    elif row.switches[DIR_E]:
                        sys.stdout.write(color + '~')
                    elif row.walls[DIR_E] or row.short_walls[DIR_E]:
                        if row.short_walls[DIR_E]:
                            extra = color_short_wall
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '▐')
                    else:
                        sys.stdout.write(color + ' ')
            sys.stdout.write("\n")
            for (x, row) in enumerate(col):
                if y % 2 == 0:
                    if x % 2 == 0:
                        color = color_bg_1
                    else:
                        color = color_bg_2
                else:
                    if x % 2 == 0:
                        color = color_bg_2
                    else:
                        color = color_bg_1
                if row.escapes[DIR_W]:
                    sys.stdout.write(color + '<')
                elif row.switches[DIR_W]:
                    sys.stdout.write(color + '~')
                elif row.walls[DIR_W] or row.short_walls[DIR_W]:
                    if row.short_walls[DIR_W]:
                        extra = color_short_wall
                    else:
                        extra = ''
                    if row.victim and row.victim.facing and row.victim.facing == DIR_W:
                        sys.stdout.write(color + extra + '←')
                    else:
                        sys.stdout.write(color + extra + '▌')
                else:
                    if row.victim and row.victim.facing and row.victim.facing == DIR_W:
                        sys.stdout.write(color + '←')
                    else:
                        sys.stdout.write(color + ' ')

                if row == self.player.cell:
                    sys.stdout.write(color + 'P')
                elif row.victim:
                    if row.victim.type == Victim.T_COP:
                        sys.stdout.write(color + 'L')
                    elif row.victim.type == Victim.T_SWAT:
                        sys.stdout.write(color + 'S')
                    elif row.victim.type == Victim.T_CAT:
                        sys.stdout.write(color + 'C')
                    else:
                        sys.stdout.write(color + 'V')
                elif row.obstacle:
                    sys.stdout.write(color + row.obstacle.get_interactive_character())
                elif row.hazard:
                    sys.stdout.write(color + 'H')
                elif row.mine:
                    sys.stdout.write(color + 'M')
                elif row.has_reticles():
                    sys.stdout.write(color + color_reticle + 'O')
                elif row.exit:
                    if self.num_alive() == 0:
                        extra = color_exit_active
                    else:
                        extra = color_exit_inactive
                    sys.stdout.write(color + extra + 'E')
                else:
                    sys.stdout.write(color + ' ')

                if row.escapes[DIR_E]:
                    sys.stdout.write(color + '>')
                elif row.switches[DIR_E]:
                    sys.stdout.write(color + '~')
                elif row.walls[DIR_E] or row.short_walls[DIR_E]:
                    if row.short_walls[DIR_E]:
                        extra = color_short_wall
                    else:
                        extra = ''
                    if row.victim and row.victim.facing and row.victim.facing == DIR_E:
                        sys.stdout.write(color + extra + '→')
                    else:
                        sys.stdout.write(color + extra + '▐')
                else:
                    if row.victim and row.victim.facing and row.victim.facing == DIR_E:
                        sys.stdout.write(color + '→')
                    else:
                        sys.stdout.write(color + ' ')
            sys.stdout.write("\n")
            for (x, row) in enumerate(col):
                if y % 2 == 0:
                    if x % 2 == 0:
                        color = color_bg_1
                    else:
                        color = color_bg_2
                else:
                    if x % 2 == 0:
                        color = color_bg_2
                    else:
                        color = color_bg_1
                if row.escapes[DIR_S]:
                    sys.stdout.write(color + 'VVV')
                elif row.switches[DIR_S]:
                    sys.stdout.write(color + '~~~')
                elif row.walls[DIR_S] or row.short_walls[DIR_S]:
                    if row.escapes[DIR_W]:
                        sys.stdout.write(color + '<')
                    elif row.switches[DIR_W]:
                        sys.stdout.write(color + '~')
                    elif row.walls[DIR_W] or row.short_walls[DIR_W]:
                        if row.short_walls[DIR_S] and row.short_walls[DIR_W]:
                            extra = color_short_wall
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '▙')
                    else:
                        if row.short_walls[DIR_S]:
                            extra = color_short_wall
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '▄')
                    if row.short_walls[DIR_S]:
                        extra = color_short_wall
                    else:
                        extra = ''
                    if row.victim and row.victim.facing and row.victim.facing == DIR_S:
                        sys.stdout.write(color + extra + '↓')
                    else:
                        sys.stdout.write(color + extra + '▄')
                    if row.escapes[DIR_E]:
                        sys.stdout.write(color + '>')
                    elif row.switches[DIR_E]:
                        sys.stdout.write(color + '~')
                    elif row.walls[DIR_E] or row.short_walls[DIR_E]:
                        if row.short_walls[DIR_S] and row.short_walls[DIR_E]:
                            extra = color_short_wall
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '▟')
                    else:
                        if row.short_walls[DIR_S]:
                            extra = color_short_wall
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '▄')
                else:
                    if row.escapes[DIR_W]:
                        sys.stdout.write(color + '<')
                    elif row.switches[DIR_W]:
                        sys.stdout.write(color + '~')
                    elif row.walls[DIR_W] or row.short_walls[DIR_W]:
                        if row.short_walls[DIR_W]:
                            extra = color_short_wall
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '▌')
                    else:
                        sys.stdout.write(color + ' ')
                    if row.victim and row.victim.facing and row.victim.facing == DIR_S:
                        sys.stdout.write(color + '↓')
                    else:
                        sys.stdout.write(color + ' ')
                    if row.escapes[DIR_E]:
                        sys.stdout.write(color + '>')
                    elif row.switches[DIR_E]:
                        sys.stdout.write(color + '~')
                    elif row.walls[DIR_E] or row.short_walls[DIR_E]:
                        if row.short_walls[DIR_E]:
                            extra = color_short_wall
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '▐')
                    else:
                        sys.stdout.write(color + ' ')
            sys.stdout.write("\n")

class State(object):

    def __init__(self, level):

        self.level = level
        self.lights = level.lights
        self.victims = []
        self.obstacles = []
        self.mines = []
        self.player = level.player.clone()

        for victim in level.victims:
            self.victims.append(victim.clone())
        for obstacle in level.obstacles:
            self.obstacles.append(obstacle.clone())
        for mine in level.mines:
            self.mines.append(mine.clone())

    def apply(self):

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

    def checksum(self):

        sumlist = []
        if self.level.lights:
            sumlist.append('l1')
        else:
            sumlist.append('l0')
        sumlist.append('p=%s' % (self.player.cell.checksum()))
        for (idx, victim) in enumerate(self.victims):
            sumlist.append('v%d=%s' % (idx, victim.checksum()))
        for (idx, obstacle) in enumerate(self.obstacles):
            sumlist.append('o%d=%s' % (idx, obstacle.checksum()))
        for (idx, mine) in enumerate(self.mines):
            sumlist.append('m%d=%s' % (idx, mine.checksum()))
        return '|'.join(sumlist)

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

    def get_state(self):
        state = State(self.level)
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
        print('Winning moves (%d) for %s:' % (len(move_set), self.level.desc))
        for (n, move) in enumerate(move_set):
            print("\t%d. %s" % (n+1, DIR_T[move]))

    def store_winning_moves(self, quiet=False, display_moves=True):
        if not quiet:
            print('Found winning solution with %d moves' % (len(self.moves)))
        self.max_steps = len(self.moves)-1
        if self.solution is None or len(self.moves) < len(self.solution):
            self.solution = []
            for direction in self.moves:
                self.solution.append(direction)
        if not quiet and display_moves:
            self.print_winning_move_set(self.moves)

    def print(self):
        self.level.print()
        if self.level.won:
            print('You win!')
            print('')
            self.store_winning_moves(display_moves=True)
        elif self.alive == False:
            print('You have lost.')
        else:
            if self.max_steps is not None:
                print('Steps: %s/%s' % (self.cur_steps, self.max_steps))
            if self.step_limit():
                print('Out of moves, you lose!')
            else:
                print('Num alive: %d' % (self.level.num_alive()))
                print('Possible moves:')
                for direction in self.level.possible_moves():
                    print("\t%s" % (DIR_T[direction]))

    def interactive(self):
        colorama.init(autoreset=True)
        self.level.update_all_facing_vars()
        while True:
            self.print()
            if self.level.won:
                return True
            elif self.step_limit():
                return False
            elif self.alive == False:
                return False
            print('[n]orth, [e]ast, [s]outh, [w]est, [u]ndo, [r]eset, [q]uit')
            sys.stdout.write('[%d] > ' % (self.cur_steps + 1))
            sys.stdout.flush()
            cmd = sys.stdin.readline()
            cmd = cmd.strip()
            if cmd == '':
                continue
            cmd = cmd[0].lower()

            direction = None
            if cmd == 'q':
                return False
            elif cmd == 'u':
                self.undo()
            elif cmd == 'r':
                while len(self.states) > 0:
                    self.undo()
            elif cmd in DIR_CMD:
                direction = DIR_CMD[cmd]
                if direction in self.level.possible_moves():
                    try:
                        self.move(DIR_CMD[cmd])
                    except PlayerLose as e:
                        self.alive = False
                        report_str = 'Player Death: %s' % (e)
                        print('-'*len(report_str))
                        print(report_str)
                        print('-'*len(report_str))

    def solve_recurs(self):
        (state, new_checksum) = self.get_state()
        if not new_checksum:
            return
        for direction in self.level.possible_moves():
            try:
                if (self.move(direction, state)):
                    self.store_winning_moves(quiet=True, display_moves=False)
                    self.undo()
                else:
                    if self.step_limit():
                        self.undo()
                    else:
                        self.solve_recurs()
                        self.undo()
            except PlayerLose:
                self.undo()

    def solve(self):
        """
        Frontend for solving - mostly just to make sure that SWAT
        reticles are updated properly after all map components have
        been added.
        """
        self.level.update_all_facing_vars()
        return self.solve_recurs()
