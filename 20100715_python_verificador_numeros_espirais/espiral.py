def verifica_matriz_espiral(matriz):
    if len(matriz[0]) == 2 and matriz[0][1] == matriz[0][0] + 1:
        return False
    return True
