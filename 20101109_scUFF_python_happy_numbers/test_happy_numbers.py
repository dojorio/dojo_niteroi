import unittest
from happy_numbers import happy

class TestHappyNumbers(unittest.TestCase):
    
    def test_numero_1_eh_feliz(self):
        self.assertEqual(happy(1), "feliz")
        
    def test_numero_2_eh_triste(self):
        self.assertEqual(happy(2), "triste")
        
    def test_numero_4_eh_triste(self):
        self.assertEqual(happy(4), "triste")
        
    def test_numero_10_eh_feliz(self):
        self.assertEqual(happy(10), "feliz")    
        
    def test_numero_7_eh_feliz(self):
        self.assertEqual(happy(7), "feliz")    
        
    def test_numero_5_eh_triste(self):
        self.assertEqual(happy(5), "triste")     
        
    def test_numero_16_eh_triste(self):
        self.assertEqual(happy(16), "triste")

    def test_numero_6_eh_triste(self):
        self.assertEqual(happy(6), "triste")
     
    def test_numero_100_eh_feliz(self):
        self.assertEqual(happy(100), "feliz")
        
    def test_numero_1000_eh_feliz(self):
        self.assertEqual(happy(1000), "feliz")
        
    def test_numero_101_eh_triste(self):
        self.assertEqual(happy(101), "triste")
        
    def test_numero_293_eh_feliz(self):
        self.assertEqual(happy(293), "feliz")
        
    def test_numero_1024_eh_triste(self):
        self.assertEqual(happy(1024), "triste")
        

unittest.main()
