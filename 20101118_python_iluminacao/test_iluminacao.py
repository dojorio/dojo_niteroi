# -*- coding:utf-8 -*-
import unittest
from iluminacao import verifica_iluminacao

class TestIluminacao(unittest.TestCase):

    def test_sala_1x1_sem_lampada_retorna_insuficiente(self):
        sala = [
            [0]
        ]
        self.assertEqual(verifica_iluminacao(sala), "iluminação insuficiente")
        
    def test_sala_1x1_com_1_lampada_retorna_suficiente(self):
        sala = [
            [1]
        ]
        self.assertEqual(verifica_iluminacao(sala), "iluminação suficiente")
        
    def test_sala_2x2_sem_lampada_retorna_insuficiente(self):
        sala = [
            [0, 0],
            [0, 0],
        ]
        self.assertEqual(verifica_iluminacao(sala), "iluminação insuficiente")
        
    def test_sala_2x2_com_1_lampada_em_0x0_retorna_suficiente(self):
        sala = [
            [1, 0],
            [0, 0],
        ]
        self.assertEqual(verifica_iluminacao(sala), "iluminação suficiente")
        
    def test_sala_2x2_com_1_lampada_em_0x1_retorna_suficiente(self):
        sala = [
            [0, 1],
            [0, 0],
        ]
        self.assertEqual(verifica_iluminacao(sala), "iluminação suficiente")
        
    def test_sala_2x2_com_1_lampada_em_1x0_retorna_suficiente(self):
        sala = [
            [0, 0],
            [1, 0],
        ]
        self.assertEqual(verifica_iluminacao(sala), "iluminação suficiente")
        
    def test_sala_3x3_com_1_lampada_em_0x0_retorna_insuficiente(self):
        sala = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        self.assertEqual(verifica_iluminacao(sala), 'iluminação insuficiente')
        
    def test_sala_3x3_com_1_lampada_em_1x1_retorna_suficiente(self):
        sala = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
        self.assertEqual(verifica_iluminacao(sala), 'iluminação suficiente')
        
    def test_sala_4x4_com_1_lampada_em_0x0_retorna_insuficiente(self):
        sala = [
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(verifica_iluminacao(sala), 'iluminação insuficiente')
        
    def test_sala_4x4_com_1_lampada_em_3x3_retorna_insuficiente(self):
        sala = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1],
        ]
        self.assertEqual(verifica_iluminacao(sala), 'iluminação insuficiente')
        
    def test_sala_4x4_com_1_lampada_em_2x3_retorna_insuficiente(self):
        sala = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0],
        ]
        self.assertEqual(verifica_iluminacao(sala), 'iluminação insuficiente')
    
    def test_sala_4x4_com_2_lampadas_em_0x0_e_0x3_retorna_insuficiente(self):
        sala = [
            [1, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(verifica_iluminacao(sala), 'iluminação insuficiente')
        
    def test_sala_4x4_com_4_lampadas_em_0x0_e_0x3_e_3x0_e_3x3_retorna_suficiente(self):
        sala = [
            [1, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 1],
        ]
        self.assertEqual(verifica_iluminacao(sala), 'iluminação suficiente')
        
    
    
unittest.main()
