import unittest
from espiral import Matriz, lista_ordenada

class TestVerificaListaOrdenada(unittest.TestCase):

    def test_lista_1_esta_ordenada(self):
        self.assertTrue(lista_ordenada([1]))

    def test_lista_1_2_esta_ordenada(self):
        self.assertTrue(lista_ordenada([1,2]))

    def test_lista_1_2_3_4esta_ordenada(self):
        self.assertTrue(lista_ordenada([1,2,3,4]))

    def test_lista_1_2_4_3esta_ordenada(self):
        self.assertFalse(lista_ordenada([1,2,4,3])


class TestVerificaMatrizEspiral(unittest.TestCase):

    def test_matriz_1_x_1_retorna_true(self):
        matriz = Matriz([
            [1],
        ])
        self.assertTrue(matriz.e_matriz_espiral())

    def test_matriz_1_x_2_retorna_true(self):
        matriz = Matriz([
            [1, 2],
        ])
        self.assertTrue(matriz.e_matriz_espiral())

    def test_matriz_1_x_2_retorna_false(self):
        matriz = Matriz([
            [1, 3],
        ])
        self.assertFalse(matriz.e_matriz_espiral())

    def test_matriz_2_x_2_retorna_true(self):
        matriz = Matriz([
            [1, 2],
            [4, 3],
        ])
        self.assertTrue(matriz.e_matriz_espiral())

    def test_matriz_2_x_2_retorna_false_pela_primeira_linha(self):
        matriz = Matriz([
            [1, 5],
            [4, 3],
        ])
        self.assertFalse(matriz.e_matriz_espiral())

    def _test_matriz_2_x_2_retorna_false_pela_segunda_linha(self):
        matriz = Matriz([
            [1, 2],
            [4, 4],
        ])
        self.assertFalse(matriz.e_matriz_espiral())

if __name__ == '__main__':
    unittest.main()
