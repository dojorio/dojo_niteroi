import unittest
from sueca import pontuacao

class TestSueca(unittest.TestCase):

    def test_foo(self):
        self.assertEquals(pontuacao(), '')

if __name__ == '__main__':
    unittest.main()
