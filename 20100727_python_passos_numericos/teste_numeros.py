# -*- coding: utf-8 -*-
import unittest
from numeros import contar_passos

class TestNumeros(unittest.TestCase):
	def test_numero_1_retorna_0(self):
		self.assertEquals(contar_passos(1), 0)
		
	def test_numero_2_retorna_1(self):
		self.assertEquals(contar_passos(2), 1)
		
	def test_numero_4_retorna_2(self):
		self.assertEquals(contar_passos(4), 2)
		
	def test_numero_8_retorna_3(self):
		self.assertEquals(contar_passos(8), 3)
		
	def test_numero_3_retorna_3(self):
		self.assertEquals(contar_passos(3), 3)
		
	def test_numero_6_retorna_4(self):
		self.assertEquals(contar_passos(6), 4)
		
	def test_numero_15_retorna_5(self):
		self.assertEquals(contar_passos(15), 5)
		
	def test_numero_1024_retorna_10(self):
		self.assertEquals(contar_passos(1024), 10)
		
	def test_numero_0_retorna_nao_e_possivel(self):
		self.assertEquals(contar_passos(0), 'não é possível')
		
	def test_numero_menos1_retorna_0(self):
		self.assertEquals(contar_passos(-1), 0)
		
	def test_numero_menos2_retorna_1(self):
		self.assertEquals(contar_passos(-2), 1)
		
	def test_numero_menos3_retorna_3(self):
		self.assertEquals(contar_passos(-3), 3)
		
	def test_numero_menos4_retorna_2(self):
		self.assertEquals(contar_passos(-4), 2)
		
	def test_numero_menos8_retorna_3(self):
		self.assertEquals(contar_passos(-8), 3)
		
	def test_numero_menos6_retorna_4(self):
		self.assertEquals(contar_passos(-6), 4)
		
	def test_numero_menos15_retorna_5(self):
		self.assertEquals(contar_passos(-15), 5)
		
	def test_numero_menos1024_retorna_10(self):
		self.assertEquals(contar_passos(-1024), 10)

unittest.main()
