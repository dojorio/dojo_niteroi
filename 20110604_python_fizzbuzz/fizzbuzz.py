def fizzbuzz(numero):
    if divisivel_por_3_e_por_5(numero):
        return "fizzbuzz"

    if eh_fizz(numero):
        return "fizz"

    if divisivel_por_5(numero):
        return "buzz"

    return numero

def divisivel_por_3_e_por_5(numero):
    return numero % 3 == 0 and numero % 5 == 0

def eh_fizz(numero):
    return numero % 3 == 0

def divisivel_por_5(numero):
    return numero % 5 == 0
