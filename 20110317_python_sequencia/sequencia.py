def calcula_intervalo(sequencia_de_numeros):
    if len(sequencia_de_numeros) == 1:
        return [sequencia_de_numeros]

    primeiro_numero = sequencia_de_numeros[0]
    segundo_numero = sequencia_de_numeros[1]

    if segundo_numero == primeiro_numero + 1:
        return [sequencia_de_numeros]

    return [[primeiro_numero], [segundo_numero]]
