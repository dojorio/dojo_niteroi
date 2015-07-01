import unittest
from collections import OrderedDict, Counter

notas = OrderedDict()
notas[100] = 'cem'
notas[50]  = 'cinquenta'
notas[20]  = 'vinte'
notas[10]  = 'dez'
notas[5]   = 'cinco'
notas[2]   = 'dois'

from copy import deepcopy

def saque (saldo, atual, melhor):
    if saldo <= 0:
        return min([atual, melhor], key = lambda x: sum(x.values()))
    for nota, nome in notas.items():
        outro = deepcopy(atual)
        outro[nome] += 1
        if saldo >= nota:
            melhor = saque(saldo - nota, outro, melhor)
    return melhor



def caixa_eletronico(saldo):
    return saque(saldo, Counter(), Counter({'erro': 10000000}))
    saldo = 1
    notas_retorno = Counter()
    
    for nota, nome in notas.items():
        valor = saldo
        saldo = valor%nota
        if int(valor/nota) != 0 and valor/nota > 0:
            notas_retorno[nome] = int(valor/nota)
            
    #     while saldo >= nota:
    #         if saldo % nota in[1,3]:
    #             break
    #         saldo -= nota
    #         notas_retorno[nome] += 1
    return notas_retorno
    

class TestCaixaEletronico(unittest.TestCase):

    def test_saca_2_retorna_1_nota_2(self):
        self.assertEqual(caixa_eletronico(2), {'dois': 1})

    def test_saca_5_retorna_1_nota_5(self):
        self.assertEqual(caixa_eletronico(5), {'cinco': 1})

    def test_saca_10_retorna_1_nota_10(self):
        self.assertEqual(caixa_eletronico(10),{'dez': 1})

    def test_saca_4_retorna_2_nota_2(self):
        self.assertEqual(caixa_eletronico(4), {'dois': 2})
    
    def test_saca_20_retorna_1_nota_20(self):
        self.assertEqual(caixa_eletronico(20), {'vinte': 1}) 

    def test_saca_50_retorna_1_nota_50(self):
        self.assertEqual(caixa_eletronico(50), {'cinquenta': 1})  

    def test_saca_100_retorna_1_nota_100(self):
        self.assertEqual(caixa_eletronico(100), {'cem': 1}) 

    def test_saca_40_retorna_2_nota_20(self):
        self.assertEqual(caixa_eletronico(40), {'vinte': 2})        

    def test_saca_300_retorna_3_nota_100(self):
        self.assertEqual(caixa_eletronico(300),{'cem': 3})

    def test_saca_15_retorna_1_nota_10_e_1_nota_5(self):
        self.assertEqual(caixa_eletronico(15), {'dez': 1, 'cinco': 1})

    def test_saca_150_retorna_1_nota_100_e_1_nota_50(self):
        self.assertEqual(caixa_eletronico(150), {'cem': 1, 'cinquenta': 1})    

    def test_saca_120_retorna_1_nota_100_e_1_nota_20(self):
        self.assertEqual(caixa_eletronico(120), {'cem': 1, 'vinte': 1})

    def test_saca_180_retorna_1_nota_100_e_1_nota_20_1_nota_10_1_nota_50(self):
        self.assertEqual(caixa_eletronico(180), {'cem': 1, 'cinquenta': 1, 'vinte': 1, 'dez': 1})

    def test_saca_6_retorna_3_notas_2(self):
        self.assertEqual(caixa_eletronico(6), {'dois': 3})

    def test_saca_8_retorna_4_notas_2(self):
        self.assertEqual(caixa_eletronico(8), {'dois': 4})
    
    def test_saca_13_retorna_1_notas_5_4_notas_2(self):
        self.assertEqual(caixa_eletronico(13), {'cinco': 1,'dois': 4})


unittest.main()
        
