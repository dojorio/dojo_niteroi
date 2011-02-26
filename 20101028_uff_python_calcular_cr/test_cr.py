import unittest
from problema_cr import calcula_cr

class TestCalcularCr(unittest.TestCase):
	
	def test_lucas_chorou_ao_tirar_9_5_em_info(self):
		notas_de_lucas = {
			"info" : 9.5,
		}
			
		self.assertEqual(calcula_cr(notas_de_lucas), 9.5)

	def test_lucas_chorou_ao_tirar_7_em_info(self):
		notas_de_lucas = {
			"info" : 7.0,
		}

	def test_lucas_chorou_ao_tirar_9_em_fis_exp(self):
		notas_de_lucas = {
			"fis exp" : 9.0,
		}
			
		self.assertEqual(calcula_cr(notas_de_lucas), 9.0)

	def test_lucas_chorou_ao_tirar_9_em_prog2(self):
		notas_de_lucas = {
			"prog2" : 9.0,
		}
			
		self.assertEqual(calcula_cr(notas_de_lucas), 9.0)

	def test_lucas_chorou_ao_tirar_9_em_fis_exp_e_7_em_info(self):
		notas_de_lucas = {
			"fis exp" : 9.0,
			"info" : 7.0,
		}
			
		self.assertEqual(calcula_cr(notas_de_lucas), 8.0)

	def test_lucas_chorou_ao_tirar_4_em_fis1_peso_2_e_7_em_info_peso_1(self):
	notas_de_lucas = {
			"fis1" : 4.0,
			"info" : 7.0,
		}
			
		self.assertEqual(calcula_cr(notas_de_lucas), 5.0)

unittest.main()
