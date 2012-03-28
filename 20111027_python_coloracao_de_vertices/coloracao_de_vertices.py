def coloracao_de_vertices(x, y):
    if x == 1 or y == 1:
        if y>1 or x>=2:
            return 2
        return 1

    return 4

