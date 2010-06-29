import unittest
from jogo_da_velha import avalia_jogo

class TestJogoDaVelha(unittest.TestCase):

    def test_X_ganha_linha_1(self):
        entrada = [
            ('X', 'X', 'X'),
            ('0', '', ''),
            ('', '0', ''),
        ]
        self.assertEquals(avalia_jogo(entrada), 'X')

    def test_0_ganha_linha_1(self):
        entrada = [
            ('0', '0', '0'),
            ('X', '', ''),
            ('', 'X', ''),
        ]
        self.assertEquals(avalia_jogo(entrada), '0')

    def test_0_ganha_linha_2(self):
        entrada = [
            ('X', '', ''),
            ('0', '0', '0'),
            ('', 'X', ''),
        ]
        self.assertEquals(avalia_jogo(entrada), '0')
if __name__ == '__main__':
    unittest.main()
