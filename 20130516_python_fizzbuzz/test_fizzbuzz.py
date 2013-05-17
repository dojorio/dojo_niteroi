import unittest
from fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):

    def test_fizzbuzz_entra_0_sai_0(self):
        self.assertEqual(fizzbuzz(0), 0)
        
    def test_fizzbuzz_entra_1_sai_1(self):
        self.assertEqual(fizzbuzz(1), 1)
        
    def test_fizzbuzz_entra_3_sai_fizz(self):
        self.assertEqual(fizzbuzz(3), 'fizz')

    def test_fizzbuzz_entra_6_sai_fizz(self):
        self.assertEqual(fizzbuzz(6), 'fizz')
        
    def test_fizzbuzz_entra_9_sai_fizz(self):
        self.assertEqual(fizzbuzz(9), 'fizz')
        
    def test_fizzbuzz_entra_5_sai_buzz(self):
        self.assertEqual(fizzbuzz(5), 'buzz')
        
    def test_fizzbuzz_entra_25_sai_buzz(self):
        self.assertEqual(fizzbuzz(25), 'buzz')
        
    def test_fizzbuzz_entra_10_sai_buzz(self):
        self.assertEqual(fizzbuzz(10), 'buzz')
        
    def test_fizzbuzz_entra_15_sai_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'fizzbuzz')
        
unittest.main()
        
