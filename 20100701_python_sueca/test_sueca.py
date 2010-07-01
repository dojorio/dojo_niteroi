import unittest
from sueca import Carta
from sueca import somatorio

class TestSomatorioMesa(unittest.TestCase):
    def test_tudo_zero(self):
        carta1 = Carta('Copas', '2', 0)
        carta2 = Carta('Copas', '3', 0)
        carta3 = Carta('Copas', '4', 0)
        carta4 = Carta('Copas', '5', 0)
        self.assertEquals(somatorio([carta1,
                                    carta2,
                                    carta3,
                                    carta4]), 0)


if __name__ == '__main__':
    unittest.main()
