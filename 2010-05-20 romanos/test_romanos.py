from romanos import romanos
import unittest

class testRomanos(unittest.TestCase):

    def test_entra_3_retornar_fizz(self):
        self.assertEquals(romanos('I'), 1)

if __name__ == '__main__':
    unittest.main()
