import unittest

class TestPiratas(unittest.TestCase):

    def test_1_moeda_para_1_pirata(self):
        tesouro = {
            5: 1,
        }
        piratas = 1
        self.assertEqual(divide_tesouro(tesouro, piratas), 5)

unittest.main()
