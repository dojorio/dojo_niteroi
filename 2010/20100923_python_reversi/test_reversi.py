import unittest
from reversi import Reversi

class TestReversi(unittest.TestCase):

    def test_primeira_jogada_branco_2_3(self):
        reversi = Reversi()
        posicao = (2, 3)
        resultado = [
            [' ', ' ', ' ', ' '],
            [' ', 'P', 'B', ' '],
            [' ', 'B', 'B', 'B'],
            [' ', ' ', ' ', ' '],
        ]
        reversi.jogada('B', posicao)
        self.assertEqual(reversi.tabuleiro, resultado)

    def test_primeira_jogada_preto_2_0(self):
        reversi = Reversi()
        posicao = (2, 0)
        resultado = [
            [' ', ' ', ' ', ' '],
            [' ', 'P', 'B', ' '],
            ['P', 'P', 'P', ' '],
            [' ', ' ', ' ', ' '],
        ]
        reversi.jogada('P', posicao)
        self.assertEqual(reversi.tabuleiro, resultado)

    def test_primeira_jogada_branco_1_0(self):
        reversi = Reversi()
        posicao = (1, 0)
        resultado = [
            [' ', ' ', ' ', ' '],
            ['B', 'B', 'B', ' '],
            [' ', 'B', 'P', ' '],
            [' ', ' ', ' ', ' '],
        ]
        reversi.jogada('B', posicao)
        self.assertEqual(reversi.tabuleiro, resultado)

    def test_primeira_jogada_branco_0_1(self):
        reversi = Reversi()
        posicao = (0, 1)
        resultado = [
            [' ', 'B', ' ', ' '],
            [' ', 'B', 'B', ' '],
            [' ', 'B', 'P', ' '],
            [' ', ' ', ' ', ' '],
        ]
        reversi.jogada('B', posicao)
        self.assertEqual(reversi.tabuleiro, resultado)

    def test_primeira_jogada_preto_3_1(self):
        reversi = Reversi()
        posicao = (3, 1)
        resultado = [
            [' ', ' ', ' ', ' '],
            [' ', 'P', 'B', ' '],
            [' ', 'P', 'P', ' '],
            [' ', 'P', ' ', ' '],
        ]
        reversi.jogada('P', posicao)
        self.assertEqual(reversi.tabuleiro, resultado)

    def test_segunda_jogada_branco_1_0(self):
        reversi = Reversi()
        reversi.jogada('P', (3, 1))
        reversi.jogada('B', (1, 0))
        resultado = [
            [' ', ' ', ' ', ' '],
            ['B', 'B', 'B', ' '],
            [' ', 'P', 'P', ' '],
            [' ', 'P', ' ', ' '],
        ]
        self.assertEqual(reversi.tabuleiro, resultado)


unittest.main()
