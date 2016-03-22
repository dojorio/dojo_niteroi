import unittest
from jokenpo import avalia_jogo

class TestJokenpo(unittest.TestCase):

    def test_pedra_com_pedra_retorna_empate(self):
        jogada_1 = 'pedra'
        jogada_2 = 'pedra'
        self.assertEqual('empate', avalia_jogo(jogada_1, jogada_2))

    def test_pedra_com_tesoura_retorna_pedra(self):
        jogada_1 = 'pedra'
        jogada_2 = 'tesoura'
        self.assertEqual('pedra', avalia_jogo(jogada_1, jogada_2))

    def test_tesoura_com_pedra_retorna_pedra(self):
        jogada_1 = 'tesoura'
        jogada_2 = 'pedra'
        self.assertEqual('pedra', avalia_jogo(jogada_1, jogada_2))

    def test_tesoura_com_tesoura_retorna_empate(self):
        jogada_1 = 'tesoura'
        jogada_2 = 'tesoura'
        self.assertEqual('empate',avalia_jogo(jogada_1, jogada_2))

    def test_tesoura_com_papel_retorna_tesoura(self):
        jogada_1 = 'tesoura'
        jogada_2 = 'papel'
        self.assertEqual('tesoura',avalia_jogo(jogada_1, jogada_2))

    def test_papel_com_papel_retorna_empate(self):
        jogada_1 = 'papel'
        jogada_2 = 'papel'
        self.assertEqual('empate', avalia_jogo(jogada_1, jogada_2))

    def test_papel_com_tesoura_retorna_tesoura(self):
        jogada_1 = 'papel'
        jogada_2 = 'tesoura'
        self.assertEqual('tesoura', avalia_jogo(jogada_1, jogada_2))

    def test_papel_com_pedra_retorna_papel(self):
        jogada_1 = 'papel'
        jogada_2 = 'pedra'
        self.assertEqual('papel', avalia_jogo(jogada_1, jogada_2))

    def test_pedra_com_papel_retorna_papel(self):
        jogada_1 = 'pedra'
        jogada_2 = 'papel'
        self.assertEqual('papel', avalia_jogo(jogada_1, jogada_2))

unittest.main()
