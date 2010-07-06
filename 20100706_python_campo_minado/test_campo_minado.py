import unittest
from campo_minado import resultado

class TestCampoMinado(unittest.TestCase):

    def test_2_x_2_sem_minas(self):
        entrada = [
            ['-', '-'],
            ['-', '-'],
        ]
        saida = [
            [0, 0],
            [0, 0],
        ]
        self.assertEquals(resultado(entrada), saida)

if __name__ == '__main__':
    unittest.main()
