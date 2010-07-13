import unittest
from espiral import numeros_espirais

class TestEspiral(unittest.TestCase):

    def test_matriz_1_x_1(self):
        self.assertEqual(numeros_espirais(1), [[1]])

if __name__ == '__main__':
    unittest.main()
