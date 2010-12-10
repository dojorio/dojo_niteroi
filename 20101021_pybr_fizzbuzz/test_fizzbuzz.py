import unittest
from fizzbuzz import *


class TestFizzBuzz(unittest.TestCase):
    def test_entra_1_sai_1(self):
        self.assertEqual(fizzbuzz(1), '1')

    def test_entra_2_sai_2(self):
        self.assertEqual(fizzbuzz(2), '2')

    def test_entra_multiplo3_naomultiplo5_sai_Fizz(self):
        self.assertEqual(fizzbuzz(3), DIV3)
        self.assertEqual(fizzbuzz(6), DIV3)
        self.assertEqual(fizzbuzz(9), DIV3)

    def test_entra_multiplo5_naomultiplo3_sai_Buzz(self):
        self.assertEqual(fizzbuzz(5), DIV5)
        self.assertEqual(fizzbuzz(10), DIV5)
        self.assertEqual(fizzbuzz(20), DIV5)

    def test_entra_15_sai_FizzBuzz(self):
        self.assertEqual(fizzbuzz(15), DIV3 + DIV5)

    def test_entra_30_sai_FizzBuzz(self):
        self.assertEqual(fizzbuzz(30), DIV3 + DIV5)


unittest.main()
