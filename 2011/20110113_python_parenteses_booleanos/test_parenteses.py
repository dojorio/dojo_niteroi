import unittest
from parenteses import conta

class TestContagem(unittest.TestCase):
	def test_true_para_contagem_de_true_retorna_1(self):
		self.assertEquals(conta("True", True), 1)

	def test_true_para_contagem_de_false_retorna_0(self):
		self.assertEquals(conta("True", False), 0)

	def test_true_and_true_para_contagem_de_true_retorna_1(self):
		self.assertEquals(conta("True and True", True), 1)

	def test_true_and_false_para_contagem_de_true_retorna_0(self):
		self.assertEquals(conta("True and False", True), 0)

	def test_true_xor_false_para_contagem_de_true_retorna_0(self):
		self.assertEquals(conta("True xor False", True), 1)

	def test_true_and_false_and_true_para_contagem_de_true_retorna_0(self):
		self.assertEquals(conta("True and False and True", True), 0)
	
	def test_true_and_false_xor_true_para_contagem_de_true_retorna_2(self):
		self.assertEquals(conta("True and False xor True", True), 2)



unittest.main()
