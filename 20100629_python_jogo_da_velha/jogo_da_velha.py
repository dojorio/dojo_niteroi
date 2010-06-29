def avalia_jogo(entrada):
    return avalia_linhas(entrada)

def avalia_linhas(entrada):
    for i in range(3):
        if entrada[i][0] == entrada [i][1] == entrada[i][2]:
            return entrada[i][0]
