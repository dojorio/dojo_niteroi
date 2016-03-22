import unittest
from collatz import collatz

class TestCollatz(unittest.TestCase):

    def test_1_retorna_1(self):
        self.assertEqual(collatz(1), [1])
    
    def test_2_retorna_2_1(self):
        self.assertEqual(collatz(2), [2, 1])

    def test_4_retorna_4_2_1(self):
        self.assertEqual(collatz(4), [4, 2, 1])
    
    def test_5_retorna_5_16_8_4_2_1(self):
        self.assertEqual(collatz(5), [5, 16, 8, 4, 2, 1])

    def test_3_retorna_3_10_5_16_8_4_2_1(self):
        self.assertEqual(collatz(3), [3, 10, 5, 16, 8, 4, 2, 1])

    def test_13_retorna_13_40_20_10_5_16_8_4_2_1(self):
        self.assertEqual(collatz(13), [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

unittest.main()
        
