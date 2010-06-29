import unittest
from olimpiadas import calcula_ranking, Pais

class TestOlimpiadas(unittest.TestCase):

    def setUp(self):
        self.brasil = Pais("Brasil", 1, 0, 0)
        self.eua = Pais("EUA", 0, 0, 0)
        self.cuba = Pais("Cuba", 2, 0, 0)

    def test_1_pais_retorna_mesmo_pais(self):
        entrada = [self.brasil]
        self.assertEquals(["Brasil"], calcula_ranking(entrada))

    def test_Brasil_EUA_retorna_Brasil_EUA(self):
        entrada = [self.brasil, self.eua]
        self.assertEquals(["Brasil", "EUA"], calcula_ranking(entrada))

    def test_EUA_Brasil_retorna_Brasil_EUA(self):
        entrada = [self.eua, self.brasil]
        self.assertEquals(["Brasil", "EUA"], calcula_ranking(entrada))

    def test_EUA_Brasil_Cuba_retorna_Cuba_Brasil_EUA(self):
        entrada = [self.eua, self.brasil, self.cuba]
        self.assertEquals(["Cuba", "Brasil", "EUA"], calcula_ranking(entrada))

if __name__ == '__main__':
    unittest.main()
