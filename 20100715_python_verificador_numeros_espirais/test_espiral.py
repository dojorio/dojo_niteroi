import unittest
from espiral import Matriz

class TestVerificaMatrizEspiral(unittest.TestCase):

    def test_matriz_1_x_1_retorna_true(self):
        matriz = [
            [1],
        ]
        teste = Matriz(matriz)
        self.assertTrue(teste.e_matriz_espiral())

    def test_matriz_1_x_2_retorna_true(self):
        matriz = [
            [1, 2],
        ]
        teste = Matriz(matriz)
        self.assertTrue(teste.e_matriz_espiral())

    def test_matriz_1_x_2_retorna_false(self):
        matriz = [
            [1, 3],
        ]
        teste = Matriz(matriz)
        self.assertTrue(teste.e_matriz_espiral())

if __name__ == '__main__':
    unittest.main()
