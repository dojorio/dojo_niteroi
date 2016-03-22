DIV3 = 'Arveres'
DIV5 = 'somo nozes'


def fizzbuzz(numero):
    valor = ''

    if numero % 3 == 0:
        valor += DIV3
    if numero % 5 == 0:
        valor += DIV5

    return valor or str(numero)
