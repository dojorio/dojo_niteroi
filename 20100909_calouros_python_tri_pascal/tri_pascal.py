from math import factorial as fat

def triangulo_pascal(num_linhas):


    if num_linhas == 1:
        return [
            [1],
        ]
    elif num_linhas == 2:
        return [
            [1],
            [1, 1],
        ]
    elif num_linhas == 3:
        return [
            [1],
            [1, 1],
            [1, 2, 1],
        ]
    return [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
    ]

def combinacao(n, p):
    return fat(n) / (fat(n-p) * fat(p))

def gera_linha(linhas):
    return [combinacao(linhas - 1, i) for i in range(linhas)]
    return [1] * linhas
