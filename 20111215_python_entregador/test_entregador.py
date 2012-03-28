#coding:utf-8
import unittest
from entregador import otimiza_distribuicao, Entregador, Item

class TestEntregador(unittest.TestCase):

    def setUp(self):
        self.carta = Item("carta")
        self.presente = Item("playstation")
        self.joao = Entregador("João", {self.carta: 10, self.presente: 60})
        self.papai_noel = Entregador("Papai Noel", {self.carta: 50, self.presente: 50})
        
    def test_carta_entregue_por_joao(self):
        entregadores = [self.joao]
        itens = [self.carta]
            
        self.assertEqual(
            otimiza_distribuicao(entregadores, itens),
            {self.carta: self.joao}
        )

    def test_presente_entegue_por_papai_noel(self):
        entregadores = [self.papai_noel]
        itens = [self.presente]
        
        self.assertEqual(
            otimiza_distribuicao(entregadores, itens), 
            {self.presente: self.papai_noel}
        )
    
    def test_papai_noel_entrega_presente_e_joao_nada(self):
        entregadores = [self.joao, self.papai_noel]
        itens = [self.presente]
        
        self.assertEqual(
            otimiza_distribuicao(entregadores, itens),
            {self.presente: self.papai_noel}
        )
        
    def test_papai_noel_entrega_presente_e_joao_nada_ordem_inversa(self):
        entregadores = [self.papai_noel, self.joao]
        itens = [self.presente]
        
        self.assertEqual(
            otimiza_distribuicao(entregadores, itens),
            {self.presente: self.papai_noel}
        )
unittest.main()        
