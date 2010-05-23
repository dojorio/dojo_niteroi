from problem import fizz_buzz
import unittest

class testFizzBuzzProblem(unittest.TestCase):

    def test_entra_3_retornar_fizz(self):
        self.assertEquals(fizz_buzz(3), 'fizz')

    def test_entra_1_retornar_1(self):
        self.assertEquals(fizz_buzz(1), 1)

    def test_entra_6_retornar_fizz(self):
        self.assertEquals(fizz_buzz(6), 'fizz')

    def test_entra_2_retornar_2(self):
        self.assertEquals(fizz_buzz(2), 2)

    def test_entra_5_retornar_buzz(self):
        self.assertEquals(fizz_buzz(5), 'buzz')

    def test_entra_15_retornar_fizzbuzz(self):
        self.assertEquals(fizz_buzz(15), 'fizzbuzz')

    def test_entra_0_retornar_fizbuzz(self):
        self.assertEquals(fizz_buzz(0), 'fizzbuzz')

if __name__ == '__main__':
    unittest.main()
