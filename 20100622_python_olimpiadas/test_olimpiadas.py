import unittest
from olimpiadas import calcula_ranking

class TestOlimpiadas(unittest.TestCase):

    def test_1_pais_retorna_mesmo_pais(self):
        tupla_brasil = ("Brasil" ,1 , 0, 0)
        entrada = [tupla_brasil]
        self.assertEquals(["Brasil"], calcula_ranking(entrada))

if __name__ == '__main__':
    unittest.main()
