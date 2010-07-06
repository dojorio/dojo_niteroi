import unittest
from campo_minado import resultado
from campo_minado import CampoMinado

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
        entrada = CampoMinado([
            ['-', '-'],
            ['-', '-'],
        ])
        saida = CampoMinado([
            [0, 0],
            [0, 0],
        ])

        self.assertEquals(resultado(entrada), saida)

    def test_2_x_2_1_mina_canto_superior_esquerdo(self):
        entrada = [
            ['*', '-'],
            ['-', '-'],
        ]
        saida = [
            ['*',1],
            [1, 1],
        ]
        self.assertEquals(resultado(entrada), saida)

if __name__ == '__main__':
    unittest.main()
