from math import factorial as fat

def triangulo_pascal(num_linhas):
    return [gera_linha(i) for i in range(1, num_linhas+1)]

def combinacao(n, p):
    return fat(n) / (fat(n-p) * fat(p))

def gera_linha(linhas):
    return [combinacao(linhas - 1, i) for i in range(linhas)]
