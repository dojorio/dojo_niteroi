# -*- coding:utf-8 -*-
import unittest

dicionario_de_jogadas = {
    'pedra':{
        'tesoura':'pedra',
        'papel':'papel',
    },
    'tesoura':{
        'pedra':'pedra',
        'papel':'tesoura',
    },
    'papel':{
        'tesoura':'tesoura',
        'pedra':'papel',
    },
}


def jokenpo(jogada_1, jogada_2):
    try:
        return dicionario_de_jogadas[jogada_1][jogada_2]
    except KeyError:
        return 'empate'

class TestJokenpo(unittest.TestCase):

    def test_pedra_vs_papel_e_papel_ganha(self):
        self.assertEquals(jokenpo('pedra', 'papel'), 'papel')

    def test_pedra_vs_tesoura_e_pedra_ganha(self):
        self.assertEquals(jokenpo('pedra', 'tesoura'), 'pedra')

    def test_papel_vs_tesoura_e_tesoura_ganha(self):
        self.assertEquals(jokenpo('papel', 'tesoura'), 'tesoura')

    def test_jogadas_iguais(self):
        self.assertEquals(jokenpo('papel', 'papel'), 'empate')
        self.assertEquals(jokenpo('tesoura', 'tesoura'), 'empate')
        self.assertEquals(jokenpo('pedra', 'pedra'), 'empate')

    def test_tesoura_vs_papel_e_tesoura_ganha(self):
        self.assertEquals(jokenpo('tesoura', 'papel'), 'tesoura')

    def test_tesoura_vs_pedra_e_pedra_ganha(self):
        self.assertEquals(jokenpo('tesoura', 'pedra'), 'pedra')

unittest.main()
