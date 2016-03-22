import unittest
from coloracao_de_vertices import coloracao_de_vertices

class TestColoracaoDeVertices(unittest.TestCase):

    def test_matriz_um_por_um_deve_ter_1_cor(self):        
        self.assertEqual(coloracao_de_vertices(1,1), 1)

    def test_matriz_um_por_dois_deve_ter_2_cores(self):
        self.assertEqual(coloracao_de_vertices(1,2), 2)

    def test_matriz_um_por_tres_deve_ter_2_cores(self):
        self.assertEqual(coloracao_de_vertices(1,3), 2)

    def test_matriz_dois_por_um_deve_ter_2_cores(self):
        self.assertEqual(coloracao_de_vertices(2,1),2)

    def test_matriz_tres_por_um_deve_ter_2_cores(self):
        self.assertEqual(coloracao_de_vertices(3,1),2)

    def test_matriz_dois_por_dois_deve_ter_4_cores(self):
        self.assertEqual(coloracao_de_vertices(2,2),4)

    def test_matriz_dois_por_tres_deve_ter_4_cores(self):
        self.assertEqual(coloracao_de_vertices(2,3), 4)

    def test_matriz_tres_por_dois_deve_ter_4_cores(self):
        self.assertEqual(coloracao_de_vertices(3,2), 4)

    def test_matriz_tres_por_tres_deve_ter_4_cores(self):
        self.assertEqual(coloracao_de_vertices(3,3), 4)
        


unittest.main()
        
