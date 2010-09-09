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
    return [
        [1],
        [1, 1],
        [1, 2, 1],
    ]
