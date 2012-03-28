
def collatz(inicio):
    return [1] if inicio == 1 else ([inicio] + (collatz(inicio * 3 + 1) if (lambda : inicio%2)() else collatz(inicio/2)))


