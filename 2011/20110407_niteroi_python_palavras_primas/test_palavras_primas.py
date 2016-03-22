import unittest2
from palavras_primas import is_primo, valor_da_palavra


class TestNumerosPrimos(unittest2.TestCase):
        
    def test_1_eh_primo(self):
        self.assertTrue(is_primo(1))

    def test_4_nao_eh_primo(self):
        self.assertFalse(is_primo(4))
        
    def test_3_eh_primo(self):
        self.assertTrue(is_primo(3))
        
    def test_2_eh_primo(self):
        self.assertTrue(is_primo(2))    
        
    def test_5_eh_primo(self):
        self.assertTrue(is_primo(5))    
        
    def test_6_nao_eh_primo(self):
        self.assertFalse(is_primo(6))
        
    def test_8_nao_eh_primo(self):
        self.assertFalse(is_primo(8))
   
    def test_9_nao_eh_primo(self):
        self.assertFalse(is_primo(9))

    def test_15_nao_eh_primo(self):
        self.assertFalse(is_primo(15))
        
    def test_11_eh_primo(self):
        self.assertTrue(is_primo(11))
        
    def test_25_nao_eh_primo(self):
        self.assertFalse(is_primo(25))
        
    def test_49_nao_eh_primo(self):
        self.assertFalse(is_primo(49))
        
    def test_7_eh_primo(self):
        self.assertTrue(is_primo(7))
    
    def test_13_eh_primo(self):
        self.assertTrue(is_primo(13))
        
class ValorDaPalavra(unittest2.TestCase):
        
    def test_a_retorna_1(self):
        self.assertEquals(valor_da_palavra('a'), 1)
        
    def test_b_retorna_2(self):
        self.assertEquals(valor_da_palavra('b'), 2)
        
    def test_c_retorna_3(self):
        self.assertEquals(valor_da_palavra('c'), 3)
        
    def test_A_retorna_27(self):
        self.assertEquals(valor_da_palavra('A'), 27)
        
    def test_B_retorna_28(self):
        self.assertEquals(valor_da_palavra('B'), 28)
        
    def test_ab_retorna_3(self):
        self.assertEquals(valor_da_palavra('ab'), 3)
   
    def test_abc_retorna_6(self):
        self.assertEquals(valor_da_palavra('abc'), 6)
        
    def test_cervejas_retorna_primo(self):
        self.assertTrue(is_primo(valor_da_palavra("cervejas")))

unittest2.main()

