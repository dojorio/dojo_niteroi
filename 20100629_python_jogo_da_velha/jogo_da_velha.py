def avalia_jogo(entrada):
    if entrada[0][0] == 'O' or entrada[1][0] == 'O':
        return entrada[0][0]
    return 'X'
