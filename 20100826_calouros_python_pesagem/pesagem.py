# -*- coding:utf-8 -*-
import unittest

def pesa_pedras(pedras, peso_ideal):
    if not pedras:
        return 'Não é possível'
    return pedras["1 kg"]



class TestPesagemDasPedras(unittest.TestCase):

    def test_0_pedras_e_peso_ideal_1kg_retorna_nao_e_possivel(self):
        pedras = {}
        self.assertEquals(pesa_pedras(pedras, 1), 'Não é possível')

    def test_1_pedra_de_1kg_e_peso_ideal_1kg_retorna_1(self):
        pedras = {
            "1 kg" : 1
        }
        self.assertEquals(pesa_pedras(pedras, 1), 1)

    def test_2_pedras_de_1kg_e_peso_ideal_2kg_retorna_2(self):
        pedras = {
            "1 kg":2
        }
        self.assertEquals(pesa_pedras(pedras, 2), 2)

unittest.main()
