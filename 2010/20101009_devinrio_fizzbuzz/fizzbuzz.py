def brincadeira(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'fizzbuzz'

    if numero % 3 == 0:
        return 'fizz'
    elif numero % 5 == 0:
        return 'buzz'
    return str(numero)
