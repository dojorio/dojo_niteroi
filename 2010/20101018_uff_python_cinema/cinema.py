#-*- coding: utf-8 -*-

valores = {
    'estudante' : 8,
    'idoso' : 6,
    'normal' : 11,
    u'criança' : 5.5,
}

class Filme(object):

    def __init__(self, tres_d=False, mais_de_120_min=False):
        self.tres_d = tres_d
        self.mais_de_120_min = mais_de_120_min

def calcula_preco(ingressos, filme):

    numero_de_ingressos = sum(ingressos.values())
    soma = 0

    if filme.tres_d:
        soma += numero_de_ingressos * 3

    if numero_de_ingressos > 20:
        return soma + numero_de_ingressos * 6

    for tipo, quantidade in ingressos.items():
        soma += quantidade * valores[tipo]

    return soma
