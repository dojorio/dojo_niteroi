def verifica_matriz_espiral(matriz):
    if len(matriz[0]) == 2:
        return matriz[0][1] == matriz[0][0] + 1
    return True
