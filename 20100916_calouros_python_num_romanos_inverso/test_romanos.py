import unittest

from romanos import NumeroRomano

class TestRomanos(unittest.TestCase):

    def test_I_deve_retornar_1(self):
        romano = NumeroRomano('I')
        self.assertEqual(romano.to_int(), 1)

unittest.main()
