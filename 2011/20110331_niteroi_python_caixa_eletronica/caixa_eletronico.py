def conta_notas(valor):
    notas = {}

    if valor / 100 != 0:
        notas["R$ 100"]= valor / 100
        valor %= 100 
    if valor / 50 != 0:
        notas["R$ 50"]= 1
        valor -= 50
    if valor / 20 != 0:
        notas["R$ 20"]= valor / 20
        valor = valor - 20

    return notas
