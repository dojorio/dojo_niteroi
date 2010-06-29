def avalia_jogo(jogo):
    if avalia_linhas(jogo):
        return avalia_linhas(jogo)
    return jogo[0][0]

def avalia_linhas(jogo):
    for linha in jogo:
        if not linha[0]:
            continue
        if linha[0] == linha[1] == linha[2] :
            return linha[0]
