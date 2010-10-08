import unittest2
from maquina import Maquina
from maquina import REFRI_1, REFRI_2

class TestMaquinaDeRefri(unittest2.TestCase):
    def setUp(self):
        self.maquina = Maquina()

    def test_5_centavos_e_pega_o_dinheiro_de_volta(self):
        moedas = [0.05]
        self.maquina.insere_moedas(moedas)
        self.assertEqual(self.maquina.cancela(), moedas)

    def test_5_e_25_centavos_e_pega_o_dinheiro_de_volta(self):
        moedas = [0.05, 0.25]
        self.maquina.insere_moedas(moedas)
        self.assertEqual(self.maquina.cancela(), moedas)

    def test_5_e_25_e_10_centavos_e_1_real_e_pega_o_dinheiro_de_volta(self):
        moedas = [0.05, 0.10, 0.25, 1.00]
        self.maquina.insere_moedas(moedas)
        self.assertEqual(self.maquina.cancela(), moedas)

    def test_nao_consegue_comprar_refri_1_com_10_centavos(self):
        moedas = [0.10]
        self.maquina.insere_moedas(moedas)
        self.assertEqual(self.maquina.comprar_refri_1(), moedas)

    def test_consegue_comprar_refri_1_sem_troco(self):
        moedas = [0.25, 0.25, 0.10, 0.05]
        self.maquina.insere_moedas(moedas)
        self.assertEqual(self.maquina.comprar_refri_1(), REFRI_1)

    def test_nao_consegue_comprar_refri_1_com_10_e_10_centavos(self):
        moedas = [0.10, 0.10]
        self.maquina.insere_moedas(moedas)
        self.assertEqual(self.maquina.comprar_refri_1(), moedas)

    def test_nao_consegue_comprar_refri_2_com_10_centavos(self):
        moedas = [0.10]
        self.maquina.insere_moedas(moedas)
        self.assertEqual(self.maquina.comprar_refri_2(), moedas)

    def test_nao_consegue_comprar_refri_2_com_10_e_10_centavos(self):
        moedas = [0.10, 0.10]
        self.maquina.insere_moedas(moedas)
        self.assertEqual(self.maquina.comprar_refri_2(), moedas)

    def test_consegue_comprar_refri_2_com_1_real(self):
        moedas = [1.00]
        self.maquina.insere_moedas(moedas)
        self.assertEqual(self.maquina.comprar_refri_2(), REFRI_2)

    def test_consegue_comprar_refri_2_com_2_de_1_real(self):
        moedas = [1.00, 1.00]
        self.maquina.insere_moedas(moedas)
        self.assertEqual(self.maquina.comprar_refri_2(), [REFRI_2, 1.00])

    def test_consegue_comprar_refri_2_com_2_de_1_real_e_1_de_10_centavos(self):
        moedas = [1.00, 1.00, 0.10]
        self.maquina.insere_moedas(moedas)
        self.assertEqual(self.maquina.comprar_refri_2(), [REFRI_2, 1.00, 0.10])

if __name__ == '__main__':
    unittest2.main()
