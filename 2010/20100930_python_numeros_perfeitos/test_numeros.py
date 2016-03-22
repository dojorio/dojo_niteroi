# -*- encoding:utf-8 -*-
import unittest
from numeros import perfeito
from numeros import seus_divisores

class TestNumeroPerfeito(unittest.TestCase):

    def test_2_nao_eh_perfeito(self):
        self.assertFalse(perfeito(2))

    def test_6_eh_perfeito(self):
        self.assertTrue(perfeito(6))

    def test_28_eh_perfeito(self):
        self.assertTrue(perfeito(28))

    def test_496_eh_perfeito(self):
        self.assertTrue(perfeito(496))

class TestSeusDivisores(unittest.TestCase):
    def test_divisores_de_2_retorna_1(self):
        self.assertEqual(seus_divisores(2),[1])

    def test_divisores_de_4_retorna_1_2(self):
        self.assertEqual(seus_divisores(4),[1, 2])


    def test_divisores_de_6_retorna_1_2_3(self):
        self.assertEqual(seus_divisores(6),[1, 2, 3])

    def test_divisores_de_5_retorna_1(self):
        self.assertEqual(seus_divisores(5), [1])

    def test_divisores_de_1_retorna_1(self):
        self.assertEqual(seus_divisores(1), [])

class TestNumerosGeneralizados(unittest.TestCase):

    def test_nao_perfeitos(self):
        numeros = range(1, 10000)
        perfeitos = [6, 28, 496, 8128]
        for numero in perfeitos:
            numeros.remove(numero)
        for numero in numeros:
            self.assertFalse(perfeito(numero))

    def test_perfeitos(self):
        perfeitos = [6, 28, 496, 8128, 33550336]
        for numero in perfeitos:
            self.assertTrue(perfeito(numero))


unittest.main()
