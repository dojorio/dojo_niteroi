import unittest
from assassino import assassino

class test_assassino(unittest.TestCase):
    
    def test_uma_pessoa_pessoa_um_fica_viva_passo_1(self):
        self.assertEqual(assassino(1, 1), 1)
    
    def test_duas_pessoas_pessoa_dois_fica_viva_passo_1(self):
        self.assertEqual(assassino(2, 1), 2)
        
    def test_nenhuma_pessoa_fica_viva_com_0_pessoas(self):
        self.assertEqual(assassino(0, 1), 0)
        
    def test_tres_pessoas_pessoa_dois_fica_viva_passo_1(self):
        self.assertEqual(assassino(3, 1), 2)
        
    def test_tres_pessoas_pessoa_tres_fica_viva_passo_2(self):
        self.assertEqual(assassino(3, 2), 3)
        
    def test_quatro_pessoas_pessoa_tres_fica_viva_passo_2(self):
        self.assertEqual(assassino(4, 2), 3)
        
    def test_quatro_pessoas_pessoa_tres_fica_viva_passo_3(self):
        self.assertEqual(assassino(4, 3), 3)
        
    def test_cinco_pessoas_pessoa_dois_fica_viva_passo_1(self):
        self.assertEqual(assassino(5, 1), 2)
    
 
    
        
unittest.main()
    

