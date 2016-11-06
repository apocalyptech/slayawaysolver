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
#     a branch will only be exlored if its state is either not
#     seen already, or if the seen state occurs at an earlier
#     point in the tree.
#
# The second point in particular makes a HUGE difference once you
# start to get beyond max_step counts of 14, 15 or so.  Without
# comparing checksums of the seen states, a max_step of 17 can take
# many tens of seconds, but returns nearly instantly when pruning.
#
# Currently the only objects actually supported are:
#   * Walls
#   * Short Walls
#   * Bookcases (though I call them Cabinets)
#   * Victims
#   * Hazards (fire, water, holes - all just considered a "hazard")
#
# Stuff not yet implemented:
#   * Police
#   * SWAT
#   * Cats
#   * Light Switches
#   * Telephones (I assume I'll want to rewrite Victim.scare()
#     a bit for re-use)
#   * Mines (probably just a special-cased Hazard)
#
# This can be run interactively with the -i/--interactive flag.
# While running interactive, 'q' will quit, 'u' will undo,
# 'r' will reset, and n/e/s/w will move in the specified
# direction.
#
# Each space will be drawn w/ 3x3 characters, with pipes, plusses, and
# dashes to indicate walls ("low" walls will be in red).  Walls will
# appear to be two characters deep 'cause we consider a south wall on
# one cell to be a north wall on the next one down.
#
# Symbols in the middle of the cell render:
#   P - Player
#   V - Victim
#   H - Hazard
#   | - Bookcase/Cabinet which can be knocked over west or east
#   = - Bookcase/Cabinet which can be knocked over north or south

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

class PlayerDeath(Exception):
    """
    Custom exception to handle player deaths
    """

class Cell(object):

    def __init__(self, x, y, level=None):
        self.x = x
        self.y = y
        self.exit = False
        self.hazard = False
        self.walls = [False]*4
        self.short_walls = [False]*4
        self.victim = None
        self.obstacle = None

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
        if self.victim:
            self.victim.die()
            self.victim = None

    def set_obstacle(self, obstacle):
        if obstacle.cell is not None:
            obstacle.cell.obstacle = None
        self.obstacle = obstacle
        self.obstacle.cell = self

    def clone(self):
        newobj = Cell(self.x, self.y)
        return newobj

class Cabinet(object):

    def __init__(self, fall_dirs, level):
        self.cell = None
        self.fall_dirs = fall_dirs
        self.level = level

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

