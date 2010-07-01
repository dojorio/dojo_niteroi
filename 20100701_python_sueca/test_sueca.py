import unittest
from sueca import Carta
from sueca import somatorio

class TestSomatorioMesa(unittest.TestCase):
    def test_tudo_zero(self):
        cartas = [
            Carta('Copas', '2', 0),
            Carta('Copas', '3', 0),
            Carta('Copas', '4', 0),
            Carta('Copas', '5', 0)]
        self.assertEquals(somatorio(cartas), 0)


if __name__ == '__main__':
    unittest.main()
