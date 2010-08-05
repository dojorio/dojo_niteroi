import unittest
from piratas import divide_tesouro

class TestPiratas(unittest.TestCase):

    def test_1_moeda_de_5_para_1_pirata(self):
        tesouro = {
            5: 1,
        }
        piratas = 1
        self.assertEqual(divide_tesouro(tesouro, piratas), 5)

    def test_1_moeda_de_3_para_1_pirata(self):
        tesouro = {
            3: 1,
        }
        piratas = 1
        self.assertEqual(divide_tesouro(tesouro, piratas), 3)

    def test_2_moeda_de_3_para_1_pirata(self):
        tesouro = {
            3: 2,
        }
        piratas = 1
        self.assertEqual(divide_tesouro(tesouro, piratas), 6)

unittest.main()