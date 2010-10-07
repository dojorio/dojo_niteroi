def diz_fizzbuzz(numero):
    retorno = ''
    if numero_e_divisivel_por_3(numero):
        retorno = 'fizz'
    if numero_e_divisivel_por_5(numero):
        retorno += 'buzz'
    if retorno_e_vazio(retorno):
      return numero

    return retorno

def retorno_e_vazio(retorno):
    return not retorno

def numero_e_divisivel_por_5(numero):
    return numero % 5 == 0

def numero_e_divisivel_por_3(numero):
    return numero % 3 == 0
