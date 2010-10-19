#coding: utf-8
import unittest2
from cinema import calcula_preco
from cinema import Filme

class TestCinema(unittest2.TestCase):

    def setUp(self):
        self.filme = Filme()

    def test_compra_1_ingresso_normal_retorna_11_reais(self):
        ingressos = {'normal': 1}
        self.assertEqual(calcula_preco(ingressos, self.filme), 11)

    def test_compra_2_ingressos_normais_retorna_22_reais(self):
        ingressos = {'normal': 2}
        self.assertEqual(calcula_preco(ingressos, self.filme), 22)

    def test_compra_1_ingresso_estudante_retorna_8_reais(self):
        ingressos = {'estudante': 1}
        self.assertEqual(calcula_preco(ingressos, self.filme), 8)

    def test_compra_2_ingressos_estudante_retorna_16_reais(self):
        ingressos = {'estudante': 2}
        self.assertEqual(calcula_preco(ingressos, self.filme), 16)

    def test_compra_3_ingressos_idoso_retorna_18_reais(self):
        ingressos = {'idoso':3}
        self.assertEqual(calcula_preco(ingressos, self.filme), 18)

    def test_compra_1_normal_e_1_estudante_retorna_19_reais(self):
        ingressos = {'normal': 1, 'estudante': 1}
        self.assertEqual(calcula_preco(ingressos, self.filme), 19)

    def test_compra_1_normal_e_1_crianca_retorna_16_50_reais(self):
        ingressos = {'normal' : 1, u'criança' : 1 }
        self.assertEqual(calcula_preco(ingressos, self.filme), 16.5)

    def test_compra_1_crianca_retorna_5_50_reais(self):
        ingressos = {u'criança': 1}
        self.assertEqual(calcula_preco(ingressos, self.filme), 5.5)

    def test_compra_10_criancas_10_normais_1_idoso_retorna_126_reais(self):
        ingressos = {u'criança': 10, 'normal': 10, 'idoso': 1}
        self.assertEqual(calcula_preco(ingressos, self.filme), 126)

    def test_compra_22_normais_retorna_132_reais(self):
        ingressos = {'normal': 22}
        self.assertEqual(calcula_preco(ingressos, self.filme), 132)

    def test_compra_1_normal_filme_3d_retorna_14_reais(self):
        ingressos = {'normal': 1}
        self.filme.tres_d = True
        self.assertEqual(calcula_preco(ingressos, self.filme), 14)

    def test_2_normais_filme_3d_retorna_28_reais(self):
        ingressos = {'normal': 2}
        self.filme.tres_d = True
        self.assertEqual(calcula_preco(ingressos, self.filme), 28)

    def test_21_normais_filme_3d_retorna_189_reais(self):
        ingressos = {'normal': 21}
        self.filme.tres_d = True
        self.assertEqual(calcula_preco(ingressos, self.filme), 189)

    def teste_1_normal_filme_mais_de_120_min_retorna_12_5_reais(self):
        ingressos = {'normal': 1}
        self.filme.mais_de_120_min = True
        self.assertEqual(calcula_preco(ingressos, self.filme), 12.5)


unittest2.main()
