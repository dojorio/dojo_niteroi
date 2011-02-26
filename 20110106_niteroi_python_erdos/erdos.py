# -*- coding: utf-8 -*-
 

def numero_de_erdos(publicacoes):
    numeros_de_erdos = {"Erdos": 0}
    
    
    #publicacoes = sorted(publicacoes, cmp=ordena)
    #for publicacao in publicacoes:
        
    while publicacoes:    
        comp = lambda a,b: buscar(numeros_de_erdos, a) - buscar(numeros_de_erdos, b) 
        publicacoes = sorted(publicacoes, cmp=comp)
        publicacao = publicacoes.pop(0)
         
        menor_valor = buscar(numeros_de_erdos, publicacao)
        
        for autor in publicacao:
            try:
                numeros_de_erdos[autor]
            except KeyError:
                numeros_de_erdos[autor] = menor_valor + 1
    return numeros_de_erdos
    
def ordena(publicacao1, publicacao2, numeros_de_erdos):
    if "Erdos" in publicacao1:
        return -1
    if "Erdos" in publicacao2:
        return 1
    return 0

def buscar(numeros, autores):
    menor = ''
    for autor in autores:
        try:
            if menor == '' or numeros[autor] < menor:
                menor = numeros[autor]
        except KeyError:
            pass
    
    return menor if menor != '' else 0 