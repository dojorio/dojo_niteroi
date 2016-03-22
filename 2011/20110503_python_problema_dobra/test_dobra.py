import unittest2
from dobra import dobra

class TestDobra(unittest2.TestCase):

    def test_lista_de_tamanho_dois(self):
        self.assertDobra(
            lista=[2, 3],
            esperado=[2, 3]
        )

    def test_lista_de_tamanho_quatro(self):
        self.assertDobra(
            lista=[2, 3, 5, 2],
            esperado=[4, 8]
        )

    def test_lista_de_tamanho_oito(self):
        self.assertDobra(
            lista=[3, 1, 2, 1, 2, 2, 3, 1],
            esperado=[7, 8]
        )

    def test_lista_de_tamanho_tres(self):
        self.assertDobra(
            lista=[1, 3, 3],
            esperado=[1, 6]
        )

    def test_nao_deixa_valores_maior_que_10(self):
        self.assertDobra(
            lista=[3, 7, 9, 4, 6, 8],
            esperado=[1, 6]
        )

    def assertDobra(self, lista, esperado):
        resultado = dobra(lista)
        self.assertEqual(resultado, esperado)

unittest2.main()
