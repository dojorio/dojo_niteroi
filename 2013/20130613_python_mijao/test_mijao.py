import unittest
from mijao import quem_vai_mijar

class TestMijao(unittest.TestCase):

    def test_mijao_0_mictorios_0(self):
        mijoes = 0
        mictorios = 0
        retorno = [0]
        self.assertEqual(quem_vai_mijar(mijoes, mictorios), retorno)

    def test_mijao_1_mictorios_0(self):
        mijoes = 1
        mictorios = 0
        retorno = [1]
        self.assertEqual(quem_vai_mijar(mijoes, mictorios), retorno)
        
    def test_mijao_1_mictorios_1(self):
        mijoes = 1
        mictorios = 1
        retorno = [0, 1]
        self.assertEqual(quem_vai_mijar(mijoes, mictorios), retorno)
        
    def test_mijao_2_mictorios_1(self):
        mijoes = 2
        mictorios = 1
        retorno = [1, 1]
        self.assertEqual(quem_vai_mijar(mijoes, mictorios), retorno)
        
    def test_mijao_1_mictorios_2(self):
        mijoes = 1
        mictorios = 2
        retorno = [0, 2]
        self.assertEqual(quem_vai_mijar(mijoes, mictorios), retorno)

    def test_mijao_2_mictorios_2(self):
        mijoes = 2
        mictorios = 2
        retorno = [1, 2]
        self.assertEqual(quem_vai_mijar(mijoes, mictorios), retorno)
        
    def test_mijao_2_mictorios_3(self):
        mijoes = 2
        mictorios = 3
        retorno = [0, 1, 3]
        self.assertEqual(quem_vai_mijar(mijoes, mictorios), retorno)

    def test_mijao_3_mictorios_3(self):
        mijoes = 3
        mictorios = 3
        retorno = [1, 1, 3]
        self.assertEqual(quem_vai_mijar(mijoes, mictorios), retorno)

unittest.main()