class Victim(object):
    """
    Victim
    """

    def __init__(self, level):
        self.cell = None
        self.alive = True
        self.level = level

    def die(self):
        self.alive = False
        
        # Check for adjacent victims who might have been scared by our death
        for direction in DIRS:
            if self.cell.walls[direction]:
                continue
            rel_cell = self.level.get_cell_relative_cell(self.cell, direction)
            if rel_cell.victim:
                rel_cell.victim.scare(direction)

    def scare(self, direction):

        while True:
            cur_cell = self.cell
            if direction not in self.level.possible_moves(from_cell=cur_cell):
                break
            next_cell = self.level.get_cell_relative_cell(cur_cell, direction)
            if next_cell.obstacle:
                next_cell.obstacle.hit(direction)
                break
            if next_cell.victim:
                break
            next_cell.set_victim(self)
            if next_cell.hazard:
                next_cell.kill_victim()
                break

        return False

    def clone(self):
        newobj = Victim(self.level)
        newobj.alive = self.alive
        newobj.cell = self.cell.clone()
        return newobj

    def apply_clone(self, newobj):
        self.alive = newobj.alive
        if self.alive:
            self.level.get_cell(newobj.cell.x, newobj.cell.y).set_victim(self)

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

        self.cells = []
        self.victims = []
        self.obstacles = []
        for y in range(height):
            self.cells.append([])
            for x in range(width):
                self.cells[y].append(Cell(x, y, self))
        player_cell = self.get_cell(player_x, player_y)
        self.player = Player(player_cell, self)
        self.won = False
        self.set_exit(exit_x, exit_y)

    def add_victim(self, x, y):
        victim = Victim(self)
        self.victims.append(victim)
        self.cells[y][x].set_victim(victim)

    def add_obstacle(self, x, y, obstacle):
        self.obstacles.append(obstacle)
        self.get_cell(x, y).set_obstacle(obstacle)

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
            if x == 8:
                return None
            else:
                return self.cells[y][x+1]
        if direction == DIR_N:
            if y == 0:
                return None
            else:
                return self.cells[y-1][x]
        if direction == DIR_S:
            if y == 8:
                return None
            else:
                return self.cells[y+1][x]

    def move_player(self, direction):
        while True:
            cur_cell = self.player.cell
            if cur_cell.exit and self.num_alive() == 0:
                self.won = True
                return True
            if direction not in self.possible_moves(from_cell=cur_cell):
                break
            next_cell = self.get_cell_relative_cell(cur_cell, direction)
            if next_cell.obstacle:
                next_cell.obstacle.hit(direction)
                break
            if next_cell.victim:
                next_cell.kill_victim()
                break
            self.player.cell = next_cell
            if next_cell.hazard:
                raise PlayerDeath()

        # check for adjacent victims to scare
        for direction in DIRS:
            if self.player.cell.walls[direction]:
                continue
            adj_cell = self.get_cell_relative_cell(self.player.cell, direction)
            if adj_cell is None:
                continue
            if adj_cell.victim is not None:
                adj_cell.victim.scare(direction)

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

    def num_alive(self):
        alive = 0
        for victim in self.victims:
            if victim.alive:
                alive += 1
        return alive

    def print(self):
        print(self.desc)
        for (y, col) in enumerate(self.cells):
            for (x, row) in enumerate(col):
                if y % 2 == 0:
                    if x % 2 == 0:
                        color = colorama.Back.RESET
                    else:
                        color = colorama.Back.YELLOW
                else:
                    if x % 2 == 0:
                        color = colorama.Back.YELLOW
                    else:
                        color = colorama.Back.RESET
                if row.walls[DIR_N] or row.short_walls[DIR_N]:
                    if row.walls[DIR_W] or row.short_walls[DIR_W]:
                        if row.short_walls[DIR_N] and row.short_walls[DIR_W]:
                            extra = colorama.Fore.RED
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '+')
                    else:
                        if row.short_walls[DIR_N]:
                            extra = colorama.Fore.RED
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '-')
                    if row.short_walls[DIR_N]:
                        extra = colorama.Fore.RED
                    else:
                        extra = ''
                    sys.stdout.write(color + extra + '-')
                    if row.walls[DIR_E] or row.short_walls[DIR_E]:
                        if row.short_walls[DIR_N] and row.short_walls[DIR_E]:
                            extra = colorama.Fore.RED
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '+')
                    else:
                        if row.short_walls[DIR_N]:
                            extra = colorama.Fore.RED
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '-')
                else:
                    if row.walls[DIR_W] or row.short_walls[DIR_W]:
                        if row.short_walls[DIR_W]:
                            extra = colorama.Fore.RED
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '|')
                    else:
                        sys.stdout.write(color + ' ')
                    sys.stdout.write(color + ' ')
                    if row.walls[DIR_E] or row.short_walls[DIR_E]:
                        if row.short_walls[DIR_E]:
                            extra = colorama.Fore.RED
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '|')
                    else:
                        sys.stdout.write(color + ' ')
            sys.stdout.write("\n")
            for (x, row) in enumerate(col):
                if y % 2 == 0:
                    if x % 2 == 0:
                        color = colorama.Back.RESET
                    else:
                        color = colorama.Back.YELLOW
                else:
                    if x % 2 == 0:
                        color = colorama.Back.YELLOW
                    else:
                        color = colorama.Back.RESET
                if row.walls[DIR_W] or row.short_walls[DIR_W]:
                    if row.short_walls[DIR_W]:
                        extra = colorama.Fore.RED
                    else:
                        extra = ''
                    sys.stdout.write(color + extra + '|')
                else:
                    sys.stdout.write(color + ' ')

                if row == self.player.cell:
                    sys.stdout.write(color + 'P')
                elif row.exit:
                    sys.stdout.write(color + 'E')
                elif row.hazard:
                    sys.stdout.write(color + 'H')
                elif row.victim:
                    sys.stdout.write(color + 'V')
                elif row.obstacle:
                    if DIR_N in row.obstacle.fall_dirs:
                        sys.stdout.write(color + '=')
                    elif DIR_W in row.obstacle.fall_dirs:
                        sys.stdout.write(color + '|')
                    else:
                        sys.stdout.write(color + 'X')
                else:
                    sys.stdout.write(color + ' ')

                if row.walls[DIR_E] or row.short_walls[DIR_E]:
                    if row.short_walls[DIR_E]:
                        extra = colorama.Fore.RED
                    else:
                        extra = ''
                    sys.stdout.write(color + extra + '|')
                else:
                    sys.stdout.write(color + ' ')
            sys.stdout.write("\n")
            for (x, row) in enumerate(col):
                if y % 2 == 0:
                    if x % 2 == 0:
                        color = colorama.Back.RESET
                    else:
                        color = colorama.Back.YELLOW
                else:
                    if x % 2 == 0:
                        color = colorama.Back.YELLOW
                    else:
                        color = colorama.Back.RESET
                if row.walls[DIR_S] or row.short_walls[DIR_S]:
                    if row.walls[DIR_W] or row.short_walls[DIR_W]:
                        if row.short_walls[DIR_S] and row.short_walls[DIR_W]:
                            extra = colorama.Fore.RED
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '+')
                    else:
                        if row.short_walls[DIR_S]:
                            extra = colorama.Fore.RED
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '-')
                    if row.short_walls[DIR_S]:
                        extra = colorama.Fore.RED
                    else:
                        extra = ''
                    sys.stdout.write(color + extra + '-')
                    if row.walls[DIR_E] or row.short_walls[DIR_E]:
                        if row.short_walls[DIR_S] and row.short_walls[DIR_E]:
                            extra = colorama.Fore.RED
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '+')
                    else:
                        if row.short_walls[DIR_S]:
                            extra = colorama.Fore.RED
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '-')
                else:
                    if row.walls[DIR_W] or row.short_walls[DIR_W]:
                        if row.short_walls[DIR_W]:
                            extra = colorama.Fore.RED
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '|')
                    else:
                        sys.stdout.write(color + ' ')
                    sys.stdout.write(color + ' ')
                    if row.walls[DIR_E] or row.short_walls[DIR_E]:
                        if row.short_walls[DIR_E]:
                            extra = colorama.Fore.RED
                        else:
                            extra = ''
                        sys.stdout.write(color + extra + '|')
                    else:
                        sys.stdout.write(color + ' ')
            sys.stdout.write("\n")

