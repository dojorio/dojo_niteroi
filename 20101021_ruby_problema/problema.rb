def menor_divisor(numero)
    for i in (2..numero).to_a
        return i if numero % i == 0
    end
end

def fatora(numero)

    return [1] if (numero == 1)

    menor_divisor = menor_divisor(numero)
    [menor_divisor].concat(fatora(numero / menor_divisor))
end