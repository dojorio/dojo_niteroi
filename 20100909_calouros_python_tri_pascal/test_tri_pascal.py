import unittest
from tri_pascal import combinacao
from tri_pascal import triangulo_pascal

class TestTrianguloPascal(unittest.TestCase):

    def test_triangulo_1_linha(self):
        self.assertEqual(triangulo_pascal(1), [
            [1],
        ])

    def test_triangulo_2_linhas(self):
        self.assertEqual(triangulo_pascal(2), [
            [1],
            [1, 1],
        ])

    def test_triangulo_3_linhas(self):
        self.assertEqual(triangulo_pascal(3), [
            [1],
            [1, 1],
            [1, 2, 1],
        ])

    def test_triangulo_4_linhas(self):
        self.assertEqual(triangulo_pascal(4), [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
        ])

class TestCombinacao(unittest.TestCase):

    def test_combinacao_1_a_1(self):
        self.assertEqual(combinacao(1, 1), 1)

    def test_combinacao_1_a_1b(self):
        self.assertEqual(combinacao(2, 1), 2)

unittest.main()
