def numeros_espirais(ordem):


    linha = [0] * ordem
    matriz = [linha] * ordem
    limite = ordem ** 2
    x, y = 0, 0
    incx, incy = 1 , 0

    valoressalvos = []
    for i in range(1, limite + 1):
        matriz[y][x] = i
        x += incx
        y += incy
        if x == ordem - 1:
            incy = 1
            incx = 0
        if y == ordem - 1:
            incy = 0
            incx = -1
        if x == 0:
            incy = -1
            incx = 0
        if matriz [x+incx, y+incy] == 0:
            incy = 0
            incx = 1


    return matriz

    if ordem == 1:
        return [[1]]
    return [[1,2],
            [4,3]]
