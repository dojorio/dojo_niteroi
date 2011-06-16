import unittest
from assassino import sobrevivente, contador, VIVO, MORTO
    

    
class TestAssassino(unittest.TestCase):

    def test_assassino_com_1_passo_e_1_pessoa_sobrevive_o_1(self):
        self.assertEqual(sobrevivente(1, 1), 1)
        
    def test_assassino_com_1_passo_e_2_pessoas_sobrevive_o_1(self):
        self.assertEqual(sobrevivente(1, 2), 1)
        
    def test_assassino_com_2_passos_e_3_pessoas_sobrevive_o_1(self):
        self.assertEqual(sobrevivente(2, 3), 1) 

    def test_assassino_com_2_passos_e_2_pessoas_sobrevive_o_2(self):
        self.assertEqual(sobrevivente(2, 2), 2)  
    
    def test_assassino_com_2_passos_e_5_pessoas_sobrevive_o_4(self):
        self.assertEqual(sobrevivente(2, 5), 4)
        
    def test_assassino_com_2_passos_e_4_pessoas_sobrevive_o_2(self):
        self.assertEqual(sobrevivente(2, 4), 2)
         
    def test_assassino_com_3_passos_e_4_pessoas_sobrevive_o_2(self):
        self.assertEqual(sobrevivente(3, 4), 2)   
        
class TestContador(unittest.TestCase):

    def test_passo_1_em_lista_1_na_posicao_1_retorna_1(self):
        passo = 1
        lista = [VIVO]
        posicao = 1
        self.assertEqual(contador(passo, lista, posicao), 1)
        
    def test_passo_1_em_lista_2_na_posicao_1_retorna_2(self):
        passo = 1
        lista = [VIVO, VIVO]
        posicao = 1
        self.assertEqual(contador(passo, lista, posicao), 2)
            
    def test_passo_1_em_lista_2_na_posicao_2_retorna_1(self):
        passo = 1
        lista = [VIVO, MORTO]
        posicao = 2
        self.assertEqual(contador(passo, lista, posicao), 1)
        
    def test_passo_2_em_lista_2_na_posicao_1_retorna_1(self):
        passo = 2
        lista = [VIVO, VIVO]
        posicao = 1
        self.assertEqual(contador(passo, lista, posicao), 1)
        
    def test_passo_1_em_lista_3_na_posicao_1_retorna_1(self):
        passo = 1
        lista = [VIVO, MORTO, MORTO]
        posicao = 1
        self.assertEqual(contador(passo, lista, posicao), 1)
        
    def test_passo_1_em_lista_3_na_posicao_1_retorna_1(self):
        passo = 1
        lista = [VIVO, MORTO, MORTO]
        posicao = 1
        self.assertEqual(contador(passo, lista, posicao), 1)    
unittest.main()
        
