import unittest
from espiral import Matriz

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

if __name__ == '__main__':
    unittest.main()
