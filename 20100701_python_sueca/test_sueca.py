import unittest
from sueca import Carta

class TestSomatorioMesa(unittest.TestCase):
    def test_tudo_zero(self):
        carta1 = Carta('Copas', '2')
        carta2 = Carta('Copas', '3')
        carta3 = Carta('Copas', '4')
        carta4 = Carta('Copas', '5')
        self.assertEquals(somatorio(carta1, carta2, carta3, carta4), 0)


if __name__ == '__main__':
    unittest.main()
