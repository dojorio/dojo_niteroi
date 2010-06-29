def avalia_jogo(entrada):
    return avalia_linhas(entrada)

def avalia_linhas(entrada):
    for linha in entrada(3):
        if entrada[linha][0] == entrada [linha][1] == entrada[linha][2]:
            return entrada[i][0]
