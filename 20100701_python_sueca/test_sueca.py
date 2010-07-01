import unittest
from sueca import Carta
from sueca import somatorio

class TestSomatorioMesa(unittest.TestCase):
    def test_tudo_zero(self):
        cartas = [
            Carta('Copas', '2'),
            Carta('Copas', '3'),
            Carta('Copas', '4'),
            Carta('Copas', '5')]
        self.assertEquals(somatorio(cartas), 0)

    def test_tudo_zero(self):
        cartas = [
            Carta('Copas', 'A'),
            Carta('Copas', '3'),
            Carta('Copas', '4'),
            Carta('Copas', '5')]
        self.assertEquals(somatorio(cartas), 11)

if __name__ == '__main__':
    unittest.main()
