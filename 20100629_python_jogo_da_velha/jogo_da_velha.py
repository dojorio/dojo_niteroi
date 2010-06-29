def avalia_jogo(jogo):
    if avalia_linhas(jogo):
        return avalia_linhas(jogo)
    return avalia_colunas(jogo)

def avalia_linhas(jogo):
    for linha in jogo:
        if not linha[0]:
            continue
        if linha[0] == linha[1] == linha[2]:
            return linha[0]

def avalia_colunas(jogo):
    for coluna in range(3):
        for linha in jogo:
            if linha[coluna] == linha[coluna] == linha[coluna]:
                return linha [coluna]
