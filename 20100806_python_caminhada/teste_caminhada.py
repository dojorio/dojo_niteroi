from caminhada import calcula_caminho
import unittest

class testProblem(unittest.TestCase):

    def test_matriz_1_elem_retorna_lista_0(self):
        entrada = [
            [3]
        ]
        self.assertEquals(calcula_caminho(entrada), [0])

    def test_matriz_2_x_2_retorna_lista_0_0(self):
        entrada = [
            [1, 3],
            [2, 4],
        ]
        self.assertEquals(calcula_caminho(entrada), [0, 0])

    def test_matriz_2_x_2_retorna_lista_0_1(self):
        entrada = [
            [1, 3],
            [4, 2],
        ]
        self.assertEquals(calcula_caminho(entrada), [0, 1])

    def test_matriz_3_x_3_retorna_lista_0_0_0(self):
        entrada = [
            [1, 3, 4],
            [2, 3, 5],
            [3, 6, 7],
        ]
        self.assertEquals(calcula_caminho(entrada), [0, 0, 0])

    def test_matriz_3_x_3_retorna_lista_0_0_1(self):
        entrada = [
            [1, 3, 4],
            [2, 3, 5],
            [6, 3, 7],
        ]
        self.assertEquals(calcula_caminho(entrada), [0, 0, 1])

    def test_matriz_3_x_3_retorna_lista_0_1_2(self):
        entrada = [
            [1, 3, 4],
            [3, 2, 5],
            [6, 7, 3],
        ]
        self.assertEquals(calcula_caminho(entrada), [0, 1, 2])

    def test_matriz_3_x_3_retorna_lista_1_2(self):
        entrada = [
            [3, 1, 4],
            [3, 5, 2],
            [6, 7, 3],
        ]
        self.assertEquals(calcula_caminho(entrada), [1, 2])

    def test_matriz_3_x_3_retorna_lista_0_0_1(self):
        entrada = [
            [1, 3, 4],
            [3, 4, 2],
            [6, 3, 7],
        ]
        self.assertEquals(calcula_caminho(entrada), [0, 0, 1])

unittest.main()
