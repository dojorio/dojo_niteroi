import unittest
from espiral import verifica_matriz_espiral

class TestVerificaMatrizEspiral(unittest.TestCase):

    def test_matriz_1_x_1_retorna_true(self):
        matriz = [
            [1],
        ]
        self.assertTrue(verifica_matriz_espiral(matriz))

    def test_matriz_1_x_2_retorna_true(self):
        matriz = [
            [1, 2],
        ]
        self.assertTrue(verifica_matriz_espiral(matriz))

    def test_matriz_1_x_2_retorna_false(self):
        matriz = [
            [1, 3],
        ]
        self.assertFalse(verifica_matriz_espiral(matriz))

if __name__ == '__main__':
    unittest.main()
