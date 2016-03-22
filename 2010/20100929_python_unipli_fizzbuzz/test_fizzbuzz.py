#-*- encoding:utf-8 -*-
from fizzbuzz import diz_fizzbuzz
import unittest

# fizz -> múltiplo de 3
# buzz -> múltiplo de 5
# fizzbuzz -> múltiplo de 3 e 5

class TestFizzBuzz(unittest.TestCase):

    def test_1_deve_retornar_1(self):
        num = 1
        self.assertEqual(diz_fizzbuzz(num), num)


    def test_2_deve_retornar_2(self):
        num = 2
        self.assertEqual(diz_fizzbuzz(num), num)

    def test_3_deve_retornar_fizz(self):
        num = 3
        self.assertEqual(diz_fizzbuzz(num), 'fizz')

    def test_4_deve_retornar_4(self):
        num = 4
        self.assertEqual(diz_fizzbuzz(num), num)

    def test_6_deve_retornar_6(self):
        num = 6
        self.assertEqual(diz_fizzbuzz(num), 'fizz')

    def test_5_deve_retornar_buzz(self):
        num = 5
        self.assertEqual(diz_fizzbuzz(num), 'buzz')

    def test_10_deve_retornar_buzz(self):
        num = 10
        self.assertEqual(diz_fizzbuzz(num), 'buzz')

    def test_15_deve_retornar_buzz(self):
        num = 15
        self.assertEqual(diz_fizzbuzz(num), 'fizzbuzz')

    def test_30_deve_retornar_buzz(self):
        num = 30
        self.assertEqual(diz_fizzbuzz(num), 'fizzbuzz')


unittest.main()
