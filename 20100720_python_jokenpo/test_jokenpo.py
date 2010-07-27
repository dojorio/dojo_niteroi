import unittest
from jokenpo import jokenpo

class TestJokenPo(unittest.TestCase):

    def test_pedra_empate_pedra(self):
        jogada_1 = jogada_2 = 'pedra'
        self.assertEquals(jokenpo(jogada_1, jogada_2), 'empate')

    def test_papel_empate_papel(self):
        jogada_1 = jogada_2 = 'papel'
        self.assertEquals(jokenpo(jogada_1, jogada_2), 'empate')

    def test_tesoura_empate_tesoura(self):
        jogada_1 = jogada_2 = 'tesoura'
        self.assertEquals(jokenpo(jogada_1, jogada_2), 'empate')

    def test_papel_ganha_de_pedra(self):
        jogada_1, jogada_2 = 'papel', 'pedra'
        self.assertEquals(jokenpo(jogada_1, jogada_2), 'papel')

    def test_pedra_perde_para_papel(self):
        jogada_1, jogada_2 = 'pedra', 'papel'
        self.assertEquals(jokenpo(jogada_1, jogada_2), 'papel')

    def test_papel_perde_para_tesoura(self):
        jogada_1, jogada_2 = 'papel', 'tesoura'
        self.assertEquals(jokenpo(jogada_1, jogada_2), 'tesoura')

    def test_tesoura_ganha_de_papel(self):
        jogada_1, jogada_2 = 'tesoura', 'papel'
        self.assertEquals(jokenpo(jogada_1, jogada_2), 'tesoura')

unittest.main()
