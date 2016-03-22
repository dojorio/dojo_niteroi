from copy import deepcopy

def dobra(array):
    copia_array = deepcopy(array)

    tamanho = len(copia_array)
    if tamanho == 2:
        return copia_array
    elif tamanho % 2:
        copia_array.append(0)
        tamanho += 1

    novo_array = []
    for i in range(tamanho/2):
        reverso = i * -1 - 1
        valor = copia_array[i] + copia_array[reverso]

        if valor >= 10:
            valor -=10

        novo_array.append(valor)

    return dobra(novo_array)
