import unittest2 as unittest
from caixa_eletronico import conta_notas

class TestCaixaEletronico(unittest.TestCase):

    def test_100_reais_retorna_1_nota_100_reais(self):
        self.assertEqual(conta_notas(100), {"R$ 100": 1})

    def test_200_reais_retorna_2_notas_100_reais(self):
        self.assertEqual(conta_notas(200), {"R$ 100": 2})

    def test_300_reais_retorna_3_notas_100_reais(self):
        self.assertEqual(conta_notas(300), {"R$ 100": 3})
    
    def test_50_reais_retorna_1_nota_50_reais(self):
        self.assertEqual(conta_notas(5), {"R$ 50": 1})

    def test_20_reais_retorna_1_nota_20_reais(self):
        self.assertEqual(conta_notas(20), {"R$ 20": 1})

    def test_40_reais_retorna_2_nota_20_reais(self):
        self.assertEqual(conta_notas(40), {"R$ 20": 2})

    def test_150_reais_retorna_1_nota_100_e_1_nota_50(self):
        self.assertEqual(conta_notas(150), {"R$ 100":1, "R$ 50":1})

    def test_90_reais_retorna_1_nota_50_e_2_nota_20(self):
        self.assertEqual(conta_notas(90), {"R$ 50" :1, "R$ 20":2})

unittest.main()
        
