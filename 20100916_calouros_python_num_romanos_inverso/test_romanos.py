import unittest

class TestRomanos(unittest.TestCase):

    def test_I_deve_retornar_1(self):
        romano = Romano('I')
        self.assertEqual(romano.to_int(), 1)

unittest.main()
