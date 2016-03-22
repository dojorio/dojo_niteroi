import unittest
from assassino import testemunha, Teoria

class TestTestemunhaComUmErro(unittest.TestCase):

    def setUp(self):
        self.fato = Teoria(assassino=1, local=2, arma=4)
 
    def test_todos_os_valores_corretos(self):
        teoria = Teoria(assassino=1, local=2, arma=4)
        self.assertEqual(testemunha(self.fato, teoria), 0)

    def test_o_acusado_3_eh_inocente(self):
        teoria = Teoria(assassino=3, local=2, arma=4)
        self.assertEqual(testemunha(self.fato, teoria), 1)

    def test_o_acusado_4_eh_inocente(self):
        teoria = Teoria(assassino=4, local=2, arma=4)
        self.assertEqual(testemunha(self.fato, teoria), 1)

    def test_todos_os_valores_corretos_com_assassino_2(self):
        self.fato = Teoria(assassino=2, local=3, arma=4)
        teoria = Teoria(assassino=2, local=3, arma=4)
        self.assertEqual(testemunha(self.fato, teoria), 0)

    def test_local_1_incorreto(self):
        teoria = Teoria(assassino=1, local=1, arma=4)
        self.assertEqual(testemunha(self.fato, teoria), 2)
    
    def test_arma_1_eh_incorreta(self):
        teoria = Teoria(assassino=1, local=2, arma=1)
        self.assertEqual(testemunha(self.fato, teoria), 3)

class TestTestemunhaComMultiplosErros(unittest.TestCase):

    def setUp(self):
        self.fato = Teoria(assassino=1, local=2, arma=4)
        
    def test_assassino_e_local_sao_incorretos(self):
        teoria = Teoria(assassino=3, local=4, arma=4)
        self.assertRandom(teoria, (1, 2))
        
    def assertRandom(self, teoria, possibilidades):
        tentativas=set()
        for i in range(30):
            tentativas.add(testemunha(self.fato, teoria))
        self.assertEqual(tentativas, set(possibilidades))
        
    def test_assassino_e_arma_incorretos(self):
        teoria = Teoria(assassino=3, local=2, arma=6)
        self.assertRandom(teoria, (1, 3))
        
    def test_local_e_arma_incorretos(self):
        teoria = Teoria(assassino=1, local=3, arma=6)
        self.assertRandom(teoria, (2, 3))
    
    def test_assassino_local_e_arma_incorretos(self):
        teoria = Teoria(assassino=3, local=3, arma=6)
        self.assertRandom(teoria, (1, 2, 3))




unittest.main()
