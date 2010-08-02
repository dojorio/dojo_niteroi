# -*- coding: utf-8 -*-
import unittest
from criptografia import revela_criptografia

class TestNumeros(unittest.TestCase):
	
	def test_a_o_retorna_a_o(self):
		self.assertEquals(revela_criptografia('a', 'o'), [('a', 'o')])
		
	def test_a_e_retorna_a_e(self):
		self.assertEquals(revela_criptografia('a', 'e'), [('a', 'e')])
		
	def test_pa_pe_retorna_a_e(self):
		self.assertEquals(revela_criptografia('pa', 'pe'), [('a', 'e')])
		
	def test_ap_ep_retorna_a_e(self):
		self.assertEquals(revela_criptografia('ap', 'ep'), [('a', 'e')])

	def test_ap_oo_retorna_a_o_p_0(self):
		self.assertEquals(revela_criptografia('ap', 'oo'), [('a', 'o'), ('p', 'o')])

	def test_md5_5dm_retorna_a_o_p_0(self):
		self.assertEquals(revela_criptografia('md5', '5dm'), [('m', '5'), ('5', 'm')])
		
	def test_md5_dm5_retorna_a_o_p_0(self):
		self.assertEquals(revela_criptografia('md5', 'dm5'), [('m', 'd'), ('d', 'm')])

	def test_mm_mm_retorna_vazio(self):
		self.assertEquals(revela_criptografia('mm', 'mm'), [])
		
	def test_mm_aa_retorna_m_a(self):
		self.assertEquals(revela_criptografia('mm', 'aa'), [('m', 'a')])
		
	def test_mm_ao_retorna_nao_e_possivel(self):
		self.assertEquals(revela_criptografia('mm', 'ao'), 'não é possível')

	def test_mmm_aa_retorna_nao_e_possivel(self):
		self.assertEquals(revela_criptografia('mmm', 'aa'), 'não é possível')
		
	
unittest.main()