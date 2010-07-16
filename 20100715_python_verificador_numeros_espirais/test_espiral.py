import unittest
from espiral import Matriz, lista_ordenada_sequencialmente

class TestVerificaListaOrdenada(unittest.TestCase):

    def test_lista_1_esta_ordenada(self):
        self.assertTrue(lista_ordenada_sequencialmente([1]))

    def test_lista_1_2_esta_ordenada(self):
        self.assertTrue(lista_ordenada_sequencialmente([1,2]))

    def test_lista_1_2_3_4_esta_ordenada(self):
        self.assertTrue(lista_ordenada_sequencialmente([1,2,3,4]))

    def test_lista_1_2_4_3_nao_esta_ordenada(self):
        self.assertFalse(lista_ordenada_sequencialmente([1,2,4,3]))

    def test_lista_1_2_3_4_nao_esta_ordenada_reversamente(self):
        self.assertFalse(lista_ordenada_sequencialmente([1,2,3,4], reverso=True))

    def test_lista_4_3_2_1_esta_ordenada_reversamente(self):
        self.assertTrue(lista_ordenada_sequencialmente([4,3,2,1], reverso=True))

    def test_lista_3_4_2_1_nao_esta_ordenada_reversamente(self):
        self.assertFalse(lista_ordenada_sequencialmente([3,4,2,1], reverso=True))

    def test_lista_1_3_nao_esta_sequecialmente_ordenada(self):
        self.assertFalse(lista_ordenada_sequencialmente([1,3]))

    def test_lista_4_3_esta_sequecialmente_ordenada_reversamente(self):
        self.assertTrue(lista_ordenada_sequencialmente([4,3], reverso=True))


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

    def test_matriz_2_x_2_retorna_false_pela_segunda_linha(self):
        matriz = Matriz([
            [1, 2],
            [4, 4],
        ])
        self.assertFalse(matriz.e_matriz_espiral())

if __name__ == '__main__':
    unittest.main()
