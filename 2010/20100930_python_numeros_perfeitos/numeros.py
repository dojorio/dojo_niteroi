def perfeito(numero):
    return sum(divisor for divisor in range(1, numero / 2 + 1) if numero % divisor == 0) == numero
