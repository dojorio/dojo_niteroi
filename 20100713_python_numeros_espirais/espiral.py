def numeros_espirais(ordem):


    linha = [0] * ordem
    matriz = [linha] * ordem
    limite = ordem ** 2
    i, j = 0, 0

    print matriz

    for numero in range(1, limite + 1):
        if i == 0 and j < ordem:
            matriz[i][j] = numero
            j += 1
            continue
        if i == 0 and j == ordem:
            j = ordem-1
            i += 1
            matriz[i][j] = numero
            continue
        if i == 1:
            j = ordem-1
            matriz[i][j] = numero


    return matriz


    if ordem == 1:
        return [[1]]
    return [[1,2],
            [4,3]]
