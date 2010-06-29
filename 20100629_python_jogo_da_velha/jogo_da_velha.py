def avalia_jogo(jogo):
    return avalia_linhas(jogo)

def avalia_linhas(jogo):
    for linha in jogo:
        if linha[0] == linha[1] == linha[2] and linha[0] != '':
            return linha[0]
