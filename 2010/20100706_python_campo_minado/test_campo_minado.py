import unittest
from campo_minado import CampoMinado

class TestCampoMinado(unittest.TestCase):

    def test_constroi_campos_2_x_2(self):
        campo = CampoMinado("""
                --
                --"""
        )
        resultado = [
            [0, 0],
            [0, 0],
        ]
        self.assertEquals(campo.campo, resultado)

    def test_constroi_campos_3_x_3(self):
        campo = CampoMinado("""
                -*-
                --*
                --*"""
        )
        resultado = [
            [0, '*', 0],
            [0, 0, '*'],
            [0, 0, '*'],
        ]
        self.assertEquals(campo.campo, resultado)


    def test_2_x_2_sem_minas(self):
        campo = CampoMinado("""
               --
               --"""
        )
        saida = [
            [0, 0],
            [0, 0],
        ]

        self.assertEquals(campo.solucao(), saida)

    def test_2_x_2_1_mina_canto_superior_esquerdo(self):
        campo = CampoMinado("""
               *-
               --"""
        )
        saida = [
            ['*',1],
            [1, 1],
        ]
        self.assertEquals(campo.solucao(), saida)

    def test_2_x_2_2_minas_primeira_linha(self):
        campo = CampoMinado("""
               **
               --"""
        )
        saida = [
            ['*','*'],
            [2, 2],
        ]
        self.assertEquals(campo.solucao(), saida)

if __name__ == '__main__':
    unittest.main()
