#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4:

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
        game.interactive()
    elif args.test:
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
                print('No solutions found in %d turns!' % (game.max_steps))
        else:
            print('')
            print('    def test_%s(self):' % (args.level))
            print('        game = Game(levels.get_level(\'%s\'))' % (args.level))
            print('        game.solve()')
            print('        self.assertEqual(game.solution, [')
            for direction in game.solution:
                print('            %s,' % (dir_str[direction]))
            print('        ])')
            print('')
    else:
        game.solve()
        if game.solution is None:
            if game.max_steps is None:
                print('No solutions found!')
            else:
                print('No solutions found in %d turns!' % (game.max_steps))
        else:
            game.print_winning_move_set(game.solution)
        #for csum in sorted(game.checksums.keys()):
        #    print(csum)

