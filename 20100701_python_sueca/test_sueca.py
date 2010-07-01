import unittest
from sueca import Carta

class TestValoresCartas(unittest.TestCase):

    def test_A_vale_11_pontos(self):
        carta = Carta('Copas', 'A')
        self.assertEquals(carta.valor, 11)

    def test_7_vale_10_pontos(self):
        carta = Carta('Copas', '7')
        self.assertEquals(carta.valor, 10)

if __name__ == '__main__':
    unittest.main()
