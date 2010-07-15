def numeros_espirais(ordem):

    linha = [0 for i in range(ordem)]
    matriz = [linha[:] for i in range(ordem)]

    limite = ordem ** 2
    i, j = 0, 0

    for numero in range(1, limite + 1):
        if i == 0 and j < ordem:
            matriz[i][j] = numero
            j += 1
        elif i == 0 and j == ordem:
            j = ordem-1
            i += 1
            matriz[i][j] = numero
        elif i == 1:
            j -= 1
            matriz[i][j] = numero

    return matriz
