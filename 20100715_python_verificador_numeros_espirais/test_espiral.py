import unittest

class TestVerificaMatrizEspiral(unittest.TestCase):

    def test_matriz_1_x_1_retorna_true(self):
        matriz = [
            [1],
        ]
        self.assertTrue(verifica_matriz_espiral(matriz))
