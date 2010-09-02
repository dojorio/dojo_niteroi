import unittest
from tecido import mede_tecido

class TestMedeTecido(unittest.TestCase):

    def test_banal(self):
        self.assertEqual(None, mede_tecido(0, 0, 0))

unittest.main()
