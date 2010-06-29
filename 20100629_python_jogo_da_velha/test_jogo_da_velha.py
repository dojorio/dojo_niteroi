import unittest
from jogo_da_velha import avalia_jogo

class TestJogoDaVelha(unittest.TestCase):

    def test_method(self):
        entrada = [
            ('X', 'X', 'X'),
            ('0', '', ''),
            ('', '0', ''),
        ]
        self.assertEquals(avalia_jogo(entrada), 'X')

if __name__ == '__main__':
    unittest.main()
