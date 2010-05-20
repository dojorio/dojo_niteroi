import unittest
from banheiro import mija

class TesteBanheiro(unittest.TestCase):
	def teste_1_mictorio_1_homem(self):
		self.assertEqual(mija(1,1),[1])

	def teste_2_mictorios_1_homem(self):
		self.assertEqual(mija(2,1),[0,1])

	def teste_2_mictorios_2_homens(self):
		self.assertEqual(mija(2,2),[0,1])

	def teste_3_mictorios_1_homem(self):
		self.assertEqual(mija(3,1),[0,0,1])

	def teste_3_mictorios_2_homens(self):
		self.assertEqual(mija(3,2),[2,0,1])

	def teste_3_mictorios_3_homens(self):
		self.assertEqual(mija(3,3),[2,0,1])

	def teste_5_mictorios_3_homens(self):
		self.assertEqual(mija(5,3),[2,0,3,0,1])

	def teste_5_mictorios_2_homens(self):
		self.assertEqual(mija(5,2),[2,0,0,0,1])

	def teste_4_mictorios_3_homens(self):
		self.assertEqual(mija(4,3),[2,0,0,1])

	def teste_6_mictorios_3_homens(self):
		self.assertEqual(mija(6,3),[2,0,0,3,0,1])
		
	def _teste_8_mictorios_4_homens(self):
		self.assertEqual(mija(8,4),[2,0,4,0,3,0,0,1])
		
	def _teste_separa_mictorios_em_intervalos(self):
		self.assertEqual(separa([2,0,0,0,3,0,0,1]),[[2,0,0,0,3],[3,0,0,1]])

unittest.main()