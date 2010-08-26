# -*- coding:utf-8 -*-
import unittest

def pesa_pedras(pedras, peso_ideal):
    return 'Não é possível'



class TestPesagemDasPedras(unittest.TestCase):

    def test_0_pedras_e_peso_ideal_1kg_retorna_nao_e_possivel(self):
        pedras = {}
        self.assertEquals(pesa_pedras(pedras, 1), 'Não é possível')
unittest.main()
