import unittest
from campo_minado import campo_minado, B, V

class TestCampoMinado(unittest.TestCase):

    def test_campo_minado_B_retorna_B(self):
        self.assertEqual(campo_minado([[B]]), [[B]])
        
    def test_campo_minado_V_retorna_V(self):
        self.assertEqual(campo_minado([[V]]), [[V]])
        
    def test_campo_minado_BV_retorna_B1(self):
        self.assertEqual(campo_minado([[B, V]]), [[B, 1]])
        
    def test_campo_minado_BB_retorna_BB(self):
        self.assertEqual(campo_minado([[B, B]]), [[B, B]])
      
    def test_campo_minado_VB_retorna_1B(self):
        self.assertEqual(campo_minado([[V, B]]), [[1, B]])
        
    def test_campo_minado_VBV_retorna_1B1(self):
        self.assertEqual(campo_minado([[V, B, V]]), [[1, B, 1]])
            
    def test_campo_minado_BVV_retorna_B1V(self):
        self.assertEqual(campo_minado([[B, V, V]]), [[B, 1, V]])
            
    def test_campo_minado_B_V_retorna_B_1(self):
        campo = [
            [B],
            [V],
        ]
        esperado = [
            [B],
            [1],
        ]
        self.assertEqual(campo_minado(campo), esperado)
        
                
    def test_campo_minado_V_B_retorna_1_B(self):
        campo = [
            [V],
            [B],
        ]
        esperado = [
            [1],
            [B],
        ]
        self.assertEqual(campo_minado(campo), esperado)
        
    def test_campo_minado_BVB_VBV_VVB_retorna_B3B_2B3_12B(self):
        campo = [
            [B,V,B],
            [V,B,V],
            [V,V,B]
        ]
        esperado = [
            [B,3,B],
            [2,B,3],
            [1,2,B]
        ]
        self.assertEqual(campo_minado(campo), esperado)
        
    def test_campo_minado_VBVB_VVBV_VVVB_retorna_1B3B_12B3_V12B(self):
        campo = [
            [V,B,V,B],
            [V,V,B,V],
            [V,V,V,B]
        ]
        esperado = [
            [1,B,3,B],
            [1,2,B,3],
            [V,1,2,B]
        ]
        self.assertEqual(campo_minado(campo), esperado)
            
    
    
    

unittest.main()
        
