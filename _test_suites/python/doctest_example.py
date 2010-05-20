import doctest

def cube(x):
    """
    teste cubo de 10
    >>> cube(10)
    100

    teste cubo de 2
    >>> cube(2)
    8

    teste cubo de 3
    >>> cube(3)
    27
    """
    result = x * x * x
    return result


if __name__ == "__main__":
    doctest.testmod()
