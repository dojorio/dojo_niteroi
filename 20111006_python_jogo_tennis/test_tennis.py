import unittest2

from tennis import Game

class TestPlacarTennis(unittest2.TestCase):

    def test_new_game(self):
        game = Game()
        self.assertEqual(game.score, (0,0))

    def test_player_1_scores_15_0(self):
        game = Game()
        game.scores(1)
        self.assertEqual(game.score, (15,0))

    def test_player_2_scores_0_15(self):
        game = Game()
        game.scores(2)
        self.assertEqual(game.score, (0, 15))

    def test_player_1_scores_30_0(self):
        game = Game(15, 0)
        game.scores(1)
        self.assertEqual(game.score, (30, 0))

    def test_player_2_scores_0_30(self):
        game = Game(0, 15)
        game.scores(2)
        self.assertEqual(game.score, (0, 30))

    def test_player_2_scores_15_30(self):
        game = Game(15, 15)
        game.scores(2)
        self.assertEqual(game.score, (15, 30))

    def test_player_1_scores_40_30(self):
        game = Game(30, 30)
        game.scores(1)
        self.assertEqual(game.score, (40, 30))

    def test_player_2_scores_30_40(self):
        game = Game(30, 30)
        game.scores(2)
        self.assertEqual(game.score, (30, 40))

    def test_player_1_scores_45_30(self):
        game = Game(40, 30)
        game.scores(1)
        self.assertEqual(game.score, (45, 30))

    def test_player_2_scores_30_45(self):
        game = Game(30, 40)
        game.scores(2)
        self.assertEqual(game.score, (30, 45))

    def test_player_1_scores_40_40(self):
        game = Game(30, 40)
        game.scores(1)
        self.assertEqual(game.score, (40, 40))
        self.assertEqual(game.status(), 'Deuce')

    def test_player_1_win(self):
        game = Game(40,30)
        game.scores(1)
        self.assertEqual(game.status(), 'player 1 win')





unittest2.main()
