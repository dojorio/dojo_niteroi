import unittest2 as unittest
from polinomio import Polinomio

class TestPolinomio(unittest.TestCase):

    def test_0_dividido_por_1_retorna_0_resto_0(self):
        dividendo = Polinomio([0])
        divisor = Polinomio([1])
        quociente = Polinomio([0])
        resto = Polinomio([0])

        dividendo.dividir_por(divisor)

        self.assertEqual(dividendo.quociente, quociente)
        self.assertEqual(dividendo.resto, resto)

    def test_1_dividido_por_1_retorna_1_resto_0(self):
        dividendo = Polinomio([1])
        divisor = Polinomio([1])
        quociente = Polinomio([1])
        resto = Polinomio([0])

        dividendo.dividir_por(divisor)

        self.assertEqual(dividendo.quociente, quociente)
        self.assertEqual(dividendo.resto, resto)

    def test_3_dividido_por_2_retorna_1_resto_1(self):
        dividendo = Polinomio([3])
        divisor = Polinomio([2])
        quociente = Polinomio([1])
        resto = Polinomio([1])

        dividendo.dividir_por(divisor)

        self.assertEqual(dividendo.quociente, quociente)
        self.assertEqual(dividendo.resto, resto)

    def test_3_dividido_por_2_retorna_1_resto_1(self):
        dividendo = Polinomio([0, 1])
        divisor = Polinomio([0, 1])
        quociente = Polinomio([1])
        resto = Polinomio([0])

        dividendo.dividir_por(divisor)

        self.assertEqual(dividendo.quociente, quociente)
        self.assertEqual(dividendo.resto, resto)




unittest.main()
