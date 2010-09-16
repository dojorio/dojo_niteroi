import unittest

from romanos import NumeroRomano

class TestRomanos(unittest.TestCase):

    def test_I_deve_retornar_1(self):
        numero_romano = NumeroRomano('I')
        self.assertEqual(numero_romano.to_int(), 1)

    def test_II_deve_retornar_2(self):
        numero_romano = NumeroRomano('II')
        self.assertEqual(numero_romano.to_int(), 2)

unittest.main()
