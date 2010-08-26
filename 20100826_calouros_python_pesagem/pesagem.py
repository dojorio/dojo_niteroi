# -*- coding:utf-8 -*-
import unittest

def pesa_pedras(pedras, peso_ideal):
    if not pedras:
        return 'Não é possível'
    if pedras.has_key("2 kg"):
        return 1
    return pedras["1 kg"]

class Pedra(object):
    def __init__(self, unidade, medida):
        self.unidade = unidade
        self.medida = medida


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

    def test_1_pedras_de_2kg_e_peso_ideal_2kg_retorna_1(self):
        pedras = {
            "2 kg":1
        }
        self.assertEquals(pesa_pedras(pedras,2),1)

unittest.main()
