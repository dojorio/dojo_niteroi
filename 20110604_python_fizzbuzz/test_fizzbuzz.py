import unittest2
from fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest2.TestCase):

    def test_1_deve_retornar_1(self):
        resultado = fizzbuzz(1)
        esperado = 1
        self.assertEqual(resultado, esperado)

    def test_2_deve_retornar_2(self):
        resultado = fizzbuzz(2)
        esperado = 2
        self.assertEqual(resultado, esperado)

    def test_3_deve_retornar_fizz(self):
        resultado = fizzbuzz(3)
        esperado = "fizz"
        self.assertEqual(resultado, esperado)

    def test_6_deve_retornar_fizz(self):
        resultado = fizzbuzz(6)
        esperado = "fizz"
        self.assertEqual(resultado, esperado)

    def test_5_deve_retornar_buzz(self):
        resultado = fizzbuzz(5)
        esperado = "buzz"
        self.assertEqual(resultado, esperado)

    def test_10_deve_retornar_buzz(self):
        resultado = fizzbuzz(10)
        esperado = "buzz"
        self.assertEqual(resultado, esperado)

    def test_15_deve_retornar_fizzbuzz(self):
        resultado = fizzbuzz(15)
        esperado = "fizzbuzz"
        self.assertEqual(resultado, esperado)

    def test_30_deve_retornar_fizzbuzz(self):
        resultado = fizzbuzz(30)
        esperado = "fizzbuzz"
        self.assertEqual(resultado, esperado)

    def test_45_deve_retornar_fizzbuzz(self):
        resultado = fizzbuzz(45)
        esperado = "fizzbuzz"
        self.assertEqual(resultado, esperado)

unittest2.main()
