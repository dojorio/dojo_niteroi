import unittest
from grafos import minimo_cores

class TestGrafos(unittest.TestCase):

    def test_1_vertice_1_cor(self):
        grafo = {
            0: [],
        }
        self.assertEqual(minimo_cores(grafo), 1)

    def test_2_vertices_nao_conectados_1_cor(self):
        grafo = {
            0: [],
            1: [],
        }
        self.assertEqual(minimo_cores(grafo), 1)

    def test_2_vertices_conectados_2_cores(self):
        grafo = {
            0: [1],
            1: [0],
        }
        self.assertEqual(minimo_cores(grafo), 2)

    def test_3_vertices_1_para_todos(self):
        grafo = {
            0: [1],
            1: [0, 2],
            2: [1],
        }
        self.assertEqual(minimo_cores(grafo), 2)
        
    def test_4_vertices_1_para_2_e_um_com_filho(self):
        grafo = {
            0: [2],
            1: [3],
            2: [0,3],
            3: [1,2],
        }
        self.assertEqual(minimo_cores(grafo), 2)

        def test_4_vertices_1_para_3_e_um_com_filho(self):
        grafo = {
            0: [],
            1: [],
            2: [0,3,1],
            3: [1],
        }
        self.assertEqual(minimo_cores(grafo), 2)


    #daqui pra baixo nao roda
    def _test_3_vertices_conectados_em_linha_2_cores(self):
        grafo = {
            0: [1],
            1: [0, 2],
            2: [1],
        }
        self.assertEqual(minimo_cores(grafo), 2)

    def _test_3_vertices_conectados_entre_si_3_cores(self):
        grafo = {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1],
        }
        self.assertEqual(minimo_cores(grafo), 3)

unittest.main()
        
