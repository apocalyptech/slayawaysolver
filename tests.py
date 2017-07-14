#!/usr/bin/env pypy3
# vim: set expandtab tabstop=4 shiftwidth=4:

import unittest

from slaysolver.app import Game, DIR_N, DIR_E, DIR_W, DIR_S
from slaysolver.levels import Levels

#
# This definitely isn't supposed to be a comprehensive set of actual
# unit tests.  Rather, we're just testing the solver versus known
# solutions of each level.
#

levels = Levels()

class LevelTests(unittest.TestCase):

    def test_s1_s01(self):
        game = Game(levels.get_level('s1_s01'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
        ])

    def test_s1_s02(self):
        game = Game(levels.get_level('s1_s02'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
        ])

    def test_s1_s03(self):
        game = Game(levels.get_level('s1_s03'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_N,
        ])

    def test_s1_s04(self):
        game = Game(levels.get_level('s1_s04'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
        ])

    def test_s1_s05(self):
        game = Game(levels.get_level('s1_s05'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_W,
        ])

    def test_s1_s06(self):
        game = Game(levels.get_level('s1_s06'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
        ])

    def test_s1_s07(self):
        game = Game(levels.get_level('s1_s07'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
        ])

    def test_s1_s08(self):
        game = Game(levels.get_level('s1_s08'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
        ])

    def test_s1_s09(self):
        game = Game(levels.get_level('s1_s09'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
        ])

    def test_s1_s10(self):
        game = Game(levels.get_level('s1_s10'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
        ])

    def test_s1_d1(self):
        game = Game(levels.get_level('s1_d1'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_W,
        ])

    def test_s1_d2(self):
        game = Game(levels.get_level('s1_d2'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_W,
        ])

    def test_s1_d3(self):
        game = Game(levels.get_level('s1_d3'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
        ])

    def test_s1_d4(self):
        game = Game(levels.get_level('s1_d4'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
        ])

    def test_s1_d5(self):
        game = Game(levels.get_level('s1_d5'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
        ])

    def test_s2_s01(self):
        game = Game(levels.get_level('s2_s01'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
        ])

    def test_s2_s02(self):
        game = Game(levels.get_level('s2_s02'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
        ])

    def test_s2_s03(self):
        game = Game(levels.get_level('s2_s03'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_E,
        ])

    def test_s2_s04(self):
        game = Game(levels.get_level('s2_s04'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_N,
        ])

    def test_s2_s05(self):
        game = Game(levels.get_level('s2_s05'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
        ])

    def test_s2_s06(self):
        game = Game(levels.get_level('s2_s06'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_E,
        ])

    def test_s2_s07(self):
        game = Game(levels.get_level('s2_s07'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
        ])

    def test_s2_s08(self):
        game = Game(levels.get_level('s2_s08'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_S,
        ])

    def test_s2_s09(self):
        game = Game(levels.get_level('s2_s09'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_E,
        ])

    def test_s2_s10(self):
        game = Game(levels.get_level('s2_s10'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
        ])

    def test_s2_s11(self):
        game = Game(levels.get_level('s2_s11'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
        ])

    def test_s2_s12(self):
        game = Game(levels.get_level('s2_s12'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
        ])

    def test_s2_s13(self):
        game = Game(levels.get_level('s2_s13'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
        ])

    def test_s2_d1(self):
        game = Game(levels.get_level('s2_d1'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
        ])

    def test_s2_d2(self):
        game = Game(levels.get_level('s2_d2'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
        ])

    def test_s2_d3(self):
        game = Game(levels.get_level('s2_d3'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
        ])

    def test_s2_d4(self):
        game = Game(levels.get_level('s2_d4'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
        ])

    def test_s2_d5(self):
        game = Game(levels.get_level('s2_d5'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
        ])

    def test_s25_s01(self):
        game = Game(levels.get_level('s25_s01'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_N,
        ])

    def test_s25_s02(self):
        game = Game(levels.get_level('s25_s02'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
        ])

    def test_s25_s03(self):
        game = Game(levels.get_level('s25_s03'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
        ])

    def test_s25_s04(self):
        game = Game(levels.get_level('s25_s04'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
        ])

    def test_s25_s05(self):
        game = Game(levels.get_level('s25_s05'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
        ])

    def test_s25_s06(self):
        game = Game(levels.get_level('s25_s06'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_E,
        ])

    def test_s25_s07(self):
        game = Game(levels.get_level('s25_s07'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_N,
        ])

    def test_s25_s08(self):
        game = Game(levels.get_level('s25_s08'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_N,
        ])

    def test_s25_s09(self):
        game = Game(levels.get_level('s25_s09'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
        ])

    def test_s25_s10(self):
        game = Game(levels.get_level('s25_s10'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
        ])

    def test_s25_s11(self):
        game = Game(levels.get_level('s25_s11'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_S,
        ])

    def test_s25_s12(self):
        game = Game(levels.get_level('s25_s12'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_E,
        ])

    def test_s25_s13(self):
        game = Game(levels.get_level('s25_s13'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_S,
        ])

    def test_s25_s14(self):
        game = Game(levels.get_level('s25_s14'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
        ])

    def test_s25_s15(self):
        game = Game(levels.get_level('s25_s15'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
        ])

    def test_s25_d1(self):
        game = Game(levels.get_level('s25_d1'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
        ])

    def test_s25_d2(self):
        game = Game(levels.get_level('s25_d2'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_E,
        ])

    def test_s25_d3(self):
        game = Game(levels.get_level('s25_d3'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
        ])

    def test_s25_d4(self):
        game = Game(levels.get_level('s25_d4'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
        ])

    def test_s25_d5(self):
        game = Game(levels.get_level('s25_d5'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
        ])

    def test_s3_s01(self):
        game = Game(levels.get_level('s3_s01'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_E,
        ])

    def test_s3_s02(self):
        game = Game(levels.get_level('s3_s02'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
        ])

    def test_s3_s03(self):
        game = Game(levels.get_level('s3_s03'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
        ])

    def test_s3_s04(self):
        game = Game(levels.get_level('s3_s04'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
        ])

    def test_s3_s05(self):
        game = Game(levels.get_level('s3_s05'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
        ])

    def test_s3_s06(self):
        game = Game(levels.get_level('s3_s06'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
        ])

    def test_s3_s07(self):
        game = Game(levels.get_level('s3_s07'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_N,
        ])

    def test_s3_s08(self):
        game = Game(levels.get_level('s3_s08'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
        ])

    def test_s3_s09(self):
        game = Game(levels.get_level('s3_s09'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
        ])

    def test_s3_s10(self):
        game = Game(levels.get_level('s3_s10'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_N,
        ])

    def test_s3_s11(self):
        game = Game(levels.get_level('s3_s11'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_W,
        ])

    def test_s3_s12(self):
        game = Game(levels.get_level('s3_s12'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_N,
        ])

    def test_s3_s13(self):
        game = Game(levels.get_level('s3_s13'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
        ])

    def test_s3_s14(self):
        game = Game(levels.get_level('s3_s14'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
        ])

    def test_s3_s15(self):
        game = Game(levels.get_level('s3_s15'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_N,
        ])

    def test_s3_s16(self):
        game = Game(levels.get_level('s3_s16'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
        ])

    def test_s3_d1(self):
        game = Game(levels.get_level('s3_d1'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
        ])

    def test_s3_d2(self):
        game = Game(levels.get_level('s3_d2'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
        ])

    def test_s3_d3(self):
        game = Game(levels.get_level('s3_d3'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_N,
        ])

    def test_s3_d4(self):
        game = Game(levels.get_level('s3_d4'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
        ])

    def test_s3_d5(self):
        game = Game(levels.get_level('s3_d5'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
        ])

    def test_s4_s01(self):
        game = Game(levels.get_level('s4_s01'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
        ])

    def test_s4_s02(self):
        game = Game(levels.get_level('s4_s02'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
        ])

    def test_s4_s03(self):
        game = Game(levels.get_level('s4_s03'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
        ])

    def test_s4_s04(self):
        game = Game(levels.get_level('s4_s04'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
        ])

    def test_s4_s05(self):
        game = Game(levels.get_level('s4_s05'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
        ])

    def test_s4_s06(self):
        game = Game(levels.get_level('s4_s06'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_W,
        ])

    def test_s4_s07(self):
        game = Game(levels.get_level('s4_s07'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
        ])

    def test_s4_s08(self):
        game = Game(levels.get_level('s4_s08'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_W,
        ])

    def test_s4_s09(self):
        game = Game(levels.get_level('s4_s09'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
        ])

    def test_s4_s10(self):
        game = Game(levels.get_level('s4_s10'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
        ])

    def test_s4_s11(self):
        game = Game(levels.get_level('s4_s11'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
        ])

    def test_s4_s12(self):
        game = Game(levels.get_level('s4_s12'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
        ])

    def test_s4_d1(self):
        game = Game(levels.get_level('s4_d1'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
        ])

    def test_s4_d2(self):
        game = Game(levels.get_level('s4_d2'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
        ])

    def test_s4_d3(self):
        game = Game(levels.get_level('s4_d3'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_E,
        ])

    def test_s4_d4(self):
        game = Game(levels.get_level('s4_d4'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
        ])

    def test_s4_d5(self):
        game = Game(levels.get_level('s4_d5'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
        ])

    def test_s5_s01(self):
        game = Game(levels.get_level('s5_s01'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_N,
        ])

    def test_s5_s02(self):
        game = Game(levels.get_level('s5_s02'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_N,
        ])

    def test_s5_s03(self):
        game = Game(levels.get_level('s5_s03'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
        ])

    def test_s5_s04(self):
        game = Game(levels.get_level('s5_s04'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
        ])

    def test_s5_s05(self):
        game = Game(levels.get_level('s5_s05'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
        ])

    def test_s5_s06(self):
        game = Game(levels.get_level('s5_s06'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
        ])

    def test_s5_s07(self):
        game = Game(levels.get_level('s5_s07'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
        ])

    def test_s5_s08(self):
        game = Game(levels.get_level('s5_s08'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_E,
        ])

    def test_s5_s09(self):
        game = Game(levels.get_level('s5_s09'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_W,
        ])

    def test_s5_s10(self):
        game = Game(levels.get_level('s5_s10'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_S,
        ])

    def test_s5_s11(self):
        game = Game(levels.get_level('s5_s11'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
        ])

    def test_s5_s12(self):
        game = Game(levels.get_level('s5_s12'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
        ])

    def test_s5_s13(self):
        game = Game(levels.get_level('s5_s13'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
        ])

    def test_s5_d1(self):
        game = Game(levels.get_level('s5_d1'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_N,
        ])

    def test_s5_d2(self):
        game = Game(levels.get_level('s5_d2'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
        ])

    def test_s5_d3(self):
        game = Game(levels.get_level('s5_d3'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_W,
        ])

    def test_s5_d4(self):
        game = Game(levels.get_level('s5_d4'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
        ])

    def test_s6_s01(self):
        game = Game(levels.get_level('s6_s01'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
        ])

    def test_s6_s02(self):
        game = Game(levels.get_level('s6_s02'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
        ])

    def test_s6_s03(self):
        game = Game(levels.get_level('s6_s03'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
        ])

    def test_s6_s04(self):
        game = Game(levels.get_level('s6_s04'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
        ])

    def test_s6_s05(self):
        game = Game(levels.get_level('s6_s05'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_N,
        ])

    def test_s6_s06(self):
        game = Game(levels.get_level('s6_s06'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
        ])

    def test_s6_s07(self):
        game = Game(levels.get_level('s6_s07'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
        ])

    def test_s6_s08(self):
        game = Game(levels.get_level('s6_s08'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
        ])

    def test_s6_s09(self):
        game = Game(levels.get_level('s6_s09'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
        ])

    def test_s6_s10(self):
        game = Game(levels.get_level('s6_s10'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
        ])

    def test_s6_s11(self):
        game = Game(levels.get_level('s6_s11'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_W,
        ])

    def test_s6_s12(self):
        game = Game(levels.get_level('s6_s12'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
        ])

    def test_s6_s13(self):
        game = Game(levels.get_level('s6_s13'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_N,
        ])

    def test_s6_d1(self):
        game = Game(levels.get_level('s6_d1'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
        ])

    def test_s6_d2(self):
        game = Game(levels.get_level('s6_d2'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
        ])

    def test_s6_d3(self):
        game = Game(levels.get_level('s6_d3'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
        ])

    def test_s6_d4(self):
        game = Game(levels.get_level('s6_d4'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
        ])

    def test_s7_s01(self):
        game = Game(levels.get_level('s7_s01'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
        ])

    def test_s7_s02(self):
        game = Game(levels.get_level('s7_s02'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
        ])

    def test_s7_s03(self):
        game = Game(levels.get_level('s7_s03'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
        ])

    def test_s7_s04(self):
        game = Game(levels.get_level('s7_s04'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
        ])

    def test_s7_s05(self):
        game = Game(levels.get_level('s7_s05'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
        ])

    def test_s7_s06(self):
        game = Game(levels.get_level('s7_s06'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
        ])

    def test_s7_s07(self):
        game = Game(levels.get_level('s7_s07'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
        ])

    def test_s7_s08(self):
        game = Game(levels.get_level('s7_s08'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
        ])

    def test_s7_s09(self):
        game = Game(levels.get_level('s7_s09'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
        ])

    def test_s7_s10(self):
        game = Game(levels.get_level('s7_s10'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
        ])

    def test_s7_s11(self):
        game = Game(levels.get_level('s7_s11'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_S,
        ])

    def test_s7_s12(self):
        game = Game(levels.get_level('s7_s12'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
        ])

    def test_s7_s13(self):
        game = Game(levels.get_level('s7_s13'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
        ])

    def test_s7_s14(self):
        game = Game(levels.get_level('s7_s14'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
        ])

    def test_s7_d1(self):
        game = Game(levels.get_level('s7_d1'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
        ])

    def test_s7_d2(self):
        game = Game(levels.get_level('s7_d2'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
        ])

    def test_s7_d3(self):
        game = Game(levels.get_level('s7_d3'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_N,
        ])

    def test_s8_s01(self):
        game = Game(levels.get_level('s8_s01'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_E,
        ])

    def test_s8_s02(self):
        game = Game(levels.get_level('s8_s02'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
        ])

    def test_s8_s03(self):
        game = Game(levels.get_level('s8_s03'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_S,
        ])

    def test_s8_s04(self):
        game = Game(levels.get_level('s8_s04'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_N,
            DIR_N,
            DIR_S,
            DIR_S,
        ])

    def test_s8_s05(self):
        game = Game(levels.get_level('s8_s05'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_N,
        ])

    def test_s8_s06(self):
        game = Game(levels.get_level('s8_s06'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
        ])

    def test_s8_s07(self):
        game = Game(levels.get_level('s8_s07'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
        ])

    def test_s8_s08(self):
        game = Game(levels.get_level('s8_s08'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
        ])

    def test_s8_s09(self):
        game = Game(levels.get_level('s8_s09'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
        ])

    def test_s8_s10(self):
        game = Game(levels.get_level('s8_s10'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
        ])

    def test_s8_s11(self):
        game = Game(levels.get_level('s8_s11'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
        ])

    def test_s8_s12(self):
        game = Game(levels.get_level('s8_s12'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_N,
        ])

    def test_s8_s13(self):
        game = Game(levels.get_level('s8_s13'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
        ])

    def test_s8_d1(self):
        game = Game(levels.get_level('s8_d1'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_W,
        ])

    def test_s8_d2(self):
        game = Game(levels.get_level('s8_d2'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
        ])

    def test_s8_d3(self):
        game = Game(levels.get_level('s8_d3'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
        ])

    def test_s10_s01(self):
        game = Game(levels.get_level('s10_s01'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_E,
        ])

    def test_s10_s02(self):
        game = Game(levels.get_level('s10_s02'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
        ])

    def test_s10_s03(self):
        game = Game(levels.get_level('s10_s03'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
        ])

    def test_s10_s04(self):
        game = Game(levels.get_level('s10_s04'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
        ])

    def test_s10_s05(self):
        game = Game(levels.get_level('s10_s05'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_N,
            DIR_N,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_N,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_E,
        ])

    def test_s10_s06(self):
        game = Game(levels.get_level('s10_s06'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_N,
        ])

    def test_s10_s07(self):
        game = Game(levels.get_level('s10_s07'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
        ])

    def test_s10_s08(self):
        game = Game(levels.get_level('s10_s08'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
        ])

    def test_s10_s09(self):
        game = Game(levels.get_level('s10_s09'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_W,
        ])

    def test_s10_s10(self):
        game = Game(levels.get_level('s10_s10'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_E,
            DIR_S,
        ])

    def test_s10_s11(self):
        game = Game(levels.get_level('s10_s11'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
        ])

    def test_s10_s12(self):
        game = Game(levels.get_level('s10_s12'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_S,
        ])

    def test_s10_s13(self):
        game = Game(levels.get_level('s10_s13'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
        ])

    def test_s10_d1(self):
        game = Game(levels.get_level('s10_d1'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_E,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
        ])

    def test_s10_d2(self):
        game = Game(levels.get_level('s10_d2'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
        ])

    def test_s10_d3(self):
        game = Game(levels.get_level('s10_d3'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
        ])

    @unittest.skip('This takes about 63secs on my CPU, using PyPy3')
    def test_s10_d4(self):
        game = Game(levels.get_level('s10_d4'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_N,
            DIR_S,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
        ])

    def test_nc17_s1_s01(self):
        game = Game(levels.get_level('nc17_s1_s01'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
        ])

    def test_nc17_s1_s02(self):
        game = Game(levels.get_level('nc17_s1_s02'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_S,
        ])

    def test_nc17_s1_s03(self):
        game = Game(levels.get_level('nc17_s1_s03'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_E,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_N,
        ])

    def test_nc17_s1_s04(self):
        game = Game(levels.get_level('nc17_s1_s04'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
        ])

    def test_nc17_s1_s05(self):
        game = Game(levels.get_level('nc17_s1_s05'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_S,
        ])

    def test_nc17_s1_s06(self):
        game = Game(levels.get_level('nc17_s1_s06'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_E,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_S,
            DIR_W,
            DIR_S,
        ])

    def test_nc17_s1_s07(self):
        game = Game(levels.get_level('nc17_s1_s07'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_N,
            DIR_E,
            DIR_W,
            DIR_S,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_S,
        ])

    def test_nc17_s1_s08(self):
        game = Game(levels.get_level('nc17_s1_s08'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_N,
        ])

    def test_nc17_s1_s09(self):
        game = Game(levels.get_level('nc17_s1_s09'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_N,
            DIR_S,
            DIR_E,
            DIR_E,
            DIR_N,
            DIR_W,
            DIR_W,
            DIR_S,
            DIR_E,
        ])

    def test_nc17_s1_s10(self):
        game = Game(levels.get_level('nc17_s1_s10'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_W,
            DIR_S,
            DIR_S,
            DIR_S,
            DIR_W,
            DIR_N,
            DIR_N,
            DIR_W,
            DIR_N,
            DIR_E,
            DIR_S,
            DIR_E,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
        ])

    def test_nc17_s2_s01(self):
        game = Game(levels.get_level('nc17_s2_s01'))
        game.solve()
        self.assertEqual(game.solution, [
            DIR_W,
            DIR_S,
            DIR_N,
            DIR_E,
            DIR_E,
            DIR_S,
            DIR_W,
            DIR_S,
            DIR_E,
        ])

if __name__ == '__main__':

    unittest.main(verbosity=2)
