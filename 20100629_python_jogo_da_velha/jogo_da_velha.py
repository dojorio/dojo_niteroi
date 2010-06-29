def avalia_jogo(entrada):
    return avalia_linhas(entrada)

def avalia_linhas(entrada):
    for linha in entrada:
        if linha[0] == linha[1] == linha[2]:
            return linha[0]
