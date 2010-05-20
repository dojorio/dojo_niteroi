from problem import soma
import unittest

class testProblem(unittest.TestCase):
	
	def test_function_loading(self):
		self.assertEqual(soma(1,1), 2)

	def test_assertion_fail(self):
		self.assertEqual(soma(1,1), 3)


unittest.main()