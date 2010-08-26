# -*- coding:utf-8 -*-
import unittest

def pesa_pedras(pedras, peso_ideal):
    if not pedras:
        return 'Não é possível'
    else:
        return 1



class TestPesagemDasPedras(unittest.TestCase):

    def test_0_pedras_e_peso_ideal_1kg_retorna_nao_e_possivel(self):
        pedras = {}
        self.assertEquals(pesa_pedras(pedras, 1), 'Não é possível')

    def test_1_pedra_de_1kg_e_peso_ideal_1kg_retorna_1(self):
        pedras = {
            1: 1
        }
        self.assertEquals(pesa_pedras(pedras, 1), 1)

unittest.main()