class State(object):

    def __init__(self, level):

        self.level = level
        self.victims = []
        self.obstacles = []
        self.player = level.player.clone()

        for victim in level.victims:
            self.victims.append(victim.clone())
        for obstacle in level.obstacles:
            self.obstacles.append(obstacle.clone())

    def apply(self):

        self.level.player.apply_clone(self.player)

        for (saved, real) in zip(self.victims, self.level.victims):
            real.apply_clone(saved)

        for (saved, real) in zip(self.obstacles, self.level.obstacles):
            real.apply_clone(saved)

    def checksum(self):

        sumlist = []
        sumlist.append('p=%d,%d' % (self.player.cell.x, self.player.cell.y))
        for (idx, victim) in enumerate(self.victims):
            if victim.alive:
                sumlist.append('v%d=%d,%d' % (idx, victim.cell.x, victim.cell.y))
            else:
                sumlist.append('v%d=d' % (idx))
        for (idx, obstacle) in enumerate(self.obstacles):
            sumlist.append('o%d=%d,%d;%s' % (idx, obstacle.cell.x, obstacle.cell.y,
                ','.join([str(d) for d in obstacle.fall_dirs])))
        return '|'.join(sumlist)

class Game(object):
    
    def __init__(self, level):

        colorama.init(autoreset=True)

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

    def store_winning_moves(self, display=True):
        print('Found winning solution with %d moves' % (len(self.moves)))
        self.max_steps = len(self.moves)-1
        if self.solution is None or len(self.moves) < len(self.solution):
            self.solution = []
            for direction in self.moves:
                self.solution.append(direction)
        if display:
            self.print_winning_move_set(self.moves)

    def print(self):
        self.level.print()
        if self.level.won:
            print('You win!')
            print('')
            self.store_winning_moves(display=True)
        elif self.alive == False:
            print('You have died.')
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
            cmd = cmd.strip()[0].lower()

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
                    except PlayerDeath:
                        self.alive = False

    def solve(self):
        (state, new_checksum) = self.get_state()
        if not new_checksum:
            return
        for direction in self.level.possible_moves():
            try:
                if (self.move(direction, state)):
                    self.store_winning_moves(display=False)
                    self.undo()
                else:
                    if self.step_limit():
                        self.undo()
                    else:
                        self.solve()
                        self.undo()
            except PlayerDeath:
                self.undo()
