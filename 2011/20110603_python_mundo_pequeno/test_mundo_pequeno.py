import unittest
from mundo_pequeno import mundo_pequeno

class TestMundoPequeno(unittest.TestCase):

    def test_mundo_pequeno_voce_5_5_e_amigos_4_4_retorna_4_4(self):
        voce = (5, 5)
        amigos = [(4,4)]
        self.assertEqual(mundo_pequeno(voce, amigos), (4,4) )
        
    def test_mundo_pequeno_voce_5_5_e_amigos_3_3_retorna_3_3(self):
        voce = (5, 5)
        amigos = [(3, 3)]
        self.assertEqual(mundo_pequeno(voce, amigos), (3, 3) )
        
    def test_mundo_pequeno_voce_5_5_e_amigos_3_3_e_4_4_retorna_4_4(self):
        voce = (5, 5)
        amigos = [(3, 3), (4, 4)]
        self.assertEqual(mundo_pequeno(voce, amigos), (4, 4) )
         
    def test_mundo_pequeno_voce_5_5_e_amigos_5_5_e_3_3_retorna_5_5(self):
        voce = (5, 5)
        amigos = [(5, 5), (3, 3)]
        self.assertEqual(mundo_pequeno(voce, amigos), (5, 5) )
        
    def test_mundo_pequeno_voce_5_5_e_amigos_5_4_e_3_3_retorna_5_4(self):
        voce = (5, 5)
        amigos = [(5, 4), (3, 3)]
        self.assertEqual(mundo_pequeno(voce, amigos), (5, 4) )
        
    def test_mundo_pequeno_voce_5_5_e_amigos_5_4_e_5_5_retorna_5_4(self):
        voce = (5, 5)
        amigos = [(5, 4), (5, 5)]
        self.assertEqual(mundo_pequeno(voce, amigos), (5, 5) )
    
        
unittest.main()
        
