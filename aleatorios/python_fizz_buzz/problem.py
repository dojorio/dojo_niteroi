def fizz_buzz(numero):
    resposta = ''
    if divisivel_por_3(numero):
        resposta += 'fizz'
    if divisivel_por_5(numero):
        resposta += 'buzz'
    if not resposta:
        resposta = numero
    return resposta

def divisivel_por_3(numero):
    return numero % 3 == 0

def divisivel_por_5(numero):
    return numero % 5 == 0
