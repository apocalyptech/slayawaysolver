#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4 fileencoding=utf-8:

import sys
import argparse
from slaysolver.app import Game, DIR_N, DIR_S, DIR_E, DIR_W
from slaysolver.levels import Levels

if __name__ == '__main__':

    levels = Levels()

    parser = argparse.ArgumentParser(
        description='Play or solve Slayaway Camp levels',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    group = parser.add_mutually_exclusive_group()

    group.add_argument('-i', '--interactive',
        action='store_true',
        help='Run interactively rather than in solver mode')

    group.add_argument('-t', '--test',
        action='store_true',
        help='Generate python code suitable for a unit test')

    parser.add_argument('-l', '--level',
        choices=levels.level_names + ['list'],
        default='s1_s01',
        metavar='LEVELNAME',
        help='Level name to run (use "list" to get a list)')

    args = parser.parse_args()

    if args.level == 'list':
        levels.report_levels()
        sys.exit(0)

    game = Game(levels.get_level(args.level))
    if args.interactive:
        # This is pretty improper, but it's a bit silly to require these
        # modules if you're *not* using interactive mode
        try:
            import readchar
        except ModuleNotFoundError:
            print('Error: "readchar" python library not found.  Please `pip install readchar`')
            print('or otherwise get that library installed.')
            sys.exit(1)
        try:
            import colorama
        except ModuleNotFoundError:
            print('Error: "colorama" python library not found.  Please `pip install colorama`')
            print('or otherwise get that library installed.')
            sys.exit(1)
        game.interactive()
    elif args.test:
        # Not actually applicable anywhere since we're using BFS now, which does this by nature
        #if game.level.return_first_solution:
        #    print('NOTE: We will return the first solution found, not the most optimal one.')
        dir_str = {
            DIR_N: 'DIR_N',
            DIR_S: 'DIR_S',
            DIR_E: 'DIR_E',
            DIR_W: 'DIR_W',
        }
        game.solve()
        if game.solution is None:
            if game.max_steps is None:
                print('No solutions found!')
            else:
                print('No solutions found in {} turns!'.format(game.max_steps))
        else:
            print('')
            print('    def test_{}(self):'.format(args.level))
            print('        game = Game(levels.get_level(\'{}\'))'.format(args.level))
            print('        game.solve()')
            print('        self.assertEqual(game.solution, [')
            for direction in game.solution:
                print('            {},'.format(dir_str[direction]))
            print('        ])')
            print('')
    else:
        # Not actually applicable anywhere since we're using BFS now, which does this by nature
        #if game.level.return_first_solution:
        #    print('NOTE: We will return the first solution found, not the most optimal one.')
        game.solve()
        if game.solution is None:
            if game.max_steps is None:
                print('No solutions found!')
            else:
                print('No solutions found in {} turns!'.format(game.max_steps))
        else:
            game.print_winning_move_set(game.solution)
        #for csum in sorted(game.checksums.keys()):
        #    print(csum)

