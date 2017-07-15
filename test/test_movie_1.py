#!/usr/bin/env python
# vim: set expandtab tabstop=4 shiftwidth=4 fileencoding=utf-8:

import unittest
from slaysolver.app import Game, DIR_N, DIR_E, DIR_W, DIR_S
from slaysolver.levels import Levels

levels = Levels()

class Movie1LevelTests(unittest.TestCase):

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
