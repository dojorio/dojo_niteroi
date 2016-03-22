def fizzbuzz(numero):
    if multiplo_de_3(numero) and multiplo_de_5(numero):
        return 'fizzbuzz'
    if multiplo_de_3(numero):
        return 'fizz'
    if multiplo_de_5(numero):
        return "buzz"
    return numero

def multiplo_de_3(numero):
    return numero % 3 == 0

def multiplo_de_5(numero):
    return numero % 5 == 0
