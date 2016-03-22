import unittest
from espiral import numeros_espirais

class TestEspiral(unittest.TestCase):

    def test_matriz_1_x_1(self):
        self.assertEqual(numeros_espirais(1), [[1]])

    def test_matriz_2_x_2(self):
        self.assertEqual(numeros_espirais(2), [
            [1, 2],
            [4, 3]
        ])

    def test_matriz_3_x_3(self):
        self.assertEqual(numeros_espirais(3), [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5],
        ])

if __name__ == '__main__':
    unittest.main()
