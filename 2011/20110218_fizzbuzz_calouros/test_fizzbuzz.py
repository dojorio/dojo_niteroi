import unittest2
from fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest2.TestCase):

    def test_numero_1_retorna_numero_1(self):
        self.assertEqual(fizzbuzz(numero=1), 1)

    def test_numero_2_retorna_numero_2(self):
        self.assertEqual(fizzbuzz(numero=2), 2)

    def test_numero_3_retorna_fizz(self):
        self.assertEqual(fizzbuzz(numero=3), 'fizz')

    def test_numero_4_retorna_numero_4(self):
        self.assertEqual(fizzbuzz(numero=4), 4)

    def test_numero_5_retorna_buzz(self):
        self.assertEqual(fizzbuzz(numero=5), "buzz")

    def test_numero_6_retorna_fizz(self):
        self.assertEqual(fizzbuzz(numero=6), "fizz")

    def test_numero_10_retorna_buzz(self):
        self.assertEqual(fizzbuzz(numero=10), 'buzz')

    def test_numero_15_retorna_fizzbuzz(self):
        self.assertEqual(fizzbuzz(numero=15),'fizzbuzz')

    def test_numero_30_retorna_fizzbuzz(self):
        self.assertEqual(fizzbuzz(numero=30),'fizzbuzz')


unittest2.main()
