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

    def test_2_moedas_de_3_para_1_pirata(self):
        tesouro = {
            3: 2,
        }
        piratas = 1
        self.assertEqual(divide_tesouro(tesouro, piratas), 6)

    def test_1_moeda_de_3_e_1_de_5_para_1_pirata(self):
        tesouro = {
            3: 1,
            5: 1,
        }
        piratas = 1
        self.assertEqual(divide_tesouro(tesouro, piratas), 8)

    def test_2_moedas_de_3_para_2_piratas(self):
        tesouro = {
            3: 2,
        }
        piratas = 2
        self.assertEqual(divide_tesouro(tesouro, piratas), 3)

    def test_2_moedas_de_5_para_2_piratas(self):
        tesouro = {
            5: 2,
        }
        piratas = 2
        self.assertEqual(divide_tesouro(tesouro, piratas), 5)

    def test_3_moedas_de_5_para_3_piratas(self):
        tesouro = {
            5: 3,
        }
        piratas = 3
        self.assertEqual(divide_tesouro(tesouro, piratas), 5)

    def test_1_moeda_de_5_1_moeda_de_3_e_uma_moeda_de_2_para_2_piratas(self):
        tesouro = {
            5: 1,
            3: 1,
            2: 1,
        }
        piratas = 2
        self.assertEqual(divide_tesouro(tesouro, piratas), 5)

    def test_1_moeda_de_5_para_2_piratas(self):
        tesouro = {
            5: 1,
        }
        piratas = 2
        self.assertEqual(divide_tesouro(tesouro, piratas), False)

    def test_1_moeda_de_10_para_2_piratas(self):
        tesouro = {
            10: 1,
        }
        piratas = 2
        self.assertEqual(divide_tesouro(tesouro, piratas), False)

    def test_1_moeda_de_10_e_1_de_2_para_2_piratas(self):
        tesouro = {
            2: 1,
            10: 1,
        }
        piratas = 2
        self.assertEqual(divide_tesouro(tesouro, piratas), False)

    def test_3_moeda_de_10_e_2_de_1_para_2_piratas(self):
        tesouro = {
            1: 2,
            10: 3,
        }
        piratas = 2
        self.assertEqual(divide_tesouro(tesouro, piratas), False)
unittest.main()
