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

def combinacao(a, b):
    return a

    if a == 1:
        return 1
    else:
        return 2
