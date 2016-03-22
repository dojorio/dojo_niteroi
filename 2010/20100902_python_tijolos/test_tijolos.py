# -*- coding: utf-8 -*-
import unittest
from tijolos import verifica_altura_possivel

class TestTijolos(unittest.TestCase):

	def test_1_tijolo_pequeno_esperado_1_polegada(self):
		pequenos = 1
		grandes = 0
		desejados = 1
		self.assertEquals(verifica_altura_possivel(pequenos , grandes, desejados),True)

	def test_2_tijolos_pequenos_esperado_2_polegadas(self):
		pequenos = 2
		grandes = 0
		desejados = 2
		self.assertEquals(verifica_altura_possivel(pequenos, grandes, desejados),True)	

	def test_0_tijolos_esperado_1_polegada(self):
		pequenos = 0
		grandes = 0
		desejados = 1
		self.assertEquals(verifica_altura_possivel(pequenos, grandes, desejados), False)

	def test_1_tijolo_pequeno_esperado_5_polegadas(self):
		pequenos = 1
		grandes = 0
		desejados = 5
		self.assertEquals(verifica_altura_possivel(pequenos, grandes, desejados), False)

	def test_1_tijolo_pequeno_esperado_6_polegadas(self):
		pequenos = 1
		grandes = 0
		desejados = 6
		self.assertEquals(verifica_altura_possivel(pequenos, grandes, desejados), False)

	def test_1_tijolo_grande_esperado_5_polegadas(self):
		pequenos = 0
		grandes = 1
		desejados = 5
		self.assertEquals(verifica_altura_possivel(pequenos, grandes, desejados), True)

	def test_2_tijolos_grandes_esperado_6_polegadas(self):
		pequenos = 0
		grandes = 2
		desejados = 6
		self.assertEquals(verifica_altura_possivel(pequenos, grandes, desejados), False)

	def test_2_tijolos_grandes_esperado_10_polegadas(self):
		pequenos = 0
		grandes = 2
		desejados = 10
		self.assertEquals(verifica_altura_possivel(pequenos, grandes, desejados), True)

	def test_2_tijolos_grandes_esperado_7_polegadas(self):
		pequenos = 0
		grandes = 2
		desejados = 7
		self.assertEquals(verifica_altura_possivel(pequenos, grandes, desejados), False)

	def test_3_tijolos_grandes_esperado_15_polegadas(self):
		pequenos = 0
		grandes = 3
		desejados = 15
		self.assertEquals(verifica_altura_possivel(pequenos, grandes, desejados), True)

	def test_3_tijolos_grandes_esperado_30_polegadas(self):
		pequenos = 0
		grandes = 3
		desejados = 30
		self.assertEquals(verifica_altura_possivel(pequenos, grandes, desejados), False)

	def test_1_tijolo_grande_e_1_pequeno_esperado_7_polegadas(self):
		pequenos = 1
		grandes = 1
		desejados = 7
		self.assertEquals(verifica_altura_possivel(pequenos, grandes, desejados), False)

	def test_2_tijolos_grandes_e_1_pequeno_esperado_7_polegadas(self):
		pequenos = 1
		grandes = 2
		desejados = 7
		self.assertEquals(verifica_altura_possivel(pequenos, grandes, desejados), False)

	def test_2_tijolos_grandes_e_3_pequenos_esperado_13_polegadas(self):
		pequenos = 3
		grandes = 2
		desejados = 13
		self.assertEquals(verifica_altura_possivel(pequenos, grandes, desejados), True)

if __name__ == '__main__':
    unittest.main()
