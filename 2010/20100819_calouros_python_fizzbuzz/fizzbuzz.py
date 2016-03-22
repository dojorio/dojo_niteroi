import unittest

def diz(numero):
    if numero % 3 == 0:
        return "fizz"
    else:
        return numero


class TestFizzBuzz(unittest.TestCase):

    def test_1_diz_1(self):
        self.assertEqual(diz(1), 1)

    def test_7_diz_7(self):
        self.assertEqual(diz(7), 7)

    def test_8_diz_8(self):
        self.assertEqual(diz(8), 8)

    def test_3_diz_fizz(self):
        self.assertEqual(diz(3), "fizz")

    def test_6_diz_fizz(self):
        self.assertEqual(diz(6), "fizz")


unittest.main()
