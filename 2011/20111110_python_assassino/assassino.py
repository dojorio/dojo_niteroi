from collections import namedtuple
from random import randrange

Teoria = namedtuple("Teoria", "assassino local arma")

def testemunha(resposta, teoria):
    if teoria == resposta:
        return 0    
    resultados = []
    if teoria.assassino != resposta.assassino:
        resultados.append(1)
    if teoria.local != resposta.local:
        resultados.append(2)
    if teoria.arma != resposta.arma:
        resultados.append(3)
    return resultados[randrange(len(resultados))]
       
