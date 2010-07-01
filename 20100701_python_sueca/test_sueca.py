import unittest
from sueca import Carta

class TestValoresCartas(unittest.TestCase):

    def test_A_vale_11_pontos(self):
        carta = Carta('Copas', 'A')
        self.assertEquals(carta.valor, 11)


if __name__ == '__main__':
    unittest.main()
