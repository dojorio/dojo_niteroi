import unittest2
from sequencia import calcula_intervalo

class TestSequencia(unittest2.TestCase):

    def test_sequencia_1_retorna_intervalo_1(self):
        intervalo_retornado = calcula_intervalo([1])
        intervalo_esperado = [
            [1]
        ]
        self.assertEqual(intervalo_retornado, intervalo_esperado)

    def test_sequencia_2_retorna_intervalo_2(self):
        intervalo_retornado = calcula_intervalo([2])
        intervalo_esperado = [
            [2]
        ]
        self.assertEqual(intervalo_retornado, intervalo_esperado)

    def test_sequencia_1_2_retorna_intervalo_1o2(self):
        intervalo_retornado = calcula_intervalo([1, 2])
        intervalo_esperado = [
            [1, 2]
        ]
        self.assertEqual(intervalo_retornado, intervalo_esperado)

    def test_sequencia_1_3_retorna_intervalo_1_3(self):
        intervalo_retornado = calcula_intervalo([1, 3])
        intervalo_esperado = [
            [1], [3]
        ]
        self.assertEqual(intervalo_retornado, intervalo_esperado)

    def test_sequencia_1_4_retorna_intervalo_1_4(self):
        intervalo_retornado = calcula_intervalo([1, 4])
        intervalo_esperado = [
            [1], [4]
        ]
        self.assertEqual(intervalo_retornado, intervalo_esperado)

    def test_sequencia_1_2_3_retorna_intervalo_1o3(self):
        intervalo_retornado = calcula_intervalo([1, 2, 3])
        intervalo_esperado = [
            [1,3]
        ]
        self.assertEqual(intervalo_retornado, intervalo_esperado)





unittest2.main()
