#coding: utf-8
import unittest 
from cinema import bilheteria

class teste(unittest.TestCase):

    def test_um_ingresso_normal_retorna_11_reais(self):
	    self.assertEquals(11.0, bilheteria({'Normal':1}))

    def test_um_ingresso_estudante_retorna_8_reais(self):
	    self.assertEquals(8.0, bilheteria({'Estudante':1}))

    def test_um_ingresso_idoso_retorna_6_reais(self):
	    self.assertEquals(6.0, bilheteria({'Idoso':1}))

    def test_um_ingresso_crianca_retorna_5_reais_50_centavos(self):
        self.assertEquals(5.50, bilheteria({'Criança':1}))

    def test_cinco_ingressos_normais_retorna_55_reais(self):
	    self.assertEquals(55.0, bilheteria({'Normal':5}))

    def test_5_normais_2_criancas_retorna_66_reais(self):
	    self.assertEquals(66.0, bilheteria({'Normal':5,'Criança':2}))

    def test_20_ingressos_retorna_120_reais(self):
	    self.assertEquals(120.0, bilheteria({'Normal':5,'Criança':5,'Idoso':10}))

    def test_1_normal_3D_retorna_14_reais(self):
	    self.assertEquals(14.0, bilheteria({'Normal':1},['3D']))

if __name__ == '__main__':
	unittest.main()
