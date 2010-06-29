def avalia_jogo(jogo):
    return avalia_linhas(jogo)

def avalia_linhas(jogo):
    for linha in jogo:
        if not linha[0]:
            if linha[0] == linha[1] == linha[2]:
                return linha[0]
