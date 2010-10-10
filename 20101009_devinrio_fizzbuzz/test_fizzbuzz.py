import unittest
from fizzbuzz import brincadeira

class TestFizzBuzz(unittest.TestCase):

    def test_entra_1_retorna_1(self):
        self.assertEqual('1', brincadeira(1))

    def test_entra_2_retorna_2(self):
        self.assertEqual('2', brincadeira(2))

    def test_entra_3_retorna_fizz(self):
        self.assertEqual('fizz', brincadeira(3))

    def test_entra_6_retorna_fizz(self):
        self.assertEqual('fizz', brincadeira(6))

    def test_entra_5_retorna_buzz(self):
        self.assertEqual('buzz', brincadeira(5))

    def test_entra_10_retorna_buzz(self):
        self.assertEqual('buzz', brincadeira(10))

    def test_entra_15_retorna_fizzbuzz(self):
        self.assertEqual('fizzbuzz', brincadeira(15))

    def test_entra_30_retorna_fizzbuzz(self):
        self.assertEqual('fizzbuzz', brincadeira(30))


unittest.main()
