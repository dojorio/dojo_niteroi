def numeros_espirais(ordem):


    linha = [0] * ordem
    matriz = [linha] * ordem
    limite = ordem ** 2
    i, j = 0, 0

    for numero in range(1, limite + 1):
        if i == 1 and j >= 0:
            matriz[i][j] = numero
            j -= 1
        if i == 0 and j < ordem:
            matriz[i][j] = numero
            j += 1
        elif j == ordem
            i += 1
            j = ordem - 1

    return matriz

    if ordem == 1:
        return [[1]]
    return [[1,2],
            [4,3]]