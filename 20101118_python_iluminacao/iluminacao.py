# -*- coding:utf-8 -*-

def verifica_iluminacao(sala):
    iluminacao = "iluminação insuficiente"

    for lista in sala:
        if 1 in lista:
            vizinhos = get_vizinhos(lista, lista.index(1))
            if len(vizinhos) == len(lista) - 1:
                iluminacao = "iluminação suficiente"

    return iluminacao
    
def esta_na_lista(lista, x):
    return x>=0 and x < len(lista)   
    
def get_vizinhos(sala, i, j):
    vizinhos =[]
    if esta_na_lista(sala, i-1):
        vizinhos.append(i-1)
    if esta_na_lista(sala, i+1):
        vizinhos.append(i+1)
    if esta_na_lista(sala, j-1):
        vizinhos.append(j-1)
    if esta_na_lista(sala, j+1):
        vizinhos.append(j+1)

    return vizinhos
