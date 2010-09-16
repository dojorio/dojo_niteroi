import unittest

from romanos import NumeroRomano

class TestRomanos(unittest.TestCase):

    def test_I_deve_retornar_1(self):
        numero_romano = NumeroRomano('I')
        self.assertEqual(numero_romano.to_int(), 1)

    def test_II_deve_retornar_2(self):
        numero_romano = NumeroRomano('II')
        self.assertEqual(numero_romano.to_int(), 2)

    def test_III_deve_retornar_3(self):
        numero_romano = NumeroRomano('III')
        self.assertEqual(numero_romano.to_int(), 3)

    def test_V_deve_retornar_5(self):
        numero_romano = NumeroRomano('V')
        self.assertEqual(numero_romano.to_int(), 5)

    def test_IV_deve_retornar_4(self):
        numero_romano = NumeroRomano('IV')
        self.assertEqual(numero_romano.to_int(), 4)

    def test_VI_deve_retornar_6(self):
        numero_romano = NumeroRomano('VI')
        self.assertEqual(numero_romano.to_int(), 6)

    def test_VII_deve_retornar_7(self):
        numero_romano = NumeroRomano('VII')
        self.assertEqual(numero_romano.to_int(), 7)

    def test_VIII_deve_retornar_8(self):
        numero_romano = NumeroRomano('VIII')
        self.assertEqual(numero_romano.to_int(), 8)

    def test_X_deve_retornar_10(self):
        numero_romano = NumeroRomano('X')
        self.assertEqual(numero_romano.to_int(), 10)

    def test_IX_deve_retornar_9(self):
        numero_romano = NumeroRomano('IX')
        self.assertEqual(numero_romano.to_int(), 9)

    def test_XI_deve_retornar_11(self):
        numero_romano = NumeroRomano('XI')
        self.assertEqual(numero_romano.to_int(), 11)

    def test_XII_deve_retornar_12(self):
        numero_romano = NumeroRomano('XII')
        self.assertEqual(numero_romano.to_int(), 12)

    def test_XIII_deve_retornar_13(self):
        numero_romano = NumeroRomano('XIII')
        self.assertEqual(numero_romano.to_int(), 13)



unittest.main()
