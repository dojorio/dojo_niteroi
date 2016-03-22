# -*- coding: utf-8 -*-
import unittest
from erdos import numero_de_erdos

class TestErdos(unittest.TestCase):
    
    def verifica_numero(self, publicacoes, numeros_de_erdos):
        self.assertEqual(numero_de_erdos(publicacoes), numeros_de_erdos)
    
    def test_deve_retornar_0_1_para_Erdos_e_Joaozinho(self):
        publicacoes = [
            ["Erdos", "Joaozinho"],   
        ]
        numeros_de_erdos = {
            "Erdos": 0,
            "Joaozinho": 1,
        }
        self.verifica_numero(publicacoes, numeros_de_erdos)

        
    def test_deve_retornar_0_1_para_Erdos_e_Zezinho(self):
        publicacoes = [
            ["Erdos", "Zezinho"],
        ]
        numeros_de_erdos = {
            "Erdos": 0,
            "Zezinho": 1,
        }
        self.verifica_numero(publicacoes, numeros_de_erdos)
        
    def test_deve_retornar_0_1_1_para_duas_publicacoes_com_Erdos(self):
        publicacoes = [
            ["Erdos", "Joaozinho"],
            ["Erdos", "Zezinho"],
        ]
        numeros_de_erdos = {
            "Erdos": 0,
            "Joaozinho": 1,
            "Zezinho": 1,
        }
        self.verifica_numero(publicacoes, numeros_de_erdos)
    
    def test_deve_retornar_0_1_1_para_Erdos_Joaozinho_e_Paulo(self):
        publicacoes = [
            ["Erdos", "Joaozinho", "Paulo"]
        ]
        numeros_de_erdos = {
           "Erdos": 0,
           "Joaozinho": 1,
           "Paulo": 1,
        }
        self.verifica_numero(publicacoes, numeros_de_erdos)  
       
    def test_deve_retornar_0_1_2_para_duas_publicacoes_apenas_uma_com_Erdos(self):
        publicacoes = [
            ["Erdos", "Joaozinho"],
            ["Joaozinho", "Paulo"],
        ]
        numeros_de_erdos = {
            "Erdos": 0,
            "Joaozinho": 1,
            "Paulo": 2,
        }
        self.verifica_numero(publicacoes, numeros_de_erdos)
        
    def test_deve_retornar_0_1_2_2_para_duas_publicacoes_apenas_uma_com_Erdos(self):
        publicacoes = [
            ["Erdos", "Joaozinho"],
            ["Joaozinho", "Paulo", "Ana"],
        ]
        numeros_de_erdos = {
            "Erdos": 0,
            "Joaozinho": 1,
            "Paulo": 2,
            "Ana": 2
        }
        self.verifica_numero(publicacoes, numeros_de_erdos)
    
    def test_deve_retornar_0_1_2_3_para_duas_publicacoes_apenas_uma_com_Erdos(self):
        publicacoes = [
            ["Erdos", "Joaozinho"],
            ["Joaozinho", "Paulo"],
            ["Paulo", "Ana"],
        ]
        numeros_de_erdos = {
            "Erdos": 0,
            "Joaozinho": 1,
            "Paulo": 2,
            "Ana": 3,

        }
        self.verifica_numero(publicacoes, numeros_de_erdos)
        
    def test_deve_retornar_0_1_2_para_erdos_na_segunda_publicacao(self):
        publicacoes = [
            ["Paulo","Ana"],
            ["Erdos","Paulo"],
        ]
        numeros_de_erdos = {
            "Erdos": 0,
            "Paulo": 1,
            "Ana": 2,
        }
        self.verifica_numero(publicacoes, numeros_de_erdos)
        
    def test_deve_retornar_0_1_2_3_para_erdos_na_segunda_publicacao(self):
        publicacoes = [
            ["Joaozinho","Ana"],
            ["Joaozinho", "Paulo"],
            ["Erdos","Paulo"],
        ]
        numeros_de_erdos = {
            "Erdos": 0,
            "Paulo": 1,
            "Joaozinho": 2,
            "Ana": 3,
        }
        self.verifica_numero(publicacoes, numeros_de_erdos)
        
        
unittest.main()
    